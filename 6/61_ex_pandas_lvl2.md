# Exercise

1. Given a dataframe...

```python
import pandas as pd

data = {
    'Employee': ['Eve', 'Frank', 'Grace', 'Heidi'],
    'Department': ['ENG', 'HR', 'ENG', 'FIN'],
    'YearsExperience': [2, 8, 5, 12],
    'Certifications': ['AWS,Python', 'HRM,SAP', 'Python,Azure,Docker', 'CPA,Excel'],
    'Salary': [70000, 85000, 95000, 120000]
}

df = pd.DataFrame(data)
```

Label the departments instead of their abbreviations using `map`

2. use `cut` or `apply` to classify seniority (jr, mid, senior)

3. flatten certifications using `explode`

4. make a one hot encoding of certs

5. Mini-Project:  Pull the EV dataset from /assets.  Using Pandas, collect some statistics.

- Avg 0-60
- efficiency to acceleration
- efficiency by battery type
- battery capacity / range
