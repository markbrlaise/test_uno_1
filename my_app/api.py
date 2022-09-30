from crypt import methods
from flask import Flask, render_template, request
import smtplib,ssl



app = Flask(__name__)
#mail = Mail(app)

#app.config["MAIL_SERVER"] = "smtp.gmail.com"
#app.config["MAIL_PORT"] = 465
#app.config["MAIL_USERNAME"] = "hola@email.com"
#app.config["MAIL_PASSWORD"] = "dvet"
#app.config["MAIL_USE_SSL"] = True
#app.config["DEBUG"] = True
#
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')



#
@app.route("/form", methods=['POST','GET'])
def result():
    if request.method == "POST":
        smtp_server = "smtp.gmail.com"
        port = 467
        sender_email = "llouzano123@gmail.com"
        password = "1louzan0~"
        receiver_email = "nadjibmouhoun1@gmail.com"
        text = request.form.get("message")

        context = ssl.create_default_context()
        try:
            with smtplib.SMTP_SSL(smtp_server,port,context=context) as server:
                server.login(sender_email,password)
                server.sendmail(sender_email,receiver_email,text)
                server.quit()
            return render_template("result.html", result="Success!")
        except OSError:
            return render_template("result.html", result="Server unreachable!")
    else:
        return render_template("result.html", result="Failure!")


#        msg = Message(request.form.get("Subject"),sender="hola@email.com",recipient=[request.form.get("email")])
#        msg.body = request.form.get("message")
#        mail.send(msg)
#        return render_template("result.html", result="Success!")
#    else:
#        return render_template("result.html", result="Failure!")
#
#if __name__ == "__main__":
#    app.run(debug=True)
