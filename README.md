# smile.py

EDIT: This was a joke, but it turns out the infix module already exists, and lets you define new infix operators in a nice way.

Use emoticons as custom infix operators!

Python doesn't have enough infix operators. And it doesn't let you override operators for built-in classes. Let's fix that with smiles!

Here's an example of creating a new infix operator ^_^ which chains iterators.

```
from smile import emoticon, _

@emoticon("^_^")
def chain(a, b):
    import itertools
    return itertools.chain(a, b)
    
[1, 2, 3] ^_^ xrange(10) ^_^ {"take": "that", "PEP": 8}
```

All emoticons must currently be of the form x_y, where x and y are one of -,^,+,*,/,&,%. Currently x must have at least as high a precedence as y (so you can't do ```^_-``` yet, only ```-_-```, ```^_^```, and ```-_^```), but this should be easy to patch. Support for that, and the emoticons ```>_>```, ```>_<```, and ```<_<```, coming soon EDIT: never, because the infix package exists.
