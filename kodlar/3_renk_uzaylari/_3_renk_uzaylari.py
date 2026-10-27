import cv2

resim = cv2.imread("../../veri/deneme.jpg")

if resim is not None:

    #3 kanallı (renkli) BGR görüntüyü tek kanallı (gri tonlamalı)
    #formata indirgemek:
    gri_resim = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)

    #Görüntünün BGR uzayından HSV uzayına taşınması:
    hsv_resim = cv2.cvtColor(resim, cv2.COLOR_BGR2HSV)

    #Parametreler:(Gri resim, eşik sınırı, maksimum değer, eşik türü)
    #cv2.thereshold() fonskiyonu her zaman dışarıya kesin 2 değer verir.
    #1.olarak eşik değeri (retval), 2. olarak işlenmiş resim matrisi.
    #_ koyarak döndürülen birinci değeri hafızada tutmayacağımızı söyleriz.
    _, basit_esiklenmis_resim = cv2.threshold(gri_resim, 127, 255, cv2.THRESH_BINARY)

    #adaptiveThreshold fosnkiyonu işlenmiş görüntüyü tek değer olarak verir.
    #Parametreler(üzerinde işlem yapılacak görüntü, sınırı geçen piksellere verilecek maksimum değer,
    #                                                        Eşik değerini yerel komşuların ortalamasını alarak hesaplama yöntemi,
    #                                                        Sınırı aşanı beyaz, aşmayanı siyah yapma kuralı (İkili eşikleme türü),
    #                                                        Pikselin etrafında taranacak yerel komşu blok boyutu (mutlaka tek sayı olmalı)
    #                                                        Hesaplanan ortalamadan çıkarılacak hassasiyet sabiti     )
    adaptif_esiklenmis_resim = cv2.adaptiveThreshold(gri_resim, 255, 
                                                     cv2.ADAPTIVE_THRESH_MEAN_C,
                                                     cv2.THRESH_BINARY,
                                                     11, 2)

    #Canny Kenar Bulma:
    #Parametreler(kaynak rresim, alt eşik değer, üst eşik değer)
    kenar_bulma = cv2.Canny(gri_resim, 100, 200)
    cv2.imshow("Orijinal BGR Resim", resim)
    cv2.imshow("Gri Tonlu Resim", gri_resim)
    cv2.imshow("HSV", hsv_resim)
    cv2.imshow("Esiklenmis Resim", basit_esiklenmis_resim)
    cv2.imshow("Adaptif Esiklenmis Resim", adaptif_esiklenmis_resim)
    cv2.imshow("Canny Kenar Bulma", kenar_bulma)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("HATA: Resim Bulunamadi!")