wookiees = [[] for _ in range(int(input()))]

cargas = [int(i) for i in input().split()]



sobras = []

for carga in cargas:

    if [] in wookiees:

        wookiees[wookiees.index([])].append(carga)

    else:

        for wookiee in wookiees:

            if wookiee[-1] >= carga:

                wookiee.append(carga)

                break

        else:

            sobras.append(carga)



if wookiees:

    print(*sorted(wookiees, key=lambda x: sum(x), reverse=True))

else:

    print('Os Wookies foram para o lado sombrio da força!')

if sobras:

    print(*sobras)

else:

    print('A força está com os Wookies!')