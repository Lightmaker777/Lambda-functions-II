# Task 4

# Rewriting the decorator 'wrap_with' from the last exercise about decorators and use a lambda function to replace the inner() function.

def wrap_with(tag):
    return lambda func: lambda *args, **kwargs: f"<{tag}>{func(*args, **kwargs)}</{tag}>"

@wrap_with(tag="strong")
def get_full_name(first, last):
    return f"{first} {last}"

@wrap_with(tag="p")
@wrap_with(tag="em")
def get_custom_html_greeting(first, last):
    full_name = get_full_name(first, last)
    return f"Hello, {full_name}!"

# Test case
print(get_custom_html_greeting("James", "Brown"))




