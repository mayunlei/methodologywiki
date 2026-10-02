---
title: "Scrum Framework: Roles, Events, Artifacts and How a Sprint Works"
description: "Scrum is an agile framework that delivers value in short, fixed-length sprints using three accountabilities, five events and three artifacts. Learn how a sprint works, each role's responsibilities, a sprint cheat sheet, Scrum vs Kanban and common mistakes."
---

# Scrum

In the vast world of Agile development, if Agile is a set of "values" guiding us to embrace change, then **Scrum** is the most popular and widely applied **lightweight framework** that puts these values into practice. Scrum is not a detailed process or method, but a **"rulebook" for the game** designed to help teams collaborate efficiently and continuously deliver value when developing complex products. It provides a simple, clear, yet powerful iterative work rhythm for teams by defining a series of clear **roles, events, and artifacts**.

The name Scrum comes from the "scrum" action in rugby, emphasizing that the entire team works together as a cohesive unit, pushing towards a common goal. It acknowledges that when facing complex problems, we cannot have all the answers from the beginning. Therefore, the core of Scrum is to break down a large, uncertain problem into a series of small, manageable experiments through short, fixed-time iterations (i.e., "**Sprints**"). At the end of each sprint, the team delivers a usable product increment and reflects and adjusts, thereby learning from experience and moving forward amidst change.

!!! abstract "Key takeaways"

    - **Three accountabilities**: Product Owner, Scrum Master, Developers.
    - **Five events**: the Sprint, Sprint Planning, Daily Scrum, Sprint Review, Sprint Retrospective.
    - **Three artifacts**: Product Backlog, Sprint Backlog, Increment, each with a commitment (Product Goal, Sprint Goal, Definition of Done).
    - **Sprints are fixed-length** (one month or less) and produce a usable increment.
    - **Empiricism**: transparency, inspection and adaptation.

## The Three Pillars of the Scrum Framework

The entire Scrum framework is built upon three empirical pillars:

1.  **Transparency**: All important aspects affecting the outcome must be visible to all people responsible for the outcome (including customers). This means that work progress, impediments, backlogs, etc., must be open and transparent.
2.  **Inspection**: Scrum artifacts and the progress towards a goal must be frequently and diligently inspected to detect undesirable variances or problems in a timely manner.
3.  **Adaptation**: When an inspection determines that the current work deviates from acceptable limits and the resulting product will be unacceptable, the process or the material being processed must be adjusted as soon as possible.

## The 3-5-3 Structure of Scrum

Scrum's "rules of the game" can be concisely summarized as a "3-5-3" structure: 3 roles, 5 events, 3 artifacts.

![Scrum Framework](./Scrum-Tutorial-en-diagram.png)

<!-- mermaid 源文件：Scrum-Tutorial-en-mermaid-src-1.mmd -->

### 3 Roles

*   **Product Owner**: The sole person responsible for the "value" of the product. Their main job is to manage and optimize the **Product Backlog**, ensuring the Development Team always works on items that create the highest value for customers and the business. They decide "what to do."
*   **Scrum Master**: The "servant leader" and "coach" of the Scrum framework. They do not manage the team but serve the team, responsible for removing impediments, facilitating events, and ensuring Scrum rules and values are correctly understood and followed by the team.
*   **Developers**: A cross-functional, self-organizing professional team who collectively are responsible for transforming items from the backlog into a high-quality, deliverable product increment within each sprint. They decide "how to do it."

### 5 Events

