---
title: "Kano Model: Five Categories, Questionnaire and Analysis Explained"
description: "The Kano model classifies features as must-be, one-dimensional, attractive, indifferent or reverse, so you can prioritize by their effect on satisfaction. Learn the five categories, the two-question survey and evaluation table, Better-Worse coefficients, a worked example and common mistakes."
---

# The Kano Model

There are twenty features on the backlog and capacity for five. Which five? Ranking by "users said they wanted it" typically produces a release full of features users did ask for and which move satisfaction not at all.

The reason is a fact that is easy to overlook: **different kinds of needs have different relationships with satisfaction**. Some features never delight however well you build them, yet their absence makes people angry. Others are never requested, but their presence produces genuine delight.

The **Kano model**, developed by Professor Noriaki Kano of the Tokyo University of Science in the 1980s, describes exactly this non-linear relationship. It sorts needs into five categories and provides a survey method for deciding, with data rather than intuition, which category a feature falls into.

!!! abstract "Key takeaways"

    - **Five categories**: must-be (absence angers), one-dimensional (more is better), attractive (presence delights), indifferent (nobody cares), reverse (presence annoys).
    - **Method**: ask one functional and one dysfunctional question per feature, then classify with the evaluation table.
    - **Priority**: satisfy must-be needs → improve one-dimensional needs → pick attractive features for differentiation.
    - **Categories decay over time**: today's attractive feature becomes tomorrow's must-be.
    - **Better-Worse coefficients** turn the results into a four-quadrant chart for ranking.

## The Five Categories

| Category | If present | If absent | Example |
| --- | --- | --- | --- |
| **Must-be** | No extra satisfaction | Strong dissatisfaction | A phone that can make calls; a clean hotel room |
| **One-dimensional** | More is better | Less is worse | Battery life; delivery speed |
| **Attractive** | Delight | No dissatisfaction | A handwritten welcome note in a hotel room |
| **Indifferent** | Doesn't matter | Doesn't matter | A setting nobody ever opens |
| **Reverse** | Dissatisfaction | Satisfaction | Forced pop-up recommendations; excessive onboarding |

**Three practical implications**:

1.  **Must-be needs are the entry ticket, not a differentiator.** However much you invest, the best you achieve is "not angry".
2.  **One-dimensional needs decide competitiveness.** Satisfaction rises with performance, so this is where you out-compete rivals.
3.  **Attractive features create word of mouth** — but they rarely come from what users explicitly ask for, because people can't request what they've never seen.

## The Two-Question Survey

The core method asks **two questions about every feature**:

*   **Functional**: "How would you feel if this feature were present?"
*   **Dysfunctional**: "How would you feel if this feature were absent?"

Both use the same five options:

1.  I like it
2.  I expect it
3.  I am neutral
4.  I can tolerate it
5.  I dislike it

**Writing good questions**: describe the **effect the user can perceive**, not the technical implementation. "If the app opened within one second" is far better than "if we optimized the startup loading logic".

### Evaluation Table

Combine each respondent's two answers:

| Functional ↓ / Dysfunctional → | Like | Expect | Neutral | Tolerate | Dislike |
| --- | --- | --- | --- | --- | --- |
| **Like** | Q | A | A | A | O |
| **Expect** | R | I | I | I | M |
| **Neutral** | R | I | I | I | M |
| **Tolerate** | R | I | I | I | M |
| **Dislike** | R | R | R | R | Q |

*A = Attractive, O = One-dimensional, M = Must-be, I = Indifferent, R = Reverse, Q = Questionable (usually means the question was misunderstood; discard)*

**How to read it**: if a respondent answers "I like it" when the feature is present and "I am neutral" when it's absent, the table gives **A (attractive)**: delighted to have it, not upset without it. If they answer "I expect it" present and "I dislike it" absent, that's **M (must-be)**.

### Better-Worse Coefficients

Aggregate all respondents, then compute:

*   **Better (satisfaction impact) = (A + O) ÷ (A + O + M + I)**
    The closer to 1, the more providing the feature raises satisfaction.
*   **Worse (dissatisfaction impact) = −(O + M) ÷ (A + O + M + I)**
    The closer the absolute value to 1, the more its absence causes dissatisfaction.

Plot each feature at (Better, |Worse|):

| | High \|Worse\| | Low \|Worse\| |
| --- | --- | --- |
| **High Better** | **One-dimensional**: the main battleground; invest | **Attractive**: differentiation opportunity |
| **Low Better** | **Must-be**: required, but "good enough" is enough | **Indifferent**: consider dropping |

## Worked Example: Prioritizing Features for a Delivery App

A team surveyed 200 users about six candidate features:

| Feature | A | O | M | I | Category | Better | \|Worse\| |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Live courier location | 18% | 52% | 24% | 6% | One-dimensional | 0.70 | 0.76 |
| On-time delivery | 5% | 30% | 60% | 5% | Must-be | 0.35 | 0.90 |
| Food arrives hot | 48% | 26% | 12% | 14% | Attractive | 0.74 | 0.38 |
| One-tap reorder | 31% | 18% | 8% | 43% | Indifferent | 0.49 | 0.26 |
| In-app social sharing | 9% | 7% | 4% | 80% | Indifferent | 0.16 | 0.11 |
| Full-screen launch ads | 3% | 4% | 5% | 30% | Reverse (R 58%) | — | — |

**Conclusions and actions**:

