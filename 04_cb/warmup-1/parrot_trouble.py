# Wesley Leon
# Ugly Duckies
# SoftDev
# K04 -- Reviewing python basics
# 2025-09-15m
# time spent: 1

def parrot_trouble(talking, hour):
  return (talking and (hour < 7 or hour > 20))

parrot_trouble(True, 6) #→ True
parrot_trouble(True, 7) #→ False
parrot_trouble(False, 6) #→ False
parrot_trouble(True, 21) #→ True
parrot_trouble(False, 21) #→ False
parrot_trouble(False, 20) #→ False
parrot_trouble(True, 23) #→ True
parrot_trouble(False, 23) #→ False
parrot_trouble(True, 20) #→ False
parrot_trouble(False, 12) #→ False
