#if !defined(_defined_h_)
#define _defined_h_

#define PROJECT_NAME  "WeatherBaby"


////////////////////////////////////////////////////
// ESP8266:
//  TX -> RX1
//  RX -> TX1
//  VCC -> 3.3V
//  GND -> GND
//  EN(CH_PD) -> 5v
// DHT11:
//  VCC -> 2
//  GND -> GND
//  DATA -> 7
////////////////////////////////////////////////////

#define PIN_SDA                 8
#define PIN_SCL                 9
#define PIN_WIFI_PORT           Serial1
#define PIN_LED                 13
#define PIN_DHT11               7

// 默认的远程服务器
#define REMOTE_ADDR             "10.11.1.62"
#define REMOTE_PORT             20000
#define REQUEST_COMMAND         "REQ|WEATHERBABY|1|7"

#define AP_SSID                 "TP-LINK-FFX905"
#define AP_PASSWORD             "O4"

// define local configuration userinfo
#define DEFAULT_USER            "admin"
#define DEFAULT_PASS            "123456"


// 最小LOOP时间周期
#define MIN_INTERVAL            1000
// 最大时间周期(超过这个值会自动重置计时器)
#define MAX_INTERVAL            1000000


#define __out
#define __in


#define INIT_LOG(x)             x.begin(9600)
#define LOG(x)                  Serial.println(x)
#define DELAY_MIN_INTERVAL(h)   if(h < MIN_INTERVAL)  delay(MIN_INTERVAL - h);
#define CLEAN_MAX_INTERVAL(x)   if(++x >= MAX_INTERVAL) x = 0;

#endif