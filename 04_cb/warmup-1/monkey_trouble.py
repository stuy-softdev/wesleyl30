# Wesley Leon
# Ugly Duckies
# SoftDev
# K04 -- Reviewing python basics
# 2025-09-15m
# time spent: 1

def monkey_trouble(a_smile, b_smile):
    return a_smile == b_smile

test_cases = [
    (True, True, True),
    (False, False, True),
    (True, False, False),
    (False, True, False)
]

all_passed = True
for a_smile, b_smile, expected in test_cases:
    actual = monkey_trouble(a_smile, b_smile)
    print(f"Input: ({a_smile}, {b_smile}) | Expected: {expected} | Actual: {actual}")
    if actual != expected:
        all_passed = False

print("All test cases passed!" if all_passed else "Some test cases failed.")