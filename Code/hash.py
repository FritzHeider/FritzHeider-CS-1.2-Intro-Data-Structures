from hashtable import HashTable



roman = HashTable()
roman.set('I', 1)

print(roman.get('I') )        # => 1
roman.set('V', 5)
roman.set('X', 9)
roman.set('X', 10)     # Oops, let's fix that (can update a key's value)
roman.get('X')         # => 10
roman.keys()           # => ['I', 'V', 'X']
roman.values()         # => [1, 5, 10]

print(roman)
