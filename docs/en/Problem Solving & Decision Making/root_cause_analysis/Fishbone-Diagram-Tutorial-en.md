---
title: "Fishbone Diagram (Ishikawa): How to Make One, 6M Categories, Template"
description: "A fishbone (Ishikawa, cause-and-effect) diagram organizes all possible causes of a problem into categories such as the 6Ms. Learn the structure, a 5-step method, a ready-to-use template, four industry examples and common mistakes."
---

# Fishbone Diagram (Ishikawa Diagram)

When a complex problem occurs, its underlying causes are often not singular, but result from multiple interconnected factors from different areas. If we rely solely on intuition, we can easily overlook some key potential causes. The **Fishbone Diagram**, also known as the **Ishikawa Diagram** after its inventor Dr. Kaoru Ishikawa, is a powerful, visual **Root Cause Analysis** tool. Its core objective is to help teams **systematically and comprehensively** brainstorm and organize all potential causes leading to a specific problem (effect) through a structured framework resembling a fish skeleton.

The appeal of the Fishbone Diagram lies in its **structured brainstorming** process. It provides a series of classic cause categories (the "main bones" of the fish) that guide the team to think from different, predefined perspectives, thereby avoiding blind spots in thinking. By presenting all possible factors such as "Man, Machine, Material, Method, Environment" on a single diagram, the team can gain a holistic and comprehensive understanding of the problem's complexity, and on this basis, further identify the key causes most worthy of in-depth investigation and verification. It is an excellent tool for organizing a team's scattered ideas into a logical, orderly "problem panorama."

!!! abstract "Key takeaways"

    - **Purpose**: list every possible cause of a problem by category, then pick the few that are worth verifying.
    - **Structure**: head = the problem; main bones = cause categories (e.g. the 6Ms); small bones = specific causes.
    - **Method**: define the problem → choose categories → brainstorm by category → circle the key causes → verify with data.
    - **Best partners**: drill into a single cause with the [5 Whys](5-Whys-Tutorial-en.md); rank causes with [Pareto analysis](../decision_making/Pareto-Analysis-Tutorial-en.md).
    - **Remember**: every item on a fishbone diagram is a hypothesis until data confirms it.

## Structure of a Fishbone Diagram

A fishbone diagram consists of several illustrative, fixed parts:

*   **Fish Head**: Located on the far right of the diagram, usually enclosed in a box, containing the **problem or effect** we want to analyze. For example, "Product defect rate increased by 20% this month."
*   **Spine**: A horizontal main line extending from the fish head to the left.
*   **Main Bones**: Several main branches extending diagonally from the spine, representing the major **cause categories** that contribute to the problem. These categories provide structure for thinking.
*   **Sub-Branches/Small Bones**: Smaller branches extending from the main bones, representing more specific **potential causes** brainstormed by team members under each major category.

### Classic Cause Classification Models (Main Bones)

Depending on the industry of the analysis object, different classic models can be flexibly chosen for the main bone classification of the fishbone diagram:

*   **"6M" Model commonly used in manufacturing**:

    *   **Manpower**: Skills, experience, responsibility, fatigue of operators, etc.
    *   **Machine**: Aging, precision, maintenance status of production equipment, etc.
    *   **Material**: Quality, specifications, supplier stability of raw materials, etc.
    *   **Method**: Work procedures, operating instructions, process parameter settings, etc.
    *   **Measurement**: Accuracy of measuring tools, inspection standards, accuracy of data recording, etc.
    *   **Milieu/Mother Nature**: Temperature, humidity, lighting of the workplace, organizational culture, etc.

*   **"4S" or "8P" Models commonly used in service industries**:

    *   **4S**: Suppliers, Systems, Surroundings, Skills.
    *   **8P**: Product (product/service), Price, Place (channel), Promotion, People, Process, Physical Evidence, Productivity & Quality.

![Fishbone Diagram (6M Model)](./Fishbone-Diagram-Tutorial-en-diagram.png)

<!-- mermaid 源文件：Fishbone-Diagram-Tutorial-en-mermaid-src-1.mmd -->

## How to Draw and Use a Fishbone Diagram

1.  **Step 1: Clearly Define the "Fish Head" (Problem)**
    Work with the team to reach a clear, specific, and unambiguous consensus on the problem to be analyzed. Write this problem statement in the "fish head" position on the right side of the whiteboard.

2.  **Step 2: Draw the "Spine" and "Main Bones" (Cause Categories)**
    Draw the main line, and based on your industry and problem characteristics, choose an appropriate classification model (e.g., 6M), draw several main bones, and label them with category names.

3.  **Step 3: Brainstorm and Fill in the "Sub-Branches/Small Bones" (Specific Causes)**
    *   This is the core part of the fishbone diagram. The facilitator guides the team, around **each** main bone category, to brainstorm all possible specific causes.
    *   **Key Technique**: Under each specific cause, you can combine the **5 Whys** method to ask continuous "Why?" questions to find deeper causes. For example, under the "Man" main bone, one cause might be "employee operational error." You can continue to ask "Why did the error occur?" to get the deeper cause "because of insufficient training," and draw it as a small bone.
    *   Connect all thought-out causes as sub-branches or small bones to the corresponding main bone.

