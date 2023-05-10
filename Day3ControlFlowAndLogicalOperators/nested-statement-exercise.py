
print("Welcome to Roller Coaster Ride in Carmen")

height = int(input("Pila imohang Height in Centimeter? "))

if height >= 120:
    print("Pwede naka makasakay sa Roller Coaster diri sa carmen")

    edad = int(input("iInput imohang edad ngari: "))
    if edad <= 18:
        print("Kay below 18 mn ka imohang bayaran kay 20 pesos")
    else:
        print("Imohang edad kay 18 year above man imohang bayaran kay 30 pesos")

else:
    print("Dili pa ka pwede maka sakay sa Roller Coaster diri sa Carmen kay kulang ka sa height")
