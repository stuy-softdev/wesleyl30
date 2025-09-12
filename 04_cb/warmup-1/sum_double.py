# Wesley Leon
# Ugly Duckies
# SoftDev
# K04 -- Reviewing python basics
# 2025-09-15m
# time spent: 1

def sum_double(a, b):
    return ((a + b) * (1 if a != b else 2))

sum_double(1, 2) #→ 3
sum_double(3, 2) #→ 5
sum_double(2, 2) #→ 8
sum_double(-1, 0) #→ -1
sum_double(3, 3) #→ 12
sum_double(0, 0) #→ 0
sum_double(0, 1) #→ 1
sum_double(3, 4) #→ 7
