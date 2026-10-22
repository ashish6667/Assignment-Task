# PROMPT_LOG.md
## AI Prompting & Charting Log

### 1. Initial Prompt to the AI
> "Can you write a Python script using matplotlib to load device_summary.json and create a bar chart showing the average temperature for each device? Please save the chart as an image."

---

### 2. Bugs & Formatting Mistakes in First Attempt
When running the AI's first code snippet, a few issues appeared:
- **Overlapping Labels & Clipping:** The device names on the x-axis were drawn flat horizontally without any rotation. Because the margin was small and `plt.tight_layout()` was missing, the device names got cramped together and slightly cut off at the bottom.
- **Missing Temperature Values:** There were no data labels on top of the bars, making it difficult to read the exact values without squinting at the y-axis.
- **No Threshold Indicator:** The prompt didn't specify the 80.0 °C filter threshold, so the chart didn't visually show why higher temperature devices were excluded.

---

### 3. Follow-Up Prompt to Fix the Issues
> "The chart looks okay, but please fix these issues:
> 1. Rotate the x-axis labels slightly (e.g., 30 degrees) and add `plt.tight_layout()` so the device names don't overlap or get clipped.
> 2. Add text above each bar showing the exact temperature (like '68.7 °C').
> 3. Add a dashed red line at 80.0 °C to show the maximum threshold limit.
> 4. Make sure it saves to 'device_temperature_chart.png'."

---

### 4. Final Result
The updated script (`visualize_summary.py`) ran cleanly and produced `device_temperature_chart.png` with clear labels, proper spacing, and exact temperature callouts.
