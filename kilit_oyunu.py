def oyunu_baslat():                         #Oyunu başlatan, içinde diğer fonksiyonları barındıran ana fonksiyon.
    
    oyunAlaniListe = []                     #İçinde oyun alanındaki taşların nerede olduğunu tutan liste.
    while(True):                            #1. Oyuncuyu temsil edecek karakterin düzgün girilip girilmediği kontrol edilen while döngüsü.
        oyuncu_1 = input("1. oyuncuyu temsil etmek için bir karakter giriniz:")
        if(len(oyuncu_1)!=1):
            print("Bir oyuncuyu temsil etmek için boşluk ya da birden fazla karakter içeren veri kullanamazsınız!")
            continue
        else:break
    while(True):                            #2. Oyuncuyu temsil edecek karakterin düzgün girilip girilmediği kontrol edilen while döngüsü.                                        
        oyuncu_2 = input("2. oyuncuyu temsil etmek için bir karakter giriniz:")
        if(len(oyuncu_2)!=1):
            print("Bir oyuncuyu temsil etmek için boşluk ya da birden fazla karakter içeren veri kullanamazsınız!")
            continue
        else:break

    siraKimde = oyuncu_1                    #Sıranın kimde olduğunu tutan değişken.
    while(True):
       
       try:                                 #Oyun alanı satır/sütun verisinin düzgün girilip girilmediğini kontrol eden try-except bloğu.
            satirSutunSayisi = int(input("Oyun alanının satır/sütun sayısını giriniz(4-8):"))
    
            if(satirSutunSayisi==4 or satirSutunSayisi==8):

                oyunAlaniListe = oyun_alani_olustur(oyuncu_1,oyuncu_2,satirSutunSayisi)   #Taşları tutan listeyi oyunun başlangıç hali olarak dolduran fonksiyon.
                oyun_alani_yazdir(oyunAlaniListe)                                         #Taşları tutan listeye göre oyun alanını ekrana bastıran fonksiyon.
                hamle_yap(siraKimde,oyunAlaniListe,oyuncu_1,oyuncu_2)                     #Hamle yapılmasını sağlayan fonksiyon.
                karar = input("Tekrar oynamak ister misiniz(E/H)?:")
                if(karar=="H"):
                    return True
                else:
                    if(oyunu_baslat()):
                        break

            else:
                raise Exception()
       except:
           print("Girdiğiniz veri hatalı satır/sütun sayısı olarak 4 ya da 8'i seçmelisiniz!")




def oyun_alani_olustur(oyuncu_1,oyuncu_2,satirSutunSayisi):                           #Taşları tutan listeyi oyunun başlangıç hali olarak dolduran fonksiyon.

    oyunAlaniListe = []
    for i in range(0,satirSutunSayisi):
        satirListe = []
        for k in range(0,satirSutunSayisi):
            if(i==0):
                satirListe.append(oyuncu_2)
            elif(i==satirSutunSayisi-1):
                satirListe.append(oyuncu_1)
            else:
                satirListe.append(" ")
        oyunAlaniListe.append(satirListe)

    return oyunAlaniListe


def oyun_alani_yazdir(oyunAlaniListe):                                              #Taşları tutan listeye göre oyun alanını ekrana bastıran fonksiyon.

   if(len(oyunAlaniListe)==4):
       print("\n    A   B   C   D    \n  " + "-"*17)
   else:
       print("\n    A   B   C   D   E   F   G   H    \n  " + "-"*30)
    
   for i in range(0,len(oyunAlaniListe)):
       print(str(i+1) + " |",end="")
       for k in range(0,len(oyunAlaniListe)):
           print(" " + oyunAlaniListe[i][k] + " |",end="")
           if(k==len(oyunAlaniListe)-1):
               print(" " + str(i+1) )

   if(len(oyunAlaniListe)==4):
       print("  "+"-"*17 + "\n    A   B   C   D    \n")
   else:
       print("  "+"-"*30 + "\n    A   B   C   D   E   F   G   H    \n")


