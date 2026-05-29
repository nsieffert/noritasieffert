import smtplib
from flask import Flask, render_template, request, redirect, flash, url_for
import emailpassword
from webemail import send_contact_email, EMAIL_KEY, PASSWORD_KEY

app = Flask(__name__)
app.secret_key = "my-new-super-secret-key"

SENDER = emailpassword.EMAIL_KEY
PASSWORD = emailpassword.PASSWORD_KEY

def send_contact_email(user_message):
    full_message = f"Subject: New Web Contact\n\n{user_message}"
    try:
        with smtplib.SMTP("://gmail.com", 587, timeout=10) as server:
            server.ehlo()  # Identify your server to Google
            server.starttls()  # Upgrade the connection to secure TLS encryption
            server.ehlo()

            server.login(SENDER, PASSWORD)
            server.sendmail(SENDER, SENDER, full_message)
            print("--- GMAIL CODE EXECUTION SUCCESSFUL ---")
    except Exception as e:
        print(f"--- GMAIL CODE ERROR: {e} ---")

@app.route("/home") # if you just use "/" it knows it is your home page
def home():
    return render_template("/home.html")

@app.route("/about")
def about():
    return render_template("/about.html")

@app.route("/fiction")
def fiction():
    return render_template("/fiction.html")

@app.route("/nonfiction")
def nonfiction():
    return render_template("/nonfiction.html")

@app.route("/sermons")
def sermons():
    return render_template("/sermons.html")

@app.route("/apologetics")
def apologetics():
    return render_template("/apologetics.html")

@app.route("/gallery")
def gallery():
    return render_template("/gallery.html")


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/send-message', methods=['POST'])
def handle_form():
    form_data = request.form.get('user_message')
    # This MUST print in your terminal now
    print("\n" + "=" * 40)
    print(f"SUCCESS: Flask route triggered!")
    print(f"Data received from browser: {form_data}")
    print("=" * 40 + "\n")

    send_contact_email(form_data)
    flash("Message sent successfully!")
    return redirect('/contact')


if __name__ == '__main__':
    app.run(debug=True, port=5000)