import pandas as pd
import string
import matplotlib.pyplot as plt

print(list(string.ascii_uppercase)[0:22])

avgBalance = pd.read_csv("avg_balance.csv", header=None, names=list(string.ascii_uppercase)[0:26], index_col=False)

newNames = {"H": "GVWY", "L": "PRSH", "P": "SHVR", "T": "ZIC", "X": "ZIP"}
avgBalance.rename(columns=newNames, inplace=True)
avgBalance.plot(x="B", y=["GVWY","PRSH", "SHVR"], kind="line")
# avgBalance.plot(x="B", y=["C", "D"], kind="line")
plt.show(block=True)

