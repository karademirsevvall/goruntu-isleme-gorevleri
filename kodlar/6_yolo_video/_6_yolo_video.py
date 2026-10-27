from ultralytics import YOLO

model = YOLO("yolov8n.pt")


#show=True -> Videoyu arka planda sessiz sedasız işleyip bitmesini bekletme; 
#videonun her bir karesini (frame) işlerken anlık olarak ekranda bir 
#pencere aç ve tespit ettiğin kutucukları canlı canlı, oynatıcı gibi göster.

print("Video düşük güven eşiği (conf=0.2) ile oynatılıyor...")
sonuclar_dusuk = model("../../veri/deneme_1.mp4", show=True, conf=0.2)

print("Video yüksek güven eşiği (conf=0.85) ile oynatılıyor...")
sonuclar_yuksek = model("../../veri/deneme_1.mp4", show=True, conf=0.85)

