import serial
import time
import traceback

PORT = 'COM2'
BAUD_RATE = 9600

try:
    try:
        ser = serial.Serial(PORT, BAUD_RATE, timeout=1)
        print(f"[*] Sistem Başlatıldı. {PORT} üzerinden araç telemetrisi dinleniyor...")
        print("[*] Yeni veri bekleniyor...\n")
    except serial.SerialException:
        print(f"[!] HATA: {PORT} açılamadı. Sanal portları kontrol edin.")
        input("Çıkmak için Enter'a basın...")
        exit()

    while True:
        if ser.in_waiting > 0:
            try:
                raw_data = ser.readline().decode('utf-8', errors='ignore').strip()
                
                if not raw_data:
                    continue
                    
                veriler = raw_data.split(',')
                
                if len(veriler) == 2:
                    sinyal_kalitesi = int(veriler[0])
                    jammer_durumu = veriler[1]
                    
                    print(f"\n> ANLIK DURUM: Sinyal Gücü: %{sinyal_kalitesi} | Jammer: {'AKTİF' if jammer_durumu == '1' else 'YOK'}")
                    
                    # KARAR ALGORİTMASI VE AÇIKLANABİLİRLİK LOGLARI
                    
                    # 1. Öncelik: Jammer Tehdidi
                    if jammer_durumu == '1':
                        print("[GÜVENLİK PROTOKOLÜ] Elektronik harp (Jamming) müdahalesi tespit edildi!")
                        print("--> Gerekçe: Veri güvenliği ihlali riski nedeniyle KRİPTOLU ACİL DURUM FREKANSINA geçildi.")
                        ser.write(b'C')
                        
                    # 2. Öncelik: Sinyal Zayıflaması
                    elif sinyal_kalitesi <= 50:
                        print("[PROTOKOL DEĞİŞİKLİĞİ] Ana istasyon sinyali zayıflıyor (<= %50).")
                        print("--> Gerekçe: Bağlantı kopmasını önlemek için video aktarımı durduruldu, DAR BANT (Sadece Telemetri) aktif.")
                        ser.write(b'B')
                        
                    # 3. Öncelik: Optimum Durum
                    else:
                        print("[SİSTEM MESAJI] Haberleşme hatları güçlü ve güvenli.")
                        print("--> Durum: GENİŞ BANT üzerinden Yüksek Çözünürlüklü Video + Telemetri aktarımı devam ediyor.")
                        ser.write(b'A')
                        
                else:
                    print(f"[BOZUK PAKET] Okunamayan veri dizilimi: {raw_data}")
                    
            except ValueError:
                 print(f"[UYARI] Sinyal verisi tam sayıya çevrilemedi: {raw_data}")
            except Exception as e:
                print(f"[UYARI] İşlem hatası: {e}")
                
        time.sleep(0.1)

except Exception as e:
    print("\n[!] BEKLENMEYEN BİR HATA OLUŞTU:")
    traceback.print_exc()
    input("\nPencereyi kapatmak için Enter'a basın...")
