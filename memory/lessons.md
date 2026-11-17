# Lessons Learned

Agent appends new lessons here after significant trades or market events. Read before every session.

---

## Format

Each lesson follows this template:

```
### YYYY-MM-DD — [SYMBOL]: [één zin wat er gebeurde]
**What happened:** Entry [datum], exit [datum], [shares] shares, entry $[prijs], exit $[prijs], P&L [bedrag], hold [dagen] dagen.
**What went wrong / right:** [Concrete root cause — niet generiek]
**Rule change or reminder:** [Één specifieke actie of regel die dit voorkomt]
```

---

## Lessons

### 2026-10-02 — STX: grootste verlies ooit, MEDIUM confidence, storage buiten AI-kern
**What happened:** Entry 2026-09-24, exit 2026-10-02, 8 shares @ $918.17 → $802.83. P&L: **-$922.72**. Hold: 8 dagen. Gestopt out.
**What went wrong:** MEDIUM confidence, thesis "Hard drive demand, AI data center storage" — generiek en zwak. STX is een legacy storage bedrijf, geen directe AI-speler. Positiegrootte van 8 shares × $918 = $7.345 is enorm voor een MEDIUM confidence trade. De stop had al op dag 2–3 getriggerd moeten zijn bij early weakness. Dit is patroon #1 (te laat gestopt) + patroon #2 (MEDIUM confidence) + patroon #4 (hoge stuksprijs).
**Rule change or reminder:** MEDIUM confidence = NO_TRADE. Geen uitzonderingen. STX had nooit de entry-check mogen passeren.

---

### 2026-10-06 — SNDK: $530 verlies op dure storage-trade, same week als STX
**What happened:** Entry 2026-09-21, exit 2026-10-06, 4 shares @ $1.804.86 → $1.672.29. P&L: **-$530.28**. Hold: 15 dagen. Gestopt out.
**What went wrong:** MEDIUM confidence, thesis "Storage demand, NAND recovery" — net als STX een storage thesis in dezelfde periode. Stuksprijs $1.804 is extreem hoog. 15 dagen vastgehouden terwijl de positie consistent daalde. Early weakness stop op dag 3 had dit moeten beëindigen bij ~-$160 i.p.v. -$530. Patroon #1 + #2 + #4.
**Rule change or reminder:** Bij stuksprijzen boven $500: early weakness stop is verplicht vanaf dag 1, niet optioneel. Nooit twee storage-aandelen tegelijk houden.

---

### 2026-09-14 — MU: -$723 door hoge stuksprijs + sector-concentratie met NVDA
**What happened:** Entry 2026-09-08, exit 2026-09-14, 7 shares @ $1.017.84 → $914.48. P&L: **-$723.54**. Hold: 6 dagen. Gestopt out.
**What went wrong:** MEDIUM confidence, thesis "Memory chip recovery, HBM demand for AI." MU geopend op dezelfde dag als NVDA #3 — twee grote semi-posities tegelijk. Toen semis die week daalden verloor de bot op beide tegelijk (-$625 NVDA + -$723 MU = -$1.349 op één dag). Stuksprijs $1.017: 7 shares = $7.125 risico. Patroon #2 + #3 (sector-concentratie) + #4 (hoge stuksprijs).
**Rule change or reminder:** Nooit twee semis tegelijk openen. Sector-correlatie = geconcentreerd risico. MU had die dag NO_TRADE moeten zijn omdat NVDA al open stond.

---

### 2026-09-14 — NVDA #3: -$625 verlies, derde NVDA-poging in korte tijd
**What happened:** Entry 2026-09-08, exit 2026-09-14, 34 shares @ $229.64 → $211.20. P&L: **-$625.80**. Hold: 6 dagen. Gestopt out.
**What went wrong:** HIGH confidence maar derde NVDA-entry binnen 4 maanden — de bot blijft hetzelfde aandeel proberen zonder te leren. Na NVDA #1 (-$160) en NVDA #2 (-$60) had dit patroon herkend moeten worden. Op dag 6 was de positie al -7.5% — de hard stop van -5% had eerder getriggerd moeten zijn. Patroon #1 (te laat gestopt) + nieuw patroon: hetzelfde aandeel te vaak opnieuw proberen na verlies.
**Rule change or reminder:** Na twee opeenvolgende verliezen op hetzelfde aandeel: cooldown van minimaal 20 handelsdagen voor een nieuwe entry in dat aandeel.

