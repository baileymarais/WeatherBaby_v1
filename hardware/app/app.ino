#include <Arduino.h>
#include "datetime.h"
#include "network.h"
#include "thermometer.h"

unsigned long interval = 0;

void setup() {
  INIT_LOG(Serial);
  LOG("Starting...");

  pinMode(2, OUTPUT);
  digitalWrite(2, HIGH);

  initialize_network();
}

void loop() {
  unsigned long haspassed = 0;
  haspassed = dosomething_network(interval);
  // forecast_weather_buffer
  LOG(forecast_weather_buffer);

  double temp = 0;
  double humidity = 0;
  update_temperature(interval);
  LOG("Temp: ");
  LOG(get_temperature());
  LOG("Humidity: ");
  LOG(get_humidity());

  DELAY_MIN_INTERVAL(haspassed);
  CLEAN_MAX_INTERVAL(interval);
}
