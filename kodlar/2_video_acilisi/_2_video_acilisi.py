import cv2
#import os

#print("Şuan ki Çalışma Dizini: ", os.getcwd())
#C:\Users\Şevval\Desktop\goruntu_isleme_gorev\kodlar\2_video_acilisi olduğundan 2 kere üste çıkıyoruz.

video = cv2.VideoCapture("../../veri/deneme_1.mp4")

if not video.isOpened():
    print("HATA: Video dosyası bulunamadı!")
else:
    print("Video başarıyla bulundu, oynatılıyor...")


#Videolar art arda gelen fotoğraflar olduğundan sonsuz döngü başlat
while True:
    #video.read(): Videodaki sıradaki tek bir fotoğrafı alır 
    #ve bize iki şey verir:
    okundu_mu, fotograf = video.read()

    if not okundu_mu:
        print("Video sonlandı veya okunamadı.")
        break

    cv2.imshow("Video Testi", fotograf)

    #Videonun akıcı olması için yaklaşık 40 FPS hızında oynar.
    #İşletim sistemi veya NumLock farklılıklarını yoksayıp basılan tuşun 
    #ASCII değerini doğru okumak için 8-bit (0xFF) maskelemesi yaptık.
    if cv2.waitKey(25) & 0xFF == ord('q'):
        print("Kullanıcı videoyu durdurdu.")
        break

#video.release(): Videoyu hafızadan (RAM) temizler ve işletim sistemine 
#videoyla işimizin bittiğini, serbest ırakabileceğini söyler.
video.release()
cv2.destroyAllWindows()