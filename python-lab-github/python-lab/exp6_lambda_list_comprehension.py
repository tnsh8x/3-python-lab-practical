"""Experiment 6: lambda functions and list comprehension."""

# ---------- Lambda functions ----------
square = lambda x: x ** 2
add = lambda a, b: a + b
is_even = lambda n: n % 2 == 0
print("=== LAMBDA ===")
print("square(5)        :", square(5))
print("add(3, 4)        :", add(3, 4))
print("is_even(10)      :", is_even(10))

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("map (cube)       :", list(map(lambda x: x ** 3, nums)))
print("filter (even)    :", list(filter(lambda x: x % 2 == 0, nums)))

words = ["banana", "kiwi", "apple", "fig"]
print("sorted by length :", sorted(words, key=lambda w: len(w)))

# ---------- List comprehension ----------
print("\n=== LIST COMPREHENSION ===")
print("squares          :", [x ** 2 for x in range(1, 11)])
print("even numbers     :", [x for x in range(1, 21) if x % 2 == 0])
print("upper-case words :", [w.upper() for w in words])
print("odd/even labels  :", ["even" if x % 2 == 0 else "odd" for x in range(1, 6)])
print("pairs (nested)   :", [(a, b) for a in range(1, 4) for b in range(1, 3)])
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("flatten matrix   :", [item for row in matrix for item in row])
