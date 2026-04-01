Subject: Pronexus interview assignment submission

Hi Erica,

Please find my submission for the Software Engineer Intern take-home below.

1. Hosted demo:
[PASTE DEPLOYED URL]

2. GitHub repo:
[PASTE GITHUB REPO URL]

3. Prompt files on GitHub:
[PASTE GITHUB URL TO prompts.py OR A PROMPTS DOC]

4. Optional video demo:
[PASTE YOUTUBE URL IF INCLUDED]

Quick summary:
I built a staged LinkedIn post generation workflow for a B2B SaaS audience focused on agentic workflows for founders and operators. The system pulls fresh trend inputs from multiple sources, extracts reusable structure and tone patterns from a curated corpus of high-performing B2B creator styles, creates a trend brief, generates a weekly batch of posts, and then lints the outputs for specificity and hook strength.

I chose a staged design instead of a single prompt so the workflow is inspectable end to end. The intermediate artifacts — style guide, trend brief, final posts, and lint output — make it clear how the system learns structure, incorporates current inputs, and evaluates quality.

Reflection / scaling highlights:
- I would next add source relevance ranking, A/B hook generation, similarity checks, and a performance feedback loop.
- To scale from dozens to hundreds of posts per week, I would move generation to async workers, persist artifacts in a database, and introduce automated reranking plus human review only for low-confidence outputs.
- To improve safety and quality, I would add claim verification, anti-copy similarity checks, and stricter linting around vague or overhyped language.

Thanks for your time — I’d be happy to walk through the architecture and prompt design live.

Best,
Karthik
