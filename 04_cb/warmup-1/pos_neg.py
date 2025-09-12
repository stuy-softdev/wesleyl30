# Wesley Leon
# Ugly Duckies
# SoftDev
# K04 -- Reviewing python basics
# 2025-09-15m
# time spent: 1

def pos_neg(a, b, negative):
  return ((a * b < 0 and not negative) or (a * b > 0 and negative and a < 0))

pos_neg(1, -1, False) #→ True
pos_neg(-1, 1, False) #→ True
pos_neg(-4, -5, True) #→ True
pos_neg(-4, -5, False) #→ False
pos_neg(-4, 5, False) #→ True
pos_neg(-4, 5, True) #→ False
pos_neg(1, 1, False) #→ False
pos_neg(-1, -1, False) #→ False
pos_neg(1, -1, True) #→ False
pos_neg(-1, 1, True) #→ False
pos_neg(1, 1, True) #→ False
pos_neg(-1, -1, True) #→ True
pos_neg(5, -5, False) #→ True
pos_neg(-6, 6, False) #→ True
pos_neg(-5, -6, False) #→ False
pos_neg(-2, -1, False) #→ False
pos_neg(1, 2, False) #→ False
pos_neg(-5, 6, True) #→ False
pos_neg(-5, -5, True) #→ True
