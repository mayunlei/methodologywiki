---
title: "PDCA Cycle (Deming Cycle): 4 Stages, Template and Examples"
description: "The PDCA cycle (Plan-Do-Check-Act) drives continuous improvement through four stages that close the loop. Learn what happens in each stage, a fill-in template, three worked examples, how PDCA differs from PDSA, OODA and DMAIC, and the mistakes that break the cycle."
---

# The PDCA Cycle (Deming Cycle)

Most teams know the pattern: a problem appears, a meeting is held, a few improvement actions are agreed, and then nothing. Weeks later the same problem returns, another meeting is held, more actions are agreed. The problem isn't effort. It's that **the improvement never closes the loop**: nobody checks whether the actions worked, and the ones that did work are never written down.

The **PDCA cycle (Plan-Do-Check-Act)** exists to fix exactly this. It breaks any improvement into four stages that must all be completed: **Plan, Do, Check, Act**. First sketched by statistician Walter Shewhart and later popularized by W. Edwards Deming in post-war Japan, it is also known as the **Deming cycle**, and it is the shared engine behind [Total Quality Management](Total-Quality-Management-Tutorial-en.md), [Lean](Lean-Operations-Tutorial-en.md) and [Kaizen](Kaizen-Tutorial-en.md).

What matters is not the four words but the fact that it is a **circle**: the output of Act becomes the input of the next Plan. Each turn raises the standard, which is why PDCA is often drawn as a wheel rolling up a slope, with standardization as the wedge that stops it rolling back.

!!! abstract "Key takeaways"

    - **Four stages**: Plan (set a target, find causes, design countermeasures) → Do (try it on a small scale) → Check (compare results with the target using data) → Act (standardize what works, or go back to Plan).
    - **Pilot before rolling out**: the most commonly skipped part of Do.
    - **Check needs data**, not "how does everyone feel about it?"
    - **Act has two jobs**: write the working method into the standard, and carry unresolved issues into the next cycle.
    - **Common partners**: [fishbone diagrams](../../Problem Solving & Decision Making/root_cause_analysis/Fishbone-Diagram-Tutorial-en.md) and the [5 Whys](../../Problem Solving & Decision Making/root_cause_analysis/5-Whys-Tutorial-en.md) in Plan, [Pareto analysis](../../Problem Solving & Decision Making/decision_making/Pareto-Analysis-Tutorial-en.md) to prioritize.

## What Happens in Each Stage

### P — Plan

This is the longest stage and the one that decides the outcome. It covers three things:

1.  **Define the problem and the target** with numbers. "Improve the pass rate" is not a target; "raise line A's pass rate from 95% to 98% by the end of June" is (see [SMART Goals](../../Personal & Team Productivity/goal_management/SMART-Goals-Tutorial-en.md)).
2.  **Analyze causes**: go and see the real situation, list possible causes with a fishbone diagram, drill down with the 5 Whys, and use data to confirm which causes actually matter.
3.  **Design countermeasures** for the confirmed causes, each with an owner, a date and an **expected effect**. Writing down the expected effect is essential: without it, the Check stage has nothing to compare against.

### D — Do

**Pilot on a small scale** rather than rolling out everywhere: one line, one shift, one store. At the same time, **record what actually happens**: was the countermeasure carried out as designed? What got in the way? Were there side effects?

The most common failure here isn't a bad countermeasure. It's a countermeasure that was never properly executed, with nobody noticing.

### C — Check

Compare the actual result with the expected effect from the Plan stage and answer three questions:

*   **Did we hit the target?** In numbers.
*   **Was it caused by our countermeasure?** Did anything else change at the same time (a seasonal dip, a different product mix)?
*   **Was the plan actually followed?** If it wasn't, a poor result doesn't prove the countermeasure is wrong.

### A — Act

Based on the check, take one of two paths:

*   **It worked** → **standardize**. Update the standard work, checklists and training material so the new method becomes the default, then spread it to other lines, shifts or departments.
*   **It didn't work, or only partly** → **go back to Plan**. Re-analyze the causes (often the first round identified the wrong one) and design new countermeasures.

Either way, list the **issues this cycle did not solve** explicitly; they are the input for the next cycle.

## PDCA Template

| Stage | Item | Content |
| --- | --- | --- |
| **P** | Problem statement | What, when, how big (measurable, no cause assumed) |
| | Target | Metric, baseline, target value, deadline |
| | Key causes | 1–3, confirmed with data |
| | Countermeasures | Action, owner, date |
| | **Expected effect** | How far the metric should move |
| **D** | Pilot scope | Which line / team / how long |
| | Execution log | What was actually done; obstacles |
| **C** | Actual result | Metric value |
| | Gap vs. expectation | Met / not met, by how much |
| | Explanation | Countermeasure ineffective? Not executed? External factor? |
| **A** | Standardization | Which document was updated, who trains on it |
| | Horizontal spread | Which other units, when |
| | Open issues | Carried into the next cycle |

**Checklist**

- [ ] The target has a number and a deadline
- [ ] Key causes were confirmed with data, not guessed
- [ ] The expected effect was written down during Plan
- [ ] The countermeasure was piloted on a small scale
- [ ] Check used data, not impressions
- [ ] What worked is now in a standard document

## Worked Examples

**Example 1: Reducing repeat calls to customer support**

*   **Plan**: 32% of customers call again within 7 days of a ticket being closed. A fishbone session plus ticket data confirmed two key causes: internal jargon in first replies, and closing tickets without confirming the issue was solved. Target: cut repeat calls to 20%, with each countermeasure expected to contribute roughly 6 percentage points.
*   **Do**: Piloted for two weeks with one 8-person team: a plain-language glossary, plus one closing question, "Does this solve the problem for you?"
*   **Check**: Repeat calls in that team fell to 21%, close to target. But average handling time rose from 6.2 to 7.0 minutes.
*   **Act**: Both countermeasures were written into the standard support script and rolled out. The handling-time increase became an open issue for the next cycle, later solved by making the glossary easier to search.

