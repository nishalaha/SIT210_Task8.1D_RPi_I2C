//referenced : thegeekpub.com
#include <Wire.h>

const int led = 12; 

void setup() {
  Wire.begin(0x8); // join I2c bus as slave with address 8
  
  Wire.onReceive(receiveValue); 
  
  pinMode(led, OUTPUT);
  digitalWrite(led, LOW); // it is off at the start
}



// function that executes when the data is received from the master
void receiveValue(int howMany) {
  while (Wire.available()) { //loop through all except last
    char val = Wire.read(); // receive byte as a character
    digitalWrite(led, val);
  }
}

void loop() {
  delay(100);
}
