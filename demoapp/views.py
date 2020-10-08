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
    to = request.data["to"]
    username = request.data["username"]
    subject = request.data["subject"]
    phone = request.data["phone"]
    content = request.data["content"]
    EMAIL_ADDRESS = settings.EMAIL_HOST_USER
    EMAIL_PASSWORD = settings.EMAIL_HOST_PASSWORD

    msg = EmailMessage()
    msg['Subject'] = 'STNLtd'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to
    msg1 = EmailMessage()
    msg1['Subject'] = 'STNLtd'
    msg1['From'] = EMAIL_ADDRESS
    msg1['To'] = "alexsasi545@gmail.com"
    msg1.add_alternative("""\
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        <!-- saved from url=(0046)file:///C:/Users/91854/Downloads/mailhtml.html -->
        <html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vml"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <!--[if gte mso 9
        ]><xml
        ><o:OfficeDocumentSettings
        ><o:AllowPNG /><o:PixelsPerInch
        >96</o:PixelsPerInch
        ></o:OfficeDocumentSettings
        ></xml
        ><!
        [endif]-->

        <meta content="width=device-width" name="viewport">
        <!--[if !mso]><!-->
        <meta content="IE=edge" http-equiv="X-UA-Compatible">
        <!--<![endif]-->
        <title></title>
        <!--[if !mso]><!-->
        <link href="./mail_files/css" rel="stylesheet" type="text/css">
        <link href="./mail_files/css(1)" rel="stylesheet" type="text/css">
        <!--<![endif]-->
        <style type="text/css">
        body {
        margin: 0;
        padding: 0;
        }

        table,
        td,
        tr {
        vertical-align: top;
        border-collapse: collapse;
        }

        * {
        line-height: inherit;
        }

        a[x-apple-data-detectors="true"] {
        color: inherit !important;
        text-decoration: none !important;
        }
        </style>
        <style id="media-query" type="text/css">
        @media (max-width: 700px) {
        .block-grid,
        .col {
        min-width: 320px !important;
        max-width: 100% !important;
        display: block !important;
        }

        .block-grid {
        width: 100% !important;
        }

        .col {
        width: 100% !important;
        }

        .col > div {
        margin: 0 auto;
        }

        img.fullwidth,
        img.fullwidthOnMobile {
        max-width: 100% !important;
        }

        .no-stack .col {
        min-width: 0 !important;
        display: table-cell !important;
        }

        .no-stack.two-up .col {
        width: 50% !important;
        }

        .no-stack .col.num4 {
        width: 33% !important;
        }

        .no-stack .col.num8 {
        width: 66% !important;
        }

        .no-stack .col.num4 {
        width: 33% !important;
        }

        .no-stack .col.num3 {
        width: 25% !important;
        }

        .no-stack .col.num6 {
        width: 50% !important;
        }

        .no-stack .col.num9 {
        width: 75% !important;
        }

        .video-block {
        max-width: none !important;
        }

        .mobile_hide {
        min-height: 0px;
        max-height: 0px;
        max-width: 0px;
        display: none;
        overflow: hidden;
        font-size: 0px;
        }

        .desktop_hide {
        display: block !important;
        max-height: none !important;
        }
        }
        </style>
        <style id="menu-media-query" type="text/css">
        @media (max-width: 700px) {
        .menu-checkbox[type="checkbox"] ~ .menu-links {
        display: none !important;
        padding: 5px 0;
        }

        .menu-checkbox[type="checkbox"] ~ .menu-links span.sep {
        display: none;
        }

        .menu-checkbox[type="checkbox"]:checked ~ .menu-links,
        .menu-checkbox[type="checkbox"] ~ .menu-trigger {
        display: block !important;
        max-width: none !important;
        max-height: none !important;
        font-size: inherit !important;
        }

        .menu-checkbox[type="checkbox"] ~ .menu-links > a,
        .menu-checkbox[type="checkbox"] ~ .menu-links > span.label {
        display: block !important;
        text-align: center;
        }

        .menu-checkbox[type="checkbox"]:checked ~ .menu-trigger .menu-close {
        display: block !important;
        }

        .menu-checkbox[type="checkbox"]:checked ~ .menu-trigger .menu-open {
        display: none !important;
        }

        #menuthzw2d ~ div label {
        border-radius: 50% !important;
        }

        #menuthzw2d:checked ~ .menu-links {
        background-color: #68a0a9 !important;
        }

        #menuthzw2d:checked ~ .menu-links a {
        color: #ffffff !important;
        }

        #menuthzw2d:checked ~ .menu-links span {
        color: #ffffff !important;
        }
        }
        </style>
        <style id="icon-media-query" type="text/css">
        @media (max-width: 700px) {
        .icons-inner {
        text-align: center;
        }

        .icons-inner td {
        margin: 0 auto;
        }
        }
        </style>
        </head>
        <body class="clean-body" style="
        margin: 0;
        padding: 0;
        -webkit-text-size-adjust: 100%;
        background-color: #f2fafc;
        ">
        <!--[if IE]><div class="ie-browser"><![endif]-->
        <table bgcolor="#f2fafc" cellpadding="0" cellspacing="0" class="nl-container" role="presentation" style="
        table-layout: fixed;
        vertical-align: top;
        min-width: 320px;
        margin: 0 auto;
        border-spacing: 0;
        border-collapse: collapse;
        mso-table-lspace: 0pt;
        mso-table-rspace: 0pt;
        background-color: #f2fafc;
        width: 100%;
        " valign="top" width="100%">
        <tbody>
        <tr style="vertical-align: top" valign="top">
        <td style="word-break: break-word; vertical-align: top" valign="top">
        <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="background-color:#f2fafc"><![endif]-->
        <div style="background-color: #787771">
        <div class="block-grid" style="
            margin: 0 auto;
            min-width: 320px;
            max-width: 680px;
            overflow-wrap: break-word;
            word-wrap: break-word;
            word-break: break-word;
            background-color: transparent;
            ">
            <div style="
                border-collapse: collapse;
                display: table;
                width: 100%;
                background-color: transparent;
            ">
            <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#787771;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:680px"><tr class="layout-full-width" style="background-color:transparent"><![endif]-->
            <!--[if (mso)|(IE)]><td align="center" width="680" style="background-color:transparent;width:680px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]-->
            <div class="col num12" style="
                min-width: 320px;
                max-width: 680px;
                display: table-cell;
                vertical-align: top;
                width: 680px;
                ">
                <div style="width: 100% !important">
                <!--[if (!mso)&(!IE)]><!-->
                <div style="
                    border-top: 0px solid transparent;
                    border-left: 0px solid transparent;
                    border-bottom: 0px solid transparent;
                    border-right: 0px solid transparent;
                    padding-top: 5px;
                    padding-bottom: 5px;
                    padding-right: 0px;
                    padding-left: 0px;
                    ">
                    <!--<![endif]-->
                    <table border="0" cellpadding="0" cellspacing="0" class="divider" role="presentation" style="
                        table-layout: fixed;
                        vertical-align: top;
                        border-spacing: 0;
                        border-collapse: collapse;
                        mso-table-lspace: 0pt;
                        mso-table-rspace: 0pt;
                        min-width: 100%;
                        -ms-text-size-adjust: 100%;
                        -webkit-text-size-adjust: 100%;
                    " valign="top" width="100%">
                    <tbody>
                        <tr style="vertical-align: top" valign="top">
                        <td class="divider_inner" style="
                            word-break: break-word;
                            vertical-align: top;
                            min-width: 100%;
                            -ms-text-size-adjust: 100%;
                            -webkit-text-size-adjust: 100%;
                            padding-top: 0px;
                            padding-right: 0px;
                            padding-bottom: 0px;
                            padding-left: 0px;
                            " valign="top">
                            <table align="center" border="0" cellpadding="0" cellspacing="0" class="divider_content" height="01" role="presentation" style="
                                table-layout: fixed;
                                vertical-align: top;
                                border-spacing: 0;
                                border-collapse: collapse;
                                mso-table-lspace: 0pt;
                                mso-table-rspace: 0pt;
                                border-top: 0px solid transparent;
                                height: 01px;
                                width: 100%;
                            " valign="top" width="100%">
                            <tbody>
                                <tr style="vertical-align: top" valign="top">
                                <td height="1" style="
                                    word-break: break-word;
                                    vertical-align: top;
                                    -ms-text-size-adjust: 100%;
                                    -webkit-text-size-adjust: 100%;
                                    " valign="top">
                                    <span></span>
                                </td>
                                </tr>
                            </tbody>
                            </table>
                        </td>
                        </tr>
                    </tbody>
                    </table>
                    <!--[if (!mso)&(!IE)]><!-->
                </div>
                <!--<![endif]-->
                </div>
            </div>
            <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
            <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
            </div>
        </div>
        </div>
        <div style="background-color: transparent">
        <div class="block-grid" style="
            margin: 0 auto;
            min-width: 320px;
            max-width: 680px;
            overflow-wrap: break-word;
            word-wrap: break-word;
            word-break: break-word;
            background-color: transparent;
            ">
            <div style="
                border-collapse: collapse;
                display: table;
                width: 100%;
                background-color: transparent;
            ">
            <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:680px"><tr class="layout-full-width" style="background-color:transparent"><![endif]-->
            <!--[if (mso)|(IE)]><td align="center" width="680" style="background-color:transparent;width:680px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]-->
            <div class="col num12" style="
                min-width: 320px;
                max-width: 680px;
                display: table-cell;
                vertical-align: top;
                width: 680px;
                ">
                <div style="width: 100% !important">
                <!--[if (!mso)&(!IE)]><!-->
                <div style="
                    border-top: 0px solid transparent;
                    border-left: 0px solid transparent;
                    border-bottom: 0px solid transparent;
                    border-right: 0px solid transparent;
                    padding-top: 5px;
                    padding-bottom: 5px;
                    padding-right: 0px;
                    padding-left: 0px;
                    ">
                    <!--<![endif]-->
                    <table border="0" cellpadding="0" cellspacing="0" class="divider" role="presentation" style="
                        table-layout: fixed;
                        vertical-align: top;
                        border-spacing: 0;
                        border-collapse: collapse;
                        mso-table-lspace: 0pt;
                        mso-table-rspace: 0pt;
                        min-width: 100%;
                        -ms-text-size-adjust: 100%;
                        -webkit-text-size-adjust: 100%;
                    " valign="top" width="100%">
                    <tbody>
                        <tr style="vertical-align: top" valign="top">
                        <td class="divider_inner" style="
                            word-break: break-word;
                            vertical-align: top;
                            min-width: 100%;
                            -ms-text-size-adjust: 100%;
                            -webkit-text-size-adjust: 100%;
                            padding-top: 0px;
                            padding-right: 0px;
                            padding-bottom: 0px;
                            padding-left: 0px;
                            " valign="top">
                            <table align="center" border="0" cellpadding="0" cellspacing="0" class="divider_content" height="5" role="presentation" style="
                                table-layout: fixed;
                                vertical-align: top;
                                border-spacing: 0;
                                border-collapse: collapse;
                                mso-table-lspace: 0pt;
                                mso-table-rspace: 0pt;
                                border-top: 0px solid transparent;
                                height: 5px;
                                width: 100%;
                            " valign="top" width="100%">
                            <tbody>
                                <tr style="vertical-align: top" valign="top">
                                <td height="5" style="
                                    word-break: break-word;
                                    vertical-align: top;
                                    -ms-text-size-adjust: 100%;
                                    -webkit-text-size-adjust: 100%;
                                    " valign="top">
                                    <span></span>
                                </td>
                                </tr>
                            </tbody>
                            </table>
                        </td>
                        </tr>
                    </tbody>
                    </table>
                    <!--[if (!mso)&(!IE)]><!-->
                </div>
                <!--<![endif]-->
                </div>
            </div>
            <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
            <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
            </div>
        </div>
        </div>
        <div style="background-color: transparent">
        <div class="block-grid three-up no-stack" style="
            margin: 0 auto;
            min-width: 320px;
            max-width: 680px;
            overflow-wrap: break-word;
            word-wrap: break-word;
            word-break: break-word;
            background-color: transparent;
            ">
            <div style="
                border-collapse: collapse;
                display: table;
                width: 100%;
                background-color: transparent;
            ">
            <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:680px"><tr class="layout-full-width" style="background-color:transparent"><![endif]-->
            <!--[if (mso)|(IE)]><td align="center" width="170" style="background-color:transparent;width:170px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 15px; padding-top:5px; padding-bottom:5px;"><![endif]-->
            <div class="col num3" style="
                display: table-cell;
                vertical-align: top;
                max-width: 320px;
                min-width: 168px;
                width: 170px;
                ">
                <div style="width: 100% !important">
                <!--[if (!mso)&(!IE)]><!-->
                <div style="
                    border-top: 0px solid transparent;
                    border-left: 0px solid transparent;
                    border-bottom: 0px solid transparent;
                    border-right: 0px solid transparent;
                    padding-top: 5px;
                    padding-bottom: 5px;
                    padding-right: 0px;
                    padding-left: 15px;
                    ">
                    <!--<![endif]-->
                    <div align="left" class="img-container left fixedwidth fullwidthOnMobile" style="padding-right: 0px; padding-left: 10px">
                    <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr style="line-height:0px"><td style="padding-right: 0px;padding-left: 10px;" align="left"><![endif]-->
                    <div style="font-size: 1px; line-height: 10px">&nbsp;</div>
                    
                    <div style="font-size: 1px; line-height: 10px">&nbsp;</div>
                    <!--[if mso]></td></tr></table><![endif]-->
                    </div>
                    <!--[if (!mso)&(!IE)]><!-->
                </div>
                <!--<![endif]-->
                </div>
            </div>
            <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
            <!--[if (mso)|(IE)]></td><td align="center" width="340" style="background-color:transparent;width:340px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]-->
            <div class="col num6" style="
                display: table-cell;
                vertical-align: top;
                max-width: 320px;
                min-width: 336px;
                width: 340px;
                ">
                <div style="width: 100% !important">
                <!--[if (!mso)&(!IE)]><!-->
                <div style="
                    border-top: 0px solid transparent;
                    border-left: 0px solid transparent;
                    border-bottom: 0px solid transparent;
                    border-right: 0px solid transparent;
                    padding-top: 5px;
                    padding-bottom: 5px;
                    padding-right: 0px;
                    padding-left: 0px;
                    ">
                    <!--<![endif]-->
                    <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="
                        table-layout: fixed;
                        vertical-align: top;
                        border-spacing: 0;
                        border-collapse: collapse;
                        mso-table-lspace: 0pt;
                        mso-table-rspace: 0pt;
                    " valign="top" width="100%">
                    <tbody><tr style="vertical-align: top" valign="top">
                        <td align="center" style="
                            word-break: break-word;
                            vertical-align: top;
                            padding-top: 20px;
                            padding-bottom: 20px;
                            padding-left: 0px;
                            padding-right: 0px;
                            text-align: center;
                            font-size: 0px;
                        " valign="top">
                        <!--[if !mso><!-->
                        <input class="menu-checkbox" id="menuthzw2d" style="
                            display: none !important;
                            max-height: 0;
                            visibility: hidden;
                            " type="checkbox">
                        <!--<![endif]-->
                        
                        </td>
                    </tr>
                    </tbody></table>
                    <!--[if (!mso)&(!IE)]><!-->
                </div>
                <!--<![endif]-->
                </div>
            </div>
            <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
            <!--[if (mso)|(IE)]></td><td align="center" width="170" style="background-color:transparent;width:170px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 15px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]-->
            <div class="col num3" style="
                display: table-cell;
                vertical-align: top;
                max-width: 320px;
                min-width: 168px;
                width: 170px;
                ">
                <div style="width: 100% !important">
                <!--[if (!mso)&(!IE)]><!-->
                <div style="
                    border-top: 0px solid transparent;
                    border-left: 0px solid transparent;
                    border-bottom: 0px solid transparent;
                    border-right: 0px solid transparent;
                    padding-top: 5px;
                    padding-bottom: 5px;
                    padding-right: 15px;
                    padding-left: 0px;
                    ">
                    <!--<![endif]-->
                    <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 5px; padding-left: 0px; padding-top: 22px; padding-bottom: 20px; font-family: Arial, sans-serif"><![endif]-->
                    <div style="
                        color: #787771;
                        font-family: Nunito, Arial, Helvetica Neue,
                        Helvetica, sans-serif;
                        line-height: 1.2;
                        padding-top: 22px;
                        padding-right: 5px;
                        padding-bottom: 20px;
                        padding-left: 0px;
                    ">
                    
                    
                    </div>
                    </div>
                    <!--[if mso]></td></tr></table><![endif]-->
                    <!--[if (!mso)&(!IE)]><!-->
                </div>
                <!--<![endif]-->
                </div>
            </div>
            <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
            <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
            </div>
        </div>

        <div style="background-color: transparent">
        <div class="block-grid" style="
            margin: 0 auto;
            min-width: 320px;
            max-width: 680px;
            overflow-wrap: break-word;
            word-wrap: break-word;
            word-break: break-word;
            background-color: transparent;
            ">
            <div style="
                border-collapse: collapse;
                display: table;
                width: 100%;
                background-color: transparent;
            ">
            <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:680px"><tr class="layout-full-width" style="background-color:transparent"><![endif]-->
            <!--[if (mso)|(IE)]><td align="center" width="680" style="background-color:transparent;width:680px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]-->
            <div class="col num12" style="
                min-width: 320px;
                max-width: 680px;
                display: table-cell;
                vertical-align: top;
                width: 680px;
                ">
                <div style="width: 100% !important">
                <!--[if (!mso)&(!IE)]><!-->
                <div style="
                    border-top: 0px solid transparent;
                    border-left: 0px solid transparent;
                    border-bottom: 0px solid transparent;
                    border-right: 0px solid transparent;
                    padding-top: 5px;
                    padding-bottom: 5px;
                    padding-right: 0px;
                    padding-left: 0px;
                    ">
                    <!--<![endif]-->
                    <div align="center" class="img-container center fixedwidth" style="padding-right: 0px; padding-left: 0px">
                    <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr style="line-height:0px"><td style="padding-right: 0px;padding-left: 0px;" align="center"><!
                    [endif]--><img align="center" alt="Light blue sphere with flowers" border="0" class="center fixedwidth" src="https://souhrudhathanal.web.app/static/media/logo.4b612cca.png" style="
                        text-decoration: none;
                        -ms-interpolation-mode: bicubic;
                        height: 100px;
                        border: 0;
                        width: 100px;
                        display: block;
                        " title="Light blue sphere with flowers" width="272">
                    <!--[if mso]></td></tr></table><![endif]-->
                    </div>
                    <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px; font-family: Georgia, serif"><![endif]-->
                    <div style="
                        color: #44464a;
                        font-family: &#39;Playfair Display&#39;, Georgia, serif;
                        line-height: 1.2;
                        padding-top: 10px;
                        padding-right: 10px;
                        padding-bottom: 10px;
                        padding-left: 10px;
                    ">
                    <div style="
                        line-height: 1.2;
                        font-size: 12px;
                        font-family: &#39;Playfair Display&#39;, Georgia, serif;
                        color: #44464a;
                        mso-line-height-alt: 14px;
                        ">
                        <p style="
                            font-size: 30px;
                            line-height: 1.2;
                            word-break: break-word;
                            text-align: center;
                            font-family: &#39;Playfair Display&#39;, Georgia, serif;
                            mso-line-height-alt: 36px;
                            margin: 0;
                        ">
                        <span style="font-size: 30px">"""+subject+"""</span>
                        </p>
                    </div>
                    </div>
                    <!--[if mso]></td></tr></table><![endif]-->
                    <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px; font-family: Arial, sans-serif"><![endif]-->
                    <div style="
                        color: #787771;
                        font-family: Nunito, Arial, Helvetica Neue,
                        Helvetica, sans-serif;
                        line-height: 1.2;
                        padding-top: 10px;
                        padding-right: 10px;
                        padding-bottom: 10px;
                        padding-left: 10px;
                    ">
                    <div style="
                        line-height: 1.2;
                        font-size: 12px;
                        color: #787771;
                        font-family: Nunito, Arial, Helvetica Neue,
                            Helvetica, sans-serif;
                        mso-line-height-alt: 14px;
                        ">
                        <p style="
                            font-size: 14px;
                            line-height: 1.2;
                            word-break: break-word;
                            text-align: center;
                            mso-line-height-alt: 17px;
                            margin: 0;
                        ">
                        
                        </p>
                        <p style="
                            font-size: 14px;
                            line-height: 1.2;
                            word-break: break-word;
                            text-align: center;
                            mso-line-height-alt: 17px;
                            margin: 0;
                        ">
                        
                        </p>
                    </div>
                    </div>
                    <!--[if mso]></td></tr></table><![endif]-->
                    <div align="center" class="img-container center fixedwidth" style="padding-right: 25px; padding-left: 25px">
                    <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr style="line-height:0px"><td style="padding-right: 25px;padding-left: 25px;" align="center"><![endif]-->
                    <div style="font-size: 1px; line-height: 25px">&nbsp;</div>
                    
                    <div style="font-size: 1px; line-height: 25px">&nbsp;</div>
                    <!--[if mso]></td></tr></table><![endif]-->
                    </div>
                    <!--[if (!mso)&(!IE)]><!-->
                </div>
                <!--<![endif]-->
                </div>
            </div>
            <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
            <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
            </div>
        </div>
        </div>

        <div style="background-color: transparent">
        <div class="block-grid" style="
            margin: 0 auto;
            min-width: 320px;
            max-width: 680px;
            overflow-wrap: break-word;
            word-wrap: break-word;
            word-break: break-word;
            background-color: transparent;
            ">
            <div style="
                border-collapse: collapse;
                display: table;
                width: 100%;
                background-color: transparent;
            ">
            <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:680px"><tr class="layout-full-width" style="background-color:transparent"><![endif]-->
            <!--[if (mso)|(IE)]><td align="center" width="680" style="background-color:transparent;width:680px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]-->
            <div class="col num12" style="
                min-width: 320px;
                max-width: 680px;
                display: table-cell;
                vertical-align: top;
                width: 680px;
                ">
                <div style="width: 100% !important">
                <!--[if (!mso)&(!IE)]><!-->
                <div style="
                    border-top: 0px solid transparent;
                    border-left: 0px solid transparent;
                    border-bottom: 0px solid transparent;
                    border-right: 0px solid transparent;
                    padding-top: 5px;
                    padding-bottom: 5px;
                    padding-right: 0px;
                    padding-left: 0px;
                    ">
                    <!--<![endif]-->
                    <table border="0" cellpadding="0" cellspacing="0" class="divider" role="presentation" style="
                        table-layout: fixed;
                        vertical-align: top;
                        border-spacing: 0;
                        border-collapse: collapse;
                        mso-table-lspace: 0pt;
                        mso-table-rspace: 0pt;
                        min-width: 100%;
                        -ms-text-size-adjust: 100%;
                        -webkit-text-size-adjust: 100%;
                    " valign="top" width="100%">
                    <tbody>
                        <tr style="vertical-align: top" valign="top">
                        <td class="divider_inner" style="
                            word-break: break-word;
                            vertical-align: top;
                            min-width: 100%;
                            -ms-text-size-adjust: 100%;
                            -webkit-text-size-adjust: 100%;
                            padding-top: 0px;
                            padding-right: 0px;
                            padding-bottom: 0px;
                            padding-left: 0px;
                            " valign="top">
                            <table align="center" border="0" cellpadding="0" cellspacing="0" class="divider_content" height="15" role="presentation" style="
                                table-layout: fixed;
                                vertical-align: top;
                                border-spacing: 0;
                                border-collapse: collapse;
                                mso-table-lspace: 0pt;
                                mso-table-rspace: 0pt;
                                border-top: 0px solid transparent;
                                height: 15px;
                                width: 100%;
                            " valign="top" width="100%">
                            <tbody>
                                <tr style="vertical-align: top" valign="top">
                                <td height="15" style="
                                    word-break: break-word;
                                    vertical-align: top;
                                    -ms-text-size-adjust: 100%;
                                    -webkit-text-size-adjust: 100%;
                                    " valign="top">
                                    <span></span>
                                </td>
                                </tr>
                            </tbody>
                            </table>
                        </td>
                        </tr>
                    </tbody>
                    </table>
                    <!--[if (!mso)&(!IE)]><!-->
                </div>
                <!--<![endif]-->
                </div>
            </div>
            <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
            <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
            </div>
        </div>
        </div>

        <div style="background-color: transparent">
        <div class="block-grid three-up no-stack" style="
            margin: 0 auto;
            min-width: 320px;
            max-width: 680px;
            overflow-wrap: break-word;
            word-wrap: break-word;
            word-break: break-word;
            background-color: transparent;
            ">
            <div style="
                border-collapse: collapse;
                display: table;
                width: 100%;
                background-color: transparent;
            ">
            <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:680px"><tr class="layout-full-width" style="background-color:transparent"><![endif]-->
            <!--[if (mso)|(IE)]><td align="center" width="226" style="background-color:transparent;width:226px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 5px; padding-left: 5px; padding-top:5px; padding-bottom:5px;"><![endif]-->
            <div class="col num4" style="
                max-width: 320px;
                min-width: 226px;
                display: table-cell;
                vertical-align: top;
                width: 226px;
                ">
                <div style="width: 100% !important">
                <!--[if (!mso)&(!IE)]><!-->
                <div style="
                    border-top: 0px solid transparent;
                    border-left: 0px solid transparent;
                    border-bottom: 0px solid transparent;
                    border-right: 0px solid transparent;
                    padding-top: 5px;
                    padding-bottom: 5px;
                    padding-right: 5px;
                    padding-left: 5px;
                    ">
                    <!--<![endif]-->
                    <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px; font-family: Arial, sans-serif"><![endif]-->
                    <div style="
                        color: #393d47;
                        font-family: Nunito, Arial, Helvetica Neue,
                        Helvetica, sans-serif;
                        line-height: 1.2;
                        padding-top: 10px;
                        padding-right: 0px;
                        padding-bottom: 10px;
                        padding-left: 10px;
                    ">
                    <div style="
                        line-height: 1.2;
                        font-size: 12px;
                        color: #393d47;
                        font-family: Nunito, Arial, Helvetica Neue,
                            Helvetica, sans-serif;
                        mso-line-height-alt: 14px;
                        ">
                        <p style="
                            font-size: 14px;
                            line-height: 1.2;
                            word-break: break-word;
                            mso-line-height-alt: 17px;
                            margin: 0;
                        ">NAME</p>
                    </div>
                    </div>
                    <!--[if mso]></td></tr></table><![endif]-->
                    <!--[if (!mso)&(!IE)]><!-->
                </div>
                <!--<![endif]-->
                </div>
            </div>
            <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
            <!--[if (mso)|(IE)]></td><td align="center" width="226" style="background-color:transparent;width:226px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 5px; padding-left: 5px; padding-top:5px; padding-bottom:5px;"><![endif]-->
            
            <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
            <!--[if (mso)|(IE)]></td><td align="center" width="226" style="background-color:transparent;width:226px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 5px; padding-left: 5px; padding-top:5px; padding-bottom:5px;"><![endif]-->
            <div class="col num4" style="
                max-width: 320px;
                min-width: 226px;
                display: table-cell;
                vertical-align: top;
                width: 226px;
                ">
                <div style="width: 100% !important">
                <!--[if (!mso)&(!IE)]><!-->
                <div style="
                    border-top: 0px solid transparent;
                    border-left: 0px solid transparent;
                    border-bottom: 0px solid transparent;
                    border-right: 0px solid transparent;
                    padding-top: 5px;
                    padding-bottom: 5px;
                    padding-right: 5px;
                    padding-left: 5px;
                    ">
                    <!--<![endif]-->
                    <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 0px; padding-top: 10px; padding-bottom: 10px; font-family: Arial, sans-serif"><![endif]-->
                    <div style="
                        color: #393d47;
                        font-family: Nunito, Arial, Helvetica Neue,
                        Helvetica, sans-serif;
                        line-height: 1.2;
                        padding-top: 10px;
                        padding-right: 10px;
                        padding-bottom: 10px;
                        padding-left: 0px;
                    ">
                    <div style="
                        line-height: 1.2;
                        font-size: 12px;
                        color: #393d47;
                        font-family: Nunito, Arial, Helvetica Neue,
                            Helvetica, sans-serif;
                        mso-line-height-alt: 14px;
                        ">
                        <p style="
                            font-size: 14px;
                            line-height: 1.2;
                            word-break: break-word;
                            text-align: center;
                            mso-line-height-alt: 17px;
                            margin: 0;
                        ">"""+username+"""</p>
                    </div>
                    </div>
                    <!--[if mso]></td></tr></table><![endif]-->
                    <!--[if (!mso)&(!IE)]><!-->
                </div>
                <!--<![endif]-->
                </div>
            </div>
            <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
            <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
            </div>
        </div>
        </div>
        <div style="background-color: transparent">
        <div class="block-grid" style="
            margin: 0 auto;
            min-width: 320px;
            max-width: 680px;
            overflow-wrap: break-word;
            word-wrap: break-word;
            word-break: break-word;
            background-color: transparent;
            ">
            <div style="
                border-collapse: collapse;
                display: table;
                width: 100%;
                background-color: transparent;
            ">
            <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:680px"><tr class="layout-full-width" style="background-color:transparent"><![endif]-->
            <!--[if (mso)|(IE)]><td align="center" width="680" style="background-color:transparent;width:680px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]-->
            <div class="col num12" style="
                min-width: 320px;
                max-width: 680px;
                display: table-cell;
                vertical-align: top;
                width: 680px;
                ">
                <div style="width: 100% !important">
                <!--[if (!mso)&(!IE)]><!-->
                <div style="
                    border-top: 0px solid transparent;
                    border-left: 0px solid transparent;
                    border-bottom: 0px solid transparent;
                    border-right: 0px solid transparent;
                    padding-top: 5px;
                    padding-bottom: 5px;
                    padding-right: 0px;
                    padding-left: 0px;
                    ">
                    <!--<![endif]-->
                    <table border="0" cellpadding="0" cellspacing="0" class="divider" role="presentation" style="
                        table-layout: fixed;
                        vertical-align: top;
                        border-spacing: 0;
                        border-collapse: collapse;
                        mso-table-lspace: 0pt;
                        mso-table-rspace: 0pt;
                        min-width: 100%;
                        -ms-text-size-adjust: 100%;
                        -webkit-text-size-adjust: 100%;
                    " valign="top" width="100%">
                    <tbody>
                        <tr style="vertical-align: top" valign="top">
                        <td class="divider_inner" style="
                            word-break: break-word;
                            vertical-align: top;
                            min-width: 100%;
                            -ms-text-size-adjust: 100%;
                            -webkit-text-size-adjust: 100%;
                            padding-top: 0px;
                            padding-right: 0px;
                            padding-bottom: 0px;
                            padding-left: 0px;
                            " valign="top">
                            <table align="center" border="0" cellpadding="0" cellspacing="0" class="divider_content" height="1" role="presentation" style="
                                table-layout: fixed;
                                vertical-align: top;
                                border-spacing: 0;
                                border-collapse: collapse;
                                mso-table-lspace: 0pt;
                                mso-table-rspace: 0pt;
                                border-top: 1px solid #e1ecef;
                                height: 1px;
                                width: 100%;
                            " valign="top" width="100%">
                            <tbody>
                                <tr style="vertical-align: top" valign="top">
                                <td height="1" style="
                                    word-break: break-word;
                                    vertical-align: top;
                                    -ms-text-size-adjust: 100%;
                                    -webkit-text-size-adjust: 100%;
                                    " valign="top">
                                    <span></span>
                                </td>
                                </tr>
                            </tbody>
                            </table>
                        </td>
                        </tr>
                    </tbody>
                    </table>
                    <!--[if (!mso)&(!IE)]><!-->
                </div>
                <!--<![endif]-->
                </div>
            </div>
            <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
            <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
            </div>
        </div>
        </div>
        <div style="background-color: transparent">
        <div class="block-grid three-up no-stack" style="
            margin: 0 auto;
            min-width: 320px;
            max-width: 680px;
            overflow-wrap: break-word;
            word-wrap: break-word;
            word-break: break-word;
            background-color: transparent;
            ">
            <div style="
                border-collapse: collapse;
                display: table;
                width: 100%;
                background-color: transparent;
            ">
            <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:680px"><tr class="layout-full-width" style="background-color:transparent"><![endif]-->
            <!--[if (mso)|(IE)]><td align="center" width="226" style="background-color:transparent;width:226px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 5px; padding-left: 5px; padding-top:5px; padding-bottom:5px;"><![endif]-->
            <div class="col num4" style="
                max-width: 320px;
                min-width: 226px;
                display: table-cell;
                vertical-align: top;
                width: 226px;
                ">
                <div style="width: 100% !important">
                <!--[if (!mso)&(!IE)]><!-->
                <div style="
                    border-top: 0px solid transparent;
                    border-left: 0px solid transparent;
                    border-bottom: 0px solid transparent;
                    border-right: 0px solid transparent;
                    padding-top: 5px;
                    padding-bottom: 5px;
                    padding-right: 5px;
                    padding-left: 5px;
                    ">
                    <!--<![endif]-->
                    <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px; font-family: Arial, sans-serif"><![endif]-->
                    <div style="
                        color: #393d47;
                        font-family: Nunito, Arial, Helvetica Neue,
                        Helvetica, sans-serif;
                        line-height: 1.2;
                        padding-top: 10px;
                        padding-right: 0px;
                        padding-bottom: 10px;
                        padding-left: 10px;
                    ">
                    <div style="
                        line-height: 1.2;
                        font-size: 12px;
                        color: #393d47;
                        font-family: Nunito, Arial, Helvetica Neue,
                            Helvetica, sans-serif;
                        mso-line-height-alt: 14px;
                        ">
                        <p style="
                            font-size: 14px;
                            line-height: 1.2;
                            word-break: break-word;
                            mso-line-height-alt: 17px;
                            margin: 0;
                        ">Email</p>
                    </div>
                    </div>
                    <!--[if mso]></td></tr></table><![endif]-->
                    <!--[if (!mso)&(!IE)]><!-->
                </div>
                <!--<![endif]-->
                </div>
            </div>
            <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
            <!--[if (mso)|(IE)]></td><td align="center" width="226" style="background-color:transparent;width:226px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 5px; padding-left: 5px; padding-top:5px; padding-bottom:5px;"><![endif]-->
            
            <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
            <!--[if (mso)|(IE)]></td><td align="center" width="226" style="background-color:transparent;width:226px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 5px; padding-left: 5px; padding-top:5px; padding-bottom:5px;"><![endif]-->
            <div class="col num4" style="
                max-width: 320px;
                min-width: 226px;
                display: table-cell;
                vertical-align: top;
                width: 226px;
                ">
                <div style="width: 100% !important">
                <!--[if (!mso)&(!IE)]><!-->
                <div style="
                    border-top: 0px solid transparent;
                    border-left: 0px solid transparent;
                    border-bottom: 0px solid transparent;
                    border-right: 0px solid transparent;
                    padding-top: 5px;
                    padding-bottom: 5px;
                    padding-right: 5px;
                    padding-left: 5px;
                    ">
                    <!--<![endif]-->
                    <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 0px; padding-top: 10px; padding-bottom: 10px; font-family: Arial, sans-serif"><![endif]-->
                    <div style="
                        color: #393d47;
                        font-family: Nunito, Arial, Helvetica Neue,
                        Helvetica, sans-serif;
                        line-height: 1.2;
                        padding-top: 10px;
                        padding-right: 10px;
                        padding-bottom: 10px;
                        padding-left: 0px;
                    ">
                    <div style="
                        line-height: 1.2;
                        font-size: 12px;
                        color: #393d47;
                        font-family: Nunito, Arial, Helvetica Neue,
                            Helvetica, sans-serif;
                        mso-line-height-alt: 14px;
                        ">
                        <p style="
                            font-size: 14px;
                            line-height: 1.2;
                            word-break: break-word;
                            text-align: center;
                            mso-line-height-alt: 17px;
                            margin: 0;
                        ">"""+to+"""</p>
                    </div>
                    </div>
                    <!--[if mso]></td></tr></table><![endif]-->
                    <!--[if (!mso)&(!IE)]><!-->
                </div>
                <!--<![endif]-->
                </div>
            </div>
            <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
            <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
            </div>
        </div>
        </div>
        <div style="background-color: transparent">
        <div class="block-grid" style="
            margin: 0 auto;
            min-width: 320px;
            max-width: 680px;
            overflow-wrap: break-word;
            word-wrap: break-word;
            word-break: break-word;
            background-color: transparent;
            ">
            <div style="
                border-collapse: collapse;
                display: table;
                width: 100%;
                background-color: transparent;
            ">
            <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:680px"><tr class="layout-full-width" style="background-color:transparent"><![endif]-->
            <!--[if (mso)|(IE)]><td align="center" width="680" style="background-color:transparent;width:680px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]-->
            <div class="col num12" style="
                min-width: 320px;
                max-width: 680px;
                display: table-cell;
                vertical-align: top;
                width: 680px;
                ">
                <div style="width: 100% !important">
                <!--[if (!mso)&(!IE)]><!-->
                <div style="
                    border-top: 0px solid transparent;
                    border-left: 0px solid transparent;
                    border-bottom: 0px solid transparent;
                    border-right: 0px solid transparent;
                    padding-top: 5px;
                    padding-bottom: 5px;
                    padding-right: 0px;
                    padding-left: 0px;
                    ">
                    <!--<![endif]-->
                    <table border="0" cellpadding="0" cellspacing="0" class="divider" role="presentation" style="
                        table-layout: fixed;
                        vertical-align: top;
                        border-spacing: 0;
                        border-collapse: collapse;
                        mso-table-lspace: 0pt;
                        mso-table-rspace: 0pt;
                        min-width: 100%;
                        -ms-text-size-adjust: 100%;
                        -webkit-text-size-adjust: 100%;
                    " valign="top" width="100%">
                    <tbody>
                        <tr style="vertical-align: top" valign="top">
                        <td class="divider_inner" style="
                            word-break: break-word;
                            vertical-align: top;
                            min-width: 100%;
                            -ms-text-size-adjust: 100%;
                            -webkit-text-size-adjust: 100%;
                            padding-top: 0px;
                            padding-right: 0px;
                            padding-bottom: 0px;
                            padding-left: 0px;
                            " valign="top">
                            <table align="center" border="0" cellpadding="0" cellspacing="0" class="divider_content" height="1" role="presentation" style="
                                table-layout: fixed;
                                vertical-align: top;
                                border-spacing: 0;
                                border-collapse: collapse;
                                mso-table-lspace: 0pt;
                                mso-table-rspace: 0pt;
                                border-top: 1px solid #e1ecef;
                                height: 1px;
                                width: 100%;
                            " valign="top" width="100%">
                            <tbody>
                                <tr style="vertical-align: top" valign="top">
                                <td height="1" style="
                                    word-break: break-word;
                                    vertical-align: top;
                                    -ms-text-size-adjust: 100%;
                                    -webkit-text-size-adjust: 100%;
                                    " valign="top">
                                    <span></span>
                                </td>
                                </tr>
                            </tbody>
                            </table>
                        </td>
                        </tr>
                    </tbody>
                    </table>
                    <!--[if (!mso)&(!IE)]><!-->
                </div>
                <!--<![endif]-->
                </div>
            </div>
            <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
            <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
            </div>
        </div>
        </div>
        <div style="background-color: transparent">
        <div class="block-grid three-up no-stack" style="
            margin: 0 auto;
            min-width: 320px;
            max-width: 680px;
            overflow-wrap: break-word;
            word-wrap: break-word;
            word-break: break-word;
            background-color: transparent;
            ">
            <div style="
                border-collapse: collapse;
                display: table;
                width: 100%;
                background-color: transparent;
            ">
            <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:680px"><tr class="layout-full-width" style="background-color:transparent"><![endif]-->
            <!--[if (mso)|(IE)]><td align="center" width="226" style="background-color:transparent;width:226px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 5px; padding-left: 5px; padding-top:5px; padding-bottom:5px;"><![endif]-->
            <div class="col num4" style="
                max-width: 320px;
                min-width: 226px;
                display: table-cell;
                vertical-align: top;
                width: 226px;
                ">
                <div style="width: 100% !important">
                <!--[if (!mso)&(!IE)]><!-->
                <div style="
                    border-top: 0px solid transparent;
                    border-left: 0px solid transparent;
                    border-bottom: 0px solid transparent;
                    border-right: 0px solid transparent;
                    padding-top: 5px;
                    padding-bottom: 5px;
                    padding-right: 5px;
                    padding-left: 5px;
                    ">
                    <!--<![endif]-->
                    <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px; font-family: Arial, sans-serif"><![endif]-->
                    <div style="
                        color: #393d47;
                        font-family: Nunito, Arial, Helvetica Neue,
                        Helvetica, sans-serif;
                        line-height: 1.2;
                        padding-top: 10px;
                        padding-right: 0px;
                        padding-bottom: 10px;
                        padding-left: 10px;
                    ">
                    <div style="
                        line-height: 1.2;
                        font-size: 12px;
                        color: #393d47;
                        font-family: Nunito, Arial, Helvetica Neue,
                            Helvetica, sans-serif;
                        mso-line-height-alt: 14px;
                        ">
                        <p style="
                            font-size: 14px;
                            line-height: 1.2;
                            word-break: break-word;
                            mso-line-height-alt: 17px;
                            margin: 0;
                        ">Phone</p>
                    </div>
                    </div>
                    <!--[if mso]></td></tr></table><![endif]-->
                    <!--[if (!mso)&(!IE)]><!-->
                </div>
                <!--<![endif]-->
                </div>
            </div>
            <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
            <!--[if (mso)|(IE)]></td><td align="center" width="226" style="background-color:transparent;width:226px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 5px; padding-left: 5px; padding-top:5px; padding-bottom:5px;"><![endif]-->
            
            <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
            <!--[if (mso)|(IE)]></td><td align="center" width="226" style="background-color:transparent;width:226px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 5px; padding-left: 5px; padding-top:5px; padding-bottom:5px;"><![endif]-->
            <div class="col num4" style="
                max-width: 320px;
                min-width: 226px;
                display: table-cell;
                vertical-align: top;
                width: 226px;
                ">
                <div style="width: 100% !important">
                <!--[if (!mso)&(!IE)]><!-->
                <div style="
                    border-top: 0px solid transparent;
                    border-left: 0px solid transparent;
                    border-bottom: 0px solid transparent;
                    border-right: 0px solid transparent;
                    padding-top: 5px;
                    padding-bottom: 5px;
                    padding-right: 5px;
                    padding-left: 5px;
                    ">
                    <!--<![endif]-->
                    <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 0px; padding-top: 10px; padding-bottom: 10px; font-family: Arial, sans-serif"><![endif]-->
                    <div style="
                        color: #393d47;
                        font-family: Nunito, Arial, Helvetica Neue,
                        Helvetica, sans-serif;
                        line-height: 1.2;
                        padding-top: 10px;
                        padding-right: 10px;
                        padding-bottom: 10px;
                        padding-left: 0px;
                    ">
                    <div style="
                        line-height: 1.2;
                        font-size: 12px;
                        color: #393d47;
                        font-family: Nunito, Arial, Helvetica Neue,
                            Helvetica, sans-serif;
                        mso-line-height-alt: 14px;
                        ">
                        <p style="
                            font-size: 14px;
                            line-height: 1.2;
                            word-break: break-word;
                            text-align: center;
                            mso-line-height-alt: 17px;
                            margin: 0;
                        ">"""+phone+"""</p>
                    </div>
                    </div>
                    <!--[if mso]></td></tr></table><![endif]-->
                    <!--[if (!mso)&(!IE)]><!-->
                </div>
                <!--<![endif]-->
                </div>
            </div>
            <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
            <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
            </div>
        </div>
        </div>
        <div style="background-color: transparent">
        <div class="block-grid" style="
            margin: 0 auto;
            min-width: 320px;
            max-width: 680px;
            overflow-wrap: break-word;
            word-wrap: break-word;
            word-break: break-word;
            background-color: transparent;
            ">
            <div style="
                border-collapse: collapse;
                display: table;
                width: 100%;
                background-color: transparent;
            ">
            <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:680px"><tr class="layout-full-width" style="background-color:transparent"><![endif]-->
            <!--[if (mso)|(IE)]><td align="center" width="680" style="background-color:transparent;width:680px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]-->
            <div class="col num12" style="
                min-width: 320px;
                max-width: 680px;
                display: table-cell;
                vertical-align: top;
                width: 680px;
                ">
                <div style="width: 100% !important">
                <!--[if (!mso)&(!IE)]><!-->
                <div style="
                    border-top: 0px solid transparent;
                    border-left: 0px solid transparent;
                    border-bottom: 0px solid transparent;
                    border-right: 0px solid transparent;
                    padding-top: 5px;
                    padding-bottom: 5px;
                    padding-right: 0px;
                    padding-left: 0px;
                    ">
                    <!--<![endif]-->
                    <table border="0" cellpadding="0" cellspacing="0" class="divider" role="presentation" style="
                        table-layout: fixed;
                        vertical-align: top;
                        border-spacing: 0;
                        border-collapse: collapse;
                        mso-table-lspace: 0pt;
                        mso-table-rspace: 0pt;
                        min-width: 100%;
                        -ms-text-size-adjust: 100%;
                        -webkit-text-size-adjust: 100%;
                    " valign="top" width="100%">
                    <tbody>
                        <tr style="vertical-align: top" valign="top">
                        <td class="divider_inner" style="
                            word-break: break-word;
                            vertical-align: top;
                            min-width: 100%;
                            -ms-text-size-adjust: 100%;
                            -webkit-text-size-adjust: 100%;
                            padding-top: 0px;
                            padding-right: 0px;
                            padding-bottom: 0px;
                            padding-left: 0px;
                            " valign="top">
                            <table align="center" border="0" cellpadding="0" cellspacing="0" class="divider_content" height="1" role="presentation" style="
                                table-layout: fixed;
                                vertical-align: top;
                                border-spacing: 0;
                                border-collapse: collapse;
                                mso-table-lspace: 0pt;
                                mso-table-rspace: 0pt;
                                border-top: 1px solid #e1ecef;
                                height: 1px;
                                width: 100%;
                            " valign="top" width="100%">
                            <tbody>
                                <tr style="vertical-align: top" valign="top">
                                <td height="1" style="
                                    word-break: break-word;
                                    vertical-align: top;
                                    -ms-text-size-adjust: 100%;
                                    -webkit-text-size-adjust: 100%;
                                    " valign="top">
                                    <span></span>
                                </td>
                                </tr>
                            </tbody>
                            </table>
                        </td>
                        </tr>
                    </tbody>
                    </table>
                    <!--[if (!mso)&(!IE)]><!-->
                </div>
                <!--<![endif]-->
                </div>
            </div>
            <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
            <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
            </div>
        </div>
        </div>






        <div style="background-color: transparent">
        <div class="block-grid" style="
            margin: 0 auto;
            min-width: 320px;
            max-width: 680px;
            overflow-wrap: break-word;
            word-wrap: break-word;
            word-break: break-word;
            background-color: #ffffff;
            ">
            <div style="
                border-collapse: collapse;
                display: table;
                width: 100%;
                background-color: #ffffff;
            ">
            <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:680px"><tr class="layout-full-width" style="background-color:#ffffff"><![endif]-->
            <!--[if (mso)|(IE)]><td align="center" width="680" style="background-color:#ffffff;width:680px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:15px; padding-bottom:15px;"><![endif]-->
            <div class="col num12" style="
                min-width: 320px;
                max-width: 680px;
                display: table-cell;
                vertical-align: top;
                width: 680px;
                ">
                <div style="width: 100% !important">
                <!--[if (!mso)&(!IE)]><!-->
                <div style="
                    border-top: 0px solid transparent;
                    border-left: 0px solid transparent;
                    border-bottom: 0px solid transparent;
                    border-right: 0px solid transparent;
                    padding-top: 15px;
                    padding-bottom: 15px;
                    padding-right: 0px;
                    padding-left: 0px;
                    ">
                    <!--<![endif]-->
                    <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 35px; padding-left: 35px; padding-top: 15px; padding-bottom: 15px; font-family: Arial, sans-serif"><![endif]-->
                    <div style="
                        color: #44464a;
                        font-family: Nunito, Arial, Helvetica Neue,
                        Helvetica, sans-serif;
                        line-height: 1.5;
                        padding-top: 15px;
                        padding-right: 35px;
                        padding-bottom: 15px;
                        padding-left: 35px;
                    ">
                    <div style="
                        line-height: 1.5;
                        font-size: 12px;
                        color: #44464a;
                        font-family: Nunito, Arial, Helvetica Neue,
                            Helvetica, sans-serif;
                        mso-line-height-alt: 18px;
                        ">
                        <p style="
                            font-size: 14px;
                            line-height: 1.5;
                            word-break: break-word;
                            text-align: center;
                            mso-line-height-alt: 21px;
                            margin: 0;
                        ">"""+content+"""</p>
                    </div>
                    </div>
                    <!--[if mso]></td></tr></table><![endif]-->
                    <div align="center" class="button-container" style="
                        padding-top: 10px;
                        padding-right: 10px;
                        padding-bottom: 10px;
                        padding-left: 10px;
                    ">
                    <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-spacing: 0; border-collapse: collapse; mso-table-lspace:0pt; mso-table-rspace:0pt;"><tr><td style="padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px" align="center"><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="http://www.example.com/" style="height:33pt; width:117.75pt; v-text-anchor:middle;" arcsize="64%" strokeweight="0.75pt" strokecolor="#68A0A9" fill="false"><w:anchorlock/><v:textbox inset="0,0,0,0"><center style="color:#68a0a9; font-family:Arial, sans-serif; font-size:16px"><!
                    [endif]-->
                    <!--[if mso]></center></v:textbox></v:roundrect></td></tr></table><![endif]-->
                    </div>
                    <!--[if (!mso)&(!IE)]><!-->
                </div>
                <!--<![endif]-->
                </div>
            </div>
            <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
            <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
            </div>
        </div>
        </div>

        <div style="background-color: transparent">
        <div class="block-grid" style="
            margin: 0 auto;
            min-width: 320px;
            max-width: 680px;
            overflow-wrap: break-word;
            word-wrap: break-word;
            word-break: break-word;
            background-color: transparent;
            ">
            <div style="
                border-collapse: collapse;
                display: table;
                width: 100%;
                background-color: transparent;
            ">
            <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:680px"><tr class="layout-full-width" style="background-color:transparent"><![endif]-->
            <!--[if (mso)|(IE)]><td align="center" width="680" style="background-color:transparent;width:680px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:15px; padding-bottom:15px;"><![endif]-->
            <div class="col num12" style="
                min-width: 320px;
                max-width: 680px;
                display: table-cell;
                vertical-align: top;
                width: 680px;
                ">
                <div style="width: 100% !important">
                <!--[if (!mso)&(!IE)]><!-->
                
                <!--<![endif]-->
                </div>
            </div>
            <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
            <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
            </div>
        </div>
        </div>

        <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
        </td>
        </tr>
        </tbody>
        </table>
        <!--[if (IE)]></div><![endif]-->


        </body></html>
        """, subtype='html')

    msg.add_alternative("""\
    
    <!-- <img
      src="https://souhrudhathanal.web.app/static/media/logo.4b612cca.png"
      alt=""
    /> -->
    <!DOCTYPE html>
    <html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
    <head>
        <meta charset="utf-8"> <!-- utf-8 works for most cases -->
        <meta name="viewport" content="width=device-width"> <!-- Forcing initial-scale shouldn't be necessary -->
        <meta http-equiv="X-UA-Compatible" content="IE=edge"> <!-- Use the latest (edge) version of IE rendering engine -->
        <meta name="x-apple-disable-message-reformatting">  <!-- Disable auto-scale in iOS 10 Mail entirely -->
        <title></title> <!-- The title tag shows in email notifications, like Android 4.4. -->
    
        <link href="https://fonts.googleapis.com/css?family=Poppins:200,300,400,500,600,700" rel="stylesheet">
    
        <!-- CSS Reset : BEGIN -->
        <style>
    
            /* What it does: Remove spaces around the email design added by some email clients. */
            /* Beware: It can remove the padding / margin and add a background color to the compose a reply window. */
            html,
    body {
        margin: 0 auto !important;
        padding: 0 !important;
        height: 100% !important;
        width: 100% !important;
        background: #f1f1f1;
    }
    
    /* What it does: Stops email clients resizing small text. */
    * {
        -ms-text-size-adjust: 100%;
        -webkit-text-size-adjust: 100%;
    }
    
    /* What it does: Centers email on Android 4.4 */
    div[style*="margin: 16px 0"] {
        margin: 0 !important;
    }
    
    /* What it does: Stops Outlook from adding extra spacing to tables. */
    table,
    td {
        mso-table-lspace: 0pt !important;
        mso-table-rspace: 0pt !important;
    }
    
    /* What it does: Fixes webkit padding issue. */
    table {
        border-spacing: 0 !important;
        border-collapse: collapse !important;
        table-layout: fixed !important;
        margin: 0 auto !important;
    }
    
    /* What it does: Uses a better rendering method when resizing images in IE. */
    img {
        -ms-interpolation-mode:bicubic;
    }
    
    /* What it does: Prevents Windows 10 Mail from underlining links despite inline CSS. Styles for underlined links should be inline. */
    a {
        text-decoration: none;
    }
    
    /* What it does: A work-around for email clients meddling in triggered links. */
    *[x-apple-data-detectors],  /* iOS */
    .unstyle-auto-detected-links *,
    .aBn {
        border-bottom: 0 !important;
        cursor: default !important;
        color: inherit !important;
        text-decoration: none !important;
        font-size: inherit !important;
        font-family: inherit !important;
        font-weight: inherit !important;
        line-height: inherit !important;
    }
    
    /* What it does: Prevents Gmail from displaying a download button on large, non-linked images. */
    .a6S {
        display: none !important;
        opacity: 0.01 !important;
    }
    
    /* What it does: Prevents Gmail from changing the text color in conversation threads. */
    .im {
        color: inherit !important;
    }
    
    /* If the above doesn't work, add a .g-img class to any image in question. */
    img.g-img + div {
        display: none !important;
    }
    
    /* What it does: Removes right gutter in Gmail iOS app: https://github.com/TedGoas/Cerberus/issues/89  */
    /* Create one of these media queries for each additional viewport size you'd like to fix */
    
    /* iPhone 4, 4S, 5, 5S, 5C, and 5SE */
    @media only screen and (min-device-width: 320px) and (max-device-width: 374px) {
        u ~ div .email-container {
            min-width: 320px !important;
        }
    }
    /* iPhone 6, 6S, 7, 8, and X */
    @media only screen and (min-device-width: 375px) and (max-device-width: 413px) {
        u ~ div .email-container {
            min-width: 375px !important;
        }
    }
    /* iPhone 6+, 7+, and 8+ */
    @media only screen and (min-device-width: 414px) {
        u ~ div .email-container {
            min-width: 414px !important;
        }
    }
    
    
        </style>
    
        <!-- CSS Reset : END -->
    
        <!-- Progressive Enhancements : BEGIN -->
        <style>
    
          .primary{
      background: #925526;
    }
    .bg_white{
      background: #ffffff;
    }
    .bg_light{
      background: #f7fafa;
    }
    .bg_black{
      background: #000000;
    }
    .bg_dark{
      background: rgba(0,0,0,.8);
    }
    .email-section{
      padding:2.5em;
    }
    
    /*BUTTON*/
    .btn{
      padding: 10px 15px;
      display: inline-block;
    }
    .btn.btn-primary{
      border-radius: 5px;
      background: #925526;
      color: #ffffff;
    }
    .btn.btn-white{
      border-radius: 5px;
      background: #ffffff;
      color: #000000;
    }
    .btn.btn-white-outline{
      border-radius: 5px;
      background: transparent;
      border: 1px solid #fff;
      color: #fff;
    }
    .btn.btn-black-outline{
      border-radius: 0px;
      background: transparent;
      border: 2px solid #000;
      color: #000;
      font-weight: 700;
    }
    .btn-custom{
      color: rgba(0,0,0,.3);
      text-decoration: underline;
    }
    
    h1,h2,h3,h4,h5,h6{
      font-family: 'Poppins', sans-serif;
      color: #000000;
      margin-top: 0;
      font-weight: 400;
    }
    
    body{
      font-family: 'Poppins', sans-serif;
      font-weight: 400;
      font-size: 15px;
      line-height: 1.8;
      color: rgba(0,0,0,.4);
    }
    
    a{
      color: #925526;
    }
    
    table{
    }
    /*LOGO*/
    
    .logo h1{
      margin: 0;
    }
    .logo h1 a{
      color: #925526;
      font-size: 24px;
      font-weight: 700;
      font-family: 'Poppins', sans-serif;
    }
    
    /*HERO*/
    .hero{
      position: relative;
      z-index: 0;
    }
    
    .hero .text{
      color: rgba(0,0,0,.3);
    }
    .hero .text h2{
      color: #000;
      font-size: 34px;
      margin-bottom: 0;
      font-weight: 200;
      line-height: 1.4;
    }
    .hero .text h3{
      font-size: 24px;
      font-weight: 300;
    }
    .hero .text h2 span{
      font-weight: 600;
      color: #000;
    }
    
    .text-author{
      bordeR: 1px solid rgba(0,0,0,.05);
      max-width: 50%;
      margin: 0 auto;
      padding: 2em;
    }
    .text-author img{
      border-radius: 50%;
      background-color: #fff;
    }
    .text-author h3{
      margin-bottom: 0;
    }
    ul.social{
      padding: 0;
    }
    ul.social li{
      display: inline-block;
      margin-right: 10px;
    }
    
    /*FOOTER*/
    
    .footer{
      border-top: 1px solid rgba(0,0,0,.05);
      color: rgba(0,0,0,.5);
    }
    .footer .heading{
      color: #000;
      font-size: 20px;
    }
    .footer ul{
      margin: 0;
      padding: 0;
    }
    .footer ul li{
      list-style: none;
      margin-bottom: 10px;
    }
    .footer ul li a{
      color: rgba(0,0,0,1);
    }
    
    
    @media screen and (max-width: 500px) {
    
    
    }
    
    
        </style>
    
    
    </head>
    
    <body width="100%" style="margin: 0; padding: 0 !important; mso-line-height-rule: exactly; background-color: #f1f1f1;">
      <center style="width: 100%; background-color: #f1f1f1;">
        <div style="display: none; font-size: 1px;max-height: 0px; max-width: 0px; opacity: 0; overflow: hidden; mso-hide: all; font-family: sans-serif;">
          &zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;
        </div>
        <div style="max-width: 600px; margin: 0 auto;" class="email-container">
          <!-- BEGIN BODY -->
          <table align="center" role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="margin: auto;">
            <tr>
              <td valign="top" class="bg_white" style="padding: 1em 2.5em 0 2.5em;">
                <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
                  <tr>
                    <td class="logo" style="text-align: center;">
                      <h1><a href="#">Souhrudha Thanal Nidhi Limited</a></h1>
                    </td>
                  </tr>
                </table>
              </td>
            </tr><!-- end tr -->
            <tr>
              <td valign="middle" class="hero bg_white" style="padding: 2em 0 4em 0;">
                <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
                  <tr>
                    <td style="padding: 0 2.5em; text-align: center; padding-bottom: 3em;">
                      <div class="text">
                        <h2>""" + username + """ Thank you for contacting us. </h2>
                      </div>
                    </td>
                  </tr>
                  <tr>
                    <td style="text-align: center;">
                      <div class="text-author">
                        <img src="https://souhrudhathanal.web.app/static/media/logo.4b612cca.png" alt="Souhrudha Thanal Nidhi Ltd" style="width: 100px; max-width: 600px; height: auto; margin: auto; display: block;">
                        <h3 class="name">We will contact you as soon as possible.</h3>
                        <span class="position">Checkout our various schemes</span>
                         <p><a href="https://souhrudhathanal.web.app/" class="btn btn-primary">Our Schemes</a></p>
                       </div>
                    </td>
                  </tr>
                </table>
              </td>
            </tr><!-- end tr -->
          <!-- 1 Column Text + Button : END -->
          </table>
          <!-- <table align="center" role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="margin: auto;">
            <tr>
              <td valign="middle" class="bg_light footer email-section">
                <table>
                  <tr>
                    <td valign="top" width="33.333%" style="padding-top: 20px;">
                      <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                        <tr>
                          <td style="text-align: left; padding-right: 10px;">
                            <h3 class="heading">About</h3>
                            <p>A small river named Duden flows by their place and supplies it with the necessary regelialia.</p>
                          </td>
                        </tr>
                      </table>
                    </td>
                    <td valign="top" width="33.333%" style="padding-top: 20px;">
                      <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                        <tr>
                          <td style="text-align: left; padding-left: 5px; padding-right: 5px;">
                            <h3 class="heading">Contact Info</h3>
                            <ul>
                              <li><span class="text">203 Fake St. Mountain View, San Francisco, California, USA</span></li>
                              <li><span class="text">+2 392 3929 210</span></a></li>
                            </ul>
                          </td>
                        </tr>
                      </table>
                    </td>
                    <td valign="top" width="33.333%" style="padding-top: 20px;">
                      <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                        <tr>
                          <td style="text-align: left; padding-left: 10px;">
                            <h3 class="heading">Useful Links</h3>
                            <ul>
                              <li><a href="#">Home</a></li>
                              <li><a href="#">About</a></li>
                              <li><a href="#">Services</a></li>
                              <li><a href="#">Work</a></li>
                            </ul>
                          </td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                </table>
              </td>
            </tr><!-- end: tr -->
            <tr>
              <!-- <td class="bg_light" style="text-align: center;">
                <p>No longer want to receive these email? You can <a href="#" style="color: rgba(0,0,0,.8);">Unsubscribe here</a></p>
              </td> -->
            </tr>
          </table> 
    
        </div>
      </center>
    </body>
    </html>
    """, subtype='html')

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
            smtp.send_message(msg1)
            data = {"status": "success"}
        return Response(data)
    except:
        data = {"status": "failed"}
        return Response({"data": EMAIL_PASSWORD})
    # except:
    #     data = {"status": "failed"}
    #     return Response(data)
