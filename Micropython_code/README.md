# Firmware

## Hardware Connections

* Microcontroller: RPI2040
* WiFi Module: ESP32-WROOM-32
* LCD Screen: 16x2 Serial LCD [Amazon Link](https://www.amazon.com/HiLetgo-HD44780-I2C1602-Interface-Backlight/dp/B07W5KC65S)

## Description

This folder includes both the tested CircuitPython and MicroPython code.

It includes the following libraries from the [CircuitPython Library Bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases):

* adafruit_bus_device
* adafruit_minimqtt
* adafruit_io
* adafruit_esp32_spi
* adafruit_requests.mpy

As well as this [ESP32SPI CircuitPython library from Adafruit](https://github.com/adafruit/Adafruit_CircuitPython_ESP32SPI).

------

Steps followed for the WIFI connection were according to this guide: [Quickstart IoT - Raspberry Pi Pico RP2040 with WIFI](https://learn.adafruit.com/quickstart-rp2040-pico-with-wifi-and-circuitpython/circuitpython-wifi)

Steps followed for the LCD screen driver included a lot of scaffolding from this video:[LCD Basics for the Pi Pico](https://youtu.be/B8Kr_3xHjqE).