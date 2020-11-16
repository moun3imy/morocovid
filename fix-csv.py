import pandas as pd

df = pd.read_csv("CSVs/corona_15-11-20.csv")

df["Décès"] = df["Décès"].astype(int)
df["Nouveaux Cas"] = df["Nouveaux Cas"].astype(int)
df ["indice"] = df.index
print(df.head())
print(df.tail())
df.to_csv("CSVs/corona_15-11-20.csv",index=False)