4.  **Step 4: Analyze the Fishbone Diagram, Identify Key Causes**
    When the fishbone diagram is filled, it provides a panoramic view of the problem's causes. At this point, the team needs to review the entire diagram together and, through discussion, voting, or simple data verification, to identify those **most likely** to lead to the problem, or have the greatest impact, the **"vital few" causes**. These key causes can be circled with a different colored pen.

5.  **Step 5: Develop a Plan for Subsequent Verification and Improvement**
    The fishbone diagram itself is a brainstorming and analysis tool; it cannot directly solve the problem. Next, the team needs to develop specific verification plans for the circled key causes (e.g., go to the site to collect data to verify whether a hypothesis is true), and on this basis, formulate the final improvement measures.

## Application Cases

**Case 1: Analyzing the Problem of "High Software App Crash Rate"**

*   **Fish Head**: App in the latest version launched, user crash rate increased by 50%.
*   **Main Bones**: A variation of the software development model can be used, such as: Code, Build, Test, Environment, People.
*   **Analysis**: Through team brainstorming, it might be found under the "Code" main bone that "new third-party library has memory leaks"; under the "Test" main bone, it might be found that "automated test cases do not cover low-end Android models." After further data verification, the team finally determined that "memory leaks" were the main cause of crashes.

**Case 2: Analyzing "Poor Performance of a Marketing Campaign"**

