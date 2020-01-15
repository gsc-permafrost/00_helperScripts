"""
Name: helperFunctions
Author: Ryan Parker
Created: 2019-12-03
Purpose:
"""


import smtplib
import arcpy


def emailMessage(receiver, message):
    port = 465
    smtpServer = "smtp.gmail.com"
    sender = "********@gmail.com"  # visit link above for instructions on how to set up a gmail account for this
    password = "********"
    try:
        server = smtplib.SMTP_SSL(smtpServer, port)
        server.login(sender, password)
        server.sendmail(sender, receiver, message)
        server.quit()
    except:
        return "Invalid email. Message not sent."
    return "Message sent"


def speak(message):
    print(message)
    arcpy.AddMessage(message)
    return

