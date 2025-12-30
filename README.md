# Expense_Tracker_Python_Project

## Project Description

The **Expense_Tracker_Python_Project** is a rules-based expense tracking and financial analysis system built in Python. It organizes income and expenses, enforces budget limits, identifies overspending patterns, and produces clear, audit-ready financial insights. The project is designed for trucking operations, small businesses, or personal finance use cases.

This capstone project intentionally combines finance and accounting concepts (budgeting, variance analysis, efficiency metrics) with data analytics and Python programming skills in a modular, explainable system.

## Project Objectives

- Track and categorize income and expenses  
- Enforce budget limits using configurable rules  
- Identify overspending and cost drivers  
- Generate efficiency scores and rankings  
- Produce executive summaries and audit logs  
- Maintain transparency and explainability  


## How to Run the Project

### 1. Clone the Repository
    ```bash
    git clone https://github.com/fbeyene/Expense_Tracker_Python_Project.git
    ```
### 2. Navigate to the Project Directory
    ```bash
    cd Expense_Tracker_Python_Project
    ```
### 3. Install Dependencies:
    ```bash
    pip install pandas pyyaml matplotlib
    ```
### 4. Update Configuration Files
- Modify files in the `config/` folder to adjust budgets or rules as needed.
### 5. Run the Application:
    ```bash
    python main.py
    ```

## Usage
After installing dependencies and running the application, the program executes a complete expense analysis workflow using the configured input files.

### Running the Program

    ```bash
    python main.py
    ```

Once executed, the program automatically performs the following steps:

### 1. Input Data

The application reads data from the following files:
- `data/transactions.csv'`
    - Contains expense transactions
    - Expected columns include:
        - `date`
        - `description`
        - `amount`
- `config/budgets.csv`
    - Defines budget limits per category
    - Used to calculate variances and trigger alerts
- `config/rules.yml`
    - Defines business rules such as:
        - Overspending thresholds
        - Category assignment logic 
        - Anomaly detection rules

Users can modify these files to test different scenarios without changing the code.

### 2. Processing Flow

When the program runs, it executes the following pipeline:

**1. Data Ingestion**
- Loads transaction data from CSV files
- Validates required fields and formats

**2. Preprocessing**
- Loads transaction data from CSV files
- Validates required fields and formats

**3. Categorization**
- Automatically assigns expense categories using rule-based logic
- Applies manual overrides if provided

**4. Rules Engine**
- Evaluates spending against budgets
- Identifies overspending and anomalies
- Logs which rules were triggered and why

**5. Financial Analysis**
- Calculates totals and category-level spend
- Computes budget variances
- Ranks cost drivers

**6. Scoring**
- Generates efficiency scores based on spending behavior
- Produces daily and/or monthly performance metrics

### 3. Outputs

After execution, results are written to the output/ directory:

- `output/reports/`

    - Executive summaries
    - Category spending breakdowns
    - Rankings and trend summaries

- `output/audit_logs/`
    - Rule execution logs
    - Budget alerts (e.g., budget_alerts.csv)
    - Audit-ready explanations of detected issues

These outputs are designed to be easy to review, share, or audit.

### 4. Interpreting Results

- **Budget Alerts**
    - Highlight categories that exceeded defined limits
    - Include variance amounts and triggering rules

- **Efficiency Scores**
    - Higher scores indicate better budget discipline
    - Useful for comparing periods or scenarios

- **Reports**
  - Summarize financial performance in a clear, explainable format
  - Intended for decision-makers, not just technical users

### 5. Example Workflow

1. Update transactions.csv with new expense data
2. Adjust budget thresholds in budgets.csv
3. Modify rules in rules.yml (optional)
4. Run the program
5. Review generated reports and audit logs

## Project Approach

The project follows a phased, modular development approach. Core functionality is implemented first to ensure a working end-to-end pipeline, followed by scoring, reporting, auditability, testing, and documentation. 

