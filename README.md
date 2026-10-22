# Device Log Summarizer CLI Tool

Technical Assessment submission for Software Engineering Intern role.

## Submission Requirements Checklist

| Requirement | Provided File / Link | Description |
| :--- | :--- | :--- |
| **GitHub Repository Link** | [https://github.com/ashish6667/Assignment-Task](https://github.com/ashish6667/Assignment-Task) | Public repository containing all source code and assets |
| **ZIP File** | device_log_summarizer_submission.zip | Standalone archive of the entire assignment |
| **Source Code** | sensor_cleaner.py, log_summarizer.py, isualize_summary.py, 	est_sensor_cleaner.py | Clean, modular Python code with descriptive variable names |
| **Sample Output File** | device_summary.json & device_temperature_chart.png | Exported aggregated JSON data and saved bar chart visualization |
| **Prompt Log** | PROMPT_LOG.md | Documents initial AI prompt, first-attempt bugs, and follow-up prompt |

---

## Project Structure & Files

- sensor_cleaner.py: Function to clean and normalize mixed sensor readings (Section 1).
- 	est_sensor_cleaner.py: Unit tests for data sanitization edge cases (Section 1).
- device_telemetry.csv: Sample input telemetry dataset (Section 2).
- log_summarizer.py: CLI tool that reads CSV, aggregates metrics, filters devices with avg temp > 80.0 C, and exports JSON (Section 2).
- device_summary.json: Sample output JSON file produced by Section 2.
- isualize_summary.py: Matplotlib script to generate comparison bar chart (Section 3).
- device_temperature_chart.png: Generated bar chart image output (Section 3).
- PROMPT_LOG.md: Documentation of AI prompts, formatting mistakes, and follow-up fixes (Section 3).
- device_log_summarizer_submission.zip: Complete submission package.

---

## How to Run

### 1. Run Sanitization & Unit Tests (Section 1)
`ash
python sensor_cleaner.py
python -m unittest test_sensor_cleaner.py -v
`

### 2. Run Data Processing CLI (Section 2)
`ash
python log_summarizer.py
`
This reads device_telemetry.csv, aggregates total records, average temperature, and error count per device, filters out any devices with average temperature above 80.0 C, saves the output to device_summary.json, and displays an aligned summary table in the terminal.

### 3. Generate the Chart (Section 3)
`ash
python visualize_summary.py
`
This reads device_summary.json and generates device_temperature_chart.png with 80.0 C threshold marking and exact temperature labels.
