import random
import os
#sayi=random.randint(1,100)  random sayı uretme canı boyle vercez
class Dusman:
    def __init__(self,can,damage):
        self.name="Düşman"
        self.damage=damage
        self.can=can
        self.canlimi= True
    def vur(self,player):
        player.can-= self.damage  #self == c# .this fonk?
                                    #** nesneye ait her metod da self ekini kullanmak zorundayız!

    def ol (self):
        self.canlimi = False

class Player:
    def  __init__(self,can,damage):
        self.name="OrhanBenceGay"  #kullanıcı adını burdan degıstırebılırız :)
        self.damage=damage
        self.can=can
        self.canlimi= True

    def vur(self, dusman):
        dusman.can -= self.damage

    def ol(self):
        self.canlimi = False

def Main():
    dusmanlar = list()
    oyuncu=Player(can =random.randint(600,900) , damage = random.randint(80,100))
    for i in range(10):
        dusmanlar.append(Dusman(can =random.randint(80,100), damage = random.randint(60,80)))

    while True:
        os.system('cls')
        if len(dusmanlar)== 0:
            print("Adaaamm! Kazandın ! You Win")
            quit()
        print("     OrhanBenceGay ===> Can: {} ---- Damage{}".format(oyuncu.can,oyuncu.damage))
        for dusman in dusmanlar:
            print("[{}]     Dusman    ----- can {} ---- Damage{}".format(dusmanlar.index(dusman)+1,dusman.can,dusman.damage))
        giris = input ("secim: ")
        if giris.isdigit():
            giris = int(giris)
            if giris > 0 and giris <= len(dusmanlar):

                index= giris -1
                saldırılan = dusmanlar[index]
                oyuncu.vur(saldırılan)
                rasgele = random.randint(0,len(dusmanlar)-1)
                tom = dusmanlar[rasgele] #bize vuran oyuncu burda seçılıyo
                tom.vur(oyuncu)
                if oyuncu.can <= 0:
                    oyuncu.ol()
                    print("oyun bitti Game Over!")
                    input("")
                    quit()
                if saldırılan.can <=0:
                    saldırılan.ol()
                    dusmanlar.remove(saldırılan)

            else:
                print("Hatalı düşman seçimi! \a")
                input('')
        else:
            print ("yalnizca rakam giriniz!")
            input("Enter'a basarak devam edebilirsiniz!")



if __name__ == "__main__":
    Main()
