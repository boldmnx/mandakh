# pip install pandas
# print(type(df))
# zamiig butneer n bichih bol df = pd.read_excel(r"c://pandas.xlsx") useg bichne
import pandas as pd
df = pd.read_excel("pandas.xlsx")
lists = df.values.tolist()

sums = 0
for i in range(0, len(lists)):
    sums += lists[i][1]*lists[i][2]


print(sums)


with open("readme.txt", "w") as f:
    f.write(str(sums))

# print(df)
