# NYC Yellow Taxi ETL Project 🚖

This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline using **PySpark**. It processes NYC Yellow Taxi trip data, performs data cleaning and transformation, and loads the result for further analysis or storage.

---

## 📁 Project Structure
nyc-taxi-etl/
├── data/ # Contains raw or sample input files
├── python_scripts/
│ ├── config.py # Contains configuration information
│ ├── extract.py # Extracts data from CSV or Parquet files
│ ├── transform.py # Cleans and transforms the dataset
│ └── load.py # Load transformed data to PostgreSql Database
├── sql_scripts/
│ └── create_table.sql # DDL scripts for the tables in Postgresql
├── diagrams/
│ └── erd_project1.png # ERD for table structure
├── run_etl.py # Orchestrates the full ETL pipeline
└── README.md # Project documentation
