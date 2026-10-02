---
title: "Pareto Analysis (80/20 Rule): How to Make a Pareto Chart, Examples"
description: "Pareto analysis uses the 80/20 principle to find the vital few causes behind most of a problem. Learn how to build a Pareto chart step by step, a data template, how to read the cumulative line, examples and the mistakes that lead to wrong priorities."
---

# Pareto Analysis

In our work and life, we often encounter a common and profound pattern: **a few key causes lead to the vast majority of results**. For example, 80% of a company's profits might come from 20% of its customers; 80% of software crashes are caused by 20% of bugs; and 80% of our worries stem from 20% of things. **Pareto Analysis**, based on this "**80/20 rule**," aims to help us identify the **"vital few"** among numerous influencing factors that play a decisive role, thereby concentrating limited time, energy, and resources on areas that yield the greatest benefits.

Pareto analysis is not just a data analysis technique but also an efficient decision-making and management philosophy. It was proposed by management guru Joseph Juran and named after Italian economist Vilfredo Pareto, who discovered in the 19th century that 80% of Italy's land was owned by 20% of the population. The core tool of Pareto analysis is the **Pareto Chart**, which, through a unique combination of bar and line graphs, sorts various causes of a problem by their importance (usually frequency or cost) from high to low, allowing us to easily identify the main issues at a glance.

!!! abstract "Key takeaways"

    - **The 80/20 principle**: a small share of causes usually accounts for most of the effect.
    - **A Pareto chart** combines bars sorted from largest to smallest with a cumulative percentage line.
    - **Measure the right thing**: count by cost, time or impact, not just frequency, when they differ.
    - **80/20 is a pattern, not a law**: it might be 70/30 or 90/10; the point is uneven distribution.
    - **Use it with root-cause tools**: Pareto tells you where to look; the [5 Whys](../root_cause_analysis/5-Whys-Tutorial-en.md) and [fishbone diagram](../root_cause_analysis/Fishbone-Diagram-Tutorial-en.md) tell you why.

## Components of a Pareto Chart

Pareto Chart is a special type of chart that cleverly combines two graphical elements to convey rich information.

*   **Bar Chart**:
    *   The X-axis represents different **cause categories** leading to the problem (e.g., different types of customer complaints).
    *   Bars are arranged from left to right in **descending order** of their impact (e.g., frequency of occurrence, cost incurred).
    *   The left Y-axis represents the specific value for each cause category (e.g., frequency).

*   **Line Graph**:
    *   This line is called the **cumulative percentage curve**.
    *   It shows the cumulative percentage of the total impact accounted for by the cause categories from left to right.
    *   The right Y-axis represents the cumulative percentage from 0% to 100%.

By observing this chart, we can quickly locate the steepest rising area of the cumulative percentage curve, and the corresponding bars are the "vital few" that we need to prioritize.

### Pareto Chart Example

Suppose a restaurant analyzed all customer complaints from the last month:

![Pareto Chart Example](./Pareto-Analysis-Tutorial-en-diagram.png)

<!-- mermaid 源文件：Pareto-Analysis-Tutorial-en-mermaid-src-1.mmd -->

*   **Analysis**: From this (hypothetical) chart, the restaurant manager can clearly see that "slow service" and "food taste" might account for 75% of all complaints. Therefore, instead of spreading efforts to solve all problems, they should concentrate resources on prioritizing the optimization of kitchen service processes and dish development processes.

## How to Conduct a Pareto Analysis

1.  **Step One: Define the Problem to Analyze and Cause Categories**
    Clearly define the core problem you want to solve (e.g., "reduce product defects") and determine the cause categories for classification (e.g., types of defects: scratches, functional failures, missing parts, etc.).

2.  **Step Two: Collect Data and Determine Measurement Units**
    Systematically collect data on the occurrence of each cause category over a period. You need to determine a consistent unit of measurement. The most common is **frequency** (number of occurrences), but in some cases, **cost** (economic loss caused by each reason) might be a more insightful unit.

3.  **Step Three: Organize and Sort Data**
    Sort all cause categories in descending order according to your chosen measurement unit (e.g., frequency). Then, calculate the percentage for each category and the cumulative percentage from high to low.

4.  **Step Four: Draw the Pareto Chart**
    *   Create a combined chart.
    *   Draw the bar chart, with the X-axis representing cause categories and the left Y-axis representing frequency, and draw the bars in the sorted order.
    *   Draw the line graph, marking the cumulative percentage at the center top of each bar, and then connect these points to form the cumulative curve. The right Y-axis indicates 0% to 100%.

5.  **Step Five: Analyze the Chart and Determine Action Focus**
    Analyze the Pareto chart to identify the "vital few" causes that account for approximately 80% of the problems. These are the key areas you need to focus on for root cause analysis (e.g., using "5 Whys" or "Fishbone Diagram") and resolution.

## Application Cases

**Case 1: Bug Management in Software Development**

*   **Problem**: A software product received a large number of user bug reports after launch.
*   **Application**: The development team categorized all bugs by module (e.g., "user login module," "payment module," "data reporting module," etc.) and counted the number of bugs under each module. By drawing a Pareto chart, they found that over 70% of the bugs were concentrated in the "data reporting module." This finding allowed the team to concentrate testing and development resources on prioritizing the refactoring and fixing of this most unstable module, thereby efficiently improving the overall product quality.

