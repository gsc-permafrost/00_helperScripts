"""
Name: helperFunctions
Author: Ryan Parker
Created: 2019-12-03
Purpose: A series of small functions to perform basic tasks.

Visit https://realpython.com/python-send-email/ for instructions on how to set up a dummy gmail account to send emails
with the emailMessage function.
"""

import smtplib
import arcpy


def emailMessage(receiver, message):
    # Sends an email to the receiver with the message as the email content.
    # Useful when scripts take multiple hours to run as they can be monitored remotely
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
    # prints out message in python terminal as well as arcpy window
    print(message)
    arcpy.AddMessage(message)
    return

