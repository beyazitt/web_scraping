#define red 9
#define green 10
#define blue 11

#define pot A0

int value_red = 0;
int value_green = 0;
int value_blue = 0;

void setup() {
    
  pinMode(red,OUTPUT);
  pinMode(blue,OUTPUT);
  pinMode(green,OUTPUT);


  Serial.begin(pot);
}

void loop() {
  int value = analogRead(pot);
  value = value/4;
  Serial.println(value);
  if (value > 100){
    value_red = value;
    value_blue = value/2;
    value_green = value/3;
  }
  else{
    value_red = value/2;
    value_blue = value/3;
    value_green = value;
    
  }
  analogWrite(red,value_red);
  analogWrite(blue,value_blue);
  analogWrite(green,value_green);

}
