from machine import Pin, ADC
import time

# Configuración del hardware
sensor_temp = ADC(Pin(35))
sensor_temp.atten(ADC.ATTN_11DB)

buzzer = Pin(26, Pin.OUT)

# Variables globales
setpoint = 25.0
buzzer_status = False
last_temp = 0.0

def leer_temperatura():
    valor_adc = sensor_temp.read()
    voltaje = valor_adc * (3.3 / 4095)
    temperatura = voltaje * 100
    return round(temperatura, 2)

def controlar_buzzer(temp, ref):
    global buzzer_status
    buzzer_status = temp > ref
    buzzer.value(buzzer_status)