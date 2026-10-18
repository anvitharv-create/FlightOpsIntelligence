# FlightOps Intelligence ✈️

### Airline Operations Performance & Delay Investigation Platform

FlightOps Intelligence is a data analytics project designed to analyze airline operational performance, flight delays, cancellations, diversions, and recorded delay causes using Python, SQL Server, and Power BI.

The project transforms raw flight operations data into an interactive dashboard to identify delay patterns, compare airline performance, and investigate operational inefficiencies.

## Project Objectives

- Analyze airline flight operations and performance.
- Measure departure and arrival delays.
- Track cancellations and diversions.
- Investigate recorded flight delay causes.
- Identify routes with high average departure delays.
- Compare operational performance across airlines.
- Present key performance indicators through interactive Power BI reports.

## Technology Stack

- **Python** — Data cleaning and preprocessing
- **Pandas** — Data manipulation
- **SQL Server Express** — Relational data storage and SQL analysis
- **SQL Server Management Studio (SSMS)** — Database management
- **Microsoft Power BI** — Interactive dashboards and visualization
- **Git and GitHub** — Version control and project hosting

## Dashboard Preview

The following screenshots should be stored in `documentation/images/images/`. Ensure that each file exists at the specified path and that the filename matches exactly.

### 1. Operations Overview

Provides a high-level view of flight operations, including total flights, delayed flights, average arrival and departure delays, cancellation rate, on-time performance, and diversions.

![FlightOps Intelligence - Operations Overview](documentation/images/images/operations-overview.png)

### 2. Daily Delay Trends

Shows daily departure-delay patterns throughout January 2025.

![FlightOps Intelligence - Daily Delay Trends](documentation/images/images/daily-delay-trends.png)

### 3. Cancellation Analysis

Visualizes daily flight cancellations to help identify changes in cancellation activity during the month.

![FlightOps Intelligence - Cancellation Analysis](documentation/images/images/cancellation-analysis.png)

### 4. Arrival vs. Departure Delays

Compares average departure and arrival delays across flight dates.

![FlightOps Intelligence - Arrival vs Departure Delays](documentation/images/images/arrival-vs-departure-delays.png)

### 5. Delay Cause Analysis

Examines recorded delay minutes across categories such as late-arriving aircraft, carrier, air traffic control (NAS), weather, and security.

![FlightOps Intelligence - Delay Cause Analysis](documentation/images/images/delay-cause-analysis.png)

### 6. Top 10 Delayed Routes

Ranks routes by average departure delay to highlight routes that may require further investigation.

![FlightOps Intelligence - Top 10 Delayed Routes](documentation/images/images/top-10-delayed-routes.png)

### 7. Airline Performance

Compares average departure delay across airline carriers for January 2025.

![FlightOps Intelligence - Airline Performance](documentation/images/images/airline-performance.png)

## Dataset

The project uses US airline on-time performance data for January 2025.

The dataset includes:

- Flight date and carrier
- Flight number
- Origin and destination airports
- Departure and arrival delays
- Cancellation and diversion indicators
- Recorded delay-cause information

