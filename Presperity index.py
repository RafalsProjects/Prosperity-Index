import pandas as pd # importujemy pandas jako pd
import numpy as np # import numpy as np
import matplotlib.pyplot as plt
#path='Projekt międzyprzedmiotowy/Dane.csv'
#table=pd.read_csv(path, sep=";")

path='Data.xlsx'
table=pd.read_excel(path, sheet_name="Dane")

#zmiana wielkości liter
table.rename(str.lower, axis=1, inplace=True)
table['kraje/wskazniki']=table['kraje/wskazniki'].str.lower()

#Wyrzucenie pierwszej kolumny 0
#table.columns[0] # Wyświetlenie nazwy kolumny 1 czyli segmentu wskaźników.
table.drop("unnamed: 0", axis=1, inplace=True) 
table

#table.drop("kontynenty", axis=1, inplace=True) #Wyrzucenie kolumny kontytnenty(wskaźniki)
#table.drop("unnamed: 51", axis=1, inplace=True) #Wyrzucenie kolumny
table.drop("unnamed: 52", axis=1, inplace=True) #Wyrzucenie kolumny
table.drop("unnamed: 53", axis=1, inplace=True) #Wyrzucenie kolumny
table.drop("unnamed: 54", axis=1, inplace=True) #Wyrzucenie kolumny
table.drop("unnamed: 55", axis=1, inplace=True) #Wyrzucenie kolumny
table.drop("unnamed: 56", axis=1, inplace=True) #Wyrzucenie kolumny
table.drop("unnamed: 57", axis=1, inplace=True) #Wyrzucenie kolumny
table.drop(1, axis=0, inplace=True) #wyrzucamy Edukacje. Osoba nie przygotowała wskaźników

table.drop(5, axis=0, inplace=True) #wyrzucamy Edukacje. Osoba nie przygotowała wskaźników
table.drop(6, axis=0, inplace=True) #wyrzucamy Edukacje. Osoba nie przygotowała wskaźników
table.drop(7, axis=0, inplace=True) #wyrzucamy Edukacje. Osoba nie przygotowała wskaźników
table.drop(8, axis=0, inplace=True) #wyrzucamy Edukacje. Osoba nie przygotowała wskaźników
table.drop(9, axis=0, inplace=True) #wyrzucamy Edukacje. Osoba nie przygotowała wskaźników

#table.columns=table.iloc[0] # Przypisanie nazwy wierszy w kolumnach jako nagłówki
#print(table)
#print("-----------------")





## Przygotowywanie tabeli 

# Zastępowanie , na .
#table=table.replace(".", ",", regex=True) 

# Zastąpienie/usunięcie years\t i years
table=table.replace(r"\t", "", regex=True)
table=table.replace(r" years\t", "", regex=True)
table=table.replace(" years", "", regex=True)
table

# Zastępienie polskich znaków i spacji
"""
table.columns=table.columns.str.replace(" ", "_", regex=True) 
table.columns=table.columns.str.replace("ś", "s", regex=True) 
table.columns=table.columns.str.replace("ź", "z", regex=True) 
table.columns=table.columns.str.replace("ó", "o", regex=True) 
table.columns=table.columns.str.replace("ż", "z", regex=True)
table.columns=table.columns.str.replace("ć", "c", regex=True) 
table.columns=table.columns.str.replace("ę", "e", regex=True) 
table.columns=table.columns.str.replace("ł", "l", regex=True) 

table=table.replace(" ", "_", regex=True) 
table=table.replace("ś", "s", regex=True) 
table=table.replace("ź", "z", regex=True) 
table=table.replace("ó", "o", regex=True) 
table=table.replace("ż", "z", regex=True)
table=table.replace("ć", "c", regex=True) 
table=table.replace("ę", "e", regex=True) 
table=table.replace("ł", "l", regex=True) """
#lub
characters_to_replace=[
    (' ', "_"),
    ("ś", "s"),
    ("ź", "z"),
    ("ó", "o"),
    ("ż", "z"),
    ("ć", "c"),
    ("ę", "e"),
    ("ł", "l")
        
]
for orig_char, new_char in characters_to_replace:
    table.columns=table.columns=table.columns.str.replace(orig_char, new_char)
    table=table.replace(orig_char, new_char, regex=True) 

# Dodawanie intexów do listy
#Zapisywanie nazwy wskaźnika do listy
name_of_indicator=table["kraje/wskazniki"]
name_of_indicator
number_of_indicator=table.index.values.tolist()
number_of_indicator

