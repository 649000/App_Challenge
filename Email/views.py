from django.shortcuts import render
from sendgrid import SendGridError, SendGridClientError, SendGridServerError,sendgrid

#SG_API = sendgrid.SendGridClient("SIA_App_Challenge", "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")
SG_API = sendgrid.SendGridClient("SIA_App_Challenge_2015","gX&#D*6vyB",raise_errors=True)

def sendEmail(email):
    print "SENDGRIDDING"
    message = sendgrid.Mail()

    message.add_to("")
    # message.add_to(['Example Dude <example@email.com>', 'john@email.com'])
    # message.set_replyto('example@email.com')
    message.set_from("SIA_Challenge@TheWrightOnes.com")
    message.set_subject("Sending emails via SIA App Challenge Base Code")
    message.set_html("I hope you enjoy these emails.")


    try:
        SG_API.send(message)
    except SendGridClientError:
        # aA
        "Error"
    except SendGridServerError:
        #A
        "Error"