**Official source:** [US Bureau of Transportation Statistics — TranStats](https://www.transtats.bts.gov/)

The raw and processed CSV files are excluded from Git tracking because of their size. Download the appropriate January 2025 flight operations data from the official source and place the required raw CSV in `data/raw/`.

The cleaning script expects the raw file to be named:

`flight_operations_january_2025.csv`

Confirm that the downloaded file contains the columns expected by the cleaning script before running it.

## Project Workflow

```text
Raw Flight CSV
      |
      v
Python and Pandas Data Cleaning
      |
      v
Processed Dataset
      |
      v
SQL Server Analysis
      |
      v
Power BI Dashboard
```

## Data Cleaning

The script `src/data_cleaning.py` is intended to prepare the raw flight data. Its documented steps are:

- Read the raw flight operations CSV.
- Convert flight dates into date values.
- Check for and remove duplicate rows.
- Create cancellation and diversion indicators.
- Create departure-delay and arrival-delay indicators.
- Calculate total recorded delay-cause minutes.
- Save the processed dataset in `data/processed/`.

These descriptions should match the actual implementation in `src/data_cleaning.py`.

## Project Structure

```text
FlightOpsIntelligence/
├── data/
│   ├── raw/
│   └── processed/
├── documentation/
│   └── images/
│       └── images/
│           ├── operations-overview.png
│           ├── daily-delay-trends.png
│           ├── cancellation-analysis.png
│           ├── arrival-vs-departure-delays.png
│           ├── delay-cause-analysis.png
│           ├── top-10-delayed-routes.png
│           └── airline-performance.png
├── powerbi/
│   └── FlightOps_Intelligence.pbix
├── sql/
├── src/
│   └── data_cleaning.py
├── .gitignore
├── README.md
└── requirements.txt
```

Only files that actually exist should be committed. Git does not track empty directories, so the `sql/`, `data/raw/`, and `data/processed/` folders may not appear in the repository until they contain tracked files.

## Getting Started

### Prerequisites

- Python 3.12 or another version compatible with the project's dependencies
- SQL Server Express
- SQL Server Management Studio (SSMS)
- Microsoft Power BI Desktop
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/anvitharv-create/FlightOpsIntelligence.git
cd FlightOpsIntelligence
```

### 2. Create and Activate a Python Virtual Environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt:

```bat
.venv\Scripts\activate.bat
```

### 3. Install Dependencies

Install the required Python libraries from the dependency file:

```powershell
python -m pip install -r requirements.txt
```

Make sure `requirements.txt` contains Pandas and every other package imported by `src/data_cleaning.py`.

### 4. Prepare the Dataset

Download the appropriate January 2025 flight operations data from [TranStats](https://www.transtats.bts.gov/).

Place the raw CSV at:

```text
data/raw/flight_operations_january_2025.csv
```

The file must contain the column names and data format expected by the cleaning script.

### 5. Run Data Cleaning

```powershell
python .\src\data_cleaning.py
```

The processed dataset should be saved in `data/processed/`. Confirm that the script completes successfully and that the output file is created.

### 6. Load the Data into SQL Server

1. Open SSMS and connect to your SQL Server Express instance.
2. Create or select the database for this project.
3. Import the processed CSV into a SQL Server table.
4. Confirm the table name, column names, data types, row count, and missing values.
5. Add and run SQL scripts from the `sql/` directory as they are developed.

SQL analysis is not documented as complete until the relevant SQL scripts have been added and tested against the imported table.

### 7. Open the Power BI Dashboard

1. Open `powerbi/FlightOps_Intelligence.pbix` in Power BI Desktop.
2. Update the data source path or connection settings for your local environment.
3. Refresh the report.
4. Check that visuals and measures load without errors.

The Power BI file must be included in the repository for this step to work as written. If it is not committed to GitHub, arrange access to the file separately and update these instructions.

## Key Considerations

- Missing delay values should not automatically be treated as zero.
- Missing delay-cause values require careful interpretation.
- Cancellation and diversion records should be handled consistently when calculating operational KPIs.
- Average delays can be influenced by flights with unusually large delays.
- Route rankings should be interpreted alongside flight counts.
- An arrival on-time metric should use a clearly stated threshold and denominator. A zero-departure-delay rate is not the same as arrival on-time performance.
- January 2025 represents one month of operations and should not be treated as a complete picture of annual airline performance.

## Future Improvements

- Add SQL scripts for repeatable database setup and analysis.
- Implement automated data-quality checks.
- Expand the analysis to multiple months and years.
- Include route-level flight counts to provide context for average delays.
- Automate data refresh and reporting.
- Add validated findings and operational recommendations after the analysis is complete.

## Project Status

The Power BI dashboard and initial Python data-cleaning workflow have been developed. SQL scripts, SQL-based analysis, KPI validation, and additional documentation should be marked complete only after they have been implemented and tested.

## Author

**Anvitha R V**

- GitHub: [anvitharv-create](https://github.com/anvitharv-create)
- LinkedIn: [anvitharv](https://www.linkedin.com/in/anvitharv)

---

*FlightOps Intelligence demonstrates an end-to-end analytics workflow: data preparation with Python, operational analysis with SQL Server, and interactive dashboard reporting with Power BI.*
