---
title: "5 Whys Root Cause Analysis: Steps, Examples and Template"
description: "The 5 Whys technique finds the root cause of a problem by repeatedly asking why. Learn the steps, when to stop asking, four classic examples, a fill-in template, how it compares with the fishbone diagram, and the six most common mistakes."
---

# 5 Whys

When dealing with daily problems, we often fall into a vicious cycle of "treating the symptoms but not the root cause": we fix a problem, but soon after, the same problem reappears in the same or a similar way. This is usually because we only dealt with the **surface symptoms** of the problem, without touching the **root cause** that led to it. **5 Whys** is an extremely simple, yet profoundly insightful **Root Cause Analysis (RCA)** technique. It was proposed by Sakichi Toyoda, the founder of Toyota Motor Corporation, and is a core problem-solving tool in the Toyota Production System (TPS).

The core idea of the 5 Whys method is to continuously and iteratively ask "**Why?**" about an existing problem, delving deeper layer by layer, like peeling an onion, until the underlying root cause is found. If this root cause is addressed, it can completely prevent the problem from recurring. It doesn't strictly require asking exactly five times; sometimes the root can be found in three whys, and sometimes it may require more. The essence lies in the **spirit of persistent inquiry, not being satisfied with superficial answers**. It is a powerful thinking tool that shifts a team's focus from "Whose fault is it?" to "Why did it happen?", and from "firefighting" to "fire prevention."

!!! abstract "Key takeaways"

    - **Purpose**: start from a problem that has happened and follow the causal chain down to a root cause whose removal stops it from recurring.
    - **Method**: state the problem → ask "why?" repeatedly → back every answer with facts → stop at a process or policy you can change → define countermeasures.
    - **"Five" is not a rule**: stop when you reach something actionable, whether that takes three whys or seven.
    - **Most common mistakes**: stopping at "someone made a mistake", or replacing facts with guesses.
    - **Combine tools**: when causes come from several directions, list them with a [fishbone diagram](Fishbone-Diagram-Tutorial-en.md) first, then drill into the key ones with the 5 Whys.

## The Logical Chain of 5 Whys

The 5 Whys process builds a clear cause-and-effect chain from symptom to root cause. The answer to each "Why" forms the subject of the next "Why."

![The Causal Chain of 5 Whys](./5-Whys-Tutorial-en-diagram.png)

<!-- mermaid 源文件：5-Whys-Tutorial-en-mermaid-src-1.mmd -->

## How to Conduct a 5 Whys Analysis

1.  **Step 1: Form a Team, Define the Problem**
    *   Gather a small group of frontline personnel who are familiar with the problem and its context.
    *   Jointly write a precise **problem statement** using clear, objective language. For example, "On October 26, 2023, at 10:00 AM, the customer order system server crashed."

2.  **Step 2: Start Continuously Asking "Why?"**
    *   **First "Why?"**: Ask the first "Why?" about the problem statement.
        *   *Question*: "Why did the customer order system server crash?"
        *   *Answer*: "Because the server's CPU usage reached 100%."

    *   **Second "Why?"**: Use the previous answer as the new subject and continue asking.
        *   *Question*: "Why did the server's CPU usage reach 100%?"
        *   *Answer*: "Because a SQL query in the database entered an infinite loop."

    *   **Third "Why?"**:
        *   *Question*: "Why did this SQL query enter an infinite loop?"
        *   *Answer*: "Because there was a logical flaw in the query when processing a special type of user data."

    *   **Fourth "Why?"**:
        *   *Question*: "Why was this flawed code deployed to the production environment?"
        *   *Answer*: "Because our code review process did not cover this specific test case."

    *   **Fifth "Why?"**:
        *   *Question*: "Why did our code review process have such an oversight?"
        *   *Answer*: "Because we haven't established a standardized **code review checklist** that includes all necessary inspection items."

3.  **Step 3: Identify the Root Cause and Formulate Countermeasures**
    *   **Identify the Root Cause**: In the example above, the root cause was identified as "lack of a standardized code review checklist." This is a **process-level** issue. If we had only fixed the logical flaw in the SQL (the answer to the third "Why"), it's highly likely that other similar, insufficiently tested code issues would arise in the future.
    *   **Formulate Countermeasures**: Develop a specific, actionable corrective measure for the root cause. For example, "The technical lead will take charge of creating a standard code review checklist, including database performance, security, and boundary condition testing, within this week, and all teams must follow it in the future."

## Application Cases

**Case 1: Corrosion of the Stone Walls of the Jefferson Memorial in Washington D.C.**

This is the most widely told 5 Whys story in management books. Details have been simplified in the retelling, but it shows well why it pays to keep asking:

