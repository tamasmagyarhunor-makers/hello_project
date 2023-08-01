def hello(name):
    if not isinstance(name, str):
        raise Exception('You can only pass strings into hello() function')
    
    return f"Hello {name}, how are you today?"