from ultralytics import YOLO

#model, YOLO sınıfından üretilen bir nesnedir.
model = YOLO("yolov8n.pt") 

#conf=0.5 ifadesi Model, gördüğü şeyin o nesne olduğundan en az 
#%50 (0.5) oranında emin olsun; eğer %50'den daha az eminse o kutuyu hiç gösterme demek.

print("Düşük güven eşiği (conf=0.2) ile çalıştırılıyor...")
sonuclar_dusuk = model("../../veri/deneme.jpg", conf=0.2)
for sonuc in sonuclar_dusuk:
    sonuc.show()

print("Yüksek güven eşiği (conf=0.85) ile çalıştırılıyor...")
sonuclar_yuksek = model("../../veri/deneme.jpg", conf=0.85)
for sonuc in sonuclar_yuksek:
    sonuc.show()
