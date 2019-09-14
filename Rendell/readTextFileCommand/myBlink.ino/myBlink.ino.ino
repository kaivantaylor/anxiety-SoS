
// the setup function runs once when you press reset or power the board
void setup() {
  pinMode(2, OUTPUT);
  Serial.begin(9600);
}

// the loop function runs over and over again forever
void loop() {
  byte byteRead;

  if (Serial.available()) {
    byteRead = Serial.read();
    byteRead = byteRead - '0';
  
  
  if (byteRead == 0){
    digitalWrite(2, LOW);
  }

  if (byteRead > 0){
    digitalWrite((byteRead + 1), HIGH); 
  }
  }
}

