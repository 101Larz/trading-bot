"""
server.py — Stock Analyser (OpenRouter edition)
Serves the pixel-office dashboard and streams SSE analysis events.
Uses OpenRouter API — no local TradingAgents needed.
Deploy on Render: set OPENROUTER_API_KEY as environment variable.
"""

from flask import Flask, Response, request
import json, time, datetime, os, traceback, re, urllib.request, urllib.error

app = Flask(__name__)

OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "")
MODEL = os.environ.get("OPENROUTER_MODEL", "anthropic/claude-haiku-4")

PAGE = """\
<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Stock Analyser</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=DM+Sans:wght@400;500;600&display=swap">
<style>
:root {
  --bg: #0e0e10; --surface: #17171a; --border: #2a2a30;
  --fg: #e8e8e2; --fg-muted: #6b6b72;
  --buy: #3ecf6e; --buy-bg: #0a2016;
  --hold: #f5c542; --hold-bg: #1e1800;
  --sell: #f05454; --sell-bg: #200a0a;
  --mono: 'DM Mono', monospace; --sans: 'DM Sans', system-ui, sans-serif;
  color-scheme: dark;
}
*, *::before, *::after { box-sizing: border-box; }
body { margin: 0; padding-block: 36px; padding-inline: 20px; background: var(--bg); color: var(--fg); font-family: var(--sans); font-size: 15px; line-height: 1.6; }
.container { max-width: 820px; margin: 0 auto; display: flex; flex-direction: column; gap: 20px; }
.header { display: flex; align-items: center; gap: 14px; padding-bottom: 18px; border-bottom: 1px solid var(--border); }
.logo { font-family: var(--mono); font-size: 0.78rem; font-weight: 500; letter-spacing: 0.08em; color: var(--fg-muted); text-transform: uppercase; }
.logo span { color: var(--fg); }
.office-wrap { border-radius: 4px; overflow: hidden; position: relative; line-height: 0; border: 1px solid #c8c0a8; }
canvas#office { display: block; width: 100%; height: auto; image-rendering: pixelated; }
.office-status { position: absolute; bottom: 10px; left: 12px; font-family: var(--mono); font-size: 0.63rem; letter-spacing: 0.07em; color: #4a5a40; background: rgba(248,244,230,0.88); padding: 3px 8px; border-radius: 2px; }
.office-status.active { color: #1a6b3c; }
.search-card { background: var(--surface); border: 1px solid var(--border); border-radius: 4px; padding: 22px 24px; }
.search-label { font-family: var(--mono); font-size: 0.65rem; letter-spacing: 0.12em; text-transform: uppercase; color: var(--fg-muted); margin-bottom: 10px; }
.search-row { display: flex; gap: 10px; flex-wrap: wrap; }
input[type="text"] { flex: 1; min-width: 100px; padding: 10px 14px; background: var(--bg); color: var(--fg); border: 1px solid var(--border); border-radius: 3px; font-family: var(--mono); font-size: 1.05rem; font-weight: 500; letter-spacing: 0.08em; text-transform: uppercase; outline: none; transition: border-color 0.15s; }
input[type="text"]:focus { border-color: var(--fg-muted); }
input[type="text"]::placeholder { color: var(--fg-muted); opacity: 0.5; }
button#analyse-btn { padding: 10px 22px; background: var(--fg); color: var(--bg); border: none; border-radius: 3px; font-family: var(--sans); font-size: 0.88rem; font-weight: 600; cursor: pointer; white-space: nowrap; transition: opacity 0.15s; }
button#analyse-btn:disabled { opacity: 0.3; cursor: not-allowed; }
.hint { margin-top: 8px; font-family: var(--mono); font-size: 0.7rem; color: var(--fg-muted); }
#result { display: none; flex-direction: column; gap: 16px; }
.verdict { padding: 24px 24px 20px; border-radius: 4px; border: 1px solid var(--border); background: var(--surface); }
.verdict.buy  { border-left: 3px solid var(--buy);  background: var(--buy-bg); }
.verdict.hold { border-left: 3px solid var(--hold); background: var(--hold-bg); }
.verdict.sell { border-left: 3px solid var(--sell); background: var(--sell-bg); }
.verdict-label { font-family: var(--mono); font-size: 0.62rem; letter-spacing: 0.14em; text-transform: uppercase; color: var(--fg-muted); margin-bottom: 4px; }
.verdict-ticker { font-family: var(--mono); font-size: 0.78rem; color: var(--fg-muted); margin-bottom: 2px; }
.verdict-rating { font-family: var(--mono); font-size: 1.8rem; font-weight: 500; letter-spacing: -0.02em; }
.verdict.buy  .verdict-rating { color: var(--buy); }
.verdict.hold .verdict-rating { color: var(--hold); }
.verdict.sell .verdict-rating { color: var(--sell); }
.verdict-meaning { margin-top: 10px; font-size: 0.86rem; color: var(--fg-muted); line-height: 1.55; }
.card { background: var(--surface); border: 1px solid var(--border); border-radius: 4px; padding: 18px 22px; }
.card-title { font-family: var(--mono); font-size: 0.62rem; letter-spacing: 0.14em; text-transform: uppercase; color: var(--fg-muted); margin: 0 0 10px; }
.card-body { font-size: 0.88rem; line-height: 1.7; white-space: pre-wrap; word-break: break-word; min-width: 0; }
details { background: var(--surface); border: 1px solid var(--border); border-radius: 4px; }
summary { padding: 13px 18px; font-family: var(--mono); font-size: 0.68rem; letter-spacing: 0.08em; color: var(--fg-muted); cursor: pointer; list-style: none; }
summary::-webkit-details-marker { display: none; }
summary::before { content: '\\25B6  '; font-size: 0.55rem; }
details[open] summary::before { content: '\\25BC  '; }
.log-body { padding: 0 18px 16px; font-family: var(--mono); font-size: 0.7rem; line-height: 1.7; color: var(--fg-muted); white-space: pre-wrap; word-break: break-word; overflow-x: auto; min-width: 0; border-top: 1px solid var(--border); }
.footer { font-family: var(--mono); font-size: 0.62rem; color: var(--fg-muted); text-align: center; letter-spacing: 0.06em; padding-top: 2px; }
@media (max-width: 480px) { .search-row { flex-direction: column; } button#analyse-btn { width: 100%; } }
</style>
</head>
<body>

<div class="container">
  <div class="header"><div class="logo"><span>101Larz</span> &middot; Stock Analyser</div></div>
  <div class="office-wrap">
    <canvas id="office"></canvas>
    <div class="office-status" id="office-label">klaar voor analyse</div>
  </div>
  <div class="search-card">
    <div class="search-label">Ticker</div>
    <div class="search-row">
      <input type="text" id="ticker" placeholder="AAPL" maxlength="8" autocomplete="off" autofocus>
      <button id="analyse-btn" onclick="startAnalyse()">Analyseer</button>
    </div>
    <p class="hint">Bijv. AAPL &middot; NVDA &middot; IREN &middot; MSFT &mdash; duurt 5&ndash;10 min</p>
  </div>
  <div id="result">
    <div class="verdict" id="verdict-card">
      <div class="verdict-label">Aanbeveling</div>
      <div class="verdict-ticker" id="result-ticker"></div>
      <div class="verdict-rating" id="verdict-rating"></div>
      <div class="verdict-meaning" id="verdict-meaning"></div>
    </div>
    <div class="card">
      <p class="card-title">Volledige beslissing</p>
      <div class="card-body" id="decision-body"></div>
    </div>
    <details>
      <summary>Agent-log (klik om te tonen)</summary>
      <pre class="log-body" id="log-body"></pre>
    </details>
  </div>
  <div class="footer">TradingAgents v0.6.0 &middot; claude-sonnet-5-5</div>
</div>

<script>
(function () {
  // -- Layout (grid units, P=4px per unit) ------------------------------------
  // GW=241, GH=100
  // TOP ZONE  -- Kantine:  y 0..34   (35u tall), full width
  // H-WALL    -- y 34..37  (3u)
  // BOT-LEFT  -- Kamer A:  x 0..119, y 37..99  (3 desks)
  // V-WALL    -- x 119..122
  // BOT-RIGHT -- Kamer B:  x 122..240, y 37..99  (4 desks)
  const GW = 241, GH = 100;
  const P  = 4;
  // zone y boundaries
  const KY0 = 0,  KY1 = 34;          // kantine
  const HW  = 34, HWH = 4;           // horizontal wall y, height
  const BY0 = 38, BY1 = GH;          // bottom zones
  const VW  = 119, VWW = 4;          // vertical wall x, width
  const AX0 = 0,   AX1 = VW;         // kamer A x
  const BX0 = VW+VWW, BX1 = GW;      // kamer B x  (=123..240)

  const canvas = document.getElementById('office');
  canvas.width  = GW * P;
  canvas.height = GH * P;
  const ctx = canvas.getContext('2d');

  function r(x,y,w,h,c){ ctx.fillStyle=c; ctx.fillRect(x*P,y*P,w*P,h*P); }
  function dot(x,y,c){ r(x,y,1,1,c); }

  // -- Palette ----------------------------------------------------------------
  const FL_OFF  = ['#e8d8a0','#dece90','#d4c480','#c8b870'];
  const FG_OFF  = '#b8a860';
  const FL_CANT1= '#d8d0c0', FL_CANT2= '#ccc4b4', FG_CANT='#b0a898';
  const WALL_CANT='#f5e8d0', WS_CANT='#e8cba8', WA_CANT='#d4b888';
  const WALL_A  ='#f2ede0',  WS_A   ='#daeae4',  WA_A   ='#c4d8d0';
  const WALL_B  ='#f0e8f8',  WS_B   ='#d8caf0',  WA_B   ='#c0aae0';
  const DIV_W='#ccc4b0', DIV_D='#b0a898', DIV_DOOR='#e8dfc8', DIV_F='#c0a868', DIV_K='#d4a020';
  const SHELF='#c09050', SHED='#a07030';
  const BOOKS=['#c83030','#2050c0','#20904a','#c09020','#903ab0','#e07030','#608090','#40a080','#d04870','#207070'];
  const RUG_A='#5a9090', RUG_AB='#3a7070', RUG_AP='#6ab0b0';
  const RUG_B2='#9090d0',RUG_BB='#6060b0', RUG_BP='#b0b0f0';
  const MUG='#e8dcc8', MUGI='#7a4010';
  const SHAD='rgba(0,0,0,0.15)', SHADB='rgba(0,0,0,0.22)';
  const MON='#282838', SCROFF='#181828', SCRON='#1a4888', SCRGR='#28884a', SCRORNG='#884418';
  const KB='#484858', KBK='#606070';
  const POT='#c06030', POTRIM='#d07040', SOIL='#604020';
  const STEM='#387020', LF1='#50a030', LF2='#70c050', LF3='#308028';
  const WIN='#a8d8f4', WSKY='#c8eaff', WFRA='#d0c8b0';
  const WLT='rgba(255,248,200,';
  // canteen
  const CTT='#c8b880',CTE='#a89860',CCT='#e8d8a0',CCE='#c8b880';
  const FOOD=['#e07050','#70b840','#e8c030','#5090d0','#d05080'];
  const CNT='#d8c898',CNTE='#b8a878',CMM='#6a3818',CMH='#8a5030';
  // people & chairs
  const CHAIRS=[
    ['#c83030','#e85050'],['#1858c0','#3878e0'],['#208848','#38b868'],
    ['#b87808','#d8a828'],['#8028b0','#a048d0'],['#c04810','#e07030'],
    ['#186898','#3898c8'],
  ];
  const DTOPS =['#c8a050','#b8c0b0','#b89060','#a8b8b0','#c0b070','#b0a8c0','#90b8a0'];
  const DEDGES=['#9a7830','#90a090','#906840','#809098','#988848','#888098','#708880'];
  const SCRS  =[SCRON, SCRGR, SCROFF, SCRON, SCRGR, SCRORNG, SCRON];
  const PPL=[
    ['#f4c880','#180e04','#1a5aa0','#1a2038'],
    ['#d49060','#4a2810','#b83030','#2a1828'],
    ['#a06040','#202020','#20884a','#202830'],
    ['#f0c070','#8a5820','#b88010','#383820'],
    ['#c07850','#1a1010','#8028b0','#281830'],
    ['#f0d0a0','#c04018','#c04818','#2a2010'],
    ['#b87860','#302010','#1a6888','#1a2030'], // Lars idx=6
  ];

  // -- Draw helpers -----------------------------------------------------------
  function floorPlanks(x0,x1,y0,y1){
    for(let y=y0;y<y1;y+=4){
      r(x0,y,x1-x0,4,FL_OFF[Math.floor(y/4)%FL_OFF.length]);
      r(x0,y,x1-x0,1,FG_OFF);
    }
    for(let y=y0;y<y1;y+=4){
      const off=(Math.floor(y/4)%2)*8;
      for(let x=x0+off;x<x1;x+=16) r(x,y+1,1,3,FG_OFF);
    }
  }
  function floorConcrete(x0,x1,y0,y1){
    // base screed colour -- slightly warm grey
    r(x0,y0,x1-x0,y1-y0,'#c8c4be');
    // subtle variation bands (horizontal)
    for(let ty=y0;ty<y1;ty+=3){
      const v=((ty*7+13)%5===0)?'rgba(0,0,0,0.04)':'rgba(255,255,255,0.04)';
      r(x0,ty,x1-x0,1,v);
    }
    // expansion-joint grid (coarser, every ~20 units)
    for(let ty=y0;ty<y1;ty+=20) r(x0,ty,x1-x0,1,'rgba(0,0,0,0.10)');
    for(let tx=x0;tx<x1;tx+=20) r(tx,y0,1,y1-y0,'rgba(0,0,0,0.10)');
    // tiny aggregate specks
    for(let ty=y0+1;ty<y1-1;ty+=5)
      for(let tx=x0+2;tx<x1-1;tx+=7)
        dot(tx,ty,'rgba(0,0,0,0.07)');
  }
  function wallStripe(x0,x1,y0,bg,stripe,acc){
    r(x0,y0,x1-x0,14,bg);
    r(x0,y0+7,x1-x0,6,stripe);
    r(x0,y0+7,x1-x0,1,acc); r(x0,y0+12,x1-x0,1,acc);
    r(x0,y0,x1-x0,2,'#e8e4d8');
  }
  function hWall(y,doorX1,doorX2){ // horizontal dividing wall
    r(0,y,GW,HWH,DIV_W); r(0,y+1,GW,HWH-2,DIV_D);
    // door slot left zone
    r(doorX1,y,16,HWH,DIV_DOOR);
    r(doorX1,y,16,1,DIV_F); r(doorX1,y+HWH-1,16,1,DIV_F);
    r(doorX1,y,1,HWH,DIV_F); r(doorX1+15,y,1,HWH,DIV_F);
    dot(doorX1+14,y+2,DIV_K);
    // door slot right zone
    r(doorX2,y,16,HWH,DIV_DOOR);
    r(doorX2,y,16,1,DIV_F); r(doorX2,y+HWH-1,16,1,DIV_F);
    r(doorX2,y,1,HWH,DIV_F); r(doorX2+15,y,1,HWH,DIV_F);
    dot(doorX2+14,y+2,DIV_K);
  }
  function vWall(x,doorY){
    r(x,BY0,VWW,BY1-BY0,DIV_W); r(x+1,BY0,VWW-2,BY1-BY0,DIV_D);
    r(x,doorY,VWW,14,DIV_DOOR);
    r(x,doorY,VWW,1,DIV_F); r(x,doorY+13,VWW,1,DIV_F);
    r(x,doorY,1,14,DIV_F); r(x+VWW-1,doorY,1,14,DIV_F);
    dot(x+VWW-1,doorY+7,DIV_K);
  }
  function desk(dx,dy,dw,dh,top,edge){
    ctx.fillStyle=SHADB;
    ctx.fillRect((dx+2)*P,(dy+dh)*P,dw*P,3*P);
    ctx.fillRect((dx+dw)*P,(dy+2)*P,2*P,dh*P);
    r(dx,dy,dw,dh,top); r(dx,dy+dh,dw+1,2,edge); r(dx,dy,2,dh,edge);
    for(let gy=dy+2;gy<dy+dh;gy+=4){ctx.fillStyle='rgba(255,255,255,0.11)';ctx.fillRect(dx*P,gy*P,dw*P,P);}
  }
  function chair(cx2,cy2,ci){
    const [bk,st]=CHAIRS[ci%CHAIRS.length];
    ctx.fillStyle=SHAD; ctx.fillRect((cx2+1)*P,(cy2+7)*P,10*P,2*P);
    r(cx2,cy2,12,8,'#505060'); r(cx2+1,cy2+1,10,6,bk); r(cx2+2,cy2+2,8,4,st);
    dot(cx2+1,cy2,'#909090'); dot(cx2+10,cy2,'#909090');
    dot(cx2+1,cy2+7,'#909090'); dot(cx2+10,cy2+7,'#909090');
  }
  function monitor(mx,my,sc,on){
    r(mx,my,14,9,MON); r(mx+1,my+1,12,7,on?sc:SCROFF);
    r(mx+5,my+9,4,2,MON); r(mx,my+11,14,2,KB);
    for(let k=0;k<5;k++) dot(mx+1+k*2,my+11,KBK);
  }
  function plant(px,py,big){
    const s=big?1:0;
    ctx.fillStyle=SHAD; ctx.fillRect((px+1)*P,(py+6+s)*P,(5+s)*P,2*P);
    r(px+1,py+3+s,4+s,4,POT); r(px+1,py+3+s,4+s,1,POTRIM); r(px+2,py+4+s,2+s,1,SOIL);
    r(px+2+s,py,1,4+s,STEM);
    r(px,py-2,4+s,3,LF1); r(px-1,py-1,3,2,LF2);
    r(px+3+s,py-2,3,3,LF1); r(px+2+s,py-4,2+s,3,LF2);
    dot(px,py-2,LF3); dot(px+4+s,py-3,LF3);
  }
  function window_(wx,wy,ww,wh){
    r(wx,wy,ww,wh,WFRA);
    r(wx+1,wy+1,ww-2,wh-2,WIN); r(wx+1,wy+1,ww-2,4,WSKY);
    r(wx+1,wy+Math.floor((wh-2)/2),ww-2,1,WFRA);
    r(wx+Math.floor((ww-2)/2),wy+1,1,wh-2,WFRA);
    ctx.fillStyle=WLT+'0.13)'; ctx.fillRect((wx-3)*P,(wy+wh)*P,(ww+6)*P,20*P);
    ctx.fillStyle=WLT+'0.05)'; ctx.fillRect((wx-7)*P,(wy+wh)*P,(ww+14)*P,32*P);
  }
  function shelf(x,y0,y1){
    r(x,y0,5,y1-y0,SHELF); r(x+5,y0,1,y1-y0,SHED);
    let bi=0;
    for(let sy=y0;sy<y1-6;sy+=8){
      r(x,sy,5,1,SHED);
      for(let bx=0;bx<4;bx++) r(x+bx,sy+1,1,6,BOOKS[(bi++)%BOOKS.length]);
    }
  }
  // canteen helpers
  function cantTable(tx,ty,wide){
    const tw=wide?32:22;
    ctx.fillStyle=SHAD; ctx.fillRect((tx+2)*P,(ty+6)*P,tw*P,3*P);
    r(tx,ty,tw,6,CTT); r(tx,ty+6,tw,2,CTE);
    r(tx,ty+8,2,3,'#b0a060'); r(tx+tw-2,ty+8,2,3,'#b0a060');
  }
  function cantChair(cx2,cy2){ r(cx2,cy2,10,5,CCT); r(cx2,cy2+5,10,1,CCE); ctx.fillStyle=SHAD;ctx.fillRect((cx2+1)*P,(cy2+6)*P,8*P,2*P); }
  function plate(fx,fy,col){ r(fx,fy,4,3,'#f0ead8'); r(fx+1,fy,2,1,col); r(fx,fy+1,1,2,col); r(fx+3,fy+2,1,1,'#40a020'); }
  function coffee(mx,my){ r(mx,my,8,10,CMM); r(mx+1,my+1,6,8,CMH); r(mx+2,my+2,4,3,'#1a1a1a'); r(mx+3,my+3,2,2,'#c8e8f0'); r(mx+2,my+6,4,2,'#282828'); r(mx+3,my+7,2,1,'#c86030'); }
  function counter(cx2,cy2,cw){ ctx.fillStyle=SHADB;ctx.fillRect((cx2+2)*P,(cy2+7)*P,cw*P,2*P); r(cx2,cy2,cw,7,CNT); r(cx2,cy2+7,cw+1,2,CNTE); }
  function person(px,py,pi,mood){
    const [sk,hr,sh,pn]=PPL[pi%PPL.length];
    ctx.fillStyle=SHAD; ctx.beginPath(); ctx.ellipse((px+3)*P,(py+8)*P,5*P,1.5*P,0,0,Math.PI*2); ctx.fill();
    r(px,py+5,2,2,'#282018'); r(px+4,py+5,2,2,'#282018');
    r(px,py+3,6,3,pn); r(px,py,7,4,sh);
    r(px+1,py-2,4,4,sk); r(px+1,py-2,4,2,hr);
    if(!blink){dot(px+2,py-1,'#1a1a1a'); dot(px+4,py-1,'#1a1a1a');}
    if(mood==='type'){
      const hb=Math.floor(typF*0.6)%2;
      r(px-1,py+1+hb,2,2,sk); r(px+6,py+1+hb,2,2,sk);
    } else if(mood==='walk'){
      const wb=Math.floor(t/6)%2;
      r(px-1,py+1+wb,1,3,sk); r(px+6,py+2-wb,1,3,sk);
    } else {
      r(px-1,py+2,1,3,sk); r(px+6,py+2,1,3,sk);
    }
  }

  // -- Desk data --------------------------------------------------------------
  // Kamer A (3 desks, pi 0-2) -- bottom-left, x 0..118
  const DA = [
    { dx:4,  dy:BY0+8, dw:22,dh:10, chx:5,  chy:BY0+19, mx:7,  my:BY0+10, sc:SCRS[0], on:true,  mugX:23, mugY:BY0+10, px:6,  py:BY0+12, pi:0, ci:0 },
    { dx:36, dy:BY0+8, dw:22,dh:10, chx:37, chy:BY0+19, mx:39, my:BY0+10, sc:SCRS[1], on:true,  mugX:0,  mugY:0,      px:38, py:BY0+12, pi:1, ci:1 },
    { dx:70, dy:BY0+8, dw:22,dh:10, chx:71, chy:BY0+19, mx:73, my:BY0+10, sc:SCRS[2], on:false, mugX:89, mugY:BY0+10, px:72, py:BY0+12, pi:2, ci:2 },
    // bottom row kamer A
    { dx:4,  dy:BY0+36, dw:22,dh:10, chx:5,  chy:BY0+47, mx:7,  my:BY0+38, sc:SCRS[0], on:true,  mugX:0, mugY:0,      px:6,  py:BY0+40, pi:0, ci:0 },
  ];
  // Kamer B (4 desks, pi 3-6, Lars=6) -- bottom-right, x 123..240
  const DB = [
    { dx:127, dy:BY0+8, dw:22,dh:10, chx:128, chy:BY0+19, mx:130, my:BY0+10, sc:SCRS[3], on:true, mugX:146, mugY:BY0+10, px:129, py:BY0+12, pi:3, ci:3 },
    { dx:162, dy:BY0+8, dw:22,dh:10, chx:163, chy:BY0+19, mx:165, my:BY0+10, sc:SCRS[4], on:true, mugX:0,   mugY:0,      px:164, py:BY0+12, pi:4, ci:4 },
    { dx:197, dy:BY0+8, dw:22,dh:10, chx:198, chy:BY0+19, mx:200, my:BY0+10, sc:SCRS[5], on:true, mugX:216, mugY:BY0+10, px:199, py:BY0+12, pi:5, ci:5 },
    // Lars bottom row kamer B
    { dx:162, dy:BY0+36, dw:22,dh:10, chx:163, chy:BY0+47, mx:165, my:BY0+38, sc:SCRS[6], on:true, mugX:0, mugY:0, px:164, py:BY0+40, pi:6, ci:6 },
  ];
  const LARS_DESK = DB[3]; // Lars sits at last desk in kamer B

  // -- State ------------------------------------------------------------------
  let state='idle', t=0;
  let cx=200, cy=55, tx=200, ty=55;
  let typF=0, blinkT=0, blink=false, glowP=0;

  function drawScene(){
    ctx.clearRect(0,0,GW*P,GH*P);

    // -- KANTINE (top) --------------------------------------------------------
    wallStripe(0,GW,KY0,WALL_CANT,WS_CANT,WA_CANT);
    floorConcrete(0,GW,14,KY1);
    // windows across top
    [14,60,110,160,208].forEach(wx=>window_(wx,1,16,11));
    // counter left
    counter(1,15,20); coffee(4,6);
    ctx.font=`bold ${P*1.7}px 'DM Mono',monospace`; ctx.fillStyle='#8a6820'; ctx.fillText('KANTINE',3*P,13*P);
    // tables: 4 across
    [[28,17],[68,17],[108,17],[150,17],[190,17]].forEach(([tx2,ty2])=>{
      cantTable(tx2,ty2,false);
      cantChair(tx2+2,ty2+8); cantChair(tx2+12,ty2+8);
      cantChair(tx2+2,ty2-6); cantChair(tx2+12,ty2-6);
    });
    // food on tables
    plate(31,17,FOOD[0]); plate(74,17,FOOD[1]); plate(113,17,FOOD[2]); plate(155,17,FOOD[3]); plate(194,17,FOOD[4]);
    // people in canteen eating/standing
    [[30,20,0,'idle'],[70,20,3,'idle'],[112,20,1,'idle'],[152,20,4,'idle']].forEach(([px,py,pi,m])=>person(px,py,pi,m));
    // plant corners
    plant(1,14,false); plant(230,14,false);

    // -- HORIZONTAL WALL ------------------------------------------------------
    hWall(HW, 25, 148); // door in left zone at x=25, right zone x=148

    // -- KAMER A (bottom-left) ------------------------------------------------
    wallStripe(AX0,AX1,BY0,WALL_A,WS_A,WA_A);
    floorPlanks(AX0,AX1,BY0+14,BY1);
    shelf(AX0,BY0+14,BY1);
    // rug
    r(6,BY0+28,106,20,RUG_A); r(6,BY0+28,106,1,RUG_AB); r(6,BY0+47,106,1,RUG_AB); r(6,BY0+28,1,20,RUG_AB); r(111,BY0+28,1,20,RUG_AB);
    for(let rp=10;rp<110;rp+=9){r(rp,BY0+30,2,2,RUG_AP);r(rp,BY0+44,2,2,RUG_AP);}
    // desks
    DA.forEach(d=>{
      desk(d.dx,d.dy,d.dw,d.dh,DTOPS[d.pi],DEDGES[d.pi]);
      chair(d.chx,d.chy,d.ci);
      monitor(d.mx,d.my,d.sc,d.on);
      if(d.mugX){ r(d.mugX,d.mugY,2,2,MUG); dot(d.mugX+1,d.mugY+1,MUGI); }
    });
    plant(108,BY0+15,false);
    ctx.font=`bold ${P*1.5}px 'DM Mono',monospace`; ctx.fillStyle='rgba(60,70,50,0.55)'; ctx.fillText('KAMER A',7*P,(BY0+13)*P);

    // -- VERTICAL WALL --------------------------------------------------------
    vWall(VW, BY0+22);

    // -- KAMER B (bottom-right) -----------------------------------------------
    wallStripe(BX0,BX1,BY0,WALL_B,WS_B,WA_B);
    floorPlanks(BX0,BX1,BY0+14,BY1);
    // rug
    r(BX0+2,BY0+28,110,20,RUG_B2); r(BX0+2,BY0+28,110,1,RUG_BB); r(BX0+2,BY0+47,110,1,RUG_BB); r(BX0+2,BY0+28,1,20,RUG_BB); r(BX0+111,BY0+28,1,20,RUG_BB);
    for(let rp=BX0+6;rp<BX0+110;rp+=9){r(rp,BY0+30,2,2,RUG_BP);r(rp,BY0+44,2,2,RUG_BP);}
    // desks
    DB.forEach((d,i)=>{
      const larsHere=i===3&&state==='working'&&Math.abs(cx-d.px)<8&&Math.abs(cy-d.py)<8;
      desk(d.dx,d.dy,d.dw,d.dh,DTOPS[d.pi],DEDGES[d.pi]);
      chair(d.chx,d.chy,d.ci);
      monitor(d.mx,d.my,d.sc,d.on);
      if(d.mugX){ r(d.mugX,d.mugY,2,2,MUG); dot(d.mugX+1,d.mugY+1,MUGI); }
    });
    plant(BX1-8,BY0+15,true); plant(BX1-8,BY0+55,false);
    ctx.font=`bold ${P*1.5}px 'DM Mono',monospace`; ctx.fillStyle='rgba(60,50,70,0.55)'; ctx.fillText('KAMER B',(BX0+4)*P,(BY0+13)*P);

    // -- window glow shimmer --------------------------------------------------
    const gv=(Math.sin(glowP*Math.PI*2)+1)/2;
    [14,60,110,160,208].forEach(wx=>{
      ctx.fillStyle=WLT+(0.04+gv*0.012)+')';
      ctx.fillRect((wx-4)*P,12*P,(16+8)*P,22*P);
    });

    // -- Kamer A people -------------------------------------------------------
    DA.forEach(d=>{ person(d.px,d.py,d.pi,d.on?'type':'idle'); });

    // -- Kamer B people (skip Lars slot, drawn separately) --------------------
    DB.forEach((d,i)=>{ if(i!==3) person(d.px,d.py,d.pi,d.on?'type':'idle'); });

    // -- Lars -----------------------------------------------------------------
    const moving=Math.abs(cx-tx)>1.5||Math.abs(cy-ty)>1.5;
    const lMood=moving?'walk':(state==='working'?'type':'idle');
    person(Math.round(cx),Math.round(cy),6,lMood);

    // -- Agent label ----------------------------------------------------------
    if(state==='working'){
      const AGENTS=['Market Analyst','News Analyst','Technical Analyst','Fundamental Analyst','Bull Researcher','Bear Researcher','Trader'];
      const label='\\u25B6 '+AGENTS[Math.floor(t/90)%AGENTS.length];
      ctx.font=`bold ${P*2.2}px 'DM Mono',monospace`;
      const tw=ctx.measureText(label).width;
      ctx.fillStyle='rgba(248,245,234,0.92)';
      ctx.fillRect(BX0*P,(GH-8)*P-2,tw+12,P*2.2+8);
      ctx.fillStyle='#1a6b3c'; ctx.fillText(label,(BX0)*P+6,(GH-6)*P);
    }
  }

  function tick(){
    t++; glowP=(t*0.012)%1;
    blinkT++; if(blinkT>165) blink=true; if(blinkT>172){blink=false;blinkT=0;}
    if(state==='working') typF+=0.5;
    const ddx=tx-cx,ddy=ty-cy,dist=Math.sqrt(ddx*ddx+ddy*ddy);
    if(dist>0.8){cx+=ddx/dist*1.0;cy+=ddy/dist*1.0;}else{cx=tx;cy=ty;}
    drawScene();
    requestAnimationFrame(tick);
  }
  tick();

  function setLabel(txt,active){
    const el=document.getElementById('office-label');
    el.textContent=txt; el.className='office-status'+(active?' active':'');
  }
  window.pixelOffice={
    setIdle()      {state='idle';   tx=200;ty=55; setLabel('klaar voor analyse',false);},
    setWorking(tk) {state='working';tx=LARS_DESK.px;ty=LARS_DESK.py; setLabel(tk+' wordt geanalyseerd...',true);},
    setDone(v)     {state='done';   tx=200;ty=55; setLabel('klaar — '+v,false);},
  };
})();

function startAnalyse(){
  const ticker=document.getElementById('ticker').value.trim().toUpperCase();
  if(!ticker){document.getElementById('ticker').focus();return;}
  document.getElementById('result').style.display='none';
  document.getElementById('analyse-btn').disabled=true;
  document.getElementById('ticker').disabled=true;
  window.pixelOffice.setWorking(ticker);
  let log='',es;
  try{
    es=new EventSource('/analyse?ticker='+encodeURIComponent(ticker));
    es.addEventListener('log',e=>{log+=e.data+'\\n';});
    es.addEventListener('done',e=>{es.close();showResult(JSON.parse(e.data),log);});
    es.addEventListener('error_msg',e=>{es.close();showError(e.data);});
    es.onerror=()=>{es.close();demoResult(ticker);};
  }catch(e){demoResult(ticker);}
}
function demoResult(ticker){
  setTimeout(()=>showResult({ticker,analyse_date:new Date().toISOString().slice(0,10),
    verdict_class:'buy',verdict_text:'Overweight',
    verdict_meaning:'Demo mode — start server.py voor echte analyse.',
    decision:'(Demo) .venv\\\\Scripts\\\\python.exe server.py'},'(demo mode)'),3500);
}
function showResult(data,log){
  window.pixelOffice.setDone(data.verdict_text);
  document.getElementById('verdict-card').className='verdict '+data.verdict_class;
  document.getElementById('result-ticker').textContent=data.ticker+' · '+data.analyse_date;
  document.getElementById('verdict-rating').textContent=data.verdict_text;
  document.getElementById('verdict-meaning').textContent=data.verdict_meaning;
  document.getElementById('decision-body').textContent=data.decision;
  document.getElementById('log-body').textContent=log||'(geen log)';
  const res=document.getElementById('result');
  res.style.display='flex';res.style.flexDirection='column';res.style.gap='16px';
  document.getElementById('analyse-btn').disabled=false;
  document.getElementById('ticker').disabled=false;
  document.getElementById('ticker').value='';
  document.getElementById('ticker').focus();
}
function showError(msg){
  window.pixelOffice.setIdle();
  document.getElementById('office-label').textContent='fout: '+msg;
  document.getElementById('analyse-btn').disabled=false;
  document.getElementById('ticker').disabled=false;
}
document.getElementById('ticker').addEventListener('keydown',e=>{if(e.key==='Enter')startAnalyse();});
</script>
</body>
</html>
"""

