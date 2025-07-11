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

```python
PUNCTUATION_LIST = """!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"""

word_count = {} #1
line_count = 0

def get_words(line):
  translation_table = str.maketrans('', '', PUNCTUATION_LIST)
  line = line.translate(translation_table).lower()
  return [x for x in line.split() if x.isalpha()]


with open('moby_dick.txt', 'r') as f:
  for line in f:
    if len(line) > 2:
      ws = get_words(line)
      line_count += 1   #5
    for w in ws:
      word_count[w] = word_count.get(w, 0) + 1

#for k,v in sorted(word_count.items(), key=lambda x: x[1]):
#  print(f'{k:15}:{v}')

with open('moby_dick_word_count.csv', 'w') as f:    #6,7
  f.write('Word,Count\n')
  for k,v in word_count.items():
    f.write(f'{k},{v}\n')

def get_count(s):   #4
  return word_count[s]

def print_count(s):
  print(f'{s}: {get_count(s)}')

print_count('whale')    #2
print_count('ahab') #3
print_count('the')

print(f'this text has {line_count} lines')
```
