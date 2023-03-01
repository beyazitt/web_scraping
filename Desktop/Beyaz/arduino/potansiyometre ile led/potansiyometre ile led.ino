#define led 3
#define pot A0

void setup() {


}

void loop() {
  int deger = analogRead(pot);
  deger = deger/4;
  analogWrite(led,deger);
//deger = map(deger,0,1023,0,255);

}
