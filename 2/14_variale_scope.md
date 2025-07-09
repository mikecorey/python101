# Variable Scope
In python variables are bound to the code block they're in.  If i define a variable within a block, i can't see it or acces it outside of that block.  Blocks are nested however, so i can see variables within the parent of a block

```python

nums = [1,2,3,4]

def main():
    print(nums)
    cars = []
    nums[2] = 0

main()
```