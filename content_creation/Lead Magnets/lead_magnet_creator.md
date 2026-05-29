# Lead Magnet Creator

**Type:** Hybrid (Type C)
**Domain:** Content Creation — Lead Magnets
**Project location:** ~/Desktop/lead-magnet-creator
**Skill:** `/lead-magnet` (already installed in Claude Code)
**Trigger:** User wants to package an asset, framework, or idea as a free shareable resource

---

## Recall from KB (load before drafting)

- `Content Creation/Lead Magnets/Lead Magnet Formats and Decision Tree.md` — format types, decision tree, per-format publish instructions
- `Content Creation/Lead Magnets/Lead Magnet Voice and Generosity Rules.md` — generosity contract, CTA table, voice registers, slop scrub
- `Content Creation/Communication Style.md` — general voice and tone

---

## Phase 1 — Draft in Chat

### Step 0: Choose mode

- **Create** — build a new magnet from an asset or idea (default)
- **Repurpose** — refresh an existing magnet
- **From notes** — restructure raw knowledge into an educational magnet

If the user's message implies a mode, pick silently.

### Step 1: Gather input

Batch these into one ask if not already provided:
1. What's the asset? Outcome promise in one sentence (result, not topic).
2. The single specific story or number that anchors it.
3. Format — or pick one using the decision tree from KB.
4. Distribution: ungated / gated comment-keyword / both.
5. Voice: operator-voice body (default) or AUTHOR-voice throughout.
6. Anything off-limits?

### Step 2–4: Analyze, pick format, match CTA

- Identify what the asset is, who it helps, core value, sophistication level.
- Apply the format decision tree (KB: Formats and Decision Tree).
- Match topic to CTA table (KB: Voice and Generosity Rules).

### Step 5–6: Create folder and draft content

```bash
mkdir -p ~/Desktop/lead-magnet-creator/lead-magnets/<slug>
```

Draft the magnet applying AUTHOR/OPERATOR voice registers and corpus voice anchoring from `corpus.md`.

### Step 7: Slop scrub

Run mandatory slop scrub (KB: Voice and Generosity Rules) before publishing. Fix every hit.

---

## Phase 2 — Publish

### Publish to Notion

```bash
# Write payload first:
# /tmp/lm_notion_payload.json → {"title": "...", "content": "...full markdown..."}
python3 ~/Desktop/lead-magnet-creator/scripts/publish_notion.py /tmp/lm_notion_payload.json
```

Requires: `NOTION_TOKEN`, `NOTION_PARENT_PAGE_ID`

### Publish to GitHub

```bash
# Write payload first:
# /tmp/lm_github_payload.json → {"repo_name": "...", "description": "...", "files": {...}}
python3 ~/Desktop/lead-magnet-creator/scripts/publish_github.py /tmp/lm_github_payload.json
```

Requires: `GITHUB_TOKEN`, `GITHUB_USERNAME`

Capture the URL printed to stdout from each script.

---

## Phase 3 — Log in Notion Content DB

After publishing, create a row in Notion Content DB (`NOTION_CONTENT_DB_ID`):

- **Title**: magnet display title
- **Format**: `Lead Magnet`
- **Channel**: `LinkedIn` (default)
- **Pillar**: `Educational / Tactical`
- **Status**: `Idea` / `Scripting` / `Scheduled`
- **Drive Assets**: canonical public URL
- **Page body**: 1-paragraph summary, comment-keyword (if gated), public URL, outcome promise

Skip if `NOTION_CONTENT_DB_ID` is not set — note it for the user.

---

## Rules

- Always Phase 1 first (draft in chat). Only run publisher scripts after draft is approved.
- Never default to PDF — pick the format that fits the content.
- Slop scrub is mandatory before every publish. No exceptions.
- After publishing, offer to chain into launch post: "Want me to draft the launch post? `/linkedin-copywriter` can pick the right hook."
- Don't fabricate stats or client names. Ask if a number is needed.
- Every magnet ends with one canonical public URL.
