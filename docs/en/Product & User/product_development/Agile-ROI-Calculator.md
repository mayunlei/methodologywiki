# Agile Transformation ROI Calculator

![Agile ROI Concept Diagram](./Agile-ROI-Calculator-diagram.png)

Determine the potential financial impact of improving team efficiency through better meeting structures and Agile ceremonies.

<div class="admonition note">
    <p class="admonition-title">Calculator</p>
    <div style="display: grid; gap: 1rem; max-width: 400px;">
        <label>
            Team Size (People):
            <input type="number" id="team-size" value="7" style="width: 100%; padding: 0.5rem;">
        </label>
        <label>
            Avg Hourly Rate ($):
            <input type="number" id="hourly-rate" value="60" style="width: 100%; padding: 0.5rem;">
        </label>
        <label>
            Weekly Meeting Hours (per person):
            <input type="number" id="meeting-hours" value="10" style="width: 100%; padding: 0.5rem;">
        </label>
        <label>
            Expected Efficiency Gain (%):
            <input type="number" id="efficiency-gain" value="20" style="width: 100%; padding: 0.5rem;">
        </label>
        <button id="calculate-btn" class="md-button md-button--primary" style="margin-top: 1rem;">Calculate ROI</button>
    </div>

    <div id="result-area" style="margin-top: 1.5rem; display: none; padding: 1rem; background: #f0fdf4; border-radius: 4px;">
        <h3 style="margin-top: 0;">Projected Savings</h3>
        <p>Current Annual Meeting Cost: <strong id="annual-cost"></strong></p>
        <p>Potential Annual Savings: <strong id="annual-savings" style="color: green;"></strong></p>
    </div>
</div>

## How it works
This tool calculates the direct labor cost savings by reducing unproductive meeting time. Agile ceremonies like the **Daily Stand-up** (15m) are designed to replace hour-long status meetings.
