x = int(input(
"""Jaką operację chcesz wykonać?
1) dodawanie
2) odejmowanie
3) mnożenie
4) dzielenie
5) potęgowanie"""))
y = int(input("podaj 1 liczbe"))
z = int(input("podaj 2 liczbe"))
if x == 1:
    print("twój wynik to", y+z )
elif x == 2:
    print("twój wynik to", y-z )
elif x == 3:
    print("twój wynik to", y*z )
elif x == 4:
    if z == 0:
        print("nie dziel przez 0")
        exit()
    print("twój wynik", y/z)
elif x == 5:
    print("twój wynik to", y**z )
else:
    print("zły wybór")