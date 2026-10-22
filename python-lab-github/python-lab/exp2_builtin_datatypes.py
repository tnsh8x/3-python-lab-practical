"""Experiment 2: creation, indexing, slicing, concatenation and repetition
on Python built-in data types: String, List, Tuple, Dictionary and Set."""

# ---------- String ----------
s = "Python"
print("=== STRING ===")
print("Creation      :", s)
print("Indexing      : s[0] =", s[0], ", s[-1] =", s[-1])
print("Slicing       : s[1:4] =", s[1:4], ", s[::-1] =", s[::-1])
print("Concatenation :", s + " Lab")
print("Repetition    :", s * 2)

# ---------- List ----------
lst = [10, 20, 30, 40, 50]
print("\n=== LIST ===")
print("Creation      :", lst)
print("Indexing      : lst[2] =", lst[2], ", lst[-1] =", lst[-1])
print("Slicing       : lst[1:4] =", lst[1:4], ", lst[::2] =", lst[::2])
print("Concatenation :", lst + [60, 70])
print("Repetition    :", [1, 2] * 3)

# ---------- Tuple ----------
tup = ("a", "b", "c", "d")
print("\n=== TUPLE ===")
print("Creation      :", tup)
print("Indexing      : tup[1] =", tup[1], ", tup[-1] =", tup[-1])
print("Slicing       : tup[1:3] =", tup[1:3])
print("Concatenation :", tup + ("e", "f"))
print("Repetition    :", ("x", "y") * 2)

# ---------- Dictionary ----------
d = {"name": "Tanish", "branch": "CSE-AIML", "year": 2}
print("\n=== DICTIONARY ===")
print("Creation      :", d)
print("Indexing      : d['name'] =", d["name"], ", d.get('year') =", d.get("year"))
print("Keys / Values :", list(d.keys()), list(d.values()))
d2 = {**d, "city": "Pune"}  # dictionaries use merge instead of '+'
print("Concatenation (merge):", d2)
print("Slicing/Repetition    : not supported (dict is unordered by position)")

# ---------- Set ----------
st = {1, 2, 3, 4}
print("\n=== SET ===")
print("Creation      :", st)
print("Indexing/Slicing/Repetition: not supported (sets are unordered)")
print("Union (like concatenation):", st | {4, 5, 6})
print("Intersection  :", st & {3, 4, 5})
print("Difference    :", st - {1, 2})
