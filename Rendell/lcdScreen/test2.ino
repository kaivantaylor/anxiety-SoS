#include "rgb_lcd.h"

rgb_lcd lcd;

const int colorR = 0;
const int colorG = 255;
const int colorB = 0;

void setup()
{
// set up the LCD's number of columns and rows:
lcd.begin(16, 2);

lcd.setRGB(colorR, colorG, colorB);
// Print a message to the LCD.
lcd.print("Rendell is trash");

delay(200);
}

void loop()
{

lcd.setCursor(0, 1);
// print the number of seconds since reset:
lcd.print(millis()/1000);

delay(1000);
}

void Clear()
{
  
}

