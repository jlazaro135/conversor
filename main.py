mille = 0.62
km = 1

while True :
    ans1 = input ("Conversor millas a km y viceversa. ¿qué quieres convertir, km a millas o millas a km?: ")
    if ans1 == "km a millas":
        km1=float(input ("introduce los kms que quieres convertir a millas: "))
        mille1 = km1 * mille
        print ("la distancia en millas es de: " +" "+str(mille1))
        break

    elif ans1 == "de km a millas":
        km1 = float(input("introduce los kms que quieres convertir a millas: "))
        mille1 = km1 * mille
        print ("la distancia en millas es de:" +" "+str(mille1))
        break

    elif ans1 == "de millas a km":
        mille1 = float(input("introduce las millas que quieres convertir a kms: "))
        km1 = mille1 / 0.62
        print("la distancia en kms es de: "+ " " + str(km1))
        break

    elif ans1 == "millas a km":
        mille1 = float(input("introduce las millas que quieres convertir a kms: "))
        km1 = mille1 / 0.62
        print("la distancia en en kms es de: "+ " " + str(km1))
        break

    else:
        print ("no te he entendido, ¿puedes ser más específico?")


ans2 = 0

while ans2 != "n":
    ans2=input("¿Quieres volver a hacer otra conversión. y/n?: ")
    if ans2 == "y":
        while True:
            ans3 = input("¿Quieres convertir de millas a km, o de km a millas: ?")
            if ans3 == "de millas a km":
                mille1 = float(input("Por favor, introduce la distancia en millas de tu viaje:  "))
                km = mille1 / 0.6
                print ("la distancia en km es de" +" "+str(km))
                break
            elif ans3 == "millas a km":
                mille1 = float(input("Por favor, introduce la distancia en millas de tu viaje:  "))
                km = mille1 / 0.6
                print ("la distancia en km es de"+" "+str(km))
                break
            elif ans3 == "de km a millas":
                km = float(input("Por favor, introduce la distancia en kms de tu viaje:  "))
                km = km * 0.6
                print ("la distancia en km es de"+" "+str(km))
                break
            elif ans3 == "km a millas":
                km = float(input("Por favor, introduce la distancia en kms de tu viaje:  "))
                km = km * 0.6
                print("la distancia en km es de" + " " + str(km))
                break
            else:
                print ("no te entiendo bien, ¿puedes ser más específico?")

    else:
        print ("Pásalo en grande en tu viaje!!")










