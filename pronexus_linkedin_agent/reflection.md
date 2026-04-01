# Reflection and Scaling

## Architecture overview

This workflow is intentionally staged instead of relying on one monolithic prompt.

### Pipeline
1. **Trend ingestion layer**
   - pulls current inputs from Hacker News, Reddit RSS, and tooling/company feeds
   - normalizes them into a single item schema
2. **Style-learning layer**
   - reads an abstracted corpus of strong B2B creator patterns
   - extracts a style guide influenced by patterns, not copied language
3. **Planning layer**
   - turns raw trend inputs into a trend brief relevant to the chosen audience and positioning
4. **Generation layer**
   - creates a weekly batch of posts under clear tone and quality constraints
5. **Evaluation layer**
   - lints the posts for weak hooks, fluff, and vague claims

## Prompting decisions

### Why separate prompts?
A single prompt can generate plausible content, but it hides whether the system is actually learning structure and using current trend inputs. The staged design makes the reasoning artifacts visible:
- style guide
- trend brief
- final post batch
- lint output

### Why an abstracted corpus?
The requirement asks to learn what performs on LinkedIn while avoiding copied language. Using structured notes about patterns makes the system safer and more defensible than storing full creator posts.

### Why hard-code the initial industry and topic?
For an interview demo, consistency matters. A narrower scope produces more credible output and reduces prompt drift.

## Tradeoffs

### Pros
- simple to deploy
- easy to explain
- visible intermediate outputs
- fresh trend inputs every run
- strong assignment coverage with a small codebase

### Cons
- corpus quality is only as good as the curated seed set
- source relevance is mixed and needs ranking
- no real feedback loop from actual LinkedIn performance yet
- no persistent storage yet for weekly learning

## If I had more time

### Make it more intelligent
- add source ranking and relevance scoring before trend briefing
- add post planning objects before generation
- add per-post audience targeting and content archetype selection
- add automatic A/B hook generation and reranking

### Make it more cost-effective
- cache trend fetches for a few hours
- cache style guide unless corpus changes
- use a smaller model for linting and ranking
- only regenerate weak posts instead of full batches

### Make it safer
- add plagiarism and similarity screening against the creator corpus
- add claim verification for product/news references
- add banned-phrase and overclaim rules
- log sources used per post for auditability

### Make it more scalable
To scale from dozens to hundreds of posts per week while keeping quality high:
- move ingestion and generation to async workers
- store trend items, briefs, style guides, and posts in a database
- shard generation by audience/topic cluster
- add batch evaluation and reranking
- use human review only for low-confidence outputs
- create a feedback loop from post performance metrics into future planning

## Quality strategy at larger scale
A scalable version should separate:
- **planning** (what angles are worth covering)
- **writing** (draft generation)
- **evaluation** (hook strength, specificity, originality)
- **selection** (publish or revise)

That allows the system to operate more like a content pipeline than a single text generator.
