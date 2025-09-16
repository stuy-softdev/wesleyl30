# Wesley Leon
# Ugly Duckies
# SoftDev
# K04 -- Reviewing python basics
# 2025-09-15m
# time spent: 1

def pos_neg(a, b, negative):
    return (a * b < 0 and not negative) or (a * b > 0 and negative and a < 0)

test_cases = [
    (1, -1, False, True),
    (-1, 1, False, True),
    (-4, -5, True, True),
    (-4, -5, False, False),
    (-4, 5, False, True),
    (-4, 5, True, False),
    (1, 1, False, False),
    (-1, -1, False, False),
    (1, -1, True, False),
    (-1, 1, True, False),
    (1, 1, True, False),
    (-1, -1, True, True),
    (5, -5, False, True),
    (-6, 6, False, True),
    (-5, -6, False, False),
    (-2, -1, False, False),
    (1, 2, False, False),
    (-5, 6, True, False),
    (-5, -5, True, True)
]
all_passed = True
for a, b, negative, expected in test_cases:
    actual = pos_neg(a, b, negative)
    print(f"Input: ({a}, {b}, {negative}) | Expected: {expected} | Actual: {actual}")
    if actual != expected:
        all_passed = False

print("All test cases passed!" if all_passed else "Some test cases failed.")