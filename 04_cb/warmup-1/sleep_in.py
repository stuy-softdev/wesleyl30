# Wesley Leon
# Ugly Duckies
# SoftDev
# K04 -- Reviewing python basics
# 2025-09-15m
# time spent: 1

def sleep_in(weekday, vacation):
    return not weekday or vacation

test_cases = [
    (False, False, True),
    (True, False, False),
    (False, True, True),
    (True, True, True)
]
all_passed = True
for weekday, vacation, expected in test_cases:
    actual = sleep_in(weekday, vacation)
    print(f"Input: ({weekday}, {vacation}) | Expected: {expected} | Actual: {actual}")
    if actual != expected:
        all_passed = False

print("All test cases passed!" if all_passed else "Some test cases failed.")