*   **On-time delivery** is must-be with the highest |Worse| (0.90): failing it loses customers outright, but over-investing buys no extra satisfaction. Hold the baseline.
*   **Live courier location** is one-dimensional with both coefficients high: this is where you beat competitors, and it deserves continued investment.
*   **Food arrives hot** is attractive (Better 0.74, |Worse| only 0.38): nobody demanded it, but delivering it creates word of mouth. It should rank above social sharing.
*   **In-app social sharing** is indifferent: however much the product manager likes it, users don't care. Cut it.
*   **Full-screen launch ads** are reverse: 58% actively dislike them, so shipping them damages the experience.
*   **One-tap reorder** classifies as indifferent overall (I 43%), but 31% call it attractive. A split like that usually signals a high-frequency sub-group; segment the sample by order frequency and look again before dropping it.

**This is the Kano model's main value: it turns "I think users will love this" into a claim that data can refute.**

## Categories Decay Over Time

**Today's attractive feature becomes tomorrow's one-dimensional and the next day's must-be.**

Touchscreens were attractive in 2007 and are must-be today; live delivery tracking was a delight a few years ago and is now standard. This means:

*   Kano studies **need repeating**, typically every one to two years.
*   **A product that only covers must-be needs slowly loses competitiveness**, because rivals' attractive features keep raising the baseline.
*   Attractive features open a differentiation window, but the window closes.

## Common Mistakes

1.  **Treating "users asked for it" as high priority.** Users tend to want everything. Kano's whole purpose is to separate kinds of wanting.
2.  **Describing implementation instead of perceived effect.** Users can't judge what "refactoring the cache layer" means for them.
3.  **Ignoring reverse needs.** Some features actively harm the experience (forced notifications, excessive pop-ups), yet few teams test for this.
4.  **Building only must-be features.** Safe but unremarkable: nobody is upset, and nobody chooses you either.
5.  **Not segmenting the sample.** New and long-term users, or free and paying users, can classify the same feature differently; combined, they cancel out.
6.  **Reusing one study for five years.** Categories decay; conclusions have a shelf life.
7.  **Ignoring a high Q rate.** If "questionable" exceeds about 10% for a feature, the wording is probably ambiguous; rewrite the question.

## Kano vs. Other Prioritization Methods

| | Kano Model | [Value Proposition Canvas](../../Strategy & Business/business_model/Value-Proposition-Canvas-Tutorial-en.md) | [Decision Matrix](../../Problem Solving & Decision Making/decision_making/Decision-Matrix-Tutorial-en.md) | [Pareto Analysis](../../Problem Solving & Decision Making/decision_making/Pareto-Analysis-Tutorial-en.md) |
| --- | --- | --- | --- | --- |
| Question | How does this feature relate to satisfaction? | Does our value match customer needs? | Which option scores best overall? | Which few causes drive most of the result? |
| Data source | User survey (two questions per feature) | User interviews | Team scoring | Historical data |
| Output | Need categories and priority | Fit analysis | Ranked options | The vital few |
| Best stage | Feature planning and release scoping | Defining product value | Choosing between options | Allocating improvement effort |

A common sequence: **value proposition canvas to understand pains and gains → Kano to classify candidate features → decision matrix to choose between implementations.**

## Frequently Asked Questions

??? question "How large a sample does a Kano survey need?"

    Around 100 valid responses per user segment is a common guideline for stable category proportions. If you want to compare segments, each segment needs that many.

??? question "How do I decide a feature's final category?"

    The most common approach is maximum frequency: whichever category the most respondents produce. If the top two are within about 5 percentage points, the user base disagrees and you should analyze by segment.

??? question "Do I have to calculate Better-Worse coefficients?"

    Not strictly, but they're strongly recommended. Classification alone tells you the type; the coefficients rank features within a type and plot neatly on a four-quadrant chart.

??? question "Is the Kano model only for product features?"

    No. It applies wherever an attribute affects satisfaction: hotel services, course design, employee benefits, internal tools. The method (two questions plus the evaluation table) is general.

??? question "How does Kano differ from RICE or MoSCoW?"

    Kano classifies by **effect on user satisfaction**; RICE and MoSCoW rank by **effort, reach and business constraints**. They're complementary: use Kano to understand the nature of each need, then a scoring method to schedule the work.

## Extensions and Connections

*   **[Value Proposition Canvas](../../Strategy & Business/business_model/Value-Proposition-Canvas-Tutorial-en.md)**: its four levels of gains (required, expected, desired, unexpected) map closely onto Kano's categories.
*   **[User Persona](User-Persona-Tutorial-en.md)** and **[Empathy Map](Empathy-Map-Tutorial-en.md)**: establish who you are classifying needs for before running the survey.
*   **[Decision Matrix](../../Problem Solving & Decision Making/decision_making/Decision-Matrix-Tutorial-en.md)**: choose among implementation options once features are classified.
*   **[MVP](../testing_and_validation/MVP-Tutorial-en.md)**: an MVP should cover all must-be needs plus one or two attractive features.
*   **[A/B Testing](../testing_and_validation/AB-Testing-Tutorial-en.md)**: Kano produces hypotheses; A/B tests verify the real impact after launch.
*   **[Total Quality Management](../../Strategy & Business/quality_and_operations/Total-Quality-Management-Tutorial-en.md)**: the Kano model originated in quality management as a concrete tool for customer focus.

---
*Reference: Noriaki Kano and colleagues formally presented the model in the 1984 paper "Attractive Quality and Must-Be Quality", which has become a classic in quality management and product planning.*
