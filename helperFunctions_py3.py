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
import shutil
import arcpy
import pandas as pd


def emailMessage(receiver, message):
    # Sends an email to the receiver with the message as the email content.
    # Useful when scripts take multiple hours to run as they can be monitored remotely
    port = 465
    smtpServer = "smtp.gmail.com"
    sender = "********@gmail.com"  # visit link above for instructions on how to set up a gmail account for this
    password = "********"
    try:
        with smtplib.SMTP_SSL(smtpServer, port) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, message)
    except:
        return "Invalid email. Message not sent."
    return "Message sent"


def cleanUp(fldr):
    """Deletes everything within a folder.
    Legacy function from code written with less knowledge. replaced with shutil.rmtree()

    :param fldr: a folder path who's contents will be deleted
    """
    print("Cleaning out " + os.path.basename(fldr) + "...")
    shutil.rmtree(fldr, ignore_errors=True)
    print("DONE!")
    return


def shpToPandas(shp):
    fields = arcpy.Describe(shp).fields
    fNames = []
    for f in fields:
        fNames.append(f.name)

    data = pd.DataFrame(columns=fNames)
    cursor = arcpy.da.SearchCursor(shp, fNames)
    lineNum = 0
    for row in cursor:
        data.loc[lineNum] = row
        lineNum += 1
    return data