*   **Sprint**: The heart of Scrum, a fixed-length time-box (typically 1-4 weeks). Within a sprint, the team focuses on achieving a valuable "Sprint Goal."
*   **Sprint Planning**: Held at the beginning of each sprint. The Product Owner explains the highest priority items from the Product Backlog to the Development Team. The team collectively selects and commits to the work they can complete within the sprint and creates a preliminary execution plan, forming the **Sprint Backlog**.
*   **Daily Scrum**: A daily synchronization meeting not exceeding 15 minutes. Each member of the Development Team takes turns answering three questions: "What did I do yesterday?" "What will I do today?" "What impediments did I encounter?" Its purpose is to quickly synchronize progress and identify impediments, not to report to management.
*   **Sprint Review**: Held at the end of the sprint. The Development Team **demonstrates** the completed, working **Increment** to the Product Owner, customers, and other stakeholders, and gathers feedback. This is an informal meeting about the "product."
*   **Sprint Retrospective**: Held after the Sprint Review and before the next sprint begins. The Scrum Team (PO, SM, Devs) collectively **reflects** on what went well and what could be improved regarding **people, relationships, processes, and tools** in the just-completed sprint, and creates a concrete improvement plan for the next sprint.

### 3 Artifacts

*   **Product Backlog**: A dynamic, prioritized, comprehensive **list** of all known product requirements, features, fixes, and improvements. It is solely managed by the Product Owner.
*   **Sprint Backlog**: The list of tasks the Development Team commits to completing in the current sprint, and the plan to achieve the "Sprint Goal." It is solely owned and managed by the Development Team.
*   **Increment**: The sum of all completed Product Backlog items at the end of each sprint. It must be **usable and conform to the "Definition of Done."** It is a direct manifestation of the team's work results.

## Application Cases

**Case 1: Developing an Online Food Ordering App**

*   **Product Backlog**: Contains hundreds of user stories like "user registration," "browse menu," "online payment," "order tracking," etc.
*   **Sprint 1 (2 weeks)**:
    *   **Sprint Goal**: "Users can successfully register and log in."
    *   **Sprint Backlog**: The team selected 5 user stories related to registration and login.
    *   **Daily Scrum**: The team synchronized progress daily and found that "unstable SMS verification code interface" was an impediment. The Scrum Master immediately coordinated to resolve it.
    *   **Sprint Review**: The team demonstrated a working, complete registration and login process.
    *   **Sprint Retrospective**: The team reflected that their task estimations were too optimistic and decided to adopt a more conservative estimation method in the next sprint.

**Case 2: A Marketing Team Planning a Product Launch Event**

*   Scrum is not only applicable to software development.
*   **Product Owner**: Marketing Director.
*   **Product Backlog**: Contains all work items such as "determine launch event theme," "design main visuals," "invite media and KOLs," "write press releases," "venue booking," etc.
*   **Sprint 1 (1 week)**:
    *   **Sprint Goal**: "Finalize the core theme and initial main visual design for the launch event."
    *   The team quickly produced results through a one-week sprint and demonstrated them to senior management at the review meeting, receiving timely feedback and avoiding investing too many design resources in the wrong direction.

**Case 3: A Student Group Completing a Semester Project**

*   **Product Owner**: One student acts as PO, responsible for communicating with the professor and clarifying project requirements.
*   **Product Backlog**: The entire project is broken down into parts such as "literature review," "data collection," "data analysis," "report writing," "PPT creation."
*   **Sprints**: They divided the remaining 8 weeks of the semester into 4 two-week sprints. Each sprint had a clear goal, for example, the goal of the first sprint was to "complete the literature review and research design." This approach effectively avoided last-minute cramming at the end of the semester.

## Advantages and Challenges of Scrum

**Core Advantages**

*   **Increased Productivity and Speed**: Through short-cycle iterations and focus, teams can deliver value faster.
*   **Enhanced Flexibility and Adaptability**: Can calmly respond to changing requirements and adjust direction in a timely manner based on feedback.
*   **Improved Transparency and Communication**: Clear roles, events, and artifacts greatly facilitate communication and information synchronization within and outside the team.
*   **Empowers Teams, Boosts Morale**: Self-organizing development teams have higher autonomy and a sense of ownership.

**Potential Challenges**

