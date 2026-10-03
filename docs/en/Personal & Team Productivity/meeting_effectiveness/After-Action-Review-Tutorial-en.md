---
title: "After Action Review (AAR): 4 Questions, Agenda, Template and Examples"
description: "An After Action Review turns an experience into reusable knowledge using four questions: what was supposed to happen, what actually happened, why the difference, and what we'll do next time. Includes a meeting agenda, facilitation tips, a template, examples and common mistakes."
---

# After Action Review (AAR)

A project ends, everyone exhales and moves on to the next one. Three months later the same mistake is made again. **Experience doesn't automatically become knowledge.** Only a structured review turns what happened into judgment you can use next time.

The **After Action Review (AAR)** is the standard method for making that conversion. It began in the US Army: after a training exercise, participants sit together regardless of rank and answer a fixed set of questions. The point isn't to judge who performed well, but to establish **what actually happened, why, and what to do differently**. Shell, General Electric and many other organizations later adopted it for business.

The method rests on four questions:

*   **What was supposed to happen?**
*   **What actually happened?**
*   **Why was there a difference?**
*   **What will we do next time?**

They look simple, but the discipline matters: **you must reach agreement on the facts in the first two questions before moving to the last two**. Most failed reviews start arguing about blame before anyone has established what actually occurred.

!!! abstract "Key takeaways"

    - **Four questions, in order**: intended outcome → actual outcome → reasons for the gap → what we'll change.
    - **About the process, not the people**: the output is improvements, not blame.
    - **Review successes too**: without it, teams can't repeat what worked and may mistake luck for skill.
    - **Do it while it's fresh**, ideally within one to three days.
    - **End with owners and dates**, or the same thing happens again.

## The Four Questions

### 1. What was supposed to happen?

Lay out the original plan, targets and expectations, including the information available and the assumptions made at the time. **Return to the state of knowledge back then** rather than judging past decisions with what you know now (hindsight bias).

If people disagree about what the goal even was, that discovery is itself the most valuable finding of the review.

### 2. What actually happened?

Reconstruct the facts in sequence: key events, key decisions, key numbers. At this stage, state only **verifiable facts**, with no evaluation or attribution.

The facilitator's job is to convert "it felt rushed" into "the approach was agreed on 2 March and had to ship on 5 March". Once the timeline is on the wall, most judgments emerge naturally and with far more agreement.

### 3. Why was there a difference?

Compare intention with outcome and analyze the gap. Use the [5 Whys](../../Problem Solving & Decision Making/root_cause_analysis/5-Whys-Tutorial-en.md) to drill down, or a [fishbone diagram](../../Problem Solving & Decision Making/root_cause_analysis/Fishbone-Diagram-Tutorial-en.md) when causes come from several directions.

**Analyze what went right as well.** Which practices produced the good results, and were they repeatable or lucky? Teams skip this question routinely, and it is the one that determines whether success can be reproduced.

### 4. What will we do next time?

Turn conclusions into concrete actions in three categories:

*   **Sustain**: what worked; write it into the process or checklist.
*   **Start**: what was missing and should be added.
*   **Stop**: what proved ineffective or harmful.

Each item needs an **owner and a date**. A conclusion without an owner is not a conclusion.

## Meeting Agenda (60–90 minutes)

| Time | Section | Notes |
| --- | --- | --- |
| 0–5 min | Opening | State the purpose: learning, not blame. Agree ground rules: process not people, everyone speaks, no interrupting |
| 5–15 min | Intended outcome | Restate goals, plans and assumptions; confirm shared understanding |
| 15–35 min | What happened | Build a timeline on a whiteboard, marking key events and decisions |
| 35–60 min | Why the difference | Analyze both failures and successes; focus on 2–3 key points |
| 60–80 min | Actions | Sustain / Start / Stop, each with owner and date |
| 80–90 min | Close | Read back the actions; agree when they'll be checked |

**Facilitation tips**

*   **Let the most junior people speak first.** If the leader speaks first, everyone else agrees.
*   **Convert judgments into facts.** "It was chaotic" → "three people were editing the same document at once".
*   **Allow silence.** Give people time to think instead of filling the gap.
*   **Limit it to two or three key issues.** Trying to solve everything solves nothing.
*   **Review your own part.** If you lead the team, naming your own mistakes is the fastest way to make the room safe.

## AAR Template

**Basics**: event or project, date, participants, facilitator

| Question | Content |
| --- | --- |
| **1. What was supposed to happen** | Goals and key assumptions at the time |
| **2. What actually happened** | Timeline: key events, decisions, numbers |
| **3. Why the difference** | What went well: which practices worked, and were they repeatable? |
| | What went badly: root causes (drill down with the 5 Whys) |
| **4. What we'll do next time** | See table below |

| Type | Action | Owner | Due |
| --- | --- | --- | --- |
| Sustain | | | |
| Start | | | |
| Stop | | | |

**Checklist**

- [ ] The facts section contains no evaluations or guesses
- [ ] Both failures and successes were analyzed
- [ ] Causes reach the process or system level, not "someone wasn't careful"
- [ ] Every action has an owner and a date
- [ ] A date is set to check that the actions happened

## Examples

**Example 1: Reviewing a production incident**

