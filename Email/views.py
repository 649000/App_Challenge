from django.shortcuts import render
import sendgrid

#SG_API = sendgrid.SendGridClient("SIA_App_Challenge", "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")
SG_API = sendgrid.SendGridClient("SIA_App_Challenge_2015","gX&#D*6vyB")

def sendEmail(email):
    print "SENDGRIDDING"
    message = sendgrid.Mail()

    message.add_to("")
    message.set_from("SIA_Challenge@TheWrightOnes.com")
    message.set_subject("Sending emails via SIA App Challenge Base Code")
    message.set_html("I hope you enjoy these emails.")

    SG_API.send(message)
