# Wesley Leon
# Ugly Duckies
# SoftDev
# K04 -- Reviewing python basics
# 2025-09-15m
# time spent: 1

def near_hundred(n):
    return abs(100 - n) <= 10 or abs(200 - n) <= 10

near_hundred(93) #→ True
near_hundred(90) #→ True
near_hundred(89) #→ False
near_hundred(110) #→ True
near_hundred(111) #→ False
near_hundred(121) #→ False
near_hundred(-101) #→ False
near_hundred(-209) #→ False
near_hundred(190) #→ True
near_hundred(209) #→ True
near_hundred(0) #→ False
near_hundred(5) #→ False
near_hundred(-50) #→ False
near_hundred(191) #→ True
near_hundred(189) #→ False
near_hundred(200) #→ True
near_hundred(210) #→ True	
near_hundred(211) #→ False
near_hundred(290) #→ False
