# Wesley Leon
# Ugly Duckies
# SoftDev
# K04 -- Reviewing python basics
# 2025-09-15m
# time spent: 1

def array_count9(nums):
    return nums.count(9)

test_cases = [
    ([1, 2, 9], 1),
    ([1, 9, 9], 2),
    ([1, 9, 9, 3, 9], 3),
    ([1, 2, 3], 0),
    ([], 0),
    ([4, 2, 4, 3, 1], 0),
    ([9, 2, 4, 3, 1], 1)
]

all_passed = True
for nums, expected in test_cases:
    actual = array_count9(nums)
    print(f"Input: {nums} | Expected: {expected} | Actual: {actual}")
    if actual != expected:
        all_passed = False

print("All test cases passed!" if all_passed else "Some test cases failed.")
