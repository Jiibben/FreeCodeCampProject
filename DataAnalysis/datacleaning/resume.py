import pandas as pd


df = pd.DataFrame({"name":["Frank", "John", "Micheal", "Allan"], "age":[12, 12, 20, 19]})



df = df.set_index(df["name"])


df["isAdult"] = df["age"] >=18


adults = df[df["isAdult"]]
print(adults)