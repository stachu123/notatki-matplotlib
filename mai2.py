import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("imiona2.xlsx")
# print(df.head(10))
#
# wieksza_od_1000 = df.loc[df.Liczba > 1000]
# print(wieksza_od_1000)
#
# moje_imie = df.loc[df.Imie == "STANISŁAW"]
# print(moje_imie)
#
# print(df.Liczba.sum())
# print(df.groupby(["Imie"]).agg({"Liczba":["sum"]}))
# print(df.loc[df.Rok>=2000].loc[df.Rok<=2005].agg({'Liczba':['sum']}))
# print(df.groupby(["Plec"]).agg({'Liczba':['sum']}))
#
# print(df["Imie"].max(axis=0))
# print(df.groupby(["Rok", "Plec"], as_index=False).agg('max'))
# grupaplec = df.groupby('Plec')
# for n in grupaplec.groups.keys():
#     for m in grupaplec.get_group(n).groupby('Rok').groups.keys():
#         print(grupaplec.get_group(n).groupby('Rok').get_group(m).sort_values(by='Liczba').iloc[-1]['Imie'])
plecrok = df.groupby(['Plec','Rok'])

for m in plecrok.groups.keys():
    print(plecrok.get_group(m).sort_values(by='Liczba').iloc[-1])

# print(df.groupby(["Rok", "Imie"]).agg({'Liczba':['max']}))
#
# plecrok = df.groupby(['Plec','Rok'])
#
# for m in plecrok.groups.keys():
#     print(plecrok.get_group(m).sort_values(by='Liczba').iloc[-1])
#
# df = pd.read_csv("zamowienia.csv", sep=";")
#
# print(df.head())
# print(df["Sprzedawca"].unique())
# print(df["Utarg"].nlargest(5))
# # print(df.loc[df["Utarg"].idmax()])
# print(df.groupby("Sprzedawca").agg({"idZamowienia" : "count"}))
# print(df.groupby("Kraj").agg({"idZamowienia" : "count"}))
# mask2005 = (df['Data zamowienia'] >= "2005-01-01") & (df['Data zamowienia'] <= "2005-12-31")
# mask2004 = (df['Data zamowienia'] >= "2004-01-01") & (df['Data zamowienia'] <= "2004-12-31")
# df1 = df[mask2005]
# df2 = df[mask2004]
# print(df1.head)
# print(df1.groupby("Kraj").agg({"Sprzedawca": "count"}))
# print(df2.groupby("Kraj").agg({"Utarg": "mean"}))
# df1.to_csv(r'dane2005', index=False)
# df1.to_csv(r'dane2004', index=False)


# df = pd.read_excel("imiona2.xlsx")
# print(df.head())
#
#
# # dzieciroku = df.groupby('Rok').agg({'Liczba':['sum']})
# # wykres = dzieciroku.plot()
# # wykres.set_xlabel('Rok')
# # wykres.set_ylabel('Dzieci')
# # wykres.legend()
# # plt.xticks([x for x in range (2000, 2020) if x%2==0])
# # plt.show()
#
# dzieciroku = df.groupby('Plec', as_index=False).sum()
# print(df.keys())
# dzieciroku.drop('Rok', axis=1, inplace=True)
# print(dzieciroku)
# #
# # c = ['black', 'blue', 'orange']
# # plt.bar(dzieciroku["Plec"], height=dzieciroku["Liczba"], color=c)
# # plt.xlabel("PLEC")
# # plt.ylabel("ilosc dzieci w liczba ch matematycznych bo tak latwiej czytac")
# # plt.title("podzial urodzonych dzieci smieci")
# # plt.show()
#
# justfive = (df['Rok'] >= 2012) & (df['Rok'] <= 2017)
# df1 = df[justfive]
# print(df1.head())
# dzieciroku1 = df1.groupby('Plec', as_index=False).agg({"Liczba"  : "sum"})
# print(dzieciroku1)
#
# dzieciroku1["procenty"] = (dzieciroku1["Liczba"] / dzieciroku1["Liczba"].sum()) * 100
# dzieciroku1.drop('Liczba', axis=1, inplace=True)
# print(dzieciroku1)
#
# myexplode = [0.05, 0]
# plt.pie(dzieciroku1["procenty"], labels=["Kobiety", "mezczyzni"], explode = myexplode)
# plt.legend()
# plt.show()

# df1 = pd.read_csv('zamowienia.csv',sep=';')
# wykres_zad4 = df1.groupby('Sprzedawca').size()
# wykres_zad4.plot(kind='bar',color=['Red','Blue','Yellow','Black','Green','Gray','Pink','Cyan','Purple'])
# plt.show()
