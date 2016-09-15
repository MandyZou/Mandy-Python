import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
 
# Sender address
fromaddr = "annahunder@gmail.com"
# Receiver address
toaddr = "mandyzou02@gmail.com"
 
msg = MIMEMultipart()

# Details about the email 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Today's bill change"

# The body text of the email 
body = "Hi, here are the Missouri bill changes for today."
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "BillChange.csv"
attachment = open("BillChange.csv", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "12334456")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()