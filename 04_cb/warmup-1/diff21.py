# Wesley Leon
# Ugly Duckies
# SoftDev
# K04 -- Reviewing python basics
# 2025-09-15m
# time spent: 1

def diff21(n):
  return (abs(n-21) if n < 21 else 2 *abs(n-21))

diff21(19) #→ 2
diff21(10) #→ 11
diff21(21) #→ 0
diff21(22) #→ 2
diff21(25) #→ 8
diff21(30) #→ 18
diff21(0) #→ 21
diff21(1) #→ 20
diff21(2) #→ 19
diff21(-1) #→ 22
diff21(-2) #→ 23
diff21(50) #→ 58
