## Dictionaries 
Similar to JS objects.
Holds key value pairs
```
human = {
    "name": "Zach",
    "age": 20,
}
```
Can access keys with get method or human["name"].
Also with the get method you can set a default value if key isn't in the dictionary. 

## Tuples

Tuples are immutable lists represented by ()

```
numbers = (1,2,3)
```

## Keyword Args 
Positioning for arguments no longer matters
```
def fakeFunction(foo, bar):
    ...
fakeFunction(bar = "test", foo ="NoOrder")
```
Helps with readability
Don't put keyword arguments in front of positional arguments.
