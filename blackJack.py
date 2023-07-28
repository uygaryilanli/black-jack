############### Blackjack Project #####################

#Burada bilgisayarın rasgele seçim yapabilmesi için random modülünü ardından ise art.py dosyasındaki logo isimli değişkeni bu dosyaya çağırabilmek için
#logo yu import ediyoruz.
import random
from art import logo

#Burada oyuncu ve bilgisayarın skorlarının yazdırılması için 2 adet boş liste oluşturduk.
user_score = []
computer_score = []


def card_list():
    """Kart listesi içerisinden ratgele kart seçmeye yarayan fonksiyon."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card


def our_card():
    """Oyuncu için rastgele kart seçen fonksiyon."""
    your_card = card_list()
    return your_card


def computer_card():
    """Bilgisayar için rastgele kart seçen fonksiyon."""
    computer_card = card_list()
    return computer_card


def game():
    """Oyun başlangıcında listeleri temizleyip hem oyuncunun hemde bilgisayarın kart seçimlerini yapıp skor listelerine ekleyen fonkiyon."""
    #OYUNU TAMAMEN KAPATMADAN ANAMENÜDEN TEKRARDAN BAŞLATTIĞIMIZDA LİSTELER SIFIRLANSIN DİYE BUNLARI BAŞA EKLEDİK.
    user_score.clear()
    computer_score.clear()
    #BİLGİSAYARIN KART SEÇMESİ ARDINDAN SEÇTİĞİ KARTI SKOR LİSTESİNE EKLEMESİNİ SAĞLADIK.
    computer_queqe1 = computer_card()
    computer_score.append(computer_queqe1)
    #OYUNCUNUN KART SEÇMESİ ARDINDAN SEÇTİĞİ KARTI SKOR LİSTESİNE EKLEMESİNİ SAĞLADIK.
    your_queqe1 = computer_card()
    user_score.append(your_queqe1)
    #BU İŞLEMLER SONUCUNDA HEM BİLGİSAYARIN HEMDE OYUNCUNUN SKORLARINI YAZDIRDIK
    print(f"Computer Score is {computer_score[0]}")
    print(f"Your score is {user_score[0]}")
    #Skorlar açıklandıktan sonra bir input ile oyuncuya kart çekicekmisin sorusunu soran döngüyü yazdık.
    while True:
        #Kart çekicekmisin sorusu.
        getCard = input("Press d to draw card, or s to stop: ")
        #Eğer oyuncu kartı çek derse önce rastgele sayı seçilir, ardından seçilen sayı yazdırılır ardından o sayı oyuncunun listesine yazdırılır
        #sonrasında listedeki sayılar toplanır, en sonunda ise toplam skor ekrana yazdırılır.  
        if getCard == "d":
            your_queqe2 = computer_card()
            print(f"Drawn card is {your_queqe2}")
            #Eğer oyuncunun çektiği kart 11 (As) ise ve toplam skor 21'i aşıyorsa, oyuncuya 1 veya 11 seçeneği sunuyoruz.
            if your_queqe2 == 11 and sum(user_score) + your_queqe2 > 21:
                #Burada oyuncuya 1 veya 11 seçeneğinden birini seçmesini söylüyoruz.
                ace_choice = int(input("You drew an ace (11). Choose 1 or 11: "))
                #Burada oyuncu eğer input a 1 veya 11 değerleri dışında bir bilgi girerse ona 1 veya 11 sayılarından birini seçmesini söylüyoruz.(1 veya 11 seçene kadar!)
                while ace_choice not in [1, 11]:
                    ace_choice = int(input("Invalid choice. Please choose 1 or 11: "))
                #Burada ace_choice değişkenine ait inputtan aldığımız bilgiyi your_queqe2 değişkenine eşitliyoruzki 2 farklı sayı değeri listeye girilmesin.
                your_queqe2 = ace_choice
            #Burada user_score isimli listemize az önce aldığımız sayıyı ekliyoruz.
            user_score.append(your_queqe2)
            #buradada listemizdeki sayıların toplamını alıp yazdırıyoruz.
            add_score = sum(user_score)
            print(f"Your score is **{add_score}**")
            #Burada oyuncunun toplam skoru 21 den fazla olursa skoru ve ardından bilgisayarın kazandığı ekrana yazdırılır en sonundada oyun kapatılır.
            if add_score > 21:
                print(f"Boom! You lose with {add_score} score.")
                print(f"Computer wins with {sum(computer_score)} score.")
                exit()
        #Burada eğer dur dersek döngüden çıkıyoruz.
        elif getCard == "s":
            break
        #Burada s veya d dışında birşey yazarsak bize hata olduğunu d veya s harflerini girmemizi söylüyor.
        else:
            print("Invalid input. Please enter 'd' or 's'.")
    #Burada bilgisayarın çektiği numaraların toplamının 17 den küçük olduğu taktirde tekrardan numara seçip onu bilgisayarın skor listesine ekliyoruz.
    while sum(computer_score) < 17:
        computer_queqe3 = computer_card()
        computer_score.append(computer_queqe3)
    #Burada hem bilgisayarın hemde oyuncunun skor listesindeki sayıları topluyoruz.
    computer_sum = sum(computer_score)
    user_sum = sum(user_score)
    #Burada bilgisayarın ve oyuncunun skorlarını ekrana yazdırıyoruz.
    print(f"Computer score is {computer_sum} and user score is {user_sum}.")
    #Burada bilgisayarın skorunun toplamı 21 den büyük veya (21 den küçük eşit ve oyuncunun skor toplamı bilgisayarın skor toplamından büyükse) oyuncunun
    #oyunu kazandığını ekrana yazdırıyoruz.
    if computer_sum > 21 or (user_sum <= 21 and user_sum > computer_sum):
        print("You win the game!")
    #Burada oyuncu ve bilgisayarın skor toplamları birbirine eşitse durumun berabere olduğunu yazdırıyoruz.
    elif user_sum == computer_sum:
        print("The game is a draw!")
    #Burada oyuncu kazanamamış ve durumda berabere değil ise oyuncunun kaybettiğini yazdırıyoruz.
    else:
        print("You lose the game!")






#Burası oyunun ana döngüsü
while True:
    #Burada önce oyun için hazırlanan logoyu ardından oyuna hoşgeldin yazısını yazdırıyoruz.
    print(logo)
    print("********************Welcome to Black Jack!********************")
    #Burada oyuncunun seçmesi için input ile 2 ayrı seçenek oluşturuyoruz bu seçenekler ise oyunu oyna ve oyundan çıkış yap seçenekleri.
    menu = int(input("1-Play Game\n2-Exit Game\nChoose One: "))
    #Burada eğer 1 dersek oyuncuyu oyun alanına gönderen döngüye geçiş yaptırıyoruz.
    if menu == 1:
        while True:
            print("********************GAME AREA********************")
            #Burada oyuncuya kart çekmesini yada anamenüye dönmesini sağlayan 2 ayrı seçenek veriyoruz.
            playOrExit = int(input("1-Deal the cards\n2-Return Main Menu\nChoose One: "))
            #Burada eğer oyuncu 1 nolu işlemi girerse game isimli oyun fonksiyonumuzu çağırıyoruz.
            if playOrExit == 1:
                game()
            #Burada oyuncu eğer 2 nolu işlemi girerse onu döngüden çıkartıp anamenüye geri gönderiyoruz.
            elif playOrExit == 2:
                print("Returning to main menu...")
                break
            #Burada oyuncu 1 veya 2 nolu işlemlerden birini değilde farklı bir rakam girerse ona 1 veya 2 nolu işlemlerden birini girmesini söylüyoruz.
            else:
                print("Please choose 1 or 2!")
    #Burada eğer 2 dersek oyuncuya oyundan çıkıldığını söyleyip veda edip oyunu kapatıyoruz.
    elif menu == 2:
        print("Exit from game!")
        print("GOOD BYE...")
        break
    #Burada oyuncu 1 veya 2 nolu işlemlerden birini değilde farklı bir rakam girerse ona 1 veya 2 nolu işlemlerden birini girmesini söylüyoruz. 
    else:
        print("Please choose 1 or 2!")







