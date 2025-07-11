# Exercise - Reading and writing files
Given the text of moby dick available here:

[Moby Dick](../assets/moby_dick.txt)

find the frequency of each word. (the number of times it occurs) (regardless of case)

Note: you can remove punctuation with this:

```python
punctuation_list = """!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"""
translation_table = str.maketrans('', '', punctuation_list)

'Hello, world!'.translate(translation_table)
# returns Hello world
```


1. You will store this information in a dictionary.

2. get the number of times 'whale' occurs.

3. get the number of times 'Ahab' occurs

4. build a function so you can check the number of times something occurs.


```python
def get_word_count(input_string, string_to_search):
    ...

def get_word_count(moby_dick_text, 'the')
```

5. count the lines in moby_dick

CSV Files

CSV files are comma separated value files.

In these we have multiple rows (one for each data entry, and the columns are separated by ','.  

6. Build a CSV file consisting of 'word', 'frequency'.

7. Save it as moby_dick_word_count.csv
