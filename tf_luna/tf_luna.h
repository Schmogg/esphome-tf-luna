#pragma once
#include "esphome.h"

class TFLunaSensor : public PollingComponent, public UARTDevice, public Sensor {
 public:
  TFLunaSensor(UARTComponent *parent) : UARTDevice(parent), PollingComponent(1000) {}

  void update() override {
    const int frame_size = 9;
    uint8_t buffer[frame_size];

    if (available() >= frame_size) {
      while (available() >= frame_size) {
        read_array(buffer, frame_size);

        if (buffer[0] == 0x59 && buffer[1] == 0x59) {
          uint16_t distance = buffer[2] + (buffer[3] << 8);
          publish_state(distance);
        }
      }
    }
  }
};
