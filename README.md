**Expense_Tracker_Python_Project**

**Project Description**

The Expense_Tracker_Python_Project is a rules-based expense tracking and financial analysis system built in Python. It organizes income and expenses, enforces budget limits, identifies overspending patterns, and produces clear, audit-ready financial insights. The project is designed for trucking operations, small businesses, or personal finance use cases.

This capstone intentionally combines finance and accounting concepts (budgeting, variance analysis, efficiency metrics) with data analytics and Python programming skills in a modular, explainable system.

**Project Objectives**

- Track and categorize income and expenses

- Enforce budget limits using configurable rules

- Identify overspending and cost drivers

- Generate efficiency scores and rankings

- Produce executive summaries and audit logs

- Maintain transparency and explainability

**Project Approach**

The project follows a phased, modular development approach. Core functionality is implemented first to ensure a working end-to-end pipeline, followed by scoring, reporting, auditability, testing, and documentation. Configuration files (CSV and YAML) are used to separate business rules from code, improving flexibility and maintainability.

**Project Structure**

 Expense_Tracker_Python_Project/
├── main.py
├── README.md
├── src/
│ ├── init.py
│ ├── ingest.py
│ ├── preprocess.py
│ ├── config_loader.py
│ ├── categorize.py
│ ├── rules_engine.py
│ ├── analysis.py
│ ├── scoring.py
│ └── reporting.py
├── data/
│ └── transactions.csv
├── config/
│ ├── budgets.csv
│ └── rules.yml
└── output/
├── reports/
└── audit_logs/  

**Master Task List**

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

**Project Timeline (Estimated 40–60 Hours)**

Phase 1: Planning & Setup (4–6 hours)
- Review approved proposal
- Define MVP scope
- Set up project folder structure
- Initialize Git repository

Phase 2: Data Handling (8–10 hours)
- Define transaction data schema
- Create sample transaction data
- Write data ingestion module
- Implement data validation and cleaning

Phase 3: Rules & Categorization (8–10 hours)
- Define expense categories
- Build rule catalog (budget, trend, anomaly rules)
- Implement auto-categorization logic
- Add manual override functionality

Phase 4: Financial Analysis (6–8 hours)
- Calculate totals and category spend
- Compute variances vs budget
- Implement cost-per-mile logic (optional)
- Rank cost drivers

Phase 5: Scoring System (4–6 hours)
- Design efficiency scoring formula
- Implement scoring logic
- Generate daily and monthly scores

Phase 6: Reporting (5–7 hours)
- Generate executive summary
- Create category ranking tables
- Build trend visualizations
- Implement what-if analysis

Phase 7: Audit & Logging (3–4 hours)
- Track which rules fired and why
- Store audit logs for review

Phase 8: Testing & Refinement (4–6 hours)
- Test with multiple datasets
- Debug edge cases
- Refactor for clarity

Phase 9: Documentation & Finalization (4–5 hours)
- Finalize README.md
- Add usage instructions
- Prepare project presentation/report


**Total Estimated Time: 40–60 hours**

**Learning Objectives**

- Apply data ingestion, validation, and preprocessing techniques

- Design and implement rule-based analytics systems

- Perform financial analysis and variance calculations

- Translate metrics into efficiency scores and KPIs

- Communicate insights through reports and summaries

- Practice auditability, testing, and documentation

**Technologies Used**

- Python

- pandas

- PyYAML

- matplotlib (optional for visualizations)

- CSV and YAML

- Git & GitHub

**How to Run the Project**

1. Clone the repository

2. Install dependencies:

    pip install pandas pyyaml matplotlib

3. Update configuration files in the config/ folder if needed

4. Run the application:

    python main.py
