const int soldugme = 2, sagdugme = 3, yesilled = 4, kirmiziled = 5, motor = 6;
int ayar = 0;


void setup() {
  pinMode(soldugme,INPUT);
  pinMode(sagdugme,INPUT);
  pinMode(kirmiziled,OUTPUT);
  pinMode(yesilled,OUTPUT);
  pinMode(motor,OUTPUT);

}

void loop() {
  ayar = map(analogRead(A0),0,1023,0,255);
  if(digitalRead(soldugme) == false && digitalRead(sagdugme) == false){
    analogWrite(motor,ayar);
    digitalWrite(yesilled,LOW);
    digitalWrite(kirmiziled,LOW);
    analogWrite(kirmiziled,ayar);
    
  }
  else{
    while(digitalRead(soldugme) == true && digitalRead(sagdugme) == false){
      analogWrite(motor,128);
      digitalWrite(yesilled,HIGH);
      digitalWrite(kirmiziled,LOW);

    }
    while(digitalRead(soldugme) == false && digitalRead(sagdugme) == true){
      analogWrite(motor,255);
      digitalWrite(yesilled,LOW);
      digitalWrite(kirmiziled,HIGH);

    }




    
  }
}
