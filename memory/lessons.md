# Lessons Learned

Agent appends new lessons here after significant trades or market events. Read before every session.

---

## Format

Each lesson follows this template:

```
### YYYY-MM-DD — [Brief Title]
**What happened:** [Describe the trade or event]
**What went wrong / right:** [Root cause or insight]
**Rule change or reminder:** [What to do differently, or confirm what to keep doing]
```

---

## Lessons

### 2026-06-25 — AAPL: MEDIUM confidence trade met minimale positiegrootte
**What happened:** AAPL gekocht op MEDIUM confidence als "initial test position". 1 share, $301.88 entry. Na 35 dagen gestopt op $285.52. Verlies: -$16.36.
**What went wrong:** MEDIUM confidence trades zouden NO_TRADE moeten zijn. Dit was een experimentele positie zonder duidelijke thesis — "defensive tech" is geen edge. 35 dagen vastgehouden zonder winst zegt genoeg: de setup werkte nooit.
**Rule change or reminder:** Geen MEDIUM confidence trades. Minimum is HIGH. Als de thesis niet in één zin scherp te omschrijven is, is het geen trade.

---

### 2026-06-10 — GOOGL: grote positiegrootte op MEDIUM confidence
**What happened:** GOOGL gekocht op MEDIUM confidence, 12 shares à $385.82 = $4.629. Na 19 dagen gestopt op $358.25. Verlies: -$330.84.
**What went wrong:** $4.600 risico op een MEDIUM confidence trade. Dit is precies het tegenovergestelde van wat de strategie zegt. De thesis "Large-cap tech, AI exposure" is generiek — dat is geen reden om 8% van portfolio te riskeren.
**Rule change or reminder:** Positiegrootte is altijd gekoppeld aan confidence. MEDIUM = geen trade. HIGH = max 8%. Generieke sector-theses ("AI exposure") tellen niet als specifieke entry-reden.

---

### 2026-06-05 — NVDA #1: te vroeg ingestapt, te snel gestopt
**What happened:** NVDA gekocht op HIGH confidence, 23 shares à $215.99. Na slechts 7 dagen gestopt op $209.04. Verlies: -$160.08.
**What went wrong:** Positie werkte nooit — direct na entry begon de daling. De hard stop (5%) was correct, maar de entry zelf was slecht getimed. RSI of MA-check heeft hier niet goed gefilterd.
**Rule change or reminder:** Controleer bij entry altijd of de prijs al boven MA20 én MA50 staat én de RSI tussen 35–70 valt. Als de setup binnen 3 dagen 3% of meer verliest, is dat bewijs de entry verkeerd was — early weakness stop toepassen.

---

### 2026-07-16 — AMD: langste verliesgevende trade (24 dagen)
**What happened:** AMD gekocht, 14 shares à $546.19 = $7.646. Na 24 dagen gestopt op $509.02. Verlies: -$520.44.
**What went wrong:** 24 dagen vastgehouden terwijl de positie consistent verloor. De early weakness stop (−3% binnen 3 dagen) zou hier veel eerder hebben ingegrepen. AMD bewoog ook in een brede techcorrectie — macro-context (SPY t.o.v. MA50) was waarschijnlijk negatief.
**Rule change or reminder:** Early weakness stop is niet optioneel. Als een positie binnen de eerste 3 dagen −3% staat, exit zonder discussie. 24 dagen wachten kost viermaal zo veel als eerder stoppen.

---

### 2026-08-13 — VGK: enige winnende trade — wat ging goed?
**What happened:** VGK (Europa ETF) gekocht, 14 shares à $90.82. Na 10 dagen verkocht op $92.39. Winst: +$22.42.
**What went wrong / right:** Dit is de enige winnende trade van de tien. Wat opvalt: lage volatiliteit instrument (Europa ETF), duidelijke target bereikt, 10 dagen hold — niet te lang vastgehouden. Maar de winst (+$22) is kleiner dan het gemiddeld verlies (-$430). Dat is het kernprobleem van de strategie.
**Rule change or reminder:** Een winnende trade moet minimaal 2× het gemiddelde risico opleveren (risk/reward ≥ 1:2). VGK winst van $22 tegenover een gemiddeld verlies van $430 is een ratio van 1:20 — volledig onhoudbaar. Profit targets moeten agressiever: pas verkopen bij +8–12%, niet bij de eerste kleine winst.

---

### 2026-08-19 — NVDA #2: tweede poging NVDA, zelfde patroon
**What happened:** NVDA opnieuw gekocht, 35 shares à $221.86. Na 9 dagen gestopt op $220.15. Verlies: -$59.77.
**What went wrong:** Tweede NVDA-trade in korte tijd, bijna op break-even gestopt. De positie bewoog nauwelijks — er was geen momentum. Als een aandeel na 7+ dagen nauwelijks beweegt, is er geen trend om op te rijden.
**Rule change or reminder:** Een trending stock moet al bewegen op het moment van entry. Als een positie na 5 dagen minder dan 2% in jouw richting beweegt, is er geen momentum — overweeg vroegtijdig exit, ook al is de stop nog niet geraakt.

