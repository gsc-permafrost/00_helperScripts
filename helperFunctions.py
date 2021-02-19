"""
Name: helperFunctions
Author: Ryan Parker
Created: 2019-12-03
Purpose: A series of small functions to perform basic tasks.

Visit https://realpython.com/python-send-email/ for instructions on how to set up a dummy gmail account to send emails
with the emailMessage function.
"""

import os
import smtplib
import arcpy
import datetime

tFmt = "%Y-%m-%d %H:%M:%S"


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


def cleanUp(fldr):
    """Deletes everything within a folder.

    This function is typically run on the folder containing all of the temporary outputs to free up disk space .

    :param fldr: a folder path who's contents will be deleted
    """
    arcpy.AddMessage(datetime.datetime.now().strftime(tFmt) + " Cleaning out " + os.path.basename(fldr) + "...")
    # loop through files/folders in folder and delete
    for f in os.listdir(fldr):
        try:
            os.remove(os.path.join(fldr, f))
        except:
            arcpy.AddMessage("Could not remove " + f)
    os.remove(fldr)
    arcpy.AddMessage("DONE!")
    return