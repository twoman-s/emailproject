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
# Create your v(iews here.


def home(request):
    return Response({"data": "HEllo world"})


@xframe_options_exempt
@api_view(['POST'])
def sendanemail(request):
    to = request.data["to"]
    username = request.data["username"]
    # send the html mail
    html_content = render_to_string(
        "email_template.html", {'username': username})
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives(
        # subject
        "testing",
        # content
        text_content,
        # from email
        settings.EMAIL_HOST_USER,
        # rec list
        [to]
    )
    email.attach_alternative(html_content, "text/html")
    try:
        email.send()
        data = {"status": "success"}
        return Response(data)
    except Exception as e:
        data = {"status": "failed"}
    return Response(data)
