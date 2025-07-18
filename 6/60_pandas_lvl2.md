# Kung-fu Pandas 

## Overview
Ok we're taking pandas up a notch.  Recall you have already learned to:
- 
- 
- 
- fill me in

No we're going to look at some deeper cuts to learn how to better manipulate our data.

## Data set
Consider the following dataset.

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 45, 35, 60],
    'Hobbies': ['reading,cycling', 'sports', 'cooking,drawing,travel', ''],
    'Income': [45000, 80000, 70000, 120000],
    'Gender': ['F', 'M', 'M', 'M']
}
df = pd.DataFrame(data)

## `cut` <- see what i did there?
Sometimes we want to split our continuous variables (recall that means numbers and such that have an ordering) into categories.  For example, we might want to split our sample data into CorvetteThoughts based on their ages.

```python
bins = [0, 10, 40, 50, 100]
labels = ['Thinks_Corvettes_Are_Lambos', 'has_enough_disposable_income_to_consider_leasing_a_corvette', 'On_Carmax_right_now_looking_for_a_convertible_yellow_corvette', 'Is_bummed_that_their_convertible_yellow_corvette_now_looks_dated_but_not_classic_enough_to_be_cool']
df['CorvetteThoughts'] = pd.cut(df['Age'], bins=bins, labels=labels)
```

## `explode`
Explode takes columns of sequences and splits them out into rows.  Think of it like a mini-join. For example, if there was a element with ['a', 'b', 'c'] in it, the row will be multiplied 3x with a column containing 'a', another row with a column containing 'b', and finally a last column containing 'c'.  Using our dataset, this will make a HobbyList column with one string in it for each of the hobbies a person had in Hobbies.

```python
df['HobbyList'] = df['Hobbies'].str.split(',')
df_exploded = df.explode('HobbyList')
```

boom.  We now have a dataframe called df exploded where each hobby is broken out into it's own row.  We've denormalized it in a sense.



## `astype`

ok if we want to be very efficient with space, it's best that we convert our hobbies to categories.  This way each cell will not be a string so much as it will be a reference to a string in a table of possible values.  Since hobbies are mostly finite, we'll make that a category.  

## `get_dummies` 
sometimes we want to do a one_hot encoding of categories for a classifier or clustering algorithm.

get_dummies allows us to take a categorical value and explode it out into a collection of bools

```python
hobby_dummies = pd.get_dummies(df_exploded['HobbyList'])
df_encoded = pd.concat([df_exploded, hobby_dummies], axis=1)
df_encoded.head()
```

## `map`
allows us to use a dict to remap some fields...

```python
gender_map = {'F': 'Female', 'M': 'Male'}
df['GenderFull'] = df['Gender'].map(gender_map)
```


## `apply`
let's us apply a function to a row...
```python
df['Tax'] = df['Income'].apply(lambda x: x * 0.25 if x > 50000 else x * 0.1)
```


We can also filter with apply.  For example if i want to see who has an AWS cert... (different dataset)

```python
df[df['CertList'].apply(lambda certs: 'AWS' in certs)]
```
