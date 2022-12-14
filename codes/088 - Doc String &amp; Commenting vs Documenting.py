'''
====================================
-- 088 - Doc String &amp; Commenting vs Documenting 
-- link : https://www.youtube.com/watch?v=6skfWbMu9MY&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs 
====================================
'''
# --------------------------------------------
# -- Doc String &amp; Commenting vs Documenting --
# --------------------------------------------
# [1] Documentation String For Class, Module or Function
# [2] Can Be Accessed From The Help and Doc Attributes
# [3] Made For Understanding The Functionality of The Complex Code
# [4] Theres One Line and Multiple Line Doc Strings
# -------------------------------------------------

def elzero_function(name):
  """
  Elzero Function
    It Say Hello From Elzero
  Parameter:
    name =&gt; Person Name That Use Function
  Return:
    Return Hello Message To The Person
  """
  print(f"Hello {name} From Elzero")

elzero_function("Ahmed")

print(dir(elzero_function))

print(elzero_function.__doc__)

help(elzero_function)