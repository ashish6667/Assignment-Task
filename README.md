# Device Log Summarizer CLI Tool

Technical Assessment submission for Software Engineering Intern role.

## Project Files
- `sensor_cleaner.py`: Function to clean and normalize sensor readings (Section 1).
- `test_sensor_cleaner.py`: Unit tests for data sanitization (Section 1).
- `device_telemetry.csv`: Sample input telemetry dataset (Section 2).
- `log_summarizer.py`: CLI tool that reads CSV, aggregates metrics, filters > 80.0 °C, and exports JSON (Section 2).
- `device_summary.json`: Exported summary output file (Section 2).
- `visualize_summary.py`: Script to plot bar chart using matplotlib (Section 3).
- `device_temperature_chart.png`: Generated chart image (Section 3).
- `PROMPT_LOG.md`: Log of AI prompts, initial bugs, and follow-up prompt (Section 3).

---

## How to Run

### 1. Run Sanitization & Unit Tests (Section 1)
```bash
python sensor_cleaner.py
python -m unittest test_sensor_cleaner.py -v
```

### 2. Run Data Processing CLI (Section 2)
```bash
python log_summarizer.py
```
This reads `device_telemetry.csv`, filters out devices with average temperature above 80.0 °C, saves the results to `device_summary.json`, and displays the summary table in the terminal.

### 3. Generate the Chart (Section 3)
```bash
python visualize_summary.py
```
This reads `device_summary.json` and creates `device_temperature_chart.png`.
