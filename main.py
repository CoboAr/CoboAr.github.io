from flask import Flask, render_template,request
import requests
import smtplib
from flask_bootstrap import Bootstrap5
import os

app= Flask(__name__)
Bootstrap5(app)

'''
# environment variables for email credentials
MAIL_ADDRESS_SENDER = os.environ.get("EMAIL_OF_SENDER")
MAIL_ADDRESS_RECEIVER = os.environ.get("EMAIL_OF_RECEIVER")
MAIL_APP_PW = os.environ.get("PASSWORD_KEY")

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = request.form
        name = data['name']
        email = data['email']
        phone = data['phone']
        message = data['message']
        print (f"{name}\n{email}\n{phone}\n{message}")
        send_email(name,email,phone,message)
        return render_template ("index.html", msg_sent=True)
    return render_template("index.html", msg_sent=False)

#sending email function
def send_email(name, email,phone, message):
    with smtplib.SMTP ("smtp.gmail.com", 587) as connection:
        connection.starttls ()
        connection.login (user=MAIL_ADDRESS_SENDER, password=MAIL_APP_PW)
        connection.sendmail (from_addr=MAIL_ADDRESS_SENDER,
                             to_addrs=MAIL_ADDRESS_RECEIVER,
                             msg=f"Subject: Data from form!\n\nName:{name}\nEmail: {email}\nPhone:{phone}\nMessage:{message}")
'''

@app.route("/")
def home():
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=False,port=8001)

