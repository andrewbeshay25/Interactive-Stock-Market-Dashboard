# Interactive Stock Market Dashboard

This project is a simple Dash and Plotly application that visualizes stock price data from multiple companies. It lets you pick a specific month and a specific stock metric (Open, Close, High, or Low) to see both the average values per company (via a bar chart) and the distribution of those values (via a box plot).

---

## Table of Contents
1. [Features](#features)
2. [Data](#data)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Project Structure](#project-structure)

---

## Features

- **Month Filter**: Select a month from a dropdown to filter the dataset.
- **Stock Metric Filter**: Choose which price metric (Open, Close, High, Low) you want to analyze.
- **Update Button**: Click "Update Charts" to refresh both the bar chart (showing average prices) and the box plot (showing price distribution).
- **Interactive Visuals**: Hover over bars or box plots to see specific data points.

---

## Data

- **File**: `StockData.csv`
- **Columns**:
  - `Company` – Name of the company (e.g., Amazon, Apple, Google, etc.)
  - `Month` – Month of the data (e.g., January, February, etc.)
  - `Open` – Opening stock price
  - `Close` – Closing stock price
  - `High` – Highest stock price
  - `Low` – Lowest stock price

Feel free to replace this dataset with any CSV file of your own, as long as it has similar columns.

---

## Installation

1. Clone or download this repository:
   ```
   git clone https://github.com/yourusername/Interactive-Stock-Market-Dashboard.git
   ```
2. Change into the project directory:
   ```
   cd Interactive-Stock-Market-Dashboard
   ```
3. (Optional) Create and activate a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
5. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

Make sure your requirements.txt includes:
  - dash
  - dash_bootstrap_components
  - pandas
  - plotly

## Usage
1. Run the Dash app:
   ```
   python app.py
   ```
2. Open your web browser and go to:
   ```
   http://127.0.0.1:8050
   ```
3. Select a month and a stock metric (Open, Close, High, Low), then click Update Charts to see the bar chart and box plot update.

## Project Structure
  ```
Interactive-Stock-Market-Dashboard/
│
├── app.py                # Dash application code
├── StockData.csv         # Sample stock data file
├── requirements.txt      # Python dependencies (optional but recommended)
├── .gitignore            # files that git should ignore
└── README.md             # This README file
  ```
