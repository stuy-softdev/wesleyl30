# Wesley Leon
# Ugly Duckies
# SoftDev
# K04 -- Reviewing python basics
# 2025-09-15m
# time spent: 1

def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)

test_cases = [
    (True, 6, True),
    (True, 7, False),
    (False, 6, False),
    (True, 21, True),
    (False, 21, False),
    (False, 20, False),
    (True, 23, True),
    (False, 23, False),
    (True, 20, False),
    (False, 12, False)
]
all_passed = True
for talking, hour, expected in test_cases:
    actual = parrot_trouble(talking, hour)
    print(f"Input: ({talking}, {hour}) | Expected: {expected} | Actual: {actual}")
    if actual != expected:
        all_passed = False

print("All test cases passed!" if all_passed else "Some test cases failed.")