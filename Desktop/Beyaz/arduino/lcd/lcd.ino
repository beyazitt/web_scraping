#include <LiquidCrystal.h>
#define buton 10
LiquidCrystal lcd(8, 7, 6, 5, 4, 3);
int butondurumu = 0;

void setup() {
  pinMode(buton,INPUT);
  lcd.begin(16,2);

}

void loop() {
  // put your main code here, to run repeatedly:
  butondurumu = digitalRead(buton);
  if(butondurumu == 1){
 
  
    lcd.print("Anani sikiyim \n dunya");
    delay(2000);
    
  }
  else{
    lcd.noDisplay();
  }
}