# ── Routes ────────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return PAGE, 200, {"Content-Type": "text/html; charset=utf-8"}


def _sse(event: str, data: str) -> str:
    safe = data.replace("\n", " ").replace("\r", "")
    return f"event: {event}\ndata: {safe}\n\n"


def _openrouter_analyse(ticker: str):
    """
    Call OpenRouter API to analyse a stock ticker.
    Yields (event_name, data_str) tuples.
    """
    # Re-read at request time so Render env vars are always picked up
    api_key = os.environ.get("OPENROUTER_API_KEY", "")
    if not api_key:
        yield ("log", "[error] OPENROUTER_API_KEY niet ingesteld op de server")
        yield ("log", "[info] Stel OPENROUTER_API_KEY in als environment variable op Render")
        raise ValueError("No API key")

    agents = [
        "Market Analyst",
        "News Analyst",
        "Technical Analyst",
        "Fundamental Analyst",
        "Bull Researcher",
        "Bear Researcher",
        "Trader",
    ]

    yield ("log", f"[init] Verbinding met OpenRouter ({MODEL}) ...")
    time.sleep(0.3)

    for i, agent in enumerate(agents):
        yield ("log", f"[{i+1}/{len(agents)}] {agent}: analysing {ticker.upper()} ...")
        time.sleep(0.4)

    yield ("log", "[trader] Ophalen marktdata en nieuwscontext ...")
    time.sleep(0.5)
    yield ("log", "[trader] Schrijven eindadvies ...")
    time.sleep(0.3)

    today = datetime.date.today().isoformat()
    prompt = f"""Je bent een professionele aandelenmarkt analist. Analyseer het aandeel {ticker.upper()} per {today}.

Geef een beknopte analyse (max 300 woorden) met:
1. Huidige marktpositie en sector
2. Recente ontwikkelingen (nieuws, earnings, trends)
3. Technische indicatoren (trend, momentum)
4. Risico's en kansen
5. Eindadvies: BUY, HOLD of SELL met korte onderbouwing

Begin je antwoord ALTIJD met exact één van deze drie woorden op de eerste regel: BUY, HOLD, of SELL
Daarna volgt je volledige analyse."""

    payload = json.dumps({
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 600,
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://101larz-stock-analyser.onrender.com",
            "X-Title": "101Larz Stock Analyser",
        },
        method="POST",
    )

    with urllib.request.urlopen(req, timeout=60) as resp:
        raw = resp.read().decode("utf-8")

    data = json.loads(raw)
    decision_text = data["choices"][0]["message"]["content"].strip()

    # Parse verdict from first line
    first_line = decision_text.split("\n")[0].strip().upper()
    if "BUY" in first_line:
        verdict_class, verdict_text = "buy", "Overweight"
        verdict_meaning = "De analyse wijst op bullish signalen. Overweeg een positie conform je risicobeheer."
    elif "SELL" in first_line:
        verdict_class, verdict_text = "sell", "Underweight"
        verdict_meaning = "De analyse signaleert bearish druk. Overweeg af te bouwen of geen positie in te nemen."
    else:
        verdict_class, verdict_text = "hold", "Neutraal"
        verdict_meaning = "Geen duidelijk signaal. Wacht op meer bevestiging voordat je een positie inneemt."

    result = {
        "ticker":          ticker.upper(),
        "analyse_date":    today,
        "verdict_class":   verdict_class,
        "verdict_text":    verdict_text,
        "verdict_meaning": verdict_meaning,
        "decision":        decision_text,
    }
    yield ("done", json.dumps(result))


