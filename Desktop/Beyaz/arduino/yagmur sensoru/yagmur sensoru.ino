int esikDegeri = 800;

int buzzerpin = 7;

int veri;

void setup() {
  Serial.begin(9600);
  pinMode(8,OUTPUT);
  pinMode(7, OUTPUT);

}

void loop() {
  Serial.print("Analog Cikis:");
  Serial.println(analogRead(A0));
  veri = analogRead(A0);
  Serial.print("Digital Cikis:");
  Serial.println(digitalRead(7));
  delay(100);
  if(veri < esikDegeri){
    digitalWrite(buzzerpin,HIGH);
    delay(100);
    digitalWrite(buzzerpin,LOW);
    delay(100);
  }
  else{
    digitalWrite(A0,LOW);
  }

}
