import serial
import pandas as pd 
from sklearn.linear_model import LinearRegression
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

try:
    data = pd.read_csv("temp_data.csv")
except FileNotFoundError:
    data = pd.DataFrame(columns=["timestamp","temperature"])
