import smtplib 
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart 
from email.mime.base import MIMEBase 
from email import encoders 

#user info sender to receiver
email_user = 'sender mail id' 
email_password = 'sender mail pass' 
email_send = 'receiver mail id' 
subject = 'Email test' 

#message format
msg = MIMEMultipart() 
msg['From'] = email_user 
msg['To'] = email_send 
msg['Subject'] = subject 

#email body content
body = 'Hello ! this message is sent from sid to shubh via python code' 

msg.attach(MIMEText(body,'plain')) 

#converting msg as string type
text=msg.as_string()

#protocols to send over smtp 
server = smtplib.SMTP('smtp.gmail.com',587) 
server.starttls() 
server.login(email_user,email_password) 
server.sendmail(email_user,email_send,text) 
server.quit()