def hamle_yap(siraKimde,oyunAlaniListe,oyuncu_1,oyuncu_2):                                  #Girilen hamle verisinin hatalı olup olmadığını kontrol eden,
                                                                                            #Hata yoksa içinde hamle_kontrol,silinecek_var_mi,oyun_alani_yazdir,
    hata = ""                                                                               #oyun_bitti_mi fonksiyonlarını çağıran fonksiyondur.
    hatalar_dict = {"hata1":"Oyun alanında böyle bir konum bulunmamaktadır!",
                    "hata2":"Belirttiğiniz konumda size ait bir taş bulunmamaktadır!",
                    "hata3":"Taşınızı sadece yatay ve dikey olarak hareket ettirebilirsiniz!",  #Hata türlerini tutan sözlük yapısı.
                    "hata4":"Gitmek istediğiniz konumda başka bir taş bulunmaktadır!",
                    "hata5":"Taşınızı götürmek istediğiniz konum ile taşınızın şu anki konumu arasında başka bir taş bulunmamalıdır!"

        }
    while(True):
        try:
            hamle = input(f"Oyuncu {siraKimde}, lütfen hareket ettirmek istediğiniz kendi taşınızın konumunu ve hedef konumu giriniz:")
            if(hamle[1] not in "ABCDEFGH" or int(hamle[0])<1 or int(hamle[0])>len(oyunAlaniListe) or hamle[-1] not in "ABCDEFGH" or int(hamle[-2])<1 or int(hamle[-2])>len(oyunAlaniListe)):
                hata = "hata1"
                raise Exception()
            elif(oyunAlaniListe[int(hamle[0])-1]["ABCDEFGH".index(hamle[1])] != siraKimde): 
                hata = "hata2"
                raise Exception()
            elif(hamle[0]!=hamle[-2] and hamle[1]!=hamle[-1]):
                hata = "hata3"
                raise Exception()
            elif(oyunAlaniListe[int(hamle[-2])-1]["ABCDEFGH".index(hamle[-1])]!=" "):
                hata = "hata4"
                raise Exception()
            elif(hamle_kontrol(hamle,oyunAlaniListe)==True):
                hata = "hata5"
                raise Exception()

            hareketYonu = hamle_kontrol(hamle,oyunAlaniListe)

            oyunAlaniListe[int(hamle[-2])-1]["ABCDEFGH".index(hamle[-1])] = siraKimde
            oyunAlaniListe[int(hamle[0])-1]["ABCDEFGH".index(hamle[1])] = " "
            
            oyunAlaniListe,silinenKonumlar = silinecek_var_mi(hamle,oyunAlaniListe,hareketYonu,siraKimde)

            oyun_alani_yazdir(oyunAlaniListe)

            for i in silinenKonumlar:
                print(f"{i} Konumundaki taş kilitlendi ve dışarı çıkarıldı.")
            if(siraKimde == oyuncu_1):
                siraKimde = oyuncu_2
            else:
                siraKimde = oyuncu_1
            if(oyun_bitti_mi(oyunAlaniListe,oyuncu_1,oyuncu_2)):
                break
        except:
            if(hata!=""):
                print(hatalar_dict[hata])
            else:print("Girilen veri hatalıdır!")

def hamle_kontrol(hamle,oyunAlaniListe):                     #Girilen hamlenin yapılabilirliğini kontrol eden, eğer yapılabilirse hareket yönünü döndüren fonksiyon.
    
    if(hamle[0]==hamle[-2]):
        if("ABCDEFGH".index(hamle[1])<"ABCDEFGH".index(hamle[-1])):
            for i in range("ABCDEFGH".index(hamle[1])+1,"ABCDEFGH".index(hamle[-1])):
                if(oyunAlaniListe[int(hamle[0])-1][i]!=" "):
                    return True
            return "saga"

        else:
            for i in range("ABCDEFGH".index(hamle[1])-1,"ABCDEFGH".index(hamle[-1])-1,-1):
                if(oyunAlaniListe[int(hamle[0])-1][i]!=" "):
                    return True
            return "sola"

    elif("ABCDEFGH".index(hamle[1])=="ABCDEFGH".index(hamle[-1])):
        if(hamle[0]<hamle[-2]):
            for i in range (int(hamle[0]),int(hamle[-2])):
                if(oyunAlaniListe[i]["ABCDEFGH".index(hamle[1])]!=" "):
                    return True
            return "asagi"
        else:
            for i in range((int(hamle[0])-1),int(int(hamle[-2])-1)):
                if(oyunAlaniListe[i]["ABCDEFGH".index(hamle[1])]!=" "):
                    return True
            return "yukari"

