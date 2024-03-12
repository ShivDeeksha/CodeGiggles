from flask import Flask, render_template, send_file,request
from flask_mail import Mail,Message
import os

app = Flask(__name__)
from dotenv import load_dotenv

load_dotenv()

app.config['MAIL_SERVER'] = "smtp-mail.outlook.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] =  os.environ.get('smtp_username')
app.config['MAIL_PASSWORD'] =  os.environ.get('smtp_password')

mail=Mail(app)




@app.route('/home', methods=['GET', 'POST'])
def home():
    email_sent_successfully=False
    if request.method=='POST':
        name=request.form.get('name')
        email=request.form.get('mail')
        subject1=request.form.get('subject')
        message=request.form.get('message')
        msg=Message(
            subject="New Feedback from Giggles!!", body=f"Name: {name}\nE-mail: {email}\nSubject: {subject1}\n\n\n{message}", sender='honmanedisha@outlook.com', recipients=['honmanedisha@outlook.com']
        )
        try:
            mail.send(msg)
            email_sent_successfully = True
        except Exception as e:
            print(e)  # Log the error for debugging
            email_sent_successfully = False
    return render_template('index.html', email_sent_successfully=email_sent_successfully)

@app.route('/')
def loader():
    return render_template('loader.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/blogs')
def blogs():
    return render_template('blogs.html')

@app.route('/singleblog')
def singleblog():
    return render_template('singleblog.html')

@app.route('/resume')
def resume():
    return send_file('static/Disha Honmane.pdf')

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
    # app.run(debug=True)