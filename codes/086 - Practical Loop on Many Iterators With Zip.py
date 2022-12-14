'''
====================================
-- 086 - Practical Loop on Many Iterators With Zip 
-- link : https://www.youtube.com/watch?v=Z1gwFze9e94&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs 
====================================
'''
# ----------------------------------------------------
# -- Practical =&gt; Loop on Many Iterators With Zip() --
# ----------------------------------------------------
# zip() Return A Zip Object Contains All Objects
# zip() Length Is The Length of Lowest Object
# ------------------------------------------------

list1 = [1, 2, 3, 4, 5]
list2 = ["A", "B", "C", "D"]
tuple1 = ("Man", "Woman", "Girl", "Boy")
dict1 = {"Name": "Osama", "Age": 36, "Country": "Egypt", "Skill": "Python"}

for item1, item2, item3, item4 in zip(list1, list2, tuple1, dict1):

  print("List 1 Item =&gt;", item1)
  print("List 2 Item =&gt;", item2)
  print("Tuple 1 Item =&gt;", item3)
  print("Dict 1 Key =&gt;", item4, "Value =&gt;", dict1[item4])

ultimateList = zip(list1, list2)
print(ultimateList)
for item in ultimateList:
  print(item)