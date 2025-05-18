# Formatted Greeting 
This challenge was a tough one for us.

```
class User(object):
    def __init__(self, title, name):
        self.title = title
        self.name = name

    def format_greeting(format_str, user):
        return format_str.format(user=user)
``` 

## Prerequisites
Basic understanding of object-oriented programming.

## The vulnerability
We noticed that the `format_str.format(user=user)` was not safe at all, because format_str is controlled by the user, so we can just input 
`{user.__class__.__init__.__globals__}` and the program will return valuable information.

### Why does it work?
We didn't have the source code, but from the program's output, we knew that we controlled the `title`, `name` and the `format_str`.

* `user.__class__.`: Gives us the class of the instance, which is a python way to say "Acess User", which we'll call `User`

* `User.__init__`: This is the `__init__` method of `User`, which is just a function that initializes the instance (called the initializer).

* `user.__class__.__init__.__globals__`: Finally, this accesses the `__globals__` dictionary, which contains all the global variables visible to the
function.

Since the flag was stored in a global variable, we were able to retrieve it.
