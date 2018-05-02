#include <Arduino.h>
#include "define.h"

static const unsigned long DAYS = 86400;
static const int FOURYEARS = 1461; 
static const int norMoth[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
static const int leapMoth[] = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

void getHourMinSec(int nSecond, int *h, int *m, int *s) {
  *h = nSecond/3600+8;
  *m = (nSecond%3600)/60;
  *s = (nSecond%3600)%60;
}

void getMothAndDay(bool bLeapYear, int nDays, int *nMoth, int *nDay) {
    int i = 0;
    int nTmp = 0;
    int *pMoth = bLeapYear?leapMoth:norMoth;
    
    for (i=0; i<12; i++) {
        nTmp = nDays-pMoth[i];
        if (nTmp <= 0) {
            *nMoth = i+1;
            if (nTmp == 0) {
                *nDay = pMoth[i];
            } else {
                *nDay = nDays;
            }
            break;
        }
        nDays = nTmp;
    }
}

void convert_timestamp(__in unsigned long ts, __in int buffer_size, __out char *timestr) {
    unsigned long nDays = ts/DAYS + ((ts%DAYS)?1:0);
    int nYear4 = nDays/FOURYEARS;
    int nRemain = nDays%FOURYEARS;
    int nDecyear = 1970 + nYear4*4;
    int nDecmoth = 0;
    int nDecday = 0;
    bool bLeapyear = false;

    if (nRemain < 365) {
        ;
    } else if (nRemain < 365*2) {
        nDecyear += 1;
        nRemain -= 365;
    } else if (nRemain < 365*3) {
        nDecyear += 2;
        nRemain -= 365*2;
    } else {
        nDecyear += 3;
        nRemain -= 365*3;
        bLeapyear = true;
    }

    getMothAndDay(bLeapyear, nRemain, &nDecmoth, &nDecday);

    int hh = 0;
    int mm = 0;
    int ss = 0;
    getHourMinSec(ts%DAYS, &hh, &mm, &ss);
    memset(timestr, 0, buffer_size);

    sprintf(timestr, "%04d-%02d-%02d %02d:%02d:%02d\n", nDecyear, nDecmoth, nDecday, hh, mm, ss);
}

void setup() {
  // delay(1000);
  // display.initialize();
  // ESP8266 wifi(Serial);
  Serial.begin(9600);
  Serial.println("start");

  pinMode(PIN_LED, OUTPUT);
}

int status = 0;
unsigned long lastvalue = 0;

void loop() {
  char s[100] = {0};
  // 假设从：1525245195 => 2018/5/2 15:13:15开始
  convert_timestamp(1525245195 + (int)(millis()/1000), 100, s);

  Serial.println(s);

  delay(1000);
  // localtime(base_timestamp);

  // // display.drawLine(0, 0, 127, 63,WHITE);
  // // display.update();
  // // delay(1000);
  // // display.clear();
  // // display.setTextSize(1);
  // // display.setTextColor(WHITE);
  // // display.setCursor(0,0);
  // // display.println("Connecting WeatherBaby Server...");
  // // display.update();
  // // display.clear();
  // unsigned long t = millis();
  // Serial.println(t - lastvalue);
  // lastvalue = t;
  // delay(1000);

  digitalWrite(PIN_LED, status);
  status = !status;
}
