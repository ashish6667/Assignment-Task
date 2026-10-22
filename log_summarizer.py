"""
Section 2: Core Data Processing Task
Device Log Summarizer CLI tool:
Reads device telemetry data, aggregates stats per device, filters out
overheated devices (average temperature > 80.0), exports to JSON,
and prints a summary table in the terminal.
"""

import csv
import json
import os
import sys


def read_telemetry_csv(csv_path):
    """
    Reads the telemetry CSV file and returns a list of valid record dictionaries.
    Handles missing file or corrupted rows gracefully.
    """
    if not os.path.exists(csv_path):
        print(f"Error: File '{csv_path}' not found.")
        return []

    records = []
    skipped_rows = 0

    try:
        with open(csv_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                device_id = row.get("device_id", "").strip()
                status = row.get("status", "").strip().upper()
                temp_str = row.get("temperature", "").strip()

                # Validate non-empty fields
                if not device_id or not status or not temp_str:
                    skipped_rows += 1
                    continue

                # Safely parse temperature
                try:
                    temperature = float(temp_str)
                except ValueError:
                    skipped_rows += 1
                    continue

                records.append({
                    "device_id": device_id,
                    "status": status,
                    "temperature": temperature
                })

    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return []

    if skipped_rows > 0:
        print(f"Warning: Skipped {skipped_rows} invalid row(s).")

    return records


def aggregate_device_data(records):
    """
    Groups records by device_id and calculates:
    - Total number of records per device
    - Average (mean) temperature
    - Count of records where status is ERROR
    """
    # Group temperatures and errors by device
    device_groups = {}

    for row in records:
        dev_id = row["device_id"]

        if dev_id not in device_groups:
            device_groups[dev_id] = {
                "temperatures": [],
                "error_count": 0
            }

        device_groups[dev_id]["temperatures"].append(row["temperature"])
        if row["status"] == "ERROR":
            device_groups[dev_id]["error_count"] += 1

    # Compute summary for each device
    summary_list = []
    for dev_id, data in device_groups.items():
        temps = data["temperatures"]
        total_records = len(temps)
        avg_temp = round(sum(temps) / total_records, 2) if total_records > 0 else 0.0

        summary_list.append({
            "device_id": dev_id,
            "total_records": total_records,
            "average_temperature": avg_temp,
            "error_count": data["error_count"]
        })

    # Sort alphabetically by device_id for clean display
    summary_list.sort(key=lambda x: x["device_id"])
    return summary_list


def filter_by_temperature(summary_list, max_temp=80.0):
    """
    Filters out any devices that have an average temperature above 80.0.
    """
    filtered_list = []
    for item in summary_list:
        if item["average_temperature"] <= max_temp:
            filtered_list.append(item)
    return filtered_list


def save_to_json(data, output_file="device_summary.json"):
    """
    Saves aggregated device results to a JSON file.
    """
    try:
        with open(output_file, mode="w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print(f"Successfully saved results to '{output_file}'.")
    except Exception as e:
        print(f"Error saving to JSON file: {e}")


def print_summary_table(summary_list):
    """
    Prints a formatted summary table in the terminal.
    """
    print("\n" + "=" * 62)
    print("                DEVICE LOG SUMMARY REPORT")
    print("=" * 62)
    print(f"{'Device ID':<12} | {'Total Records':<15} | {'Avg Temp (C)':<14} | {'Error Count':<11}")
    print("-" * 62)

    if not summary_list:
        print("No devices found or all devices filtered out.")
    else:
        for item in summary_list:
            dev = item["device_id"]
            records = item["total_records"]
            avg_temp = item["average_temperature"]
            errors = item["error_count"]
            print(f"{dev:<12} | {records:<15} | {avg_temp:<14.2f} | {errors:<11}")

    print("=" * 62 + "\n")


def main():
    # Allow passing custom CSV path as command line argument or use default
    csv_file = sys.argv[1] if len(sys.argv) > 1 else "device_telemetry.csv"
    output_json = "device_summary.json"

    print(f"Reading telemetry data from: {csv_file}")
    records = read_telemetry_csv(csv_file)

    if not records:
        print("No valid records found. Exiting.")
        return

    # 1. Group and aggregate data
    all_devices_summary = aggregate_device_data(records)

    # 2. Filter out devices with average temperature above 80.0
    valid_devices = filter_by_temperature(all_devices_summary, max_temp=80.0)

    # 3. Export to JSON file
    save_to_json(valid_devices, output_json)

    # 4. Print formatted summary table to terminal
    print_summary_table(valid_devices)


if __name__ == "__main__":
    main()
