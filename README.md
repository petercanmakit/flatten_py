# flatten_py

A function that accepts an arbitrarily-deep nested Array-like structure and returns a flattened structure with any null values removed. Note that it will return objects which are contained in the list and are not lists or None values themselfs. If it is a list, it will do flatten recursively.

In order to use this function, put it at the top of your code. Put both both *flatten_help()* and *flatten()*, but **only call** *flatten()* when using. 

e.g.

    print flatten([0, "2", [[2, "hello![][][]"], 8, {"A":1,"b":2}, None, [[None]]], -2])
    # should return [0, '2', 2, 'hello![][][]', 8, {'A': 1, 'b': 2}, -2]
