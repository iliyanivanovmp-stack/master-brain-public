# Lead Magnet Formats and Decision Tree

## What a lead magnet can be

A lead magnet is a free asset given away on LinkedIn or a website. Format is a decision, not a default:

- Notion page
- Google Doc
- Designed PDF
- Google Sheet (calculator, scorecard, tracker)
- Claude Code Skills repo (installable into a reader's `~/.claude/skills/`)
- GitHub starter repo (code drop, n8n template, agent template)
- Custom GPT
- Small interactive web tool (audit, calculator)
- Recorded video / Loom
- Vault bundle (3-5 of the above behind one CTA)

---

## Format decision tree

| Asset type | Default format |
|---|---|
| n8n workflow (JSON/YAML) | GitHub starter repo |
| Claude Code skill (markdown) | Claude Code Skills repo |
| Code, scripts, config files | GitHub starter repo |
| Notion template / database | Notion page |
| Framework / checklist / guide / playbook | Notion page |
| Calculator / scorecard / tracker | Google Sheet |
| Step-by-step system, portfolio piece | PDF |
| Repeat-use AI tool | Custom GPT |
| Interactive web experience | Web tool |
| Walkthrough / tutorial | Video / Loom |
| Mixed (workflow + written explainer) | Vault bundle |

Explicit user instruction overrides the table. If it's unclear, ask.

---

## Per-format authoring and publish

### A. Notion page

**Pick when:** content is naturally hyperlinked, includes screenshots, references other Notion pages, or will be updated over time. Long-form playbooks fit here.

**Source file:** `lead-magnets/<slug>/page.md`

**Structure:**
- Benefit-first title
- 2-3 sentence hook (what it is, who it's for, specific result)
- Main content (steps/bullets/headings)
- Subtle CTA

**Publish:** Python publisher writes markdown to Notion blocks under `NOTION_PARENT_PAGE_ID`.

**Title examples:**
- Bad: "My n8n Lead Sourcing Workflow"
- Good: "The Exact Workflow We Use to Source 50 Warm Leads a Day Without Touching LinkedIn"

---

### B. Google Doc

**Pick when:** the magnet should feel collaborative — comments enabled, reader makes a copy to annotate.

**Source file:** `lead-magnets/<slug>/doc.md`

**Publish:**
1. Render to `.docx` via `python-docx`
2. Upload to Drive with `mimeType: application/vnd.google-apps.document`
3. Set sharing to "anyone with the link can view"

---

### C. PDF

**Pick when:** the magnet doubles as a portfolio piece — designed layout, cover that screenshots well.

**Source file:** `lead-magnets/<slug>/magnet.html` + `_print.css`

**Structure:** 6-10 letter pages, one `<section class="page">` each. Two-line cover hero: `[outcome].<br/><em>[mechanism].</em>`

**Publish:** Headless Chrome render → upload to Drive Lead Magnets folder.

**Smoke checks before render:**
- `grep -c '—' magnet.html` must be 0
- `grep -n '{{' magnet.html` must be empty

---

### D. Google Sheet

**Pick when:** the value is "punch in your numbers and see your answer" — calculators, scorecards, trackers.

**Source file:** `lead-magnets/<slug>/sheet.py` (builds `.xlsx` via `openpyxl`)

**Publish:** Run script → upload to Drive with `mimeType: application/vnd.google-apps.spreadsheet` → sharing "anyone can VIEW" (reader copies to use).

Include a "Read me first" tab with outcome promise, instructions, and CTA.

---

### E. Claude Code Skills repo

**Pick when:** the value is repeatable behavior, not a one-off artifact. Examples: `/cold-email` skill, `/icp-audit` skill.

**Source:** `lead-magnets/<slug>/skills/<skill-name>/SKILL.md` per skill + top-level `README.md`

Each SKILL.md follows standard frontmatter (`name`, `description`) + When-to-invoke + Workflow + Voice rules + Don'ts. Add `LICENSE` (MIT or 0BSD).

**Publish:** GitHub Python publisher. Repo name: kebab-case-benefit-description.

---

### F. GitHub starter repo

**Pick when:** reader clones, sets up, and runs a full project — cold-email system, n8n template, Trigger.dev agent.

**Source:** `lead-magnets/<slug>/repo/`

README: benefit-first title, 2-3 line intro, what it does, prerequisites, numbered setup steps, expected output. Include working `.env.example`.

**Publish:** GitHub Python publisher.

---

### G. Custom GPT

**Pick when:** repeat-use tool the reader pins in ChatGPT sidebar — audits, rewriters, coaches, idea generators.

**Source file:** `lead-magnets/<slug>/gpt-spec.md` with: Name, description (<300 chars), full system prompt, 4 conversation starters, knowledge files list, capabilities toggles.

**Publish: manual.** Cannot be automated. Output the spec for the user to copy-paste into the GPT builder. Ask them to paste the GPT URL back after publishing.

---

### H. Web tool

**Pick when:** the value is interactive — cold-email score, acquisition calculator, profile audit form.

**Stack:** Next.js + Vercel, or static HTML + webhook.

**Deploy:** Vercel under `aiessentials.us/free/<slug>` or a subdomain. Canonical URL must not be `*.vercel.app` in production.

---

### I. Video / Loom

**Pick when:** the asset is the video — 5-minute walkthrough, recorded webinar, "roast my profile" Loom.

**Source file:** `lead-magnets/<slug>/script.md` — hook, beats, close outline + thumbnail brief.

**Publish:** Record manually. Loom: set to "public". YouTube: Unlisted default. Archive MP4 to Drive Videos folder.

---

### J. Vault bundle

**Pick when:** combining 3-5 formats behind one CTA. Classic: PDF + Notion + GPT gated behind one comment-keyword.

**Structure:** Each component in its own subfolder `lead-magnets/<vault-slug>/<component-name>/`. Top-level `index.md` lists all components with outcome promises and URLs.

**Publish:** Each component via its own format pipeline. One comment-keyword DMs the wrapper URL.

---

## Distribution modes

**Ungated public link** (default for "be generous" briefs):
- Anyone grabs without commenting
- Linked from LinkedIn featured section, bio, and launch post

**Gated comment-keyword DM:**
- Reader comments a keyword. Bot or you DMs the canonical URL.

**Both** (recommended default for launch posts):
- Public URL in bio / featured section / website
- Comment-keyword on the launch post for engagement lift

Record the comment-keyword and canonical URL in the Notion Content DB row so `/linkedin-copywriter` can pull both into the launch post draft.

---

## Local folder structure

Each magnet lives at `lead-magnets/<magnet-slug>/`. Slug is kebab-case, descriptive, no date. Source files stay in git; large renders (PDFs, PNGs) go to Drive or stay local-only.

```bash
mkdir -p lead-magnets/<magnet-slug>
```
