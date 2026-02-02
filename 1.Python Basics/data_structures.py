numbers = [1,2,3,4]

fruties = ['apple', 'banana', 'cherry']

mixed = [1, 'apple', 3.14, True]

print(numbers[1])      # Output: 2
print(fruties[-1])     # Output: cherry 
print(mixed[2])        # Output: 3.14


fruties.append('orange')
print(fruties)         # Output: ['apple', 'banana', 'cherry', 'orange']
fruties.insert(1, 'kiwi')
print(fruties)         # Output: ['apple', 'kiwi', 'banana', 'cherry', 'orange']
fruties.remove('banana')
print(fruties)         # Output: ['apple', 'kiwi', 'cherry', 'orange']
popped_fruit = fruties.pop()
print(popped_fruit)    # Output: orange
print(fruties)         # Output: ['apple', 'kiwi', 'cherry']