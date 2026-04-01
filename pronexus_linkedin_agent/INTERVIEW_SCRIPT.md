# 2-Minute Interview Explanation

I built a staged LinkedIn post generation workflow for a B2B SaaS audience focused on agentic workflows for founders and operators.

The goal was to avoid a single generic prompt and instead make the workflow inspectable end to end. On each run, the app first pulls current trend inputs from multiple sources like Hacker News, Reddit RSS, and tooling or company feeds. Then it analyzes a curated corpus of high-performing B2B LinkedIn creator patterns to extract reusable structure and tone signals such as hook types, formatting rhythm, CTA style, and credibility moves.

From there, it creates two intermediate artifacts: a style guide and a trend brief. Those are then passed into the generation step, which creates a weekly batch of posts under explicit tone and quality constraints. After generation, there is a linting step that flags generic phrasing, weak hooks, or low-specificity writing.

I chose a staged design because it makes the system more reliable and easier to evaluate than just asking a model to write a post from scratch. It also shows that the app is actually grounding on recent trend inputs and learned structural patterns rather than producing disconnected AI text.

If I had more time, I would add similarity checking, A/B hook generation, stronger ranking, and a feedback loop from post performance back into future planning.
