from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# api stuff

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response


# html email required stuff

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import json
from django.views.decorators.clickjacking import xframe_options_exempt
import os
import smtplib
import imghdr
from email.message import EmailMessage
# Create your v(iews here.


def home(request):
    return Response({"data": "HEllo world"})


@xframe_options_exempt
@api_view(['POST'])
def sendanemail(request):
    # to = request.data["to"]
    # username = request.data["username"]
    # # send the html mail
    # html_content = render_to_string(
    #     "email_template.html", {'username': username})
    # text_content = strip_tags(html_content)

    # email = EmailMultiAlternatives(
    #     # subject
    #     "testing",
    #     # content
    #     text_content,
    #     # from email
    #     settings.EMAIL_HOST_USER,
    #     # rec list
    #     [to]
    # )
    # email.attach_alternative(html_content, "text/html")
    # # try:
    # email.send()
    EMAIL_ADDRESS = "twoman44@gmail.com"
    EMAIL_PASSWORD = "Aquad3vid@"

    contacts = ['YourAddress@gmail.com', 'test@example.com']

    msg = EmailMessage()
    msg['Subject'] = 'Check out Bronx as a puppy!'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = 'alexsasi545@gmail.com'

    msg.set_content('This is a plain text email')

    msg.add_alternative("""\
    <!DOCTYPE html>
    <html>
        <body>
            <h1 style="color:green;">This is an HTML Email!</h1>
        </body>
    </html>
    """, subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
        data = {"status": "success"}
    return Response(data)
    # except:
    #     data = {"status": "failed"}
    #     return Response(data)
