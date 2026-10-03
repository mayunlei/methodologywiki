---
title: "Lean Startup: Build-Measure-Learn, Validated Learning and Pivots"
description: "The Lean Startup treats a new venture as a set of hypotheses to test through Build-Measure-Learn cycles and minimum viable products. Learn validated learning, innovation accounting, the four steps of customer development, types of pivot, an experiment template and common mistakes."
---

# The Lean Startup

The most common reason startups fail isn't that the product was badly built. It's that they built **a good product nobody wanted**. A team works in private for a year, launches, and only then discovers the market isn't interested, by which point the money and the time are gone. The **Lean Startup** method exists to prevent that ending: it treats a new venture as a series of **hypotheses to be tested**, not a plan to be executed.

Eric Ries set out the approach in his 2011 book of the same name, drawing on two sources: Toyota's [lean production](../../Strategy & Business/quality_and_operations/Lean-Operations-Tutorial-en.md) (eliminate everything that doesn't create value) and Steve Blank's **Customer Development** methodology (get out of the building and validate). In a startup, the biggest waste of all is **building features nobody uses**.

The engine is the **Build-Measure-Learn loop** — and the crucial detail is that you **plan it backwards and execute it forwards**: first decide what you need to learn, then what to measure, and only then what to build.

!!! abstract "Key takeaways"

    - **Treat the venture as an experiment**: every line of the business plan is a hypothesis, not a fact.
    - **The loop**: build the smallest thing → measure real behavior → learn whether the hypothesis holds → repeat.
    - **Plan backwards**: learn → measure → build.
    - **Validated learning** relies on behavior, not on survey answers saying "I would use this".
    - **Three possible outcomes**: persevere, pivot or stop. Define the criteria in advance.

## Three Core Concepts

### 1. Validated Learning

In the early stage, the real output isn't code; it is **reliable knowledge about what works**. Progress is measured not by "how many features we shipped" but by "how many hypotheses we validated".

The key is to **validate with behavior rather than opinion**. A user saying "this would be useful" carries almost no information. A user paying for it, or returning in week two, does.

### 2. The Build-Measure-Learn Loop

| Stage | What you do | Key principle |
| --- | --- | --- |
| **Build** | Create the smallest thing that can test the hypothesis | Not "version 1.0 with fewer features" but "the smallest experiment that yields reliable learning" — see [MVP](../testing_and_validation/MVP-Tutorial-en.md) |
| **Measure** | Collect real user behavior | Use actionable metrics, not vanity metrics |
| **Learn** | Decide whether the hypothesis holds | Set the success criterion in advance so you can't rationalize afterwards |

**Cycle speed matters more than single-cycle perfection.** A team that completes a loop monthly learns far more than one that completes a loop annually.

### 3. Innovation Accounting

Traditional financial metrics are near zero early on and say nothing about progress. Innovation accounting works in three moves:

1.  **Establish a baseline** with a rough MVP: for example, 4% signup conversion and 12% month-two retention.
2.  **Tune the engine**: make targeted improvements and see whether the metrics move toward what the business model requires.
3.  **Decide to persevere or pivot**: if several rounds of effort don't move the numbers, a foundational hypothesis is wrong.

**Beware vanity metrics.** Cumulative signups and total downloads only go up and can't guide decisions. Use **cohort metrics** instead: of the users who arrived this month, how many are still active next month?

## The Four Steps of Customer Development

Customer development, from Steve Blank, is the other side of the same coin: the Lean Startup governs *how* to test quickly, customer development governs *where* to test and *what*.

| Stage | Goal | Key question |
| --- | --- | --- |
| **Customer Discovery** | Confirm the problem is real | Does this problem exist? Are these really the target customers? |
| **Customer Validation** | Confirm the solution and a repeatable sales model | Will they pay? Can we sell it repeatedly? |
| **Customer Creation** | Scale up demand | How do we amplify the channels that worked? |
| **Company Building** | Shift from a search organization to an execution organization | How do we build formal functions and processes? |

**The first two steps can't be skipped.** Most startup failures come from scaling spend on customer creation before customer validation is complete.

## Pivots: When to Change Direction

A pivot isn't failure. It is **keeping what has been validated and changing what hasn't**. Common types:

| Type | Meaning | Example |
| --- | --- | --- |
| **Zoom-in** | One feature becomes the whole product | A project tool discovers users only use its chat |
| **Zoom-out** | The whole product becomes one feature of a bigger one | A complex suite reduced to a single tool |
| **Customer segment** | Right product, wrong customer | A consumer tool repositioned for business teams |
| **Customer need** | Right customer, wrong problem | Solve a more painful problem for the same people |
| **Platform** | Application becomes a platform, or vice versa | A single app opens up as a platform |
| **Business architecture / revenue model** | How you charge changes | One-off licence becomes a subscription |
| **Channel** | A different path to the customer | Direct sales become partner distribution |
| **Technology** | The same value delivered with new technology | A cheaper technical stack |

**Signals**: core metrics don't move after several rounds of targeted improvement; interviews keep pointing at a different problem; growth depends entirely on continued spending.

**Practical tip**: hold a fixed "pivot or persevere" meeting (for example monthly) so the team must reach an explicit, data-based conclusion rather than drifting on "let's try one more thing".

## Experiment Template

| Field | Content |
| --- | --- |
| Riskiest assumption | If this is false, the whole business model fails |
| Hypothesis | We believe [target customers] will [behavior] because [reason] |
| Experiment | Landing page / interviews / concierge / single-feature product… |
| Metric | One primary metric, based on behavior |
| Success criterion | Continue if [metric] reaches [value] within [time] |
| Time and cost budget | |
| Actual result | |
| Decision | Persevere / pivot / stop |

