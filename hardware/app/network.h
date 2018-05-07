#include <Arduino.h>
#include "ESP8266.h"
#include "define.h"

#if !defined(_network_h_)
#define _network_h_

char forecast_weather_buffer[5120] = {0};
bool network_ready = false;

ESP8266 wifi(PIN_WIFI_PORT, 115200);

void initialize_network() {
    LOG("Initialing...");
    if(wifi.setOprToStation()) {
        network_ready = wifi.joinAP(AP_SSID, AP_PASSWORD);
        if(network_ready) {
            LOG("WIFI Initialized.");
        }
    }
}

// 网络操作
// already: 执行dosomething的时候，从进入loop主循环已经经过的时间(毫秒)
unsigned long dosomething_network(unsigned long already) {
    if(already > 0 && already % 5 != 0) {
        return 0;
    }

    unsigned long ulStart = millis();

    do {
        if(!network_ready) {
            // 没有正确的初始化wifi
            initialize_network();

            break;
        }

        LOG("Connecting to server...");
        if(wifi.createTCP(REMOTE_ADDR, REMOTE_PORT)) {
            LOG("Sending Data.");
            if(wifi.send(REQUEST_COMMAND, strlen(REQUEST_COMMAND))) {
                wifi.recv(forecast_weather_buffer, sizeof(forecast_weather_buffer));
            }
        }
    } while(false);

    return millis() - ulStart;
}

#endif