
# gegeven een lage en hoge integer, tel het aantal symmetrische getallen
# een symmetrisch getal is een getal waarvan de som van de eerste helft van de cijfers gelijk is aan de som van de tweede helft van de cijfers
# vb: 1230 is symmetrisch omdat 1 + 2 = 3 + 0
# vb 1 -100 -> uitkomst is 9 en de symmetrische getallen zijn 11, 22, 33, 44, 55, 66, 77, 88, 99.



def countSymmetricIntegers(low,high):
    c = 0 # counter
    for index in range(low, high + 1):
        s = str(index)                  # hier zetten we de index om naar een string
        n = len(s)                      # hier halen we de lengte van de string op nodig voor getallen met een oneven aantal cijfers
                                        # en ook om de helft te berekenen

        if n % 2 != 0:
            index += 1
            continue

        half = n // 2       # hier delen we de lengte van de string door 2 om de helft te berekenen
        left = s[:half]     # alle karakters voor de index[half])
        right = s[half:]    # alle karakters vanaf de index[half] tot het einde van de string

        if (sum(map(int, left)) == (sum(map(int, right)))): # zet de string om naar een lijst van integers en tel ze apart op
            index += 1
            c += 1

    return c

print(countSymmetricIntegers(1, 100))       # 9
print(countSymmetricIntegers(5000, 10000))  # 335
print(countSymmetricIntegers(1, 10000))     # 624
