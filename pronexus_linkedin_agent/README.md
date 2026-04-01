# Pronexus LinkedIn Post Agent

A hosted-demo friendly workflow for generating a weekly batch of high-signal LinkedIn posts for a B2B SaaS startup.

## What this project does

On each run, the app:
1. Pulls current trend inputs from multiple sources.
2. Distills pattern signals from a seed corpus of strong B2B LinkedIn creators.
3. Produces a reusable style guide.
4. Creates a trend brief relevant to a chosen audience and positioning.
5. Generates a fresh batch of LinkedIn posts.
6. Runs a lightweight lint step to flag weak or generic writing.

## Chosen setup

- **Industry:** B2B SaaS founders and operators
- **Topic focus:** Agentic workflows for content and operations
- **Why this choice:** It is specific enough to generate credible, concrete posts, but broad enough to stay relevant across current AI and workflow trends.

## Repo structure

- `app.py` — Streamlit app and workflow orchestration
- `trend_sources.py` — lightweight ingestion from Hacker News, Reddit RSS, and tooling/company feeds
- `linkedin_corpus.py` — abstracted high-performing creator pattern corpus
- `prompts.py` — all prompts used by the workflow
- `reflection.md` — design choices, tradeoffs, scaling plan
- `submission_email_draft.md` — draft submission email

## Local run

```bash
pip install -r requirements.txt
cp .env.example .env
streamlit run app.py
```

## Deploy quickly

### Streamlit Community Cloud
1. Push this folder to GitHub.
2. Create a new Streamlit app.
3. Set the main file to `app.py`.
4. Add `OPENAI_API_KEY` in app secrets.
5. Deploy.

### Other simple options
- Render
- Railway
- Hugging Face Spaces with Streamlit

## Notes on freshness

The app fetches mixed-source trend inputs at runtime, so clicking **Generate new posts** produces fresh input context each time. With a configured `OPENAI_API_KEY`, the posts are also freshly generated on each run. Without an API key, the app still demonstrates the workflow using a fallback generation mode.

## Required capability mapping

### A) Learn what performs on LinkedIn
- Uses an abstracted creator corpus to extract:
  - hook patterns
  - line-break / formatting norms
  - CTA behavior
  - credibility moves
  - typical post length tendencies
- Outputs a **style guide** rather than copying source text.

### B) Track latest trends
- Pulls from multiple source types:
  - Hacker News
  - Reddit
  - AI/tooling company feeds
  - Product/tool launch feed
- Produces a **trend brief** relevant to the chosen audience.

## Prompting strategy

The workflow uses four stages:
1. **Style extraction** — derive reusable voice and structure rules from a creator pattern corpus.
2. **Trend synthesis** — convert noisy multi-source items into a compact brief with implications.
3. **Post generation** — combine audience, tone, constraints, style guide, and trend brief to produce posts.
4. **Linting** — score and critique the outputs for specificity, hook strength, clarity, and originality.

## Design choices and tradeoffs

- **Seed corpus instead of raw scraping:** faster, safer, and avoids directly copying creators.
- **RSS/API-friendly sources:** easy to deploy and demo without brittle scraping.
- **Single-button UX:** optimized for the assignment requirement.
- **Hard-coded initial audience/topic:** reduces failure modes and makes the demo more consistent.
- **Visible intermediate artifacts:** style guide and trend brief prove that the workflow is not just “one big prompt.”

## What to submit

- deployed URL
- GitHub repo URL
- `prompts.py` or a prompt doc URL in repo
- summary of architecture, prompting choices, reflection, and scaling plan
# pronexus-linkedin-agent
# pronexus-linkedin-agent