---

### 2026-08-19 — NVDA #2: -$60 verlies, positie bewoog nauwelijks
**What happened:** Entry 2026-08-10, exit 2026-08-19, 35 shares @ $221.86 → $220.15. P&L: **-$59.77**. Hold: 9 dagen. Gestopt out.
**What went wrong:** HIGH confidence, re-entry na NVDA #1 verlies. Positie bewoog in 9 dagen slechts -0.8% — er was geen momentum. De bot stapte in op een aandeel dat still stond. Geen duidelijke catalyst voor het moment van entry. Patroon #6 (geen momentum bij entry).
**Rule change or reminder:** Een trending stock moet al bewegen bij entry. Eis: prijs +2% of meer in de 5 dagen voor entry. Zo niet → wacht of NO_TRADE.

---

### 2026-08-13 — VGK: +$22 winst — enige winner, maar profit te snel genomen
**What happened:** Entry 2026-08-03, exit 2026-08-13, 14 shares @ $90.82 → $92.39. P&L: **+$22.42**. Hold: 10 dagen. Target reached.
**What went wrong / right:** Dit was MEDIUM confidence ("European equity diversification") — dus ook deze winner had eigenlijk NO_TRADE moeten zijn op basis van de nieuwe regels. De winst (+$22) staat tegenover een gemiddeld verlies van -$430: ratio 1:20. VGK bewoog +1.7% — dat is geen echte momentum move. Target te vroeg genomen.
**Rule change or reminder:** Een winner van +1.7% op 10 dagen is onvoldoende. Minimum target is +8% voor een echte exit. Laat winnaars lopen tot de trailing stop of het profit target.

---

### 2026-07-16 — AMD: -$520, langste verliezende trade (24 dagen)
**What happened:** Entry 2026-06-22, exit 2026-07-16, 14 shares @ $546.19 → $509.02. P&L: **-$520.44**. Hold: 24 dagen. Gestopt out.
**What went wrong:** MEDIUM confidence, thesis "Semiconductor recovery, AI GPU exposure" — generiek. AMD daalde consistent over 24 dagen. Early weakness stop op dag 3 had dit beëindigd bij ~-3% (-$229) i.p.v. -$520. Stuksprijs $546 is hoog. Patroon #1 (te laat gestopt) + #2 (MEDIUM confidence) + #4 (hoge stuksprijs).
**Rule change or reminder:** 24 dagen vastgehouden terwijl alles wees op een mislukte trade. Early weakness stop is niet onderhandelbaar. Had dit op dag 3 gesloten: verlies ~$229 i.p.v. $520.

---

### 2026-06-05 — NVDA #1: -$160, te vroeg ingestapt zonder bevestigd momentum
**What happened:** Entry 2026-05-29, exit 2026-06-05, 23 shares @ $215.99 → $209.04. P&L: **-$160.08**. Hold: 7 dagen. Gestopt out.
**What went wrong:** HIGH confidence, thesis "AI chip leader, momentum play." De positie ging direct na entry omlaag — er was geen momentum op het moment van instappen. RSI of MA-check heeft hier niet goed gefilterd. Op dag 3 stond de positie al negatief — early weakness stop had toen al getriggerd moeten zijn. Patroon #6 (geen momentum bij entry) + #1 (te laat gestopt).
**Rule change or reminder:** HIGH confidence beschermt niet tegen een slechte entry-timing. Controleer altijd of de prijs al in beweging is (momentum zichtbaar) voor je instapt.

---

### 2026-06-10 — GOOGL: -$330, grote positie op MEDIUM confidence
**What happened:** Entry 2026-05-22, exit 2026-06-10, 12 shares @ $385.82 → $358.25. P&L: **-$330.84**. Hold: 19 dagen. Gestopt out.
**What went wrong:** MEDIUM confidence, thesis "Large-cap tech, AI exposure" — 12 shares × $385 = $4.629 risico. Dit is de definitie van een te grote positie op te lage confidence. 19 dagen vastgehouden ondanks consistent verlies. Patroon #1 + #2 + de thesis is volledig generiek (patroon #5 straks).
**Rule change or reminder:** Positiegrootte is altijd gekoppeld aan confidence. MEDIUM confidence = geen trade. NOOIT $4.000+ riskeren zonder HIGH confidence en specifieke thesis.

