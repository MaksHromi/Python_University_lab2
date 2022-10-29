wiek = input ('podaj wiek')
wiek = int(wiek)
if wiek < 4:
    cena = 0
elif wiek <= 18:
    cena = 10
else: cena = 20

print(f"cena biletu {cena} zl")