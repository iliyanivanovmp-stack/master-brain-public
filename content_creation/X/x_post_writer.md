# X Post Writer

**Type:** Hybrid (Type C)
**Domain:** Content Creation — X (Twitter)
**Project location:** ~/Desktop/x-post-writer
**Trigger:** User asks to draft, generate, or post an X/Twitter post or thread

---

## Recall from KB (always load before drafting)

- `Content Creation/X (Twitter)/X Post Writing Frameworks.md` — hook patterns H1-H8, body shapes S1-S5/T1-T3, CTA rules, slop scrub, voice register
- `Content Creation/X (Twitter)/X Platform Culture.md` — platform voice, cadence, content pillars, LinkedIn imports to avoid
- `Content Creation/Communication Style.md` — voice and tone

---

## Phase 1 — Draft in Chat (Pure Skill)

Use when the user gives a topic, idea, number, or raw content and wants a tweet or thread drafted in conversation.

**Inputs:**
- Source: a fact, metric, failure, lesson, or hot take (required — must have at least one specific number)
- Post type hint (optional — if none, pick based on topic)
- Format hint: solo or thread (optional — default solo)

**Steps:**
1. Identify the best post type from the 11 available (recall `X Post Writing Frameworks.md`)
2. Pick a hook pattern (H1-H8) that fits the content — vary, don't default to the same one
3. Pick a body shape (S1-S5 for solo, T1-T3 for thread)
4. Assign voice register (lowercase or sentence case)
5. Draft following all writing rules from `X Post Writing Frameworks.md`
6. Run slop scrub before showing output
7. Output: draft in code block + format / char count / hook / body / voice / slop scrub result / why it works / alt hook

**Default output:** 1 solo tweet + 1 alt solo from a different hook. If thread requested: thread + 1 solo variant.

---

## Phase 2 — Run Full Pipeline (Execution)

Use when the user wants to run the automated pipeline: generate → Telegram approval → Twitter publish.

### Generate a single post (pick type manually)
```bash
cd ~/Desktop/x-post-writer && python3 test_generator.py [post_type] [format]
```
`post_type` — one of: case_study, contrarian_take, system_breakdown, ai_income, lead_magnet, milestone, lesson, hot_take, build_in_public, ip_giveaway, self_roast (omit for random)
`format` — solo (default) or thread (lesson and ip_giveaway only)

### Run the full orchestrator
```bash
cd ~/Desktop/x-post-writer && python3 main.py
```
Generates post, sends to Telegram for approval, publishes to Twitter on approval.

### Absorb a high-performing post into the post bank
```bash
cd ~/Desktop/x-post-writer && python3 absorb_post.py "<POST TEXT>"
```

### Deploy to Modal (cloud)
```bash
cd ~/Desktop/x-post-writer && modal deploy modal_app.py
```

**After running:** Draft is sent to Telegram. Approve there → posts to Twitter. Results logged to Google Sheets.

---

## Post Type Weights (for auto/random selection)

```
case_study 15%       contrarian_take 15%   system_breakdown 15%
ai_income 15%        lead_magnet 10%
milestone 10%        lesson 15%            hot_take 15%
build_in_public 15%  ip_giveaway 10%       self_roast 10%
```

---

## Rules

- Always do Phase 1 first (draft in chat) unless user explicitly asks to run the pipeline
- Never invent numbers — ask the user if no specific fact is provided
- Solo by default; thread only if the idea genuinely needs 4-7 beats
- Two solo tweets beats a 3-tweet thread
- The x-copywriter Claude skill lives at `~/Desktop/x-post-writer/x-copywriter/SKILL.md` — load it for deeper drafting guidance
