# Wesley Leon
# Ugly Duckies
# SoftDev
# K04 -- Reviewing python basics
# 2025-09-15m
# time spent: 1

def near_hundred(n):
    return abs(100 - n) <= 10 or abs(200 - n) <= 10

test_cases = [
    (93, True),
    (90, True),
    (89, False),
    (110, True),
    (111, False),
    (121, False),
    (-101, False),
    (-209, False),
    (190, True),
    (209, True),
    (0, False),
    (5, False),
    (-50, False),
    (191, True),
    (189, False),
    (200, True),
    (210, True),
    (211, False),
    (290, False)
]
all_passed = True
for n, expected in test_cases:
    actual = near_hundred(n)
    print(f"Input: {n} | Expected: {expected} | Actual: {actual}")
    if actual != expected:
        all_passed = False

print("All test cases passed!" if all_passed else "Some test cases failed.")