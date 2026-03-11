# Spark Coding Challenge: Employees and Departments

## Overview

You are provided with two CSV datasets containing information about employees and company departments.

Using **Apache Spark (PySpark)**, write a program that processes the datasets and produces the required result described below.

You may use any Spark DataFrame operations necessary to achieve the result.

---

# Dataset Files

## employees.csv

```csv
employee_id,name,department_id,salary
1,Alice,1,90000
2,Bob,2,75000
3,Charlie,1,85000
4,David,3,65000
5,Eva,2,80000
6,Frank,3,60000
7,Grace,1,95000
8,Helen,2,72000
```

---

## departments.csv

```csv
department_id,department_name
1,Engineering
2,Finance
3,HR
```

---

# Objective

Using the datasets provided, produce a result that shows the **average salary for each department**.

Your final result should include:

- The **department name**
- The **average salary for employees in that department**

---

# Output Requirements

Your program should display a Spark DataFrame containing:

- `department_name`
- `avg_salary`

The results should be ordered so that the **department with the highest average salary appears first**.

---

# Example Output

Your output should look similar to the following:

```
+---------------+-----------+
|department_name|avg_salary |
+---------------+-----------+
|Engineering    |90000.0    |
|Finance        |75666.67   |
|HR             |62500.0    |
+---------------+-----------+
```

---

# Requirements

Your solution must:

- Use **PySpark**
- Read the datasets from **CSV files**
- Produce the required result using **Spark DataFrame operations**
- Display the final DataFrame

---

# Submission

Submit a **PySpark script** that:

1. Creates a Spark session
2. Loads the datasets
3. Produces the required result
4. Displays the output

---

Good luck!

- ALSO COMPLETE THE hackerrank open at 9:30AM EST:
[SQL and Python](http://www.hackerrank.com/dataengineering1-1)