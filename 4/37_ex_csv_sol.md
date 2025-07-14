# Exercise - CSV

1. As we've seen, csv writer mostly just cleans up our code a bit.  In fact, we could probably just write our own csv writer functions...

Write a function that acts as a csv writer, given a file name, create a function that takes a tuple or list and writes it to the file

```python
def write_a_file(fn, input_list):
    with open(fn, 'w') as f:
        for l in input_list:
            stringed_input_list = map(str, input_list)
            s = ','.join(stringed_input_list) + '\n'
            f.write(s)

```

2. Write a function that takes a file name and reads it to a tuple or list.

```python
import csv

def read_a_file(fn):
    rows = None
    with open(fn, newline='') as f:
        rows = []
        reader = csv.reader(f)
        for row in reader:
            rows.append(row)
    return rows
```

3. Google Colab has a popular dataset in it, california housing prices.  Open the file and calculate the median number of bedrooms in a zipcode.  Note: you'll get a weird number like 500 or so,  that's because this isn't each house it's per zip code if I recall.  You may want to use a DictReader for this.

```python
# Note this is mean not median...

import csv

def avg(l):
  return sum(l) / len(l)

with open('sample_data/california_housing_train.csv') as f:
  reader = csv.DictReader(f)
  tot_bedrooms = [float(record['total_bedrooms']) / float(record['households']) for record in reader]
  print(avg(tot_bedrooms))
```