**Case 2: Personal Time Management**

*   **Problem**: An individual feels busy every day but is inefficient and doesn't know where their time goes.
*   **Application**: They spent a week recording all their daily time expenditures and categorizing them (e.g., "coding," "meetings," "browsing social media," "processing emails," etc.). After drawing a Pareto chart, they were shocked to find that nearly 60% of their working time was occupied by "ineffective meetings" and "frequent social media checks." This analysis prompted them to selectively attend meetings and use the Pomodoro Technique to reduce distractions, thereby investing more time in truly important work.

**Case 3: Inventory Management Optimization**

*   **Problem**: A retailer wants to reduce its inventory management costs.
*   **Application**: They analyzed the annual sales of all products in their warehouse and drew a Pareto chart. This is known as **ABC Classification**. They found that Class A products (approximately 20% of all product types) contributed about 80% of sales. Based on this, they developed differentiated inventory management strategies: for Class A products, they implemented the strictest inventory monitoring and demand forecasting to ensure no stockouts; for Class C products with very low sales, they adopted a more lenient management strategy, or even considered delisting them.

## Advantages and Challenges of Pareto Analysis

**Core Advantages**

*   **Focus on Key Issues**: The most significant advantage is that it helps us quickly identify the most important driving factors from a multitude of complex problems, avoiding scattered and wasted resources.
*   **Strong Basis for Decision-Making**: Provides clear, visual data evidence to support decisions on "what we should prioritize," making it easy to reach consensus within the team.
*   **Highly Versatile**: Can be applied in almost all fields, including quality management, project management, time management, and sales analysis.

**Potential Challenges**

*   **Looks Only at History, Not Future**: Pareto analysis is based on historical data; it cannot predict new problems that may arise in the future.
*   **Neglect of Qualitative Factors**: It primarily focuses on quantifiable factors (e.g., frequency, cost). For problems that occur infrequently but have extremely severe impacts (e.g., a rare but fatal safety accident), Pareto analysis might underestimate their importance.
*   **Lack of Cause Analysis**: Pareto analysis can only tell you "what" the main problems are, but not "why" these problems occur. It is a tool for identifying problems, not for solving them.

## Pareto Chart Data Template

| Category (cause) | Count / cost | % of total | Cumulative % |
| --- | --- | --- | --- |
| Wrong item shipped | 120 | 40.0% | 40.0% |
| Late delivery | 75 | 25.0% | 65.0% |
| Damaged in transit | 45 | 15.0% | 80.0% |
| Missing invoice | 30 | 10.0% | 90.0% |
| Billing error | 18 | 6.0% | 96.0% |
| Other | 12 | 4.0% | 100.0% |
| **Total** | **300** | **100%** | |

**How to build the chart**: sort categories from largest to smallest (keep "Other" last), draw bars for the counts, then plot the cumulative percentage as a line on a second axis. The categories to the left of where the line crosses roughly 80% are the "vital few"; here, the first three categories.

## Common Mistakes

1.  **Counting frequency when impact matters.** Ten minor complaints may matter less than one lost key account. Weight by cost or severity when appropriate.
2.  **A huge "Other" bar.** If "Other" is one of the largest categories, your categories are too coarse. Break it down.
3.  **Too short a data period.** One week of data may reflect an unusual event. Use a period long enough to be representative.
4.  **Treating 80/20 as exact.** Don't force the cut-off at exactly 80%; look for the natural break where the bars drop off.
5.  **Stopping at the chart.** Pareto analysis shows priorities, not causes or solutions. Follow up with root cause analysis.
6.  **Ignoring the trivial many forever.** After fixing the top causes, re-run the analysis; the next layer becomes the new priority.

## Frequently Asked Questions

??? question "Who came up with the Pareto principle?"

    Italian economist Vilfredo Pareto observed around 1896 that about 80% of land in Italy was owned by about 20% of the population. Quality pioneer Joseph Juran later generalized it as the "vital few and trivial many".

??? question "Does it have to be exactly 80/20?"

    No. The numbers don't need to add up to 100 either: 20% of causes might produce 70% or 90% of effects. The principle is about imbalance.

??? question "What tools can I use to make a Pareto chart?"

    Excel and Google Sheets have built-in Pareto chart types; most statistics and quality tools (Minitab, Python, R) do too. A hand-drawn chart works fine for team discussions.

??? question "How does Pareto analysis relate to Six Sigma?"

    It is one of the basic quality tools used in Six Sigma's Measure and Analyze phases to decide which defect types or causes to tackle first.

## Extensions and Connections

*   **Root Cause Analysis**: After identifying the "vital few" problems through Pareto analysis, the next step is usually to use tools like **Fishbone Diagram** or **5 Whys** to conduct an in-depth root cause analysis of these key problems.
*   **Quality Management**: Pareto analysis is a fundamental and core tool in quality management systems such as Total Quality Management (TQM) and Six Sigma.

---
*Reference: The concept of Pareto analysis, as one of the seven basic tools of quality management, its ideas and applications are extensively elaborated in the Project Management Body of Knowledge (PMBOK) and various textbooks on quality management and operations management. Joseph Juran's "Quality Control Handbook" made pioneering contributions to the application of this principle in management.*