*   **"Easy to Understand, Difficult to Master"**: Scrum rules are simple, but truly understanding the underlying Agile spirit and successfully practicing it within a specific organizational culture is very difficult.
*   **Extremely High Demands on Product Owner**: The Product Owner needs to deeply understand the business, market, and customers, and possess excellent communication and decision-making skills.
*   **Potential for "Scope Creep"**: If the Product Owner does not manage the backlog and stakeholder expectations well, it can lead to frequent changes in sprint goals.
*   **Requires Team Maturity**: Self-organizing teams require members to have a high sense of responsibility, collaborative spirit, and cross-functional skills.

## Scrum Events Cheat Sheet

| Event | Timebox (1-month sprint) | Purpose | Who |
| --- | --- | --- | --- |
| **Sprint** | ≤ 1 month | Container for all other events; deliver an increment | Whole Scrum Team |
| **Sprint Planning** | ≤ 8 hours | Decide why (Sprint Goal), what and how | Whole Scrum Team |
| **Daily Scrum** | 15 minutes | Inspect progress toward the Sprint Goal; adapt the plan | Developers |
| **Sprint Review** | ≤ 4 hours | Inspect the increment with stakeholders; adapt the backlog | Scrum Team + stakeholders |
| **Sprint Retrospective** | ≤ 3 hours | Improve how the team works | Scrum Team |

Timeboxes are shorter for shorter sprints.

## Accountabilities at a Glance

| Accountability | Responsible for |
| --- | --- |
| **Product Owner** | Maximizing product value; managing and ordering the Product Backlog; the Product Goal |
| **Scrum Master** | Scrum effectiveness; coaching the team and organization; removing impediments |
| **Developers** | Creating a usable increment each sprint; the Sprint Backlog; quality (Definition of Done) |

## Common Mistakes

1.  **The Daily Scrum as a status report.** It's for Developers to coordinate toward the Sprint Goal, not to report to a manager.
2.  **No real Sprint Goal.** A list of unrelated tickets gives the team nothing to focus or trade off against.
3.  **Changing sprint scope constantly.** Some adjustment is normal, but endangering the Sprint Goal mid-sprint undermines planning.
4.  **A weak Definition of Done.** "Done except testing" leads to hidden work piling up.
5.  **Product Owner as a proxy without authority.** If decisions must be escalated, the backlog can't be managed effectively.
6.  **Skipping retrospectives.** The team stops improving; problems become permanent.

## Frequently Asked Questions

??? question "How long should a sprint be?"

    One month or less; two weeks is the most common choice. Shorter sprints give faster feedback; longer ones reduce overhead but increase risk.

??? question "What is the difference between Scrum and Agile?"

    Agile is a set of values and principles; Scrum is a specific framework that implements them. See [Agile](Agile-Tutorial-en.md).

??? question "Who wrote the Scrum framework?"

    Ken Schwaber and Jeff Sutherland, who maintain *The Scrum Guide* (latest major revision 2020).

??? question "Can Scrum be used outside software?"

    Yes. Marketing, research, education and event teams use Scrum when work can be broken into increments and benefits from regular feedback.

## Extensions and Connections

*   **[Agile Development](Agile-Tutorial-en.md)**: Scrum is a specific, mainstream **framework** for realizing Agile values and principles.
*   **[Kanban](Kanban-Tutorial-en.md)**: Another popular Agile method. Unlike Scrum's rhythm based on "time-box (sprints)," Kanban focuses more on "continuous flow." In practice, many teams combine the two; for example, using Kanban within a Scrum sprint to visualize and manage the flow of tasks, which is called "Scrumban."
*   **Extreme Programming (XP)**: Scrum provides the "management framework," while XP provides a set of excellent "engineering practices." Integrating XP practices (such as Test-Driven Development, Pair Programming) into the Scrum framework can greatly improve the technical quality of product increments.

---
*Reference: The Scrum framework was first jointly proposed by Jeff Sutherland and Ken Schwaber in the early 1990s. Their collaborative work, "The Scrum Guide," is the sole official definition of the Scrum framework and is regularly updated to reflect the evolution of practice.*