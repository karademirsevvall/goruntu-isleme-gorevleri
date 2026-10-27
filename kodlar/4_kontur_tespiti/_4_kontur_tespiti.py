import cv2

resim = cv2.imread("../../veri/deneme.jpg")

if resim is not None:
    gri_resim = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)

    _, thres = cv2.threshold(gri_resim, 127, 255, cv2.THRESH_BINARY)


    #Parametreler: findContours(kaynak resim, en dıştaki konturlar, sadece köşeler)
    #cv2.RETR_EXTERNAL: Sadece en dıştaki konturları alır.
    # cv2.CHAIN_APPROX_SIMPLE: Konturun sadece uç noktalarını (köşe) saklayarak hafıza tasarrufu yapar.
    konturler, hiyerarsi = cv2.findContours(thres, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #len() fonksiyonu bir listenin içinde kaç eleman olduğnu sayar.
    print(f"Bulunan toplam nesne/kontur sayısı: {len(konturler)}")

    #.copy():Orijinal resmi korumak ve ana veriyi kirletmemek için hafızada birebir aynı 
    #özelliklere sahip bağımsız bir ikiz kopya oluşturur.
    kontur_cizilmis = resim.copy()
    #-1 parametresi tüm konturları çizer, (0, 255, 0) yeşil renk, 2 ise çizgi kalınlığıdır.
    cv2.drawContours(kontur_cizilmis, konturler , -1, (0, 255, 0), 2)

    for i, kontur in enumerate(konturler):
        alan = cv2.contourArea(kontur)
        cevre = cv2.arcLength(kontur, True)
        
        if alan > 500:
            print(f"Kontur {i} -> Alan: {alan:.1f}, Çevre: {cevre:.1f}")
            
            #1. Sınırlayıcı kutunun koordinatlarını alıyoruz (x, y, genişlik, yükseklik)
            x, y, w, h = cv2.boundingRect(kontur)
            
            # (255, 0, 0) -> BGR formatında Mavi renk, 2 -> Çizgi kalınlığı
            cv2.rectangle(kontur_cizilmis, (x, y), (x + w, y + h), (255, 0, 0), 2)
            
    cv2.imshow("Orijinal Resim", resim)
    cv2.imshow("Esiklenmis Resim", thres)
    cv2.imshow("Kontur Cizilmis Resim", kontur_cizilmis)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("HATA: Resim Bulunamadi!")

    
