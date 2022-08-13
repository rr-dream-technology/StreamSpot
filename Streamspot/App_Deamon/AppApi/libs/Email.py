from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl

class Mail:

    def __init__(self):
        self.port = 465
        self.smtp_server_domain_name = "smtp.gmail.com"
        self.sender_mail = "rr3343500@gmail.com"
        self.password = "equhrtguhxxbduwt"
    

    def send(self, emails, subject, content):
        ssl_context = ssl.create_default_context()
        service = smtplib.SMTP_SSL(self.smtp_server_domain_name, self.port, context=ssl_context)
        service.login(self.sender_mail, self.password)
        
        for email in emails:
            result = service.sendmail(self.sender_mail, emails,f"Subject: {subject}\n{content}")
            print(result)

        service.quit()

    def setContent(self, otp, email):
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Link"
        msg['From'] = self.sender_mail
        msg['To'] = email

        html= """\
            <div style="font-family: Helvetica,Arial,sans-serif;min-width:1000px;overflow:auto;line-height:2">
            <div style="margin:50px auto;width:70%;padding:20px 0">
                <div style="border-bottom:1px solid #eee">
                <a href="" style="font-size:1.4em;color: #00466a;text-decoration:none;font-weight:600"></a>
                </div>
                <p style="font-size:1.1em">Hi,</p>
                <p>Thank you for choosing Stream Spot. Use the following OTP to complete your Sign Up procedures. OTP is valid for 5 minutes</p>
                <h2 style="background: #00466a;margin: 0 auto;width: max-content;padding: 0 10px;color: #fff;border-radius: 4px;">      
                {otp}
                </h2>
                <p style="font-size:0.9em;">Team ,<br />Stream Spot</p>
                <hr style="border:none;border-top:1px solid #eee" />
                <div style="float:right;padding:8px 0;color:#aaa;font-size:0.8em;line-height:1;font-weight:300">
                </div>
            </div>
            </div>""".format(otp=otp)

        part2 = MIMEText(html, 'html')
        msg.attach(part2)
        return msg.as_string()

