'''
====================================
-- 040 - Practical Your Age Full Details 
-- link : https://www.youtube.com/watch?v=S6dhvob-4DM&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs 
====================================
'''
# -------------------------------------
# -- Practical Your Age Full Details --
# -------------------------------------

# Input Age
age = int(input('What\'s Your Age ? ').strip())

# Get Age in All Time Units
months = age * 12
weeks = months * 4
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print('You Lived For:')
print(f"{months} Months.")
print(f"{weeks:,} Weeks.")
print(f"{days:,} Days.")
print(f"{hours:,} Hours.")
print(f"{minutes:,} Minutes.")
print(f"{seconds:,} Seconds.")