*   **Problem**: The stone walls of the memorial were severely corroded.
*   **Why? (1)** Because cleaners used high-strength detergents too frequently to wash the walls.
*   **Why? (2)** Because there was a large amount of bird droppings on the walls every day, necessitating frequent cleaning.
*   **Why? (3)** Because many birds gathered around the memorial to feed on the spiders there.
*   **Why? (4)** Because there were many spiders, feeding on the midges that swarmed around the memorial.
*   **Why? (5)** Because the memorial's lights were switched on before dusk, attracting large numbers of midges.
*   **Root Cause**: Improper setting of the lighting system's turn-on time.
*   **Solution**: Switch the lights on after sunset. This simple process change reduced the need for cleaning at its source, and with it the damage to the stone.

**Case 2: A Puddle of Oil on the Factory Floor**

*   **Problem**: There was a puddle of oil on the factory floor.
*   **Why? (1)** Because a machine's oil pipe joint was leaking.
*   **Why? (2)** Because the gasket in that oil pipe joint was old and cracked.
*   **Why? (3)** Because the company purchased a batch of low-quality, cheap gaskets.
*   **Why? (4)** Because the company's procurement policy's only requirement was "lowest price wins."
*   **Why? (5)** Because the procurement department's performance was only linked to how much procurement cost they "saved" for the company, and had nothing to do with the quality and lifespan of spare parts.
*   **Root Cause**: Unreasonable performance appraisal system for the procurement department.
*   **Solution**: Revise procurement policies and performance systems to include supplier quality, reliability, and long-term costs in the evaluation system.

**Case 3: A Student Fails a Final Exam**

*   **Problem**: Xiao Ming failed his math final exam.
*   **Why? (1)** Because he only started reviewing in the last week before the exam, which was not enough time.
*   **Why? (2)** Because he didn't understand much of the content taught in class.
*   **Why? (3)** Because he always played with his phone during class and couldn't concentrate.
*   **Why? (4)** Because he fundamentally disliked math and had no interest in it.
*   **Why? (5)** Because in junior high, he was severely criticized by a teacher after failing a math test, which caused a psychological shadow and fear of math.
*   **Root Cause**: Early negative learning experiences led to psychological barriers.
*   **Solution**: May require psychological counseling and building self-confidence, and re-establishing his interest in math by starting with more basic knowledge points where he can experience success.

**Case 4: A Product Launch Delayed by Two Weeks**

*   **Problem**: A new product launched two weeks later than planned.
*   **Why? (1)** Because final QA testing failed.
*   **Why? (2)** Because a core module had a serious defect.
*   **Why? (3)** Because code from two sub-teams conflicted during integration.
*   **Why? (4)** Because the engineers on the two modules hadn't aligned on the interface design before development.
*   **Why? (5)** Because the project process had no cross-module design review; aligning interfaces depended on individuals remembering to talk.
*   **Root Cause**: The project process lacks a cross-module communication checkpoint.
*   **Solution**: Add a cross-module technical design review before development starts; any feature touching several modules must have its interfaces reviewed first.

Had the team stopped at the fourth why ("engineers didn't communicate"), the countermeasure would probably have been "remind everyone to communicate more", which rarely changes anything.

## Advantages and Challenges of 5 Whys

**Core Advantages**

*   **Simple and Easy to Use**: Does not require complex statistical tools or specialized knowledge; any team can quickly get started.
*   **Gets to the Root**: Helps teams penetrate the surface symptoms of a problem to find high-leverage solutions that can fundamentally solve the problem.
*   **Promotes Understanding, Not Blame**: Shifts the focus from "who made the mistake" to "why did the process allow the mistake to happen," helping to build a healthier, issue-focused problem-solving culture.

**Potential Challenges**

*   **May Have Multiple Root Causes**: For complex problems, the root cause may not be singular but an interconnected system. In such cases, the 5 Whys may oversimplify the problem.
*   **Depends on Participant Knowledge**: The depth of the analysis highly depends on the participating team's understanding of the actual process and situation.
*   **May Stop Midway**: The team might stop asking "Why?" after finding a seemingly reasonable but not the most fundamental cause.

## When to Stop Asking Why

"Five" is a rule of thumb. You have probably reached the root cause when:

*   **The answer is a process, standard, policy or resource allocation** that the team can change.
*   **Removing it would prevent this whole class of problem**, not just this one occurrence.
*   **Asking further leads outside the team's control**, such as "the market changed" or "that's human nature". You've gone too far; step back one level.

If your last answer is "someone wasn't careful" or "an operator made an error", you almost certainly haven't finished. Ask why the process didn't catch the error.