def _demo_stream(ticker: str):
    """Fallback demo when no API key is set."""
    agents = ["Market Analyst","News Analyst","Technical Analyst",
              "Fundamental Analyst","Bull Researcher","Bear Researcher","Trader"]
    for i, agent in enumerate(agents):
        time.sleep(0.5)
        yield ("log", f"[{i+1}/{len(agents)}] {agent}: analysing {ticker.upper()} ...")
    time.sleep(0.5)
    yield ("log", "[trader] writing final decision ...")
    time.sleep(0.4)
    result = {
        "ticker":          ticker.upper(),
        "analyse_date":    datetime.date.today().isoformat(),
        "verdict_class":   "hold",
        "verdict_text":    "Demo modus",
        "verdict_meaning": (
            "Stel OPENROUTER_API_KEY in als environment variable op Render "
            "voor een echte analyse. Haal je key op bij openrouter.ai"
        ),
        "decision": (
            "Demo modus — geen API key gevonden.\n\n"
            "Ga naar Render → je service → Environment → voeg toe:\n"
            "  OPENROUTER_API_KEY = sk-or-...\n\n"
            "Haal je key op bij: https://openrouter.ai/keys"
        ),
    }
    yield ("done", json.dumps(result))


@app.route("/analyse")
def analyse():
    ticker = request.args.get("ticker", "").strip().upper()
    if not ticker:
        def err():
            yield _sse("error_msg", "Geen ticker opgegeven.")
        return Response(err(), mimetype="text/event-stream")

    if not re.match(r'^[A-Z\.]{1,10}$', ticker):
        def bad():
            yield _sse("error_msg", f"Ongeldige ticker: {ticker}")
        return Response(bad(), mimetype="text/event-stream")

    def generate():
        yield ": keepalive\n\n"
        try:
            for event, data in _openrouter_analyse(ticker):
                yield _sse(event, data)
                if event == "done":
                    return
        except Exception as exc:
            tb = traceback.format_exc()
            yield _sse("log", f"[error] {exc}")
            yield _sse("log", tb[:200])
            yield _sse("log", "[server] demo modus")

        for event, data in _demo_stream(ticker):
            yield _sse(event, data)
            if event == "done":
                return

    headers = {
        "Content-Type":  "text/event-stream",
        "Cache-Control": "no-cache",
        "X-Accel-Buffering": "no",
    }
    return Response(generate(), headers=headers)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"Stock Analyser running on http://localhost:{port}", flush=True)
    app.run(host="0.0.0.0", port=port, threaded=True, debug=False)
