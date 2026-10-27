import cv2
#import os:Python programlama dilinde yerleşik olarak bulunan ve işletim sistemiyle (Operating System) 
#doğrudan etkileşime girmeyi sağlayan os modülünü projeye dahil eden komuttur.

# Kodun o anda nerede çalıştığını öğrenmek için:
#print("Şu anki çalışma dizini:", os.getcwd())

#C:\Users\Şevval\Desktop\goruntu_isleme_gorev\kodlar\1_goruntu_acilisi olduğundan 2 kere üste çıkmalıyız.
resim = cv2.imread("../../veri/deneme.jpg") 

#Eğer OpenCV resim değişkenini boş bırakmışsa,
if resim is None:
    print("HATA: Resim bulunamadı!")
#Eğer resim başarıyla okunup belleğe alındıysa,
else:
    print("Resim başarıyla yüklendi!")
    cv2.imshow("Test Goruntusu", resim)
    cv2.waitKey(0)
    cv2.destroyAllWindows()