---

### 2026-06-25 — AAPL: -$16, test positie zonder echte thesis
**What happened:** Entry 2026-05-21, exit 2026-06-25, 1 share @ $301.88 → $285.52. P&L: **-$16.36**. Hold: 35 dagen. Gestopt out.
**What went wrong:** MEDIUM confidence, thesis "Initial test position, defensive tech." 35 dagen vastgehouden voor het kleinste verlies van de portfolio. "Test position" is geen geldige reden om een trade te openen — elke trade moet een volwaardige setup zijn. Patroon #2 (MEDIUM confidence) + patroon #1 (35 dagen voor er actie was).
**Rule change or reminder:** Er bestaan geen "test positions." Elke trade volgt exact dezelfde criteria. Als de setup niet sterk genoeg is voor een volwaardige positie, is het geen trade.

---

## Patroonanalyse (na 10 closed trades)

| # | Patroon | Voorkomt in | Fix |
|---|---------|-------------|-----|
| 1 | **Te laat gestopt** | AAPL (35d), GOOGL (19d), AMD (24d), SNDK (15d), STX (8d) | Early weakness stop verplicht dag 1–3 |
| 2 | **MEDIUM confidence trades genomen** | AAPL, GOOGL, AMD, VGK, MU, SNDK, STX (7 van 10!) | Minimum confidence = HIGH, geen uitzonderingen |
| 3 | **Sector-concentratie** | NVDA+MU zelfde dag, STX+SNDK zelfde week | Max 1 semi / 1 storage tegelijk |
| 4 | **Hoge stuksprijs onderschat** | AMD $546, MU $1017, SNDK $1804, STX $918 | Max $500/share OF max 2 shares + verplichte early weakness stop |
| 5 | **Generieke thesis** | AAPL "defensive tech", GOOGL "AI exposure", AMD "semi recovery" | Thesis moet specifieke catalyst + timing bevatten |
| 6 | **Geen momentum bij entry** | NVDA #1, NVDA #2 | Eis +2% prijsbeweging in 5 dagen vóór entry |
| 7 | **Zelfde aandeel te vaak herproberen** | NVDA: 4 entries, 3 verliezen op rij | Cooldown 20 handelsdagen na 2 opeenvolgende verliezen op zelfde aandeel |
| 8 | **Wins te vroeg genomen** | VGK +$22 (slechts +1.7%) vs avg loss -$430 | Minimum profit target 8%, laat winnaars lopen |

**Kernprobleem:** 8 van 10 trades waren MEDIUM confidence. De strategie zei al dat MEDIUM = NO_TRADE, maar de bot negeerde dat consequent.

---

## Recurring Reminders

- Always check `heartbeat.json` before trading. If the last routine failed, investigate first.
- Never trade in the first 5 minutes after open (9:30–9:35 AM ET) — spreads are wide and volatility is elevated.
- Earnings weeks are high-risk. Exit positions at least 2 days before scheduled earnings unless thesis explicitly includes an earnings catalyst.
- When SPY is down >1% pre-market, reduce position targets by 50% for that day.
- A journal entry is mandatory even on days with zero trades.
- **After every closed trade: immediately write a new lesson block at the top of the Lessons section.** No exceptions.

---

## Automatisch lessen schrijven — Protocol

Na elke gesloten trade schrijft de bot een nieuwe les bovenaan de Lessons-sectie (onder de horizontale lijn):

```markdown
### YYYY-MM-DD — [SYMBOL]: [één zin wat er gebeurde]
**What happened:** Entry [datum], exit [datum], [shares] shares, entry $[prijs], exit $[prijs], P&L [bedrag], hold [dagen] dagen.
**What went wrong / right:** [Root cause — welk patroon uit de tabel herhaalde zich?]
**Rule change or reminder:** [Één concrete actie die dit de volgende keer voorkomt]
```

Regels:
- Elke winnende trade krijgt ook een les ("wat ging goed en waarom, en lieten we de winst ver genoeg lopen?")
- Elke verliezende trade: zoek de **vroegste waarschuwing** die gemist werd
- Vergelijk altijd met de patroonanalyse-tabel — welk patroon herhaalde zich (nummer vermelden)?
- Update de patroonanalyse-tabel als een nieuw patroon ≥2x voorkomt
