# Wesley Leon
# Ugly Duckies
# SoftDev
# K04 -- Reviewing python basics
# 2025-09-15m
# time spent: 1

def makes10(a, b):
    return a + b == 10 or a == 10 or b == 10

test_cases = [
    (9, 10, True),
    (9, 9, False),
    (1, 9, True),
    (10, 1, True),
    (10, 10, True),
    (8, 2, True),
    (8, 3, False),
    (10, 42, True),
    (12, -2, True)
]
all_passed = True
for a, b, expected in test_cases:
    actual = makes10(a, b)
    print(f"Input: ({a}, {b}) | Expected: {expected} | Actual: {actual}")
    if actual != expected:
        all_passed = False

print("All test cases passed!" if all_passed else "Some test cases failed.")