*   **Intended**: the evening release should complete within 30 minutes with no impact on orders.
*   **Actual**: deployment started at 21:00; payment API error rates spiked at 21:12; rollback completed at 21:48, affecting users for 48 minutes.
*   **Why**: what went well was that alerting fired within two minutes and the on-call engineer responded immediately. What went badly was the 36-minute rollback. Drilling down, the root cause was that the rollback script hadn't been rehearsed in six months, and a configuration dependency had changed in the meantime.
*   **Actions**: *Sustain* — keep the current alert thresholds (owner: Li). *Start* — rehearse the rollback quarterly (owner: Zhang, scheduled this month). *Stop* — no more major releases on Friday evenings (owner: engineering lead, effective immediately).

**Example 2: Reviewing a successful campaign**

Teams routinely skip reviews when things go well. This campaign beat its target by 40%. The review found that the conversions came not from the heavily funded paid channel, but from one customer's post in a community forum that was widely shared. That insight changed the next quarter's budget allocation and led the team to *start* a systematic customer-content program. Without the review, the team would have credited the ad spend and simply spent more.

**Example 3: Personal AAR after a deal fell through**

Individuals can use AAR too. Intended: sign a letter of intent. Actual: the other side stopped replying after the second meeting. Reconstructing the facts showed that in the first meeting, 40 minutes were spent presenting the product and only about 10 minutes listening. The reason for the gap: the pitch started before anyone understood what the other side actually cared about. Next time: spend no more than a third of the first meeting talking, and use the rest to ask questions (the [ORID](ORID-Focused-Conversation-Tutorial-en.md) question structure helps here).

## Common Mistakes

1.  **Turning it into a blame session.** Once someone is held up as responsible, everyone shifts into self-protection and the truth stops surfacing. Say explicitly at the start that the goal is improving the process.
2.  **Jumping to causes before facts.** Discussing "why" before agreeing on "what happened" produces conclusions built on different memories.
3.  **Only reviewing failures.** Unexamined success can't be repeated and is easily mistaken for skill rather than luck.
4.  **Judging past decisions with present information.** "We should have seen it coming" ignores what was knowable at the time.
5.  **Stopping at "someone was careless".** Keep asking why the process allowed the mistake and why it wasn't caught.
6.  **No follow-through.** Actions without owners, dates or a check-in guarantee a repeat.
7.  **Waiting too long.** A month later, only impressions remain.

## AAR vs. Project Post-Mortem vs. Pre-Mortem

| | After Action Review | Project report / post-mortem | Pre-mortem |
| --- | --- | --- | --- |
| Timing | Right after the event | At project close | **Before** execution, after planning |
| Purpose | Team learning and better practice | Reporting results upward | Finding risks that could cause failure |
| Format | Open discussion, everyone contributes | Written document, often by one author | Imagine the project has failed; work backwards |
| Output | Sustain / Start / Stop actions | Summary report | Risk list and preventive measures |

They combine well: **pre-mortem to find risks → execute → AAR to learn → project report to communicate.**

## Frequently Asked Questions

??? question "Who created the After Action Review?"

    The US Army developed AAR in the 1970s as a formal method for learning from training exercises, and it later spread to business through organizations such as Shell and General Electric.

??? question "How big does something have to be to deserve a review?"

    Any event with transferable lessons: an incident, a milestone, an important negotiation, a campaign. Small events can use a 15-minute lightweight version with one round per question.

??? question "How many people should attend?"

    Everyone directly involved, usually 5–12. Larger groups go quiet; split into smaller reviews and combine the findings. If a key participant can't attend, it's usually better to reschedule.

??? question "What if people won't speak freely with the boss in the room?"

    Have the leader name their own mistakes first; let the most junior speak first; collect sensitive points anonymously on sticky notes; or run a first round facilitated by a neutral person without the leader present.

??? question "How does AAR relate to a sprint retrospective?"

    A [Scrum](../../Product & User/product_development/Scrum-Tutorial-en.md) retrospective is an institutionalized AAR with a fixed cadence, focused on how the team works. AAR is event-driven and focused on the gap between intention and outcome.

## Extensions and Connections

*   **[ORID Focused Conversation](ORID-Focused-Conversation-Tutorial-en.md)**: a question structure that works well for facilitating reviews, especially when emotions are involved.
*   **[5 Whys](../../Problem Solving & Decision Making/root_cause_analysis/5-Whys-Tutorial-en.md)** and **[Fishbone Diagram](../../Problem Solving & Decision Making/root_cause_analysis/Fishbone-Diagram-Tutorial-en.md)**: the main tools for analyzing why the gap occurred.
*   **[PDCA Cycle](../../Strategy & Business/quality_and_operations/PDCA-Cycle-Tutorial-en.md)**: an AAR is essentially the Check and Act stages of PDCA.
*   **[Kaizen](../../Strategy & Business/quality_and_operations/Kaizen-Tutorial-en.md)**: locking in the improvements from a review is a kaizen step.
*   **[SBI Feedback Model](../feedback_techniques/SBI-Feedback-Model-Tutorial-en.md)**: when individual feedback is needed during a review, SBI keeps it specific and non-defensive.
*   **[Scrum](../../Product & User/product_development/Scrum-Tutorial-en.md)** and **[Agile](../../Product & User/product_development/Agile-Tutorial-en.md)**: the sprint retrospective is the agile team's version of a regular AAR.

---
*Reference: The After Action Review was developed by the US Army as part of its training and leadership doctrine and later adapted for organizational learning in business, where it has been discussed in Harvard Business Review and in literature on learning organizations.*