Configuration files (CSV and YAML) are used to separate business rules from code, improving flexibility and maintainability.

## Project Structure

```text
Expense_Tracker_Python_Project/
├── main.py
├── README.md
├── src/
│   ├── __init__.py
│   ├── ingest.py
│   ├── preprocess.py
│   ├── config_loader.py
│   ├── categorize.py
│   ├── rules_engine.py
│   ├── analysis.py
│   ├── scoring.py
│   ├── reporting.py
│   ├── budget.py
│   └── audit_logger.py
├── data/
│   └── transactions.csv
├── config/
│   ├── budgets.csv
│   └── rules.yml
└── output/
    ├── reports/
    └── audit_logs/
        └── budget_alerts.csv
```

## Technologies Used

- Python

- pandas

- PyYAML

- matplotlib (optional for visualizations)

- CSV and YAML

- Git & GitHub


## Master Task List

**Phase 1: Planning & Setup**

- Review approved proposal

- Define MVP scope

- Set up project structure

- Initialize Git repository

**Phase 2: Data Handling**

- Define transaction schema

- Create sample CSV data

- Ingest data

- Validate and clean records

**Phase 3: Rules & Categorization**

- Define expense categories

- Build rule catalog

- Implement auto-categorization

- Add manual overrides

**Phase 4: Financial Analysis**

- Calculate totals and category spend

- Compute budget variances

- Rank cost drivers

- Optional cost-per-mile logic

**Phase 5: Scoring System**

- Design efficiency scoring

- Implement scoring logic

- Generate daily/monthly scores

**Phase 6: Reporting**

- Generate executive summaries

- Create ranking tables

- Build trend visualizations

- Implement what-if analysis

**Phase 7: Audit & Logging**

- Track fired rules

- Store audit logs

**Phase 8: Testing & Refinement**

- Test multiple datasets

- Debug edge cases

- Refactor code

**Phase 9: Documentation & Finalization**

- Finalize README

- Add usage instructions

- Prepare final report or presentation

## Project Timeline (Estimated 40–60 Hours)

**Phase 1: Planning & Setup (4–6 hours)**
- Review approved proposal
- Define MVP scope
- Set up project folder structure
- Initialize Git repository

**Phase 2: Data Handling (8–10 hours)**
- Define transaction data schema
- Create sample transaction data
- Write data ingestion module
- Implement data validation and cleaning

**Phase 3: Rules & Categorization (8–10 hours)**
- Define expense categories
- Build rule catalog (budget, trend, anomaly rules)
- Implement auto-categorization logic
- Add manual override functionality

**Phase 4: Financial Analysis (6–8 hours)**
- Calculate totals and category spend
- Compute variances vs budget
- Implement cost-per-mile logic (optional)
- Rank cost drivers

**Phase 5: Scoring System (4–6 hours)**
- Design efficiency scoring formula
- Implement scoring logic
- Generate daily and monthly scores

**Phase 6: Reporting (5–7 hours)**
- Generate executive summary
- Create category ranking tables
- Build trend visualizations
- Implement what-if analysis

**Phase 7: Audit & Logging (3–4 hours)**
- Track which rules fired and why
- Store audit logs for review

**Phase 8: Testing & Refinement (4–6 hours)**
- Test with multiple datasets
- Debug edge cases
- Refactor for clarity

**Phase 9: Documentation & Finalization (4–5 hours)**
- Finalize README.md
- Add usage instructions
- Prepare project presentation/report


**Total Estimated Time: 40–60 hours**

## Learning Objectives

- Apply data ingestion, validation, and preprocessing techniques

- Design and implement rule-based analytics systems

- Perform financial analysis and variance calculations

- Translate metrics into efficiency scores and KPIs

- Communicate insights through reports and summaries

- Practice auditability, testing, and documentation


## 📌 Author
**Fikadu Beyene**  
Data & Financial Systems Professional 