---

### 2026-09-14 — NVDA #3 + MU: beide gestopt op dezelfde dag, grote verliezen
**What happened:** NVDA (34 shares à $229.64) en MU (7 shares à $1017.84) beide gekocht op 2026-09-08 en beide gestopt op 2026-09-14. NVDA verlies: -$625.80. MU verlies: -$723.54. Totaal op één dag: -$1.349.
**What went wrong:** Twee grote posities tegelijk geopend in sterk gecorreleerde sectoren (semis). Toen de semimarkt draaide, verloor de bot op beide posities tegelijk. Dit is het concentratierisico in de praktijk. Bovendien was MU entry op $1.017 een extreem hoge stuksprijs — kleine beweging = groot verlies in dollars.
**Rule change or reminder:** Nooit twee semis tegelijk houden als grote posities. Sector-correlatie telt als geconcentreerd risico. Bij aandelen boven $500 per share: pas de positionering extra conservatief aan (minder shares). Verspreid entries over verschillende dagen.

---

### 2026-10-06 — SNDK: 15 dagen vastgehouden tot volledig stop
**What happened:** SNDK 4 shares à $1.804.86 = $7.219. Na 15 dagen gestopt op $1.672.29. Verlies: -$530.28.
**What went wrong:** Hoge stuksprijs ($1.800+), kleine aantalposities maar groot dollarrisico. 15 dagen vastgehouden terwijl de positie consistent daalde. Geen early weakness stop toegepast in de eerste 3 dagen.
**Rule change or reminder:** Bij aandelen met een stuksprijs boven $500: maximaal 2–3 shares, en de early weakness stop (−3% in 3 dagen) is verplicht. SNDK van $1.800 naar $1.672 is −7.3% — dat was ruimschoots binnen de 5% hard stop die eerder getriggerd had moeten worden.

---

### 2026-10-02 — STX: grootste verlies van de portfolio
**What happened:** STX was de slechtste trade: verlies -$922.72 (exacte entry/exit uit performance.md).
**What went wrong:** Dit is de worst trade. STX is een storage-aandeel — fundamenteel anders dan de AI/semi thesis van de rest van de bot. Het paste niet in de strategie. Grote positiegrootte op een instrument buiten de kernthesis.
**Rule change or reminder:** Elk aandeel dat de bot overweegt moet expliciet passen in de Markov+momentum screeningcriteria. "Opportunistisch" instappen op een aandeel buiten de universe is verboden. STX zit wel in de universe maar als storage play — alleen handelen als het ook de AI-infrastructuurthesis ondersteunt.

---

## Patroonanalyse (na 10 trades)

Dit zijn de terugkerende fouten op basis van alle gesloten trades:

| # | Patroon | Voorkomt in | Fix |
|---|---------|-------------|-----|
| 1 | **Te laat gestopt** | GOOGL, AMD, SNDK, STX | Early weakness stop verplicht dag 1–3 |
| 2 | **MEDIUM confidence trades genomen** | AAPL, GOOGL | Minimum confidence = HIGH |
| 3 | **Sector-concentratie** | NVDA+MU zelfde dag | Max 1 semi tegelijk |
| 4 | **Wins te vroeg genomen** | VGK +$22 vs avg loss -$430 | Risk/reward min 1:2, profit target ≥8% |
| 5 | **Hoge stuksprijzen onderschat** | MU $1017, SNDK $1804 | Max $500/share OF extra conservatief |
| 6 | **Geen momentum bij entry** | NVDA #2 (nauwelijks bewogen) | Entry alleen als trend al zichtbaar is |

---

## Recurring Reminders

- Always check `heartbeat.json` before trading. If the last routine failed, investigate first.
- Never trade in the first 5 minutes after open (9:30–9:35 AM ET) — spreads are wide and volatility is elevated.
- Earnings weeks are high-risk. Exit positions at least 2 days before scheduled earnings unless thesis explicitly includes an earnings catalyst.
- When SPY is down >1% pre-market, reduce position targets by 50% for that day.
- A journal entry is mandatory even on days with zero trades.
- **After every closed trade: immediately write a new lesson block above the Patroonanalyse section.** No exceptions.

---

## Automatisch lessen schrijven — Protocol

Na elke gesloten trade schrijft de bot een nieuwe les in dit formaat bovenaan de Lessons-sectie:

```markdown
### YYYY-MM-DD — [SYMBOL]: [één zin wat er gebeurde]
**What happened:** Entry [datum], exit [datum], [shares] shares, entry $[prijs], exit $[prijs], P&L [bedrag], hold [dagen] dagen.
**What went wrong / right:** [Concrete root cause — niet generiek]
**Rule change or reminder:** [Één specifieke actie of regel die dit voorkomt]
```

Regels:
- Elke winnende trade krijgt ook een les ("wat ging goed en waarom")
- Elke verliezende trade: zoek de **vroegste waarschuwing** die gemist werd
- Vergelijk altijd met de patroonanalyse hierboven — welk patroon herhaalde zich?
- Update de patroonanalyse-tabel als een nieuw patroon ≥2x voorkomt
