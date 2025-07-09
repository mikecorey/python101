Given the text of moby dick available here:

[Moby Dick](../assets/moby_dick.txt)

find the frequency of each word. (regardless of case)

Note: you can remove punctuation with this:

```python
punctuation_list = """!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"""
translation_table = str.maketrans('', '', punctuation_list)

'Hello, world!'.translate(translation_table)
# returns Hello world
```

Second note:

to read a file you will need to call:

```python
f = open('myfile.txt', 'r')
moby_dick_text = f.read()
f.close()
```

(technically `with` is perferred but for now just use f open and close)

```python
with open('myfile.txt', 'r') as f
    moby_dick_text = f.read()
    ...
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

bonus: make a function that can load the file