# Zapisywanie list do słownika
#indicators=dict(zip(number_of_indicator, name_of_indicator))
#indicators
#for key in indicators:
#    print(key, ' : ', indicators[key])
    



    
# Transponowanie tabeli
table=table.transpose()

# Usuwanie pierwszego wiersza kraje/wskazniki
table=table.drop("kraje/wskazniki", axis=0)

## Zastępowanie "-" średnimi w kolumnach
# Pierwszy krok. 
# Zastąpienie "-" na NaN
table=table.replace("-", np.nan, regex=True) 

# drugi krok. 
# Konwersja niektórych stringów na int
for i in number_of_indicator:
    table[i]=pd.to_numeric(table[i])
    
# trzeci krok
# Zastępowanie "NaN" czyli pustych kolumn na średnimi w kolumnach
table=table.replace(np.nan, table.mean(numeric_only=False), regex=True) 

# Usuwanie pustych kolumn 
#table=table.dropna("columns") 
#table

# Numeracja i liczenie wskaźników
indexs_new=[]
for i in range(len(table.columns)):
   indexs_new.append(i+1)

# Zamianiamy nazwy kolumn (Liczby które są rozrzucone) na nazwy (liczby w liscie indexs_new) Lepiej to rozwiązanie niż rozwiązanie poniżej które jest zakomentowen
table.set_axis(indexs_new, axis=1, inplace=True) 

# Zapisywanie list do słownika z nowymi indeksami
indicators=dict(zip(indexs_new, name_of_indicator))
#Wysietlanie tego słownika
#for key in indexs_new:
#    print(key, ' : ', indicators[key])

#lub
#table.columns = indexs_new
#table.columns[0]

# Zamiana nazw kolumn na liczby w liśćie (ale tutaj niestety mamy problem z odniesieniem się do niej przez np table[i]
"""# Numeracja kolumn po usunięciu pustych kolumn
for i in range(len(table.columns)):
   print(i)
   table.columns.values[i]=i+1"""
   
"""for i in range(len(table.columns)):   
    table[i].rename(columns={table[i] : i}, inplace=True)"""

# Wyświetla nam pierwszą kolume o nazwie 1 z tabeli 
#print(table.get(1)) 
#table[1]

## [2pkt] Przeprowadzenie normalizacji danych.
# Normalizacja dla wskaźników 
for i in range(1, len(indexs_new) + 1):
    sub_result_a=(table[i]-table[i].min())
    sub_result_b=(max(table[i])-min(table[i]))
    table[i]=sub_result_a/sub_result_b
table[1]
# Pomnożenie odpowiednich kolumn (wskaźników) przez -1, które zmniejszają względny dobrobyt
#Sprawdzić czy te kolumny rzeczywiście powinny mieć takie wagi :)
#Ściąga 
# 1  :  samobójstwo na 100.000 ludzi
# 2  :  średnia długość życia kobiet
# 3  :  migracje procentowe kobiet do innych krajów (ilość kobiet emigrujących) rok 2022
# 4  :  ile jest procent kobiet w danym kraju
# 5  :  średnie wynagrodzenie roczne (w $) na rok 2021 na osobę
# 6  :  stopa bezrobocia (w %) na rok 2021
# 7  :  ilość kobiet pracujących (w %) w stosunku do mężczyzn
# 8  :  ilość osób, które ukończyły studia wyższe (w%)
# 9  :  ilość dzieci pracujących (w %, 5-17 lat)
# 10  :  dostępność ochrony zdrowia (ilość łóżek na 1000 kobiet)
# 11  :  wydatki na ochronę zdrowia w 2021(usd) (podzielone na ilość kobiet)
# 12  :  dostępność szczepień w grupie wiekowej 15-25 (ilość szczepionek przypadająca na jedną kobietę)
# 13  :  wskaźnik zachorowań na hiv (ilość zdrowych kobiet podzielona na ilość chorych kobiet)
# 14  :  wskaźnik zachorowań na choroby wymagające hospitalizacji w 2021 roku (ilość kobiet podzielona na kobiety hospitalizowane)
# 15  :  cena 1 m2 mieszkania (usd)/średni dochód
# 16  :  stopa inflacji cpi
# 17  :  producer prices change (inflaca producentów yoy czyli rok do roku)
# 18  :  sprzedaż detaliczna/pkb
# 19  :  oszczędności brutto / pkb (w %) - gross savings (% of gdp)
table[1]=table[1]*(-1)
table[2]=table[2]*(1)
table[3]=table[3]*(-1)
table[4]=table[4]*(1)
table[5]=table[5]*(1)
table[6]=table[6]*(-1)
table[7]=table[7]*(1)
table[8]=table[8]*(1)
table[9]=table[9]*(-1)
table[10]=table[10]*(1)
table[11]=table[11]*(1)
table[12]=table[12]*(1)
table[13]=table[13]*(-1)
table[14]=table[14]*(-1)
table[15]=table[15]*(-1)
table[16]=table[16]*(-1)
table[17]=table[17]*(-1)
table[18]=table[18]*(1) # Średnia wartość najlepsza
table[19]=table[19]*(1) # Średnia wartość najlepsza 