def silinecek_var_mi(hamle,oyunAlaniListe,hareketYonu,siraKimde):              #Yapılan hamle sonrasında hareket yönüne göre silinecek taş varsa silen fonksiyon.
    silinenKonumlar = []            #Silinen konum varsa ekrana basmak için silinen konumları tutan liste.
    if(hareketYonu == "saga"):
        oyunAlaniListe,silinenKonumlar = kontrol_sag(oyunAlaniListe,hamle,siraKimde,silinenKonumlar)
        oyunAlaniListe,silinenKonumlar = kontrol_yukari(oyunAlaniListe,hamle,siraKimde,silinenKonumlar)
        oyunAlaniListe,silinenKonumlar = kontrol_asagi(oyunAlaniListe,hamle,siraKimde,silinenKonumlar)
        oyunAlaniListe,silinenKonumlar = sag_ust_kose(oyunAlaniListe,hamle,siraKimde,silinenKonumlar)
        oyunAlaniListe,silinenKonumlar = sag_alt_kose(oyunAlaniListe,hamle,siraKimde,silinenKonumlar)

    elif(hareketYonu == "sola"):
        oyunAlaniListe,silinenKonumlar = kontrol_sol(oyunAlaniListe,hamle,siraKimde,silinenKonumlar)
        oyunAlaniListe,silinenKonumlar = kontrol_yukari(oyunAlaniListe,hamle,siraKimde,silinenKonumlar)
        oyunAlaniListe,silinenKonumlar = kontrol_asagi(oyunAlaniListe,hamle,siraKimde,silinenKonumlar)
        oyunAlaniListe,silinenKonumlar = sol_ust_kose(oyunAlaniListe,hamle,siraKimde,silinenKonumlar)
        oyunAlaniListe,silinenKonumlar = sol_alt_kose(oyunAlaniListe,hamle,siraKimde,silinenKonumlar)

    elif(hareketYonu == "yukari"):
        oyunAlaniListe,silinenKonumlar = kontrol_sag(oyunAlaniListe,hamle,siraKimde,silinenKonumlar)
        oyunAlaniListe,silinenKonumlar = kontrol_sol(oyunAlaniListe,hamle,siraKimde,silinenKonumlar)
        oyunAlaniListe,silinenKonumlar = kontrol_yukari(oyunAlaniListe,hamle,siraKimde,silinenKonumlar)
        oyunAlaniListe,silinenKonumlar = sag_ust_kose(oyunAlaniListe,hamle,siraKimde,silinenKonumlar)
        oyunAlaniListe,silinenKonumlar = sol_ust_kose(oyunAlaniListe,hamle,siraKimde,silinenKonumlar)

    elif(hareketYonu == "asagi"):
        oyunAlaniListe,silinenKonumlar = kontrol_sag(oyunAlaniListe,hamle,siraKimde,silinenKonumlar)
        oyunAlaniListe,silinenKonumlar = kontrol_sol(oyunAlaniListe,hamle,siraKimde,silinenKonumlar)
        oyunAlaniListe,silinenKonumlar = kontrol_asagi(oyunAlaniListe,hamle,siraKimde,silinenKonumlar)
        oyunAlaniListe,silinenKonumlar = sag_alt_kose(oyunAlaniListe,hamle,siraKimde,silinenKonumlar)
        oyunAlaniListe,silinenKonumlar = sol_alt_kose(oyunAlaniListe,hamle,siraKimde,silinenKonumlar)

    return oyunAlaniListe,silinenKonumlar

def kontrol_sag(oyunAlaniListe,hamle,siraKimde,silinenKonumlar):           #Taşın sağ tarafında silinecek taş var mı kontrol eden, varsa silen fonksiyon.

    if("ABCDEFGH".index(hamle[-1])<len(oyunAlaniListe)-2):
            if(oyunAlaniListe[int(hamle[-2])-1]["ABCDEFGH".index(hamle[-1])+1] not in (siraKimde+" ") and oyunAlaniListe[int(hamle[-2])-1]["ABCDEFGH".index(hamle[-1])+2]==siraKimde):
                silinenKonumlar.append(hamle[-2]+"ABCDEFGH"["ABCDEFGH".index(hamle[-1])+1])
                oyunAlaniListe[int(hamle[-2])-1]["ABCDEFGH".index(hamle[-1])+1] = " "
    return oyunAlaniListe,silinenKonumlar


