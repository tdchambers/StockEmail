"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Travis Chambers
ID:     180773710
Email:  cham3710@mylaurier.ca
__updated__ = "2018-09-13"
------------------------------------------------------------------------
"""
import os
import smtplib
import ssl
import rew 
import imghdr
from test.test_decimal import file
from email.message import EmailMessage


SENDER = "travisautosender@gmail.com"
PASS = "pycharmtrash12"

data = rew.getStockData("SPCE")
rew.getStockGraph("SPCE", "1mo")

with open("filename.png", 'rb') as file:
    file_data = file.read()
    file_type = imghdr.what(file.name)
    file_name = file.name






subject = "Travis SPCE stock update"
body = "Yesterdays stock data\n\n {} \n\n Graph Attached...".format(data)

msg = rew.setupEmailSpecs("bpmtravchambers@gmail.com", SENDER, subject, body)

msg.add_attachment(file_data, maintype = 'image', subtype= file_type, filename = file_name)

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:

    smtp.login(SENDER,PASS)
    smtp.send_message(msg)
    
    
