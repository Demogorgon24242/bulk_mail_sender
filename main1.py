import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

data= pd.read_csv(r"Dummy Data from Email(Local) - Sheet1.csv")
email_col= data.get('email')
email_list= list(email_col)

for i in email_list:
#print(email_list)
    from_address = # your email id
    to_address =   str(i)

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Test email"
    msg['From'] = from_address
    msg['To'] = to_address

    # Create the message (HTML).
    html = """
     <html>
     <section class="container">
    
    <h1>Join Aluminati Today</h1>
    <h3>at Odisha's largest Alumini junction </h3>
    <br>
    <a href="https://6e9f-2402-8100-3868-cf3f-8d38-1e74-ffd1-201e.in.ngrok.io/"><button data-hover="click me!" <div>Connect</div></button></a>
    </section>

   </html>   """

    # Record the MIME type - text/html.
    part1 = MIMEText(html, 'html')

    # Attach parts into message container
    msg.attach(part1)

    # Credentials provided by google after registration
    username = ""
    password = ""

    # Sending the email
    # note - this smtp config worked for me, I found it googling around, you may have to tweak the # (587) to get yours to work
    server = smtplib.SMTP('smtp.gmail.com', 587)
    try:
        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.sendmail(from_address, to_address, msg.as_string())
        server.quit()
    except Exception as e:
        print(e)