**Example 2: Shortening new-hire ramp-up**

*   **Plan**: New engineers took on average 6 weeks to ship their first production change. Interviews pointed to environment setup and not knowing whom to ask. Target: 3 weeks.
*   **Do**: For the next cohort of five, provided a one-command environment script and assigned both a mentor and a buddy.
*   **Check**: Average first change shipped in 3.5 weeks; four of five were under 3 weeks. The one outlier was blocked by an access-approval process.
*   **Act**: Script and mentor/buddy scheme added to the onboarding handbook; slow access approval became a new problem for the next cycle.

**Example 3: Personal use — building a running habit**

*   **Plan**: Go from one run a week to three within a month. Obstacles: too tired after work, gear never ready.
*   **Do**: Switched to morning runs and put the gear by the door the night before; trialed for two weeks.
*   **Check**: Five runs in two weeks against a plan of six; the missed one followed a late night.
*   **Act**: "Gear by the door" became the default. For the late nights, the next cycle adds "no phone after 11 pm".

## Common Mistakes

1.  **Only P and D, never C and A.** The most widespread failure: actions are agreed and carried out, but nobody verifies the effect or locks in what worked. Without Check and Act it isn't a cycle.
2.  **No expected effect in the plan.** Without it, Check degenerates into "it feels a bit better".
3.  **Skipping the pilot.** Rolling out everywhere at once makes mistakes expensive and hard to reverse.
4.  **Confusing "not executed" with "doesn't work".** Always confirm execution before judging the countermeasure.
5.  **Succeeding without standardizing.** If the improvement depends on a few people remembering, it disappears when they move on.
6.  **Trying to solve everything in one turn.** The power of PDCA comes from turning the wheel repeatedly, solving one or two key causes each time.

## PDCA vs. OODA vs. DMAIC

| | PDCA | OODA Loop | DMAIC |
| --- | --- | --- | --- |
| Stands for | Plan-Do-Check-Act | Observe-Orient-Decide-Act | Define-Measure-Analyze-Improve-Control |
| Origin | Quality management (Shewhart, Deming) | Military strategy (John Boyd) | [Six Sigma](Six-Sigma-Tutorial-en.md) |
| Core aim | Continuous improvement and locking in gains | Deciding faster than an opponent | Removing variation with statistics |
| Tempo | Weeks to months | Seconds to minutes | 3–6 months per project |
| Best for | Everyday improvement, process optimization | Competitive or emergency situations | Complex quality problems needing statistical analysis |

One way to see it: **DMAIC is PDCA with a heavier Plan stage** (rigorous measurement and statistical analysis), while **OODA is PDCA at high speed** for adversarial situations.

## Frequently Asked Questions

??? question "What is the difference between PDCA and PDSA?"

    Deming later preferred **PDSA (Plan-Do-Study-Act)**, replacing Check with Study. He felt "check" suggested merely verifying that something was done, whereas "study" emphasizes learning what the results mean. The flow is the same.

??? question "How long should one PDCA cycle take?"

    It depends on the scale of the change and how quickly the metric responds. Team-level improvements may turn in one or two weeks; process changes often take one to three months. The cycle should be short enough to learn quickly and long enough for the metric to move meaningfully.

??? question "How does PDCA relate to Kaizen?"

    Kaizen is the philosophy of continuous small improvement; PDCA is the standard method for carrying out one improvement. Kaizen answers "why keep improving"; PDCA answers "how to complete one improvement properly".

??? question "Is PDCA only for manufacturing?"

    No. It applies anywhere there is a goal, a process and a measurable result: support, software, healthcare, teaching, marketing and personal habits. The three examples above come from support, software and personal life.

??? question "If Check shows no improvement, has the cycle failed?"

    No. Once you've ruled out poor execution, "this countermeasure doesn't work" is a valuable result: it eliminates a wrong hypothesis and brings the next cycle closer to the real cause. PDCA aims at learning, not at every cycle succeeding.

## Extensions and Connections

*   **[Kaizen](Kaizen-Tutorial-en.md)**: PDCA is the standard execution framework for kaizen activities.
*   **[Total Quality Management](Total-Quality-Management-Tutorial-en.md)** and **[Lean Operations](Lean-Operations-Tutorial-en.md)**: both use PDCA as their basic improvement loop.
*   **[Six Sigma](Six-Sigma-Tutorial-en.md)**: DMAIC can be read as PDCA reinforced with statistical tools.
*   **[Fishbone Diagram](../../Problem Solving & Decision Making/root_cause_analysis/Fishbone-Diagram-Tutorial-en.md)** and **[5 Whys](../../Problem Solving & Decision Making/root_cause_analysis/5-Whys-Tutorial-en.md)**: the main tools for cause analysis in the Plan stage.
*   **[Gemba Walk](../../Problem Solving & Decision Making/problem_solving/Gemba-Walk-Tutorial-en.md)**: going to the real place is how you get trustworthy information for Plan.
*   **[A/B Testing](../../Product & User/testing_and_validation/AB-Testing-Tutorial-en.md)**: in digital products, the typical implementation of Do and Check.

---
*Reference: The cycle originated with Walter A. Shewhart's work in the 1930s and was systematized and popularized by W. Edwards Deming in his quality lectures in post-war Japan, where it became known as the Deming cycle. Deming himself later preferred the PDSA formulation, arguing that "Study" better captures the intent of learning from results.*
