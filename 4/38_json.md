
# JSON 


## Why JSON?

- JSON is everywhere.  If you're using an API.  You'll almost certainly use json
- Much cleaner than XML.  Human readable versus protobuf
- Python can automatically infer types!


## Reading JSON

### From a String

```python
json_str = '{"ok": true, "value": 42}'
data = json.loads(json_str)
```

We'll do this with API responses.  Or if reading from a file, etc. There's plenty of reasons for this.


### From a File

```python
with open('data.json', 'r') as f:
    my_data = json.load(f)
```

- note we do NOT have an 's' in the json.load call.
- `s` is for string


## Writing JSON

### `json.dumps` dump to a string

```python
print(json.dumps(my_data, indent=2, sort_keys=True))
```

- This dumps to a string formatted as json.
- use `indent=2` to make the output look cleaner
- use `sort_keys=True` to order the keys.


### `json.dump` (without the s) dump to a file

```python
with open("my_data.json", "w") as f:
    json.dump(my_data, f, indent=2)
```


## Serialization

### What's serialization
When going from objects to dictionaries.  Some objects can't easily be converted to 1's and 0's.  There state is a bit up in the air so python can't concretely write it to a file.  Think of a person.  How would you write that to a file.  What's important? What's the state?

As a result, if we try to serialize (go from an object in a state to a file) something that can't be serialized, we'll get a TypeError.

Note: the fact that json calls this a TypeError and doesn't create its own suggests that you shouldn't make your own custom error classes.

```python
from datetime import datetime
json.dumps({"ts": datetime.utcnow()})
# TypeError: Object of type datetime is not JSON serializable
```

To remedy this, we can convert it to a string if we have a method like that.

```python
json.dumps({"ts": datetime.utcnow().isoformat()})
```

Just remember, whatever software is reading this json, should be aware of your formatting choice.

## ND-JSON (newline delimited)
JSON is normally one parent object in a file.  However sometimes we want to send multiple.  ND-JSON will allow us to pull multiple json objects from one file.

Note: if we do this, we must have ONE line per json object.  So no pretty print or indents.  Also, this is less a standard and more a guideline.  But it's a popular guideline.  Also, we could do one array as our top element, but then we have to load the whole thing into memory.

Given an input file like:

```json
{"name": "mike", "age": 40}
{"name": "matt", "age": 45}
{"name": "mark", "age": 35}

```

We can ingest multiple json objects using...

```python
import json

people = []

with open('people.ndjson') as f:
  for l in f:
    people.append(json.loads(l))

people  ## contains mike matt and mark

len(people) ## is three

type(people[1]['age']) ## is an int!
```


## Validation
Sometimes we want to know if a file is in the right format that we're reading or after writing.  Think back to the csv writer and all the exceptional cases of needing to clean up commas, newlines, etc in data.

json schema is a tool which will do this.  this is available in pip as `jsonschema`.