## Examples

**Example 1: The Dropbox demo video**

Founder Drew Houston needed to test whether people really wanted seamless file sync. Building a working version would have taken months, so instead he made a three-minute video showing how it would work and posted it in a technical community. The waiting list jumped from 5,000 to 75,000 overnight — strong validation at the cost of a video.

**Example 2: A customer-segment pivot in a B2B tool**

A team built an invoicing tool for freelancers. Six months in, monthly retention sat stubbornly around 15% despite three interface redesigns. Interviews revealed that the few users with excellent retention were **small accounting practices**, who invoiced dozens of clients each month and felt the pain far more acutely. The team pivoted the segment and repositioned the product for batch invoicing by small practices; retention rose above 60%. **Note**: the product barely changed; the customer did.

**Example 3: A Wizard-of-Oz experiment**

A team planning an "AI meeting notes" product didn't train a model first. Users uploaded recordings and team members listened and wrote the notes by hand, returning them within the promised two hours. Users didn't know humans were behind it. Forty sessions over two weeks validated three things: people would upload recordings, a two-hour turnaround was acceptable, and what users actually cared about was **extracted action items**, not full transcripts. That insight redefined the product before a single line of model code existed.

## Common Mistakes

1.  **Treating the MVP as a rough version 1.0.** An MVP is an experiment designed to produce learning, not a stripped-down product. The test is "what will this teach us", not "how many features did we leave out".
2.  **Testing the easiest hypothesis.** Teams often test technical feasibility when the real risk is demand. Test the most dangerous assumption first.
3.  **Using opinions instead of behavior.** "Would you use this?" produces systematically optimistic answers. Watch whether people leave an email address, pre-pay or return.
4.  **No success criterion set in advance.** Without one, any result can be read as "some encouraging signals".
5.  **Thinking Lean Startup means no planning.** The opposite: it requires turning plans into explicit, falsifiable hypotheses.
6.  **Pivoting too late or too often.** Too late means refusing to accept invalidation; too often means not giving hypotheses a fair test. A fixed decision meeting helps with both.
7.  **Applying it to proven businesses.** Established operations with validated models need execution and optimization; Lean Startup is for high uncertainty.

## Lean Startup vs. Design Thinking vs. Agile

| | Lean Startup | [Design Thinking](Design-Thinking-Tutorial-en.md) | [Agile](Agile-Tutorial-en.md) |
| --- | --- | --- | --- |
| Core question | Is this a viable business? | Are we solving the right problem? | How do we build it efficiently? |
| Loop | Build–Measure–Learn | Empathize–Define–Ideate–Prototype–Test | Plan–Build–Review–Adapt |
| Main output | Validated (or invalidated) business hypotheses | A validated problem and concept | Working product increments |
| Risk addressed | Market and business-model risk | User-need risk | Delivery and quality risk |

They work in sequence: **design thinking finds the right problem → lean startup validates the business → agile delivers it.**

## Frequently Asked Questions

??? question "How does the Lean Startup relate to lean manufacturing?"

    It borrows the core idea of eliminating waste but redefines waste. [Lean manufacturing](../../Strategy & Business/quality_and_operations/Lean-Operations-Tutorial-en.md) removes waste from production; the Lean Startup removes the waste of **building things nobody needs**.

??? question "Is the Lean Startup only for startups?"

    No. It applies to any venture with **high uncertainty**: new product lines in large companies, internal innovation projects, new services in non-profits. The criterion is uncertainty, not company size.

??? question "What is a vanity metric?"

    A cumulative number that only rises and can't guide decisions: total signups, total downloads, total page views. Actionable metrics include cohort retention, paid conversion and customer acquisition cost.

??? question "How fast should one loop be?"

    As fast as possible while keeping the learning reliable. Landing-page and interview experiments can run in days; experiments involving a real product usually take one to four weeks. If a loop would take months, find a way to break the experiment down.

??? question "How do I know whether to pivot or persevere?"

    Look at three things: whether core metrics move after several rounds of targeted improvement; whether interviews keep pointing at a different problem; and whether growth depends entirely on continued spending. Decide at a scheduled meeting against criteria set in advance.

## Extensions and Connections

*   **[Minimum Viable Product](../testing_and_validation/MVP-Tutorial-en.md)**: how the Build stage of the loop is actually implemented.
*   **[Lean Canvas](../../Strategy & Business/business_model/Lean-Canvas-Tutorial-en.md)**: the one-page tool designed to capture and iterate startup hypotheses.
*   **[Value Proposition Canvas](../../Strategy & Business/business_model/Value-Proposition-Canvas-Tutorial-en.md)**: sharpening problem–solution fit before scaling.
*   **[Design Thinking](Design-Thinking-Tutorial-en.md)**: making sure the problem is real before testing the business.
*   **[A/B Testing](../testing_and_validation/AB-Testing-Tutorial-en.md)**: the most common Measure technique once you have traffic.
*   **[Agile](Agile-Tutorial-en.md)**: how to deliver efficiently once hypotheses are validated.
*   **[Business Model Canvas](../../Strategy & Business/business_model/Business-Model-Canvas-Tutorial-en.md)**: describing the model once it is validated and scaling.

---
*Reference: Eric Ries, *The Lean Startup* (2011), is the authoritative account of the method. Steve Blank's *The Four Steps to the Epiphany* introduced customer development, one of its direct intellectual sources.*
