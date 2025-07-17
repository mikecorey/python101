## To convert the netflix csv to a one-hot encoding

```python
# Step 1: Convert the comma-separated string into a list
df["listed_in"] = df["listed_in"].fillna("").apply(lambda x: [genre.strip() for genre in x.split(",")])

# Step 2: Use explode + get_dummies + groupby to one-hot encode
one_hot = pd.get_dummies(df["listed_in"].explode()).groupby(level=0).sum()

# Step 3: Merge back to original DataFrame
df = pd.concat([df, one_hot], axis=1)
```