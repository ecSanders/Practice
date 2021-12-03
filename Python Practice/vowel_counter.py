def vowel_counter(my_string):
    my_string = my_string.lower()
    vowels = ['a','e','i','o','u']
    counter = 0
    for i in my_string:
        if i in vowels:
            counter += 1
    return counter

vowel_counter('This is my string')
