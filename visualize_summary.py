"""
Section 3: AI Prompting & Charting Challenge
Loads device_summary.json and generates a bar chart comparing average temperatures per device.
"""

import json
import os
import matplotlib.pyplot as plt


def load_data(json_file="device_summary.json"):
    """
    Loads summarized device records from the JSON file.
    """
    if not os.path.exists(json_file):
        print(f"Error: {json_file} does not exist.")
        return []

    try:
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(f"Error loading JSON data: {e}")
        return []


def plot_average_temperatures(data, output_image="device_temperature_chart.png"):
    """
    Generates and saves a clean bar chart comparing average device temperatures.
    """
    if not data:
        print("No data available to plot.")
        return

    # Extract device IDs and their average temperatures
    device_ids = [item["device_id"] for item in data]
    avg_temps = [item["average_temperature"] for item in data]

    # Initialize figure
    plt.figure(figsize=(8, 5))

    # Create bar chart
    bars = plt.bar(device_ids, avg_temps, color="#3498db", edgecolor="#2980b9", width=0.5)

    # Add numeric value labels on top of each bar
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height + 1.2,
            f"{height:.1f} °C",
            ha="center",
            va="bottom",
            fontsize=10,
            fontweight="bold"
        )

    # Add 80°C threshold reference line
    plt.axhline(y=80.0, color="crimson", linestyle="--", linewidth=1.5, label="80.0 °C Threshold")

    # Titles and axis labels
    plt.title("Average Temperature per Device", fontsize=14, fontweight="bold", pad=12)
    plt.xlabel("Device ID", fontsize=11, labelpad=8)
    plt.ylabel("Average Temperature (°C)", fontsize=11, labelpad=8)

    # Adjust y-limit for spacing
    plt.ylim(0, 95)

    # Rotate device labels so they don't overlap
    plt.xticks(rotation=30)

    # Add legend and horizontal grid lines
    plt.legend(loc="upper right")
    plt.grid(axis="y", linestyle="--", alpha=0.5)

    # Fix layout margins
    plt.tight_layout()

    # Save output chart
    plt.savefig(output_image, dpi=200)
    plt.close()
    print(f"Chart successfully generated and saved to '{output_image}'.")


def main():
    data = load_data("device_summary.json")
    plot_average_temperatures(data, "device_temperature_chart.png")


if __name__ == "__main__":
    main()
