# ESP32 Serial-Based System Monitor

A project establishing a bidirectional serial communication bridge between a Linux host and an ESP32 microcontroller.

## Description
This system enables a Python-based controller running on a Xubuntu environment to transmit real-time text data over a USB serial interface, which is then processed and rendered onto an SSD1306 OLED display via I2C protocol.

## Technical Highlights
* **Host-to-Device Interfacing:** Utilization of `pyserial` for robust, asynchronous data transmission from a host machine to the ESP32.
* **Firmware Implementation:** Efficient management of serial buffers on the ESP32 to ensure real-time display updates with low latency.
* **Systems Integration:** A successful demonstration of bridging high-level Python scripting with low-level C++ firmware, critical for IoT and embedded systems development.

## Setup Instructions
1. **Hardware:** Connect the SSD1306 OLED (SDA to D21, SCL to D22).
2. **Firmware:** Upload the `.ino` sketch to your ESP32.
3. **Host Controller:** Ensure `pyserial` is installed on your Linux machine:
   ```bash
   pip install pyserial