A quick test of the chain: **read it backwards from the last answer using "therefore"**. If every "therefore" makes sense, the chain is sound. If a step sounds forced, you've skipped a link or mistaken correlation for causation.

## 5 Whys Template

| Level | Why? | Answer (cause) | Evidence (data / observation / records) |
| --- | --- | --- | --- |
| Problem | — | What happened, when, and how big the impact was | Records of the incident |
| 1 | Why did the problem happen? | … | … |
| 2 | Why did level 1 happen? | … | … |
| 3 | Why did level 2 happen? | … | … |
| 4 | … | … | … |
| 5 | … | … | … |
| Root cause | — | A process / standard / policy you can change | |
| Countermeasures | — | Containment + permanent fix, each with an owner and date | |

**The evidence column must not be empty.** Any level where you can't write evidence is where you need to go and check.

## Common Mistakes

1.  **Stopping at a person.** "The operator was careless" is not a root cause. Ask why the process allowed the error and why it wasn't caught. The 5 Whys focus on the system, not on blame.
2.  **Guessing instead of checking.** Each answer should be confirmed by data, records or direct observation. Chains reasoned out in a meeting room often drift away from reality by the second or third level; go and look where it happened (see the [Gemba Walk](../problem_solving/Gemba-Walk-Tutorial-en.md)).
3.  **Jumps in logic.** Going from "the server crashed" straight to "the team is understaffed" skips several links. Reading the chain backwards with "therefore" exposes the jumps.
4.  **Following only one path.** Complex problems often have several causes. When a level has two valid answers, branch and follow both.
5.  **Asking exactly five times, mechanically.** If the third why lands on a changeable process, stop. If after five the answer is still "someone's mistake", keep going.
6.  **Finding the cause but not following through.** Countermeasures without owners, deadlines and a check that they worked mean the problem will come back.

## 5 Whys vs. Fishbone Diagram

| | 5 Whys | [Fishbone Diagram](Fishbone-Diagram-Tutorial-en.md) |
| --- | --- | --- |
| Direction | Drills vertically down one causal chain | Spreads horizontally across all possible causes |
| Best for | Problems with a fairly clear, single causal path | Complex problems with causes in several areas |
| Group size | A small team of 2–5 people | Cross-functional group discussion |
| Output | One (or a few) root causes and countermeasures | A map of all suspected causes |
| Main risk | Missing causes in other directions | Staying at the surface without depth |

They work well together: list causes with a fishbone diagram, pick the biggest ones with [Pareto analysis](../decision_making/Pareto-Analysis-Tutorial-en.md), then drill into each with the 5 Whys.

## Frequently Asked Questions

??? question "Do I have to ask "why" exactly five times?"

    No. Five is Toyota's rule of thumb; most problems reach a changeable process within three to five levels. What matters is whether the answer is actionable and whether removing it prevents recurrence, not the count.

??? question "What if there is more than one root cause?"

    When a level has two valid answers, split into two chains and follow each. If it's clear from the start that causes come from several areas, draw a fishbone diagram first, then apply the 5 Whys to each key cause.

??? question "Can I use the 5 Whys on my own?"

    Yes, for example to reflect on a missed deadline or a personal mistake. Working alone, it's easier to talk yourself into a convenient answer, so treat each level as a hypothesis to check, and ask someone who knows the situation to review it.

??? question "What kinds of problems suit the 5 Whys?"

    Problems that have already happened, are specific, and have a traceable process: quality defects, system outages, missed deliveries, process errors. It isn't suited to forward-looking decisions like "which market should we enter next year?".

??? question "How do the 5 Whys relate to root cause analysis (RCA)?"

    Root cause analysis is a family of methods aimed at fixing causes rather than symptoms. The 5 Whys are the simplest and most widely used; fishbone diagrams, fault tree analysis and Pareto analysis are other common RCA tools.

## Extensions and Connections

*   **[Fishbone Diagram (Ishikawa Diagram)](Fishbone-Diagram-Tutorial-en.md)**: When a problem may be caused by multiple different, parallel reasons from various areas, a fishbone diagram can first be used to systematically brainstorm and organize all possible potential causes. Then, the 5 Whys can be used to deeply investigate the most suspicious causes.
*   **[Lean Production](../../Strategy & Business/quality_and_operations/Lean-Operations-Tutorial-en.md)** and **Six Sigma**: The 5 Whys is one of the most commonly used and fundamental tools for root cause analysis in both of these quality and operational improvement methodologies.

---
*Source Reference: The 5 Whys method, as one of the cornerstones of the Toyota Production System (TPS), was conceived by Sakichi Toyoda and popularized by Taiichi Ohno in his work. It is a core embodiment of problem-solving and continuous improvement culture in lean thinking.*