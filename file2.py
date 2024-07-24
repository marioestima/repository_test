def a_counter(string):
    counter = 0
    for char in string:
       if char == 'a':
          counter+=1
    return counter

name = input('what is your name: ')
a_count = a_counter(name)
print("letter 'a' in your name: " + str(a_count))
