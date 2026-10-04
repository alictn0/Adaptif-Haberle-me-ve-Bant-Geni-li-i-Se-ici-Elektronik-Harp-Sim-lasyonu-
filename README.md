
Bu proje, otonom sistemlerin (İHA, İKA) zorlu çevresel faktörler ve Elektronik Harp (Jamming) tehditleri altında hayatta kalabilmesi için geliştirilmiş **açıklanabilir bir adaptif haberleşme prototipidir**. 

## ⚙️ Sistem Şeması ve Donanım
Potansiyometre (Sinyal Kalitesi) ve Jammer (Bozucu Sinyal) girişlerinin bulunduğu Proteus donanım mimarisi:

<img width="576" height="492" alt="şema" src="https://github.com/user-attachments/assets/9da232a0-2724-4ac0-98eb-831b3f590c41" />

## 🎯 Projenin Amacı
Bir otonom aracın ana istasyon ile olan iletişim kalitesi (RSSI) düştüğünde veya dış kaynaklı bir sinyal boğucu (Jammer) saldırısına uğradığında, sistemin kendi kendine haberleşme protokolünü değiştirmesini sağlamaktır. Sistem aldığı bu hayati kararı "Kara Kutu" mantığıyla gerekçelendirerek terminale yansıtır.

## 🚀 Tehdit Senaryoları ve Karar Mekanizması

### 1. Durum: Normal Operasyon
Sinyal kalitesi %50'nin üzerindedir ve Jammer tehdidi yoktur. Geniş bant video aktarımı aktiftir (Yeşil LED).
![Normal Operasyon](gorseller/durum_1_normal.png)<img width="1600" height="851" alt="yeşil" src="https://github.com/user-attachments/assets/ce57260e-1cba-48f8-ae9f-ad8f7ce0c6a1" />


### 2. Durum: Sinyal Zayıflaması
Araç istasyondan uzaklaştıkça sinyal seviyesi düşer. Sistem dar banda geçer (Sarı LED) ve sadece uçuş telemetrisi iletir.
[Sinyal Zayıflamas](gorseller/durum_2_zayif_sinyal.png)<img width="1600" height="851" alt="sarı" src="https://github.com/user-attachments/assets/2dcd0710-e794-4937-a9d6-b47a404ba419" />


### 3. Durum: Elektronik Harp (Jamming Saldırısı)
Sinyal kalitesi ne olursa olsun dış kaynaklı bir Jammer tespit edildiğinde, sistem derhal UHF Kriptolu frekansa atlar (Kırmızı LED).
![Elektronik Harp Durumu](gorseller/durum_3_jammer_aktif.png)<img width="1600" height="848" alt="kırmızı" src="https://github.com/user-attachments/assets/633eca1d-06ac-4068-8c69-50b48c079ba7" />


## 🛠️ Kurulum ve Test
1. VSPE üzerinden `COM1 <-> COM2` bağlantısını aktifleştirin.
2. Proteus simülasyonunu başlatın (Güç raylarının ayarlandığından emin olun).
3. `Python_Code` dizinindeki algoritmayı çalıştırın.
4. Potansiyometre ile oynayarak sinyal zayıflamasını, D2 butonuna basarak Jammer saldırısını simüle edin.
