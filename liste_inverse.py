nombres = input("Entre une liste de nombres : ")
liste = nombres.split()
for i in range(len(liste)-1,-1,-1):

    print( liste[i], end = " ")