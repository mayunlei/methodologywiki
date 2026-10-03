---
title: "Value Stream Mapping (VSM): How to Draw One, Metrics and Examples"
description: "Value stream mapping puts every process step, every wait and the information flow on a single page, exposing the real bottleneck. Learn how to draw current-state and future-state maps, key metrics like process cycle efficiency, a worked example, a template and common mistakes."
---

# Value Stream Mapping (VSM)

An order takes 21 days from placement to delivery. How should the team improve it? The usual answer is to make every step "a bit faster" — but in many processes, of those 21 days only about three hours involve anyone actually working. The rest is **waiting**. Making people 20% faster at the work changes almost nothing.

**Value stream mapping (VSM)** exists to reveal that truth. It draws an entire process on one page: what each step does, how long it takes, how much piles up in between, and how information travels. When the map is finished, **the gap between value-added time and total lead time** usually shocks everyone in the room. That gap is the opportunity.

VSM comes from the Toyota Production System's material and information flow diagrams and is a core [lean](Lean-Operations-Tutorial-en.md) tool. The crucial difference from an ordinary flowchart: **a flowchart shows steps; a value stream map also shows waiting, inventory and information flow, with real data attached**.

!!! abstract "Key takeaways"

    - **Draw two maps**: current state (what really happens) and future state (the target), with an action plan between them.
    - **Three flows**: material/work flow (left to right), information flow (right to left), timeline (along the bottom).
    - **Key metric**: value-added time ÷ total lead time = process cycle efficiency. Most processes are under 5%.
    - **Walk it, don't imagine it**: collect data on the floor with a stopwatch, not from process documents.
    - **Bottlenecks usually live in waiting and handoffs**, not in anyone working slowly.

## What's on a Value Stream Map

A standard map has three layers:

| Layer | Position | Content |
| --- | --- | --- |
| **Information flow** | Top, right to left | How customer demand reaches each step: orders, schedules, kanban signals |
| **Material / work flow** | Middle, left to right | Each processing step and the inventory piling up between them |
| **Timeline** | Bottom, as a staircase | Upper steps = value-added time; lower steps = waiting |

Each processing step carries a **data box**, commonly with:

| Metric | Meaning |
| --- | --- |
| **C/T (cycle time)** | Time to process one unit |
| **C/O (changeover time)** | Time to switch from one task type to another |
| **Available time** | Working time actually available per day |
| **First pass yield** | Share that passes without rework |
| **WIP** | Work in progress waiting between steps |

## The Key Metric: Process Cycle Efficiency

| Term | Definition |
| --- | --- |
| **Value-added time (VA)** | Time the customer would pay for: time that actually transforms the product or service |
| **Non-value-added time (NVA)** | Waiting, moving, rework, approval queues |
| **Lead time** | Total elapsed time from start to finish |
| **Process cycle efficiency** | Value-added time ÷ lead time |

**Most unoptimized processes run between 1% and 5%.** The implication is direct: rather than speeding up the 3%, eliminate the 97%. That is the single most important insight VSM delivers.

**Three tests for value-added** (all must hold):

1.  The customer would pay for it;
2.  It changes the form of the product or information;
3.  It is done right the first time.

Approvals, inspections, transport, waiting and rework fail these tests. Some are necessary under current conditions (regulatory inspection, for example) and are called "necessary non-value-added": reduce them rather than remove them outright.

## How to Draw One

1.  **Pick one product family or process.** Don't try to map everything at once; choose something representative and high volume.
2.  **Define the start and end points**, usually "customer order to customer receipt" or "request raised to live in production".
3.  **Walk the floor backwards**, starting from the step closest to the customer. It makes each step's purpose clearer.
4.  **Draw the work flow and collect data**: cycle time, WIP, first pass yield for each step. **Time it yourself; don't use the numbers in the process document.**
5.  **Draw the information flow.** How does demand reach each step? Is work pushed downstream when upstream finishes, or pulled when downstream needs it?
6.  **Draw the timeline and calculate efficiency.** This is the step with the most impact.
7.  **Mark the problems** on the map (traditionally with "kaizen burst" symbols): bottlenecks, long waits, high rework.
8.  **Draw the future state**: a target that removes waiting and shortens lead time.
9.  **Build the action plan**: break the future state into projects with owners and dates.

## Template

**Basics**: product family or process, date, participants, start and end points

| Step | What happens | Cycle time | Wait before next step | WIP | First pass yield | Problems found |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | | | | | | |
| 2 | | | | | | |
| … | | | | | | |
| **Total** | | **VA time =** | **Total wait =** | | | **Efficiency =** |

**Future-state action plan**

| Improvement | Problem it addresses | Expected effect | Owner | Due |
| --- | --- | --- | --- | --- |

**Checklist**

- [ ] Data was measured on the floor, not taken from documents
- [ ] Information flow is drawn, not just work flow
- [ ] The timeline separates value-added time from waiting
- [ ] Process cycle efficiency is calculated
- [ ] Every future-state improvement has an owner and a date

## Worked Example: An Insurance Claims Process

Small home-insurance claims at one insurer took **21 days** on average, and complaints centered on the wait. The team mapped it:

