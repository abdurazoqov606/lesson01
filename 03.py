kun = input("Hafta kunini kiriting: ")
soat = int(input("soatni kiriting: "))
dam_olish = 'shanba' or 'yakshanba' == True
if kun == dam_olish:
    if soat >=9 and soat <= 18:
        print("Do'kon yopiq")
else:
    print("do'kon ochiq")