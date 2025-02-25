def greet(*args, **kwargs):
    print(args)
    print(kwargs)
greet('Alice', 'Bob', age=25)