# Wesley Leon
# Ugly Duckies
# SoftDev
# K04 -- Reviewing python basics
# 2025-09-15m
# time spent: 1

def diff21(n):
    return abs(n-21) if n < 21 else 2 * abs(n-21)

test_cases = [
    (19, 2),
    (10, 11),
    (21, 0),
    (22, 2),
    (25, 8),
    (30, 18),
    (0, 21),
    (1, 20),
    (2, 19),
    (-1, 22),
    (-2, 23),
    (50, 58)
]
all_passed = True
for n, expected in test_cases:
    actual = diff21(n)
    print(f"Input: {n} | Expected: {expected} | Actual: {actual}")
    if actual != expected:
        all_passed = False

print("All test cases passed!" if all_passed else "Some test cases failed.")