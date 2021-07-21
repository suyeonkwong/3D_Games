from flask import Flask, render_template, jsonify, request
import smtplib
from email.mime.text import MIMEText
# for getting full paths to attachements
import os
# for encoding messages in base64
from base64 import urlsafe_b64encode
# for dealing with attachement MIME types
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from mimetypes import guess_type as guess_mime_type

from gmail.GmailAPI.testMyMail.common import our_email, gmail_authenticate

app=Flask(__name__,  static_url_path="", static_folder='./static/')

@app.route('/pass')
def passok():
    return render_template('passok.html')


@app.route('/')
@app.route('/mail')
def home():
    return render_template('password.html')

@app.route('/pass_find.ajax', methods=['POST'])
def pass_find():
    myMail = request.get_json()
    mailAddress = myMail['myMail']
    print(mailAddress)
    def add_attachment(message, filename):
        content_type, encoding = guess_mime_type(filename)
        if content_type is None or encoding is not None:
            content_type = 'application/octet-stream'
        main_type, sub_type = content_type.split('/', 1)
        if main_type == 'text':
            fp = open(filename, 'rb')
            msg = MIMEText(fp.read().decode(), _subtype=sub_type)
            fp.close()
        elif main_type == 'image':
            fp = open(filename, 'rb')
            msg = MIMEImage(fp.read(), _subtype=sub_type)
            fp.close()
        elif main_type == 'audio':
            fp = open(filename, 'rb')
            msg = MIMEAudio(fp.read(), _subtype=sub_type)
            fp.close()
        else:
            fp = open(filename, 'rb')
            msg = MIMEBase(main_type, sub_type)
            msg.set_payload(fp.read())
            fp.close()
        filename = os.path.basename(filename)
        msg.add_header('Content-Disposition', 'attachment', filename=filename)
        message.attach(msg)

    def build_message(destination, obj, body, attachments=[]):
        if not attachments: # no attachments given
            message = MIMEText(body)
            message['to'] = destination
            message['from'] = our_email
            message['subject'] = obj
        else:
            message = MIMEMultipart()
            message['to'] = destination
            message['from'] = our_email
            message['subject'] = obj
            message.attach(MIMEText(body))
            for filename in attachments:
                add_attachment(message, filename)
        return {'raw': urlsafe_b64encode(message.as_bytes()).decode()}

    def send_message(service, destination, obj, body, attachments=[]):
        return service.users().messages().send(
          userId="me",
          body=build_message(destination, obj, body, attachments)
        ).execute()
    
    if __name__ == "__main__":
     
        service = gmail_authenticate()
        send_message(service, mailAddress, "비밀번호입니다.", 
                    "비밀번호는 1입니다.")
        
    msg = "success"
    return jsonify(result = msg)

if __name__ == '__main__':
    app.run(debug=True)