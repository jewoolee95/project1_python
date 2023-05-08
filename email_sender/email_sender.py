from email.message import EmailMessage
from sender2 import password
import ssl
import smtplib

email_sender = '' # private
email_password = password # private

email_receiver = 'genot11498@jobbrett.com'

subject = "Test for Project"
body = """
Test for Project.
Practice and Fighting!
"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())