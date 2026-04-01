# 3-Minute Video Demo Script

## 1. Intro
Hi, this is my submission for the Pronexus Software Engineer Intern assignment. I built a LinkedIn post generation workflow for a B2B SaaS startup audience focused on agentic workflows.

## 2. Show the app
On the left side, I can configure the industry, topic focus, audience, positioning, tone, and post count. For the demo, I kept the default configuration focused on founders and operators at B2B SaaS companies.

## 3. Explain the workflow
When I click **Generate new posts**, the app runs a staged pipeline:
- it pulls current trend inputs from multiple sources
- it extracts style signals from a curated corpus of strong B2B LinkedIn examples
- it builds a style guide
- it synthesizes a trend brief
- it generates a fresh weekly batch of posts
- it lints the outputs for quality

## 4. Click Generate
Click **Generate new posts**.

## 5. Walk through outputs
First, here is the style guide. This shows the structural patterns the workflow learned, like hook types, spacing, and credibility moves.

Next, here is the trend brief. This condenses current source inputs into angles that matter for the chosen audience.

Then here are the generated posts. These are the actual copy-paste-ready LinkedIn drafts.

Finally, here is the lint output, which critiques the posts for clarity, specificity, and hook strength.

## 6. Close
I chose this staged architecture because it is more transparent and controllable than a single prompt. If I extended it further, I would add similarity checks, post ranking, and a real performance feedback loop.