def kontrol_sol(oyunAlaniListe,hamle,siraKimde,silinenKonumlar):           #Taşın sol tarafında silinecek taş var mı kontrol eden, varsa silen fonksiyon.

    if("ABCDEFGH".index(hamle[-1])>1):
            if(oyunAlaniListe[int(hamle[-2])-1]["ABCDEFGH".index(hamle[-1])-1] not in (siraKimde+" ") and oyunAlaniListe[int(hamle[-2])-1]["ABCDEFGH".index(hamle[-1])-2]==siraKimde):
                silinenKonumlar.append(hamle[-2]+"ABCDEFGH"["ABCDEFGH".index(hamle[-1])-1])
                oyunAlaniListe[int(hamle[-2])-1]["ABCDEFGH".index(hamle[-1])-1] = " "
    return oyunAlaniListe,silinenKonumlar

def kontrol_yukari(oyunAlaniListe,hamle,siraKimde,silinenKonumlar):         #Taşın yukarısında silinecek taş var mı kontrol eden, varsa silen fonksiyon.

    if(int(hamle[-2])>2):
            if(oyunAlaniListe[int(hamle[-2])-2]["ABCDEFGH".index(hamle[-1])] not in (siraKimde+" ") and oyunAlaniListe[int(hamle[-2])-3]["ABCDEFGH".index(hamle[-1])]== siraKimde):
                silinenKonumlar.append(str(int(hamle[-2])-1)+hamle[-1])
                oyunAlaniListe[(int(hamle[-2])-2)]["ABCDEFGH".index(hamle[-1])] = " "
    return oyunAlaniListe,silinenKonumlar

def kontrol_asagi(oyunAlaniListe,hamle,siraKimde,silinenKonumlar):          #Taşın aşağısında silinecek taş var mı kontrol eden, varsa silen fonksiyon.

    if(int(hamle[-2])<len(oyunAlaniListe)-1):
            if(oyunAlaniListe[int(hamle[-2])]["ABCDEFGH".index(hamle[-1])] not in (siraKimde+" ") and oyunAlaniListe[int(hamle[-2])+1]["ABCDEFGH".index(hamle[-1])]== siraKimde):
                silinenKonumlar.append(str(int(hamle[-2])+1)+hamle[-1])
                oyunAlaniListe[(int(hamle[-2]))]["ABCDEFGH".index(hamle[-1])] = " "
    return oyunAlaniListe,silinenKonumlar

def sag_ust_kose(oyunAlaniListe,hamle,siraKimde,silinenKonumlar):           #Oyun alanının sağ üst köşesindeki taşın silinmesini kontrol eden fonksiyon.

    if(int(hamle[-2])==1 and "ABCDEFGH".index(hamle[-1])==len(oyunAlaniListe)-2):
        if(oyunAlaniListe[1][len(oyunAlaniListe)-1]==siraKimde and oyunAlaniListe[0][len(oyunAlaniListe)-1] not in (siraKimde+" ")):
            oyunAlaniListe[0][len(oyunAlaniListe)-1] = " "
            silinenKonumlar.append("1"+"ABCDEFGH"[len(oyunAlaniListe)-1])

    elif(int(hamle[-2])==2 and "ABCDEFGH".index(hamle[-1])==len(oyunAlaniListe)-1):
        if(oyunAlaniListe[0][len(oyunAlaniListe)-2]==siraKimde and oyunAlaniListe[0][len(oyunAlaniListe)-1] not in (siraKimde+" ")):
            oyunAlaniListe[0][len(oyunAlaniListe)-1] = " "
            silinenKonumlar.append("1"+"ABCDEFGH"[len(oyunAlaniListe)-1])
    return oyunAlaniListe,silinenKonumlar