| Step | Actual processing time | Wait before next step | Problem |
| --- | --- | --- | --- |
| Register claim | 15 min | 1 day (batched handover) | Batch processing |
| Document review | 30 min | 4 days (waiting on customer) | Document list sent in three separate requests |
| Assessment and pricing | 45 min | 6 days (waiting for scheduling) | Assessors scheduled by region; cross-region claims queue |
| Approval | 20 min | 7 days (weekly Thursday committee) | Every claim goes to committee regardless of size |
| Payment | 10 min | 2 days (batched payment runs) | Payments run twice a week |
| **Total** | **≈ 2 hours** | **20 days** | **Efficiency ≈ 0.4%** |

**The key finding**: only two hours of the 21 days involved actual work. Making every step 20% faster would have cut total time from 21 days to about 20.98 — effectively nothing.

**Three future-state improvements**:

1.  **Complete document list up front**, sent at registration → removes most of the 4-day document wait.
2.  **Delegated approval for small claims**: assessors approve anything under a set amount without the committee → removes the 7-day approval wait.
3.  **Daily payment runs** instead of twice weekly → 2 days down to 0.5.

**Result**: average claim settlement fell from 21 days to **6 days** with the same headcount, because what changed was the structure of the waiting, not the speed of the work.

## Common Mistakes

1.  **Mapping steps without waits.** A map showing only processing steps is just a flowchart and hides where 97% of the time goes.
2.  **Using documented rather than measured data.** The process document may say "approval: one working day" when the real average is seven.
3.  **Too much detail.** Fifty steps on one map obscures the point. Start with 8–12 major steps and expand individual ones if needed.
4.  **Stopping at the current-state map.** The current state is the diagnosis; the future state and action plan are the output.
5.  **Each department mapping its own section.** The value of VSM lies in the cross-functional whole; mapping in pieces loses the handoff waits, which are usually the biggest problem.
6.  **Optimizing a non-bottleneck.** Doubling the speed of a step that isn't the constraint may not change lead time at all.
7.  **Treating it as a one-off.** Redraw the map periodically, especially after significant process changes.

## VSM vs. Related Tools

| | Value Stream Map | Flowchart | [Kanban](../../Product & User/product_development/Kanban-Tutorial-en.md) | [Logic Tree](../../Problem Solving & Decision Making/problem_solving/Logic-Tree-Tutorial-en.md) |
| --- | --- | --- | --- | --- |
| Shows | Steps + waits + information flow + data | Steps and branches | Current flow of work in progress | Hierarchical breakdown of a problem |
| Time dimension | Yes (timeline, efficiency) | No | Real time | No |
| Main use | Diagnosing waste in a process | Describing how a process runs | Managing day-to-day flow | Analyzing causes |
| Output | Current + future state + action plan | Process documentation | Continuous flow improvement | List of causes |

**A common combination**: VSM to find structural waste → [5 Whys](../../Problem Solving & Decision Making/root_cause_analysis/5-Whys-Tutorial-en.md) to dig into specific causes → [Kanban](../../Product & User/product_development/Kanban-Tutorial-en.md) to manage the improved flow → [PDCA](PDCA-Cycle-Tutorial-en.md) to drive each improvement.

## Frequently Asked Questions

??? question "What is the difference between a value stream map and a flowchart?"

    A flowchart shows what happens and in what order. A value stream map adds **waiting time, work in progress and information flow**, attaches measured data to each step, and calculates process cycle efficiency, so you can see where the waste is.

??? question "Does VSM work for services and software?"

    Yes, often with greater impact. In software it's commonly applied to "request raised to live in production", exposing hidden waits for review, test environments and release windows. The insurance example above is a service process.

??? question "How long does it take to map a value stream?"

    For a moderately complex process, a cross-functional group of five to eight people typically needs one to two days: half a day walking the process and collecting data, half a day on the current state, half a day on the future state and plan.

??? question "Is 1% efficiency really normal?"

    Very. Unoptimized processes commonly run between 1% and 5%. It doesn't mean people are slacking; it means **the waste is in the structure of the process, not in individual effort**.

??? question "How ambitious should the future state be?"

    Usually a state reachable within 6–12 months, broken into three to five improvement projects that can run independently. Set it too far out and it becomes a vision nobody acts on.

## Extensions and Connections

*   **[Lean Operations](Lean-Operations-Tutorial-en.md)**: VSM is the core tool for the "map the value stream" principle of lean.
*   **[PDCA Cycle](PDCA-Cycle-Tutorial-en.md)**: each future-state improvement can be driven and verified with one PDCA turn.
*   **[Kaizen](Kaizen-Tutorial-en.md)**: value stream maps are often used to choose the theme for a kaizen event.
*   **[Gemba Walk](../../Problem Solving & Decision Making/problem_solving/Gemba-Walk-Tutorial-en.md)**: how you collect the real data the map depends on.
*   **[Kanban](../../Product & User/product_development/Kanban-Tutorial-en.md)**: the usual way to implement the pull system a future-state map calls for.
*   **[Six Sigma](Six-Sigma-Tutorial-en.md)**: in Lean Six Sigma, VSM is commonly used in the Measure and Analyze phases of DMAIC.

---
*Reference: Value stream mapping originated as the material and information flow diagram in the Toyota Production System. Mike Rother and John Shook systematized it as VSM in *Learning to See* (1999), still the standard text on the method.*