# [3pkt] Wyznaczenie średniej ważonej.

## Średnia ważona
# Przypisanie Wagi
#weights=[1, 0.9, 0.2 , 0, 1, 1, 2, 2]
weights={
    1 : 1,      # samobójstwo na 100.000 ludzi
    2 : 0.9,    # średnia długość życia kobiet
    3 : 0.2,    # migracje procentowe kobiet do innych krajów (ilość kobiet emigrujących) rok 2022
    4 : 0,      # ile jest procent kobiet w danym kraju
    5 : 1,      # średnie wynagrodzenie roczne (w $) na rok 2021 na osobę
    6 : 1,      # stopa bezrobocia (w %) na rok 2021
    7 : 0.5,    # ilość kobiet pracujących (w %) w stosunku do mężczyzn
    8 : 1,      # ilość osób, które ukończyły studia wyższe (w%)
    9 : 1,      # ilość dzieci pracujących (w %, 5-17 lat)
    10 : 0.5,   # dostępność ochrony zdrowia (ilość łóżek na 1000 kobiet)
    11 : 0.6,   # wydatki na ochronę zdrowia w 2021(usd) (podzielone na ilość kobiet)
    12 : 0.2,   # dostępność szczepień w grupie wiekowej 15-25 (ilość szczepionek przypadająca na jedną kobietę)
    13 : 1,     # wskaźnik zachorowań na hiv (ilość zdrowych kobiet podzielona na ilość chorych kobiet)  
    14 : 1,     # wskaźnik zachorowań na choroby wymagające hospitalizacji w 2021 roku (ilość kobiet podzielona na kobiety hospitalizowane)
    15 : 1,     # cena 1 m2 mieszkania (usd)/średni dochód
    16 : 0.6,   # stopa inflacji cpi
    17 : 0.7,   # producer prices change (inflaca producentów yoy czyli rok do roku)
    18 : 0.5,   # sprzedaż detaliczna/pkb
    19 : 0.6    # oszczędności brutto / pkb (w %) - gross savings (% of gdp)
}
# Przerzucanie wartości słownika do listy
weights=list(weights.values())


# Pomnożenie tabeli przez wagi
#table.columns.values*pd.Series(weights)
#lub
table.mul(weights, axis=1)

## Średnia
"""
# Stworzenie listy
top_of_values=[]
for i in range(len(indexs_new)):
    top_of_values=top_of_values+table[i+1]
    

sum_weights=sum(weights)
top_of_values=top_of_values/sum_weights

table.assign(Srednia_wazona=top_of_values)"""

srednia_wazona=table.sum(axis=1)/sum(weights)
srednia_wazona

table["srednia_wazona"]=srednia_wazona

# [2pkt] Zaprezentowanie pięciu najlepszych i najgorszych krajów w formie skróconej tabelizawierającej wyłącznie nazwy tych krajów i wartości średnich ważonych.

table["srednia_wazona"].nlargest(5)
table["srednia_wazona"].nsmallest(5).sort_values(ascending=False)

resaults=table["srednia_wazona"].nlargest(5)
resaults=resaults.append(table["srednia_wazona"].nsmallest(5).sort_values( ascending=False))
resaults=resaults
table['srednia_wazona']=table['srednia_wazona']+0.221906

#lub 
# posrotować i wyświetlić table.head() dwa razy 
#table.sort_values('srednia_wazona', ascending=False).head().srednia_wazona

#table.sort_values('srednia_wazona', ascending=False).tail().srednia_wazona

table=table.sort_values('srednia_wazona', ascending=True)

# Wizualizacja
plt.barh(table.index , table["srednia_wazona"], )
plt.show()

## https://colab.research.google.com/drive/1IoDawGTGZtIASmvnczyTZ_8YAXTzZzbr?usp=sharing
