from flask import Flask, render_template
import serial
import time

try:
    arduino = serial.Serial('COM4', 9600, timeout = 1)
    time.sleep(2)
except serial.SerialException as e:
    print(f"Erro ao conectar com o arduino: {e}")
    arduino = None