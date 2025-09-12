# Wesley Leon
# Ugly Duckies
# SoftDev
# K04 -- Reviewing python basics
# 2025-09-15m
# time spent: 1

def makes10(a, b):
  return (a + b == 10 or (b == 10 or a == 10))

makes10(9, 10) #→ True
makes10(9, 9) #→ False
makes10(1, 9) #→ True
makes10(10, 1) #→ True
makes10(10, 10) #→ True
makes10(8, 2) #→ True
makes10(8, 3) #→ False
makes10(10, 42) #→ True
makes10(12, -2) #→ True
