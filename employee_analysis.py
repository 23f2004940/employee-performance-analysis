# Employee Performance Analysis
# Author: 23f2004940@ds.study.iitm.ac.in

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------
# 1. Generate sample dataset
# --------------------------
np.random.seed(42)
departments = ["Finance", "HR", "IT", "Operations", "Marketing", "Sales"]
regions = ["North", "South", "East", "West"]

data = {
    "EmployeeID": range(1, 101),
    "Department": np.random.choice(departments, 100, p=[0.2,0.15,0.25,0.15,0.15,0.1]),
    "Region": np.random.choice(regions, 100),
    "PerformanceScore": np.random.randint(60, 100, 100),
}

df = pd.DataFrame(data)

# --------------------------
# 2. Frequency count for Finance
# --------------------------
finance_count = (df["Department"] == "Finance").sum()
print("Number of employees in Finance department:", finance_count)

# --------------------------
# 3. Visualization
# --------------------------
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x="Department", palette="viridis")
plt.title("Employee Distribution by Department")
plt.xticks(rotation=45)
plt.tight_layout()

# --------------------------
# 4. Save visualization to HTML
# --------------------------
# Save the matplotlib figure as PNG first
plt.savefig("department_hist.png")

# Create a very simple HTML file embedding the result
with open("employee_analysis.html", "w") as f:
    f.write("<html><head><title>Employee Analysis</title></head><body>")
    f.write("<h1>Employee Performance Analysis</h1>")
    f.write(f"<p><b>Email:</b> 23f2004940@ds.study.iitm.ac.in</p>")
    f.write(f"<p>Number of employees in Finance department: {finance_count}</p>")
    f.write('<img src="department_hist.png" width="600">')
    f.write("</body></html>")
