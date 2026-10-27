import json
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

sonuclar = model("../../veri/deneme_1.mp4", stream=True)

# Tespit edilen tüm verileri biriktirmek için boş bir liste 
tum_veriler = []

# Her bir kareyi döngüye sokuyoruz
for kare_no, sonuc in enumerate(sonuclar):
    
    kutular = sonuc.boxes
    
    for kutu in kutular:
        sinif_id = int(kutu.cls[0])
        sinif_adi = model.names[sinif_id]
        guven = float(kutu.conf[0])
        kutu_koordinati = kutu.xyxy[0].tolist()
        
        # Her bir nesnenin bilgilerini bir Python sözlüğünde (dictionary) topluyoruz
        veri_sozlugu = {
            "kare_no": kare_no,
            "zaman_sn": round(kare_no / 30.0, 2),
            "sinif": sinif_adi,
            "guven": round(guven, 2), # Virgülden sonra 2 basamak yapar
            "kutu": kutu_koordinati
        }
        
        tum_veriler.append(veri_sozlugu)
    
    if kare_no > 5:
        break

#Toplanan tüm verileri bilgisayara "tespit_sonuclari.json" dosyası olarak kaydediyoruz
#with open(...) as dosya:: Python'da dosya açma/oluşturma komutudur. İşlem bitince dosyayı otomatik olarak güvenli bir şekilde kapatır.
with open("tespit_sonuclari.json", "w", encoding="utf-8") as dosya:
    # json.dump() fonksiyonu Python listesini JSON formatına çevirip dosyaya yazar
    # ensure_ascii=False Türkçe karakterler bozulmasın diye, indent=4 ise güzel görünsün diye alt alta indent verir
    json.dump(tum_veriler, dosya, ensure_ascii=False, indent=4)

print("İşlem tamam! Veriler JSON dosyasına başarıyla kaydedildi.")

# --- MODEL PERFORMANS DEĞERLENDİRME NOTU ---
# Videonun ilk 7 karesi (Kare 0 - Kare 6 arası) manuel olarak incelendi
# - Toplam Tespit Sayısı: 14 (Her karede 2 tespit)
# - Doğru Tespit (True Positive): 7 adet -> Kedi (cat) tespitlerinin tamamı doğru (7/7 doğru, %75-%87 güven).
# - Yanlış Tespit (False Positive): 7 adet -> Kase (bowl) tespitlerinin tamamı yanlış (7/7 yanlış). 
#   Videoda gerçekte kase olmamasına rağmen model düşük güven skorlarıyla (%37-%54) yanlış alarm üretmiştir.
# - Çözüm: Güven eşiği conf=0.6 yapılarak bu 7 yanlış tespit tamamen filtrelenebilir.