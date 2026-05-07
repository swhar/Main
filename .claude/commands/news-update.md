# /news-update — Daily News Brief

Run each morning for a fast-loading summary of what matters in the world today, filtered for your context and goals.

## Steps

1. Read `memory/profile.md` to understand current goals, focus areas, and values. Note any specific industries, domains, or topics mentioned — these will personalize the tips section. If the profile still contains placeholder template text, note it and skip the personalized tips section at the end.

2. Use WebSearch to find **global news headlines** — search for "top world news headlines today". Extract the 4–5 most significant stories. For each, write one tight sentence: what happened and why it matters globally.

3. Use WebSearch to find **tech and AI news** — search for "AI news today" and "technology news today". Extract the 3–4 most relevant developments. If any story directly intersects with the user's focus areas from their profile, flag it with *(Relevant to your focus: [area])*.

4. Use WebSearch to find **markets and finance snapshot** — search for "stock market today" and "financial markets news today". Report:
   - Major index direction (S&P 500, NASDAQ, Dow) with approximate % move
   - The main macro driver (Fed news, earnings, geopolitical event, economic data)
   - One sentence on overall risk sentiment (risk-on / risk-off and why)

5. Generate **personalized tips** — based solely on what you read in `memory/profile.md` (no additional search needed):
   - Surface 1–2 ways today's news connects to the user's stated goals or current focus areas
   - Offer one actionable suggestion based on the intersection of current events and their profile
   - If the profile is empty or still contains placeholder text, skip this section and note: "Fill in `memory/profile.md` to unlock personalized tips."

6. Present everything in the format below. Do **not** save this output to any file.

---

## Daily News Brief — [Weekday, Month Day Year]

### Global Headlines
- **[Story headline]** — [One sentence: what happened and why it matters]
- **[Story headline]** — [One sentence]
- **[Story headline]** — [One sentence]
- **[Story headline]** — [One sentence]

### Tech & AI
- **[Development]** — [One sentence] *(Relevant to your focus: [area] — if applicable)*
- **[Development]** — [One sentence]
- **[Development]** — [One sentence]

### Markets Snapshot
- **Indices:** S&P [direction+%] · NASDAQ [direction+%] · Dow [direction+%]
- **Driver:** [Main macro event or catalyst]
- **Sentiment:** [Risk-on / Risk-off — one sentence explanation]

### For You
- **[Goal/focus area]:** [Insight connecting today's news to user's profile]
- **Today's angle:** [One actionable suggestion based on profile + news intersection]

---

7. After displaying the brief, ask: "Anything here you want to dig into? Use `/research <topic>` for a deep dive, or `/briefing` to move into your day plan."
