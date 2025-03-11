number=int(input("Введите число: "))
if number>0:
    print("Число положительное.")
    if number%2==0:
        print("Число четное.")
    else:
        print("Число нечетное.")
elif number<0:
    print("Число отрицательное.")
else:
    print(    "Число равно нулю.")


#Ü2


nurk1=float(input("esimene nurk: "))
nurk2=float(input("teine nurk: "))
nurk3=float(input("kolmas nurk: "))
if nurk1>0 and nurk2>0 and nurk3>0 and nurk1+nurk2+nurk3==180:
    print("saa olla kolmnurk")
    if nurk1==nurk2==nurk3:
        print("see on võrdkülgne kolmnurk")
    elif nurk1==nurk2 or nurk2==nurk3 or nurk1==nurk3:
        print("see on võrdharne kolmnurk")
    else:
        print("see on mitmekülgne kolmnurk")
else:
    print("ei saa olla kolmnurk")


#Ü3


answer=input(" (yes/no): ")
if answer=="yes":
    day=int(input("kirjuta nädala päeva number (1 kuni 7): "))
    if 1<=day and day<=7:
        days_of_week=["esmaspäev", "teisipäev", "kolmapäev", "neljapäev", "reede", "laupäev", "pühapäev"]
        print(f"nädala päev: {days_of_week[day-1]}")
    else:
        print("viga kirjuta ainult 1 kuni 7")
else:
    print("ei")


#Ü4


päev=int(input("kirjuta oma sünnipäev: "))
kuu=int(input("kirjuta oma sünnikuu: "))
if (1<=päev<=31) and (1<=kuu<=12):
    if (kuu==3 and päev>=21) or (kuu==4 and päev<=19):
        tähemärk="Jäär"
    elif (kuu==4 and päev>=20) or (kuu==5 and päev<=20):
        tähemärk="Sõnn"
    elif (kuu==5 and päev>=21) or (kuu==6 and päev<=20):
        tähemärk="Kaksikud"
    elif (kuu==6 and päev>=21) or (kuu==7 and päev<=22):
        tähemärk="Vähk"
    elif (kuu==7 and päev>=23) or (kuu==8 and päev<=22):
        tähemärk="Lõvi"
    elif (kuu==8 and päev>=23) or (kuu==9 and päev<=22):
        tähemärk="Neitsi"
    elif (kuu==9 and päev>=23) or (kuu==10 and päev<=22):
        tähemärk="Kaalud"
    elif (kuu==10 and päev>=23) or (kuu==11 and päev<=21):
        tähemärk="Skorpion"
    elif (kuu==11 and päev>=22) or (kuu==12 and päev<=21):
        tähemärk ="Ambur"
    elif (kuu==12 and päev>=22) or (kuu==1 and päev<=19):
        tähemärk ="Kaljukits"
    elif (kuu==1 and päev>=20) or (kuu==2 and päev<=18):
        tähemärk="Veevalaja"
    else:
        tähemärk = "Kalad"
    print(f"sinu tähemärk on: {tähemärk}")
else:
    print("vale andmed palun vaata")


#ü 5


user_input=input("kirjuta number: ")
if user_input():
    num=int(user_input)
    print(f"täis arv. 50% arvest: {num*0.5}")
elif user_input("."," ", 1) and user_input(".")==1:
    num=float(user_input)
    print(f"Дробное arv. 70% arvest:{num*0.7}")    
elif user_input():
    print(f"{user_input}")
else:
    print("vale andmet")

#ü6

def lahenda_ruutvorrand():
    valik=input("Kas soovite lahendada ruutvõrrandi? (jah/ei): ").strip().lower()
    if valik!="jah":
        print("Head aega!")
    try:
        a=float(input("Sisestage kordaja a: "))
        b=float(input("Sisestage kordaja b: "))
        c=float(input("Sisestage kordaja c: "))
    except:
        print("Viga: Sisestage arvulised väärtused.")
    if a==0:
        print("Viga: kordaja a ei tohi olla 0.")
    D=b**2-4*a*c
    print(f"Diskriminant D={D}") 
    if D>0:
        x1=(-b+math.sqrt(D))/(2*a)
        x2=(-b-math.sqrt(D))/(2*a)
        print(f"Kaks lahendit: x1={round(x1,2)}, x2={round(x2,2)}")
    elif D==0:
        x=-b/(2*a)
        print(f"Üks lahend: x={round(x,2)}")
    else:
        print("Lahend puudub (D<0)")
lahenda_ruutvorrand()