def sol_ust_kose(oyunAlaniListe,hamle,siraKimde,silinenKonumlar):           #Oyun alanının sol üst köşesindeki taşın silinmesini kontrol eden fonksiyon.

    if(int(hamle[-2])==1 and "ABCDEFGH".index(hamle[-1])==1):
        if(oyunAlaniListe[1][0]==siraKimde and oyunAlaniListe[0][0] not in (siraKimde+" ")):
            oyunAlaniListe[0][0] = " "
            silinenKonumlar.append("1A")

    elif(int(hamle[-2])==2 and "ABCDEFGH".index(hamle[-1])==0):
        if(oyunAlaniListe[0][1]==siraKimde and oyunAlaniListe[0][0] not in (siraKimde+" ")):
            oyunAlaniListe[0][0] = " "
            silinenKonumlar.append("1A")
    return oyunAlaniListe,silinenKonumlar

def sag_alt_kose(oyunAlaniListe,hamle,siraKimde,silinenKonumlar):           #Oyun alanının sağ alt köşesindeki taşın silinmesini kontrol eden fonksiyon.

    if(int(hamle[-2])==len(oyunAlaniListe)-1 and "ABCDEFGH".index(hamle[-1])==len(oyunAlaniListe)-1):
        if(oyunAlaniListe[len(oyunAlaniListe)-1][len(oyunAlaniListe)-2]==siraKimde and oyunAlaniListe[len(oyunAlaniListe)-1][len(oyunAlaniListe)-1] not in (siraKimde+" ")):
            oyunAlaniListe[len(oyunAlaniListe)-1][len(oyunAlaniListe)-1] = " "
            silinenKonumlar.append(str(len(oyunAlaniListe))+"ABCDEFGH"[len(oyunAlaniListe)-1])

    elif(int(hamle[-2])==len(oyunAlaniListe) and "ABCDEFGH".index(hamle[-1])==len(oyunAlaniListe)-2):
        if(oyunAlaniListe[len(oyunAlaniListe)-2][len(oyunAlaniListe)-1]==siraKimde and oyunAlaniListe[len(oyunAlaniListe)-1][len(oyunAlaniListe)-1] not in (siraKimde+" ")):
            oyunAlaniListe[len(oyunAlaniListe)-1][len(oyunAlaniListe)-1] = " "
            silinenKonumlar.append(str(len(oyunAlaniListe))+"ABCDEFGH"[len(oyunAlaniListe)-1])
    return oyunAlaniListe,silinenKonumlar

def sol_alt_kose(oyunAlaniListe,hamle,siraKimde,silinenKonumlar):           #Oyun alanının sol alt köşesindeki taşın silinmesini kontrol eden fonksiyon.

    if(int(hamle[-2])==len(oyunAlaniListe)-1 and "ABCDEFGH".index(hamle[-1])==0):
        if(oyunAlaniListe[len(oyunAlaniListe)-1][1]==siraKimde and oyunAlaniListe[len(oyunAlaniListe)-1][0] not in (siraKimde+" ")):
            oyunAlaniListe[len(oyunAlaniListe)-1][0] = " "
            silinenKonumlar.append(str(len(oyunAlaniListe))+"A")

    elif(int(hamle[-2])==len(oyunAlaniListe) and "ABCDEFGH".index(hamle[-1])==1):
        if(oyunAlaniListe[len(oyunAlaniListe)-2][0]==siraKimde and oyunAlaniListe[len(oyunAlaniListe)-1][0] not in (siraKimde+" ")):
            oyunAlaniListe[len(oyunAlaniListe)-1][0] = " "
            silinenKonumlar.append(str(len(oyunAlaniListe))+"A")
    return oyunAlaniListe,silinenKonumlar

def oyun_bitti_mi(oyunAlaniListe,oyuncu_1,oyuncu_2):                        #Oyunun bitip bitmediğini kontrol eden, bittiyse kazananı ekrana basan fonksiyon.

    if(sum(satir.count(oyuncu_1) for satir in oyunAlaniListe)==1):
        print(f"Oyuncu {oyuncu_2} oyunu kazandı.")
        return True
    
    elif(sum(satir.count(oyuncu_2) for satir in oyunAlaniListe)==1):
        print(f"Oyuncu {oyuncu_1} oyunu kazandı.")
        return True
    else:
        return False



oyunu_baslat()

