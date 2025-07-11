# Exercise - imports

## Non-deterministic web scraper

1. Import a package requests (you'll have to pip install this)

2. Import a package random (this is built in)

3. create a list of 10 websites (google.com, yahoo.com, etc.)

4. randomly choose 3 (using `random.`) website, use resp = requests.get('your_website')

5. print the first 200 chars of the response from each website.

```python
import random
import requests
websites = ['http://google.com', 'http://yahoo.com', 'http://apple.com', 'http://amazon.com', 'http://youtube.com', 'http://facebook.com', 'http://microsoft.com', 'http://eay.com']
for _ in range(3):
    print(requests.get(random.choice(websites)).text[:200])
```

## Exercise - Numpy
1. import numpy (you will need to pip install this)

2. create a list containing 100 random floats between zero and one

3. convert the list into a numpy array

4. compute the mean of the array

```python
>>> import numpy as np
>>> import random
>>> x = [random.random() for _ in range(100)]
>>> x_a = np.array(x)
>>> np.mean(x_a)
np.float64(0.5007492847180631)
>>> 
```

## Exercise json
Json looks very similar to python dicts.  Json is a bit more picky on syntax, but it should look somewhat familiar to you.

1. import the package json

2. save your moby dick word count as a json file

3. open the file in colab, find the word 'the' and change it's value to only occur 2 times.

4. save the file

5. load the file back into python

6. get word_count['the'] (hopefully it's two)


```python
import json
json.dump(word_count, open('word_count.json', 'w'), indent=4)

word_count = json.load(open('modded_word_count.json', 'r'))
word_count.get('the')
```