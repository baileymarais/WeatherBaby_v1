#include <dht.h>
#include "define.h"

double last_temperature = 0;
double last_humidity = 0;
dht DHTobj;

void update_temperature(unsigned long already) {
    if(already == 0 || already % 3 == 0) {
        DHTobj.read11(PIN_DHT11);
        last_temperature = DHTobj.temperature;
        last_humidity = DHTobj.humidity;
    }
}

// 获取温度
double get_temperature() {
    return last_temperature;
}

// 获取湿度
double get_humidity() {
    return last_humidity;
}