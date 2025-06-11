import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart, sensor
from esphome.const import (
    CONF_ID, UNIT_CENTIMETER, ICON_RULER, DEVICE_CLASS_DISTANCE
)

CONF_UART_ID = "tf_uart"

tf_luna_ns = cg.esphome_ns.namespace("tf_luna")
TFLunaSensor = tf_luna_ns.class_("TFLunaSensor", sensor.Sensor, cg.Component, uart.UARTDevice)

CONFIG_SCHEMA = sensor.sensor_schema(
    UNIT_CENTIMETER, ICON_RULER, 1, DEVICE_CLASS_DISTANCE
).extend({
    cv.GenerateID(): cv.declare_id(TFLunaSensor),
    cv.GenerateID(CONF_UART_ID): cv.use_id(uart.UARTComponent),
})

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await sensor.register_sensor(var, config)
    uart_dev = await cg.get_variable(config[CONF_UART_ID])
    cg.add(var.set_uart_parent(uart_dev))
