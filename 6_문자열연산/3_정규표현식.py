import numpy as np
import pandas as pd

name_tuple = ["Dong Ju", "Steven Jobs", "Larry Page", "Elon Musk",
              "Bill Gates", "Mark Zuckerberg", None, "Jeff Bezos"]
names = pd.Series(name_tuple)
print(names)

# 알파벳이면 True, 아니면 False
print(names.str.match('([A-Za-z]+)'))

print(names.str.findall('([A-Za-z]+)'))
