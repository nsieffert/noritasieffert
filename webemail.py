import smtplib
import emailpassword

EMAIL_KEY = emailpassword.EMAIL_KEY
PASSWORD_KEY = emailpassword.PASSWORD_KEY

def send_contact_email(user_message):
    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(EMAIL_KEY, PASSWORD_KEY)
    gmail.sendmail(EMAIL_KEY, EMAIL_KEY, user_message.as_string())
    gmail.quit()