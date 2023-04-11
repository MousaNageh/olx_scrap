from flask import render_template
from flask_mail import Message, Mail


class EmailSender:
    def __init__(self, app, recipient):
        self.recipient = recipient
        self.mail = Mail(app)

    def send_email(self, data):
        with self.mail.connect() as conn:
            subject = 'Olx Ads'
            message = render_template('olx_email.html', data=data)
            msg = Message(subject, recipients=[self.recipient], html=message)
            conn.send(msg)