import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import openpyxl

# df = pd.read_csv('dirtydata.csv')
# print(df.head())
#
# df["Date"] = pd.to_datetime(df['Date'])
# df.dropna(subset=['Date'], inplace=True)
#
# for x in df.index:
#     if df.loc[x, "Duration"] > 120:
#         df.loc[x, "Duration"] + 120

# df = df.transpose()
# df.reset_index()
# df.columns = ["opis"]

#zadanie 1 kolokwium
#  x = [1, 20] krok 0.75 wygenerowac taka serie, calkowite to krok wiadomo
#moze byc tez ze 75 wartosci z tego przedzialu

# y to jakas funkcja fx np 1/x
# i ustawaianie rzeczy do wykresu

 #zzadanie 2
 #zrobic nowa ramke nowa z jakiejs kolumny
 #zrobic grupe
 #np recordy gdy wartosc w kolumnie jest wieksza lub mniejsza itd
 # i wyrzucic rezultat z pogrupowania na  wykres np. kolowy, slupkowy

 #zadanie 3 wczytac ramke danych, pogrupowac, (ta sama ramka w 2 i 3)
 #wykres innny niz w 2 zadaniu, za kazdym razem wczytywac dane
# d = np.arange(1, 20)
# d = np.linspace(1, 20, 30)
# print(d)
# df = pd.read_csv("automobile.csv", header = 0, sep=";")
# print(df)
# df1 = df.loc[df['Length'] < 170]
# print(df1)
# df2 = df.groupby("Car model")["Aspiration"].count()
# # df2.columns = [col[1] for col in df2.columns]
# print(df2)
#autopct= lambda pct:"{:1f}%".format(pct)
# plt.pie(df2, textprops=dict(color="black"), autopct='%.2f%%')
# plt.legend(df2.index , bbox_to_anchor=(0.95, 1), loc="upper left", borderaxespad=0)
# plt.savefig('foo.png')
# plt.show()

# x = np.arange(15, 31)
# y = [math.sqrt(x) + (math.cos(x)/math.sin(x)) for x  in x]
# plt.plot(x, y, label="x^1/2 + cosx/sinx")
# plt.legend()
# plt.title("x^1/2 + cosx/sinx")
# plt.xlabel("x")
# plt.ylabel('y')
# plt.show()
# plt.bar(df2.index, df2)
# plt.xticks(rotation='vertical')
#
# plt.show()
# data0 = [0, 1, 2, 3, 4, 5]
# data3 = [120, 120, 120 ,120, 120, 120]
# data1 = [20,10,30,35,50,0]
# data2 = [80,60,45,15,50,0]
#
#
#
#
# plt.bar(range(len(data1)), data1, alpha=0.5, color='b')
# plt.bar(range(len(data2)), data2, bottom=data1, alpha=0.5, color='r')
# plt.plot(data0, data3, c='green')
#
# plt.xticks([1,2,3,4,5])
# plt.ylabel("Count")
# plt.yticks(np.arange(0,141, 20))
# plt.xticks([0, 1, 2, 3, 4, 5])
# plt.legend(loc='upper left')
#
#
# plt.show()

# df = pd.read_excel('mieszkania1.xlsx', header=0)
# df1 = df.loc[df["Formy budownictwa"] == 'indywidualne']
# df2 = df.loc[df["Formy budownictwa"] == 'spółdzielcze']
# df3 = df.loc[df["Formy budownictwa"] == 'komunalne']
# print(df)
# plt.bar(df1["Rok"] - 0.2, df1["Wartość"], width=0.2, label='indywidualne')
# plt.bar(df2["Rok"], df2["Wartość"], width=0.2, label='spółdzielcze')
# plt.bar(df3["Rok"] + 0.2, df3["Wartość"], width=0.2, label='komunalne')
# plt.legend(loc='best')
# plt.xticks(df1["Rok"])
# plt.figtext(y=1, x=0, s="sz65818")
# plt.yticks(np.arange(0, 100001, 20000))
# plt.show()

df = pd.read_excel('turystyka1.xlsx', header=None)
# print(df)
dfT = df.transpose()
print(dfT)

print(dfT.columns)
dfT.columns = ['kategoria hotelu', 'rok', 'ilosc']

df1 = dfT[dfT['rok'] == '2015']
df2 = dfT[dfT['rok'] == '2018']

labels = df1['kategoria hotelu']
sizes = df1['ilosc']
# wykres 1
plt.pie(sizes, labels=labels)
plt.show()