import pandas as pd
import numpy as np

# data extraction
df = pd.read_csv("/home/allanburnier/Documents/freeCodeCampProject/DataAnalysis/datacleaning/medical_examination/medical_examination.csv")


# data cleaning

#setting the index to id
df.set_index(df["id"])
#dropping id 
# df.drop("id",inplace=True, axis=1)

# converting age from days to year

df["age"] = (df["age"] / 365).apply(np.floor).astype(int)

# convert size in meters :

df["height"] = df["height"] / 100


# adding bmi : poids[kg] / taille^2[m^2] 

df["bmi"] = df["weight"] / (df["height"] ** 2)

#adding overweight if bmi is more than 25, 0 if not overweight else 1

df["overweight"] = df["bmi"] >=25

df["overweight"] = df["overweight"].astype(int)

#normalizing data 
df[]

print(df.head())