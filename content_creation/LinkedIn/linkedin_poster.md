# LinkedIn Post Writer

**Type:** Hybrid (Type C)
**Domain:** Content Creation — LinkedIn
**Project location:** ~/Desktop/linkedin_poster
**Trigger:** User asks to draft, generate, or post a LinkedIn post

---

## Recall from KB (always load before drafting)
- `Content Creation/LinkedIn/LinkedIn Writing Rules.md` — formatting, punctuation, tone, banned phrases, corrector pass
- `Content Creation/LinkedIn/LinkedIn Post Frameworks.md` — post types, outcomes, hook patterns, body structures, CTAs
- `Content Creation/Swipe File/LinkedIn Post Templates.md` — swipe file examples and post templates
- `Content Creation/Communication Style.md` — voice and tone

---

## Phase 1 — Draft in Chat (Pure Skill)

Use when the user gives a topic, idea, or raw content and wants a draft in the conversation.

**Inputs:**
- Topic or idea (required)
- Post type hint (optional — if none, pick based on topic)
- Outcome (optional — if none, pick based on post type)

**Steps:**
1. Identify the best post type from the 8 available (recall `LinkedIn Post Templates.md`)
2. Assign an outcome (EDUCATE / SAVE / LEAD_MAGNET / CONNECT / KEYWORD_CTA)
3. Pick a hook pattern (H1–H13) that fits the topic — vary, don't default to the same one
4. Pick a body structure (S1–S10) — S10 for automation/ops topics, Framework A/B for insightful
5. Draft the post following all writing rules from `Content Style.md`
6. Apply the corrector pass: remove em-dashes, asterisks, banned phrases, check length

**Output:** Final post text, ready to copy-paste. State the post type and outcome used.

---

## Phase 2 — Run Full Pipeline (Execution)

Use when the user wants to go through the automated pipeline: generate → Telegram approval → LinkedIn publish.

### Generate from idea
```bash
cd ~/Desktop/linkedin_poster && python3 main.py --idea "<TOPIC OR IDEA>"
```
Add `--post-type <type>` if user specifies one (insightful / personal / case_study / lead_magnet / industry_update / paradigm_shift / emotional_case_study / offer_post).

### Generate from CMS (auto pick topic)
```bash
cd ~/Desktop/linkedin_poster && python3 main.py
```

### Process Input Queue
```bash
cd ~/Desktop/linkedin_poster && python3 main.py --from-queue
```

### Dry run (test, no saves)
```bash
cd ~/Desktop/linkedin_poster && python3 main.py --dry-run
```

### Record a manually drafted post
```bash
cd ~/Desktop/linkedin_poster && python3 main.py --record-manual-post --post-text "<FULL POST TEXT>"
```
Add `--image-url "<URL>"` if an image was generated.

**After running:** Draft is saved to Google Sheets (Drafts tab) and sent to Telegram for approval. User approves in Telegram → post publishes with AI image.

---

## Phase 3 — Repurpose

Use when the user pastes a reference post and wants it rewritten in their voice.

```bash
cd ~/Desktop/linkedin_poster && python3 main.py --repurpose "<REFERENCE POST>" --repurpose-mode <extract|adapt>
```

- `extract` — take the core idea, write a completely new post
- `adapt` — keep same structure, rewrite every sentence in your voice

---

## Rules
- Always do Phase 1 first (draft in chat) unless user explicitly asks to run the pipeline
- After a chat draft is approved, offer to record it via `--record-manual-post`
- Never invent client names or case study results — ask the user if needed
- Post type weights (for auto selection): insightful 25%, personal 15%, lead_magnet 15%, industry_update 10%, paradigm_shift 10%, case_study 10%, emotional_case_study 10%, offer_post 5%