*   **Fish Head**: This "Double Eleven" (Singles' Day) promotion's sales did not meet the target.
*   **Main Bones**: The 4P model of marketing can be used: Product, Price, Place, Promotion.
*   **Analysis**: The team might find that under the "Price" main bone, there was "coupon rules were too complex for users to understand"; under the "Place" main bone, there was "social media advertising did not accurately reach the target audience." Through this analysis, the team can provide clear "pitfall avoidance guidelines" for the next campaign.

**Case 3: Analyzing "Increased Post-Surgical Infection Rate in Patients"**

*   **Fish Head**: This quarter's orthopedic ward's post-surgical infection rate increased by 5% compared to the previous quarter.
*   **Main Bones**: Use the 6M model for the medical field.
*   **Analysis**: A cross-functional team consisting of doctors, nurses, and infection control experts, jointly drew a fishbone diagram. They might eventually find that "inadequate execution of pre-surgical skin disinfection procedures" under the "Method" main bone, and "untimely replacement of ward ventilation system filters" under the "Environment" main bone, are the two most suspicious key causes. Next, they will focus on these two points for data collection and on-site observation.

**Case 4: Analyzing "Software Builds Take Too Long"**

*   **Head**: A full build of the main branch went from 8 to 25 minutes; developers lose about an hour a day waiting.
*   **Main bones and causes**:
    *   **Build environment**: under-powered build servers; several pipelines sharing one machine.
    *   **Build approach**: incremental builds not enabled; caches cleared on every run.
    *   **Code structure**: circular dependencies between modules, so one change triggers large rebuilds.
    *   **Dependency management**: third-party dependencies downloaded from scratch each time.
    *   **People and process**: no monitoring of build times, so the problem went unnoticed for months.
*   **Conclusion**: After timing each stage, the team found "under-powered build servers", "no incremental builds" and "circular dependencies" were the three biggest causes, and planned hardware upgrades and refactoring accordingly. "No monitoring" wasn't a direct cause, but it explained why the problem lasted so long, so they added a build-time alert as well.

## Advantages and Challenges of Fishbone Diagram

**Core Advantages**


*   **Structured and Comprehensive**: Provides a clear structure that guides the team to think systematically from multiple dimensions, effectively avoiding omissions.
*   **Promotes Team Participation and Consensus**: An excellent team collaboration tool that can gather everyone's wisdom and reach consensus on the complexity of the problem.
*   **Visual**: Presents complex causal relationships in a very intuitive and clear way.

**Potential Challenges**


*   **Can Become Overly Complex**: For an extremely complex problem, the fishbone diagram can become very large and cluttered, losing its clear focus.
*   **Cannot Reflect the Weight of Causes**: The fishbone diagram itself, does not show which cause has a greater impact. It needs to be combined with other tools like Pareto analysis to determine priorities.
*   **Only a Collection of "Hypotheses"**: All "causes" on the fishbone diagram, before being validated by data, are still only "potential, suspicious" causes, not facts.

## Fishbone Diagram Template

Prepare this "cause register" before the session and fill it in as you draw. By the end of the meeting you'll have an actionable verification list.

**Problem statement (head)**: ________ (measurable, time-bound, no cause assumed)

| Category (main bone) | Specific cause | Deeper cause (5 Whys) | Existing evidence / data needed | Key? | Owner |
| --- | --- | --- | --- | --- | --- |
| People | Errors by new staff | No standardized training material | Rework records of new staff, last month | ✓ | Alex |
| Machine | Equipment precision declining | Maintenance interval extended | Maintenance log | | Sam |
| Method | … | … | … | | |
| Material | … | … | … | | |
| Measurement | … | … | … | | |
| Environment | … | … | … | | |

**Pre-meeting checklist**

- [ ] The problem statement contains no "because..."
- [ ] Participants cover every stage involved (front line, management, quality/testing)
- [ ] Basic data is ready (when, how often, how widespread)
- [ ] The categories are chosen and written on the board in advance

## Common Mistakes

1.  **Writing a cause into the head.** "Complaints rose because we're understaffed" answers the question before the analysis starts, and the team will only look for evidence in that direction. The head states the effect only.
2.  **Treating "causes we thought of" as "causes we found".** A fishbone diagram is a list of hypotheses. Acting without verifying can waste a lot of effort without fixing anything.
3.  **Stopping at the surface.** "Careless staff" or "bad equipment" can't be acted on. Ask why two or three more times until you reach a process, standard or resource you can change.
4.  **One person drawing it alone.** The value comes from different roles' perspectives. With only managers or only front-line staff, whole categories of causes go missing.
5.  **Trying to fill every bone.** A diagram with a hundred causes can't be focused. If there are too many, split the problem (by product line or time period) or keep only the more likely causes.
6.  **Overlapping categories.** Having both "process" and "method" leaves people arguing about where a cause belongs. Keep categories distinct.

## Fishbone Diagram vs. 5 Whys vs. Pareto Analysis

| | Fishbone Diagram | [5 Whys](5-Whys-Tutorial-en.md) | [Pareto Analysis](../decision_making/Pareto-Analysis-Tutorial-en.md) |
| --- | --- | --- | --- |
| Question it answers | What are all the possible causes? | What is the root of this particular cause? | Which causes matter most? |
| Direction | Broad, horizontal | Deep, vertical | Quantified ranking |
| Needs data? | Not necessarily; draws on team experience | Ideally backed by facts | Yes: counts or costs per cause |
| Best for | Complex problems with causes in several areas | Problems with a fairly clear causal chain | Allocating effort once causes are known |
| Typical use | List all suspected causes first | Drill into the key causes on the fishbone | Decide which to fix first after collecting data |

The most common combination: **fishbone diagram to list causes → Pareto analysis to prioritize → 5 Whys to dig into the top ones.**

## Frequently Asked Questions

??? question "Are a fishbone diagram, an Ishikawa diagram and a cause-and-effect diagram the same thing?"

    Yes. "Fishbone" comes from its shape, "Ishikawa" from its inventor Kaoru Ishikawa, and "cause-and-effect" from what it shows.

??? question "Do I have to use the 6M categories?"

    No. The 6Ms (Man, Machine, Material, Method, Measurement, Mother Nature) suit manufacturing and quality problems. Services often use the 4Ss or 8Ps; software teams often use code, build, test, infrastructure, people and process. Any set works as long as it covers all possible sources without overlapping.

??? question "How many causes should a fishbone diagram have?"

    There's no hard rule; typically 3–6 specific causes per bone and 20–30 overall. Far more usually means the problem is defined too broadly and should be split.

??? question "What tools can I use to draw one?"

    In a live session, a whiteboard and sticky notes are fastest because you can move things around. For records or remote work, spreadsheet templates, Miro, Lucidchart or draw.io all work. Getting the problem and categories right matters more than the tool.

??? question "What do I do after drawing the diagram?"

    Collect data to verify the circled key causes, use Pareto analysis to decide which to fix first, use the 5 Whys to reach an actionable root cause for each confirmed cause, then implement countermeasures and track the results.

## Extensions and Connections

*   **[5 Whys](5-Whys-Tutorial-en.md)**: The golden partner of the fishbone diagram. When using the fishbone diagram for horizontal, broad cause brainstorming, the 5 Whys can be used at any time to conduct a vertical, in-depth root cause analysis for a specific cause.
*   **[Brainstorming](../ideation/Brainstorming-Tutorial-en.md)**: The fishbone diagram provides a structured framework for brainstorming, making idea generation more orderly and focused.
*   **[Pareto Analysis](../decision_making/Pareto-Analysis-Tutorial-en.md)**: After identifying all potential causes with a fishbone diagram, data can be collected, and Pareto analysis used to determine which are the "vital few" causes that lead to 80% of the problems.

---
*Source Reference: Dr. Kaoru Ishikawa was one of the pioneers of the post-war quality management movement in Japan. The fishbone diagram, as one of the "Seven Quality Control Tools" he invented, is widely used in quality management and continuous improvement activities worldwide, and is an indispensable basic tool in Total Quality Management (TQM) and Six Sigma practices.*