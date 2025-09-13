# Wesley Leon
# Ugly Duckies
# SoftDev
# K04 -- Reviewing python basics
# 2025-09-15m
# time spent: 1

def sum_double(a, b):
    return (a + b) * (1 if a != b else 2)

test_cases = [
    (1, 2, 3),
    (3, 2, 5),
    (2, 2, 8),
    (-1, 0, -1),
    (3, 3, 12),
    (0, 0, 0),
    (0, 1, 1),
    (3, 4, 7)
]
all_passed = True
for a, b, expected in test_cases:
    actual = sum_double(a, b)
    print(f"Input: ({a}, {b}) | Expected: {expected} | Actual: {actual}")
    if actual != expected:
        all_passed = False

print("All test cases passed!" if all_passed else "Some test cases failed.")