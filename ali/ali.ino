// Pin Tanımlamaları
const int PIN_SIGNAL = A0;   // Sinyal gücü potansiyometresi
const int PIN_JAMMER = 2;    // Jammer tehdit butonu (Logic State)

const int LED_GENIS_BANT = 5; // Yeşil
const int LED_DAR_BANT = 6;   // Sarı
const int LED_ACIL_BANT = 7;  // Kırmızı

// Önceki değerleri tutacağımız değişkenler
int sonSinyal = -1;
int sonJammer = -1;

void setup() {
  Serial.begin(9600);
  pinMode(PIN_JAMMER, INPUT);
  
  pinMode(LED_GENIS_BANT, OUTPUT);
  pinMode(LED_DAR_BANT, OUTPUT);
  pinMode(LED_ACIL_BANT, OUTPUT);
}

void loop() {
  // 1. Verileri Oku
  int hamSinyal = analogRead(PIN_SIGNAL); // 0-1023 arası değer döner
  int sinyalYuzdesi = map(hamSinyal, 0, 1023, 0, 100); // 0-100 yüzdesine çevir
  int jammerDurumu = digitalRead(PIN_JAMMER); // 0 veya 1

  // 2. Sinyalde %3'ten fazla değişim veya Jammer tetiklemesi varsa veri gönder
  if (abs(sinyalYuzdesi - sonSinyal) >= 3 || jammerDurumu != sonJammer) {
    // Format: Sinyal,Jammer (Örn: 75,0)
    Serial.print(sinyalYuzdesi);
    Serial.print(",");
    Serial.println(jammerDurumu);

    sonSinyal = sinyalYuzdesi;
    sonJammer = jammerDurumu;
    delay(50); // Debounce
  }

  // 3. Python'dan Gelen Kararı Dinle ve Uygula
  if (Serial.available() > 0) {
    delay(10);
    char gelenEmir = Serial.read();

    digitalWrite(LED_GENIS_BANT, LOW);
    digitalWrite(LED_DAR_BANT, LOW);
    digitalWrite(LED_ACIL_BANT, LOW);

    if (gelenEmir == 'A') {
      digitalWrite(LED_GENIS_BANT, HIGH);
    } else if (gelenEmir == 'B') {
      digitalWrite(LED_DAR_BANT, HIGH);
    } else if (gelenEmir == 'C') {
      digitalWrite(LED_ACIL_BANT, HIGH);
    }
  }
}