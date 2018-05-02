#include "define.h"

#include <Adafruit_ssd1306syp.h>
Adafruit_ssd1306syp display(PIN_SDA, PIN_SCL);

void setup() {
  delay(1000);
  display.initialize();
}

void loop() {
    display.drawLine(0, 0, 127, 63,WHITE);
    display.update();
    delay(1000);
    display.clear();
    display.setTextSize(1);
    display.setTextColor(WHITE);
    display.setCursor(0,0);
    display.println("Connecting WeatherBaby Server...");
    display.update();
    display.clear();
}
