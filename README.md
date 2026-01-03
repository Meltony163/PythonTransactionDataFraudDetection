# Python Transaction Data Fraud Detection (GUI Application)

## 📌 Project Overview

This project is a **GUI-based Python application** designed to clean, analyze, and detect suspicious patterns in **transaction data**.  
It provides a complete workflow starting from **data loading**, through **data cleaning**, **feature engineering**, **risk scoring**, and **transaction flagging**, ending with **exportable analytical reports**.

The application is built using **Object-Oriented Programming (OOP)** principles and includes a graphical interface implemented using **pygame**.

---

## 🖥️ Application Type

- **Type:** Desktop GUI Application  
- **GUI Library:** pygame  
- **Programming Paradigm:** Object-Oriented Programming (OOP)

---

## 🔄 Application Workflow

### 1️⃣ Load Transaction Data
- Load transaction data into the application as a pandas DataFrame.
- This dataset becomes the base for all processing steps.

---

### 2️⃣ Data Cleaning

The application provides **three main data-cleaning options**:

#### 🔹 A. Convert Column to Datetime
- Select a categorical column to convert into a **datetime/timestamp** column.
- The application informs the user of:
  - Number of null values **before conversion**
  - Number of null values **after conversion**

This ensures transparency and avoids unintended data loss.

---

#### 🔹 B. Handle Missing Values (Nulls)
- The application detects and lists **columns containing null values**.
- For each column, the user can choose how to handle missing data.

**Categorical Columns:**
- Delete rows containing null values
- Delete the entire column
- Replace nulls with **mode**

**Numerical Columns:**
- Delete rows containing null values
- Delete the entire column
- Replace nulls with:
  - Mean
  - Median
  - Mode

---

#### 🔹 C. Remove Duplicates
- Detects and removes duplicate rows from the dataset.

---

### 3️⃣ Feature Engineering

After cleaning, the user can create new features such as:

- Number of transactions per customer
- Maximum transaction amount per customer
- Average transaction amount per customer
- Total transaction amount per customer
- Number of transactions per day

These features help analyze customer behavior more effectively.

---

### 4️⃣ Risk Scoring

Risk scoring is available **only for numerical columns** and includes two methods:

#### 🔹 A. Z-Score
- Calculates the Z-score for a selected numerical column.

#### 🔹 B. Risk Band Classification
- Classifies numerical values into risk bands:
  - Low
  - Medium
  - High
  - **Critical**

---

### 5️⃣ Suspicious Transaction Flagging

Flagging is available **only for columns that have Z-score or risk band classification**.

- **Z-Score Based Flagging:**  
  Transactions with `|Z-score| > 3` are flagged as suspicious.

- **Risk Band Based Flagging:**  
  Transactions classified as **Critical** are flagged.

---

### 6️⃣ Report Exporting

The application supports exporting multiple reports:

- Full cleaned dataset with:
  - Engineered features
  - Risk scores
  - Flag columns
- Flagged transactions only
- Number of flagged transactions
- Numerical summary statistics for numerical columns

---

## 🧪 Application Testing

The application was tested using the dataset located in the `data` folder with the following steps:

1. Loaded the dataset
2. Used **TransactionDate** as the datetime column
3. Removed duplicate records
4. Verified that there were no columns with null values
5. Built features:
   - Number of transactions per customer
   - Maximum transaction per customer
   - Average transaction per customer
   - Total transaction amount per customer
   - Number of transactions per day
6. Applied risk scoring to the newly created features
7. Flagged transactions using **Z-score**
8. Exported:
   - New enriched dataset
   - Numerical summary report
   - Flagged transactions
   - Number of flagged transactions

---

## 🧠 Object-Oriented Design

The project follows a modular **OOP architecture**.

### 🔹 Parent Class
- Stores the main DataFrame
- Holds shared attributes and common utility methods

### 🔹 Child Classes
Each class inherits from the parent class:

- `DataManager` – Data loading and management
- `TransactionCleaner` – Data cleaning operations
- `FeatureBuilder` – Feature engineering
- `RiskScorer` – Risk scoring (Z-score & risk bands)
- `TransactionFlagger` – Suspicious transaction detection
- `ReportGenerator` – Exporting reports

### 🔹 App Class
- Inherits from all processing classes
- Acts as the main controller that manages all functionality using a single object

### 🔹 ConsoleApp
- Provides the GUI interface using **pygame**
- Connects user actions to backend logic

---

## 🚀 Future Features

- Z-score calculation based on **multiple columns simultaneously**

---

## 📦 Technologies Used

- Python
- Pandas
- NumPy
- Pygame
- Object-Oriented Programming (OOP)
