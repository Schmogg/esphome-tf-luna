# esphome-tf-luna

ESPHome custom component for TF-Luna LiDAR sensor (UART).

## Usage

```yaml
external_components:
  - source: github://dein-user/esphome-tf-luna
    components: [tf_luna]

uart:
  id: uart1
  rx_pin: GPIO16
  tx_pin: GPIO17
  baud_rate: 115200

sensor:
  - platform: tf_luna
    uart_id: uart1
    name: "Distance"
