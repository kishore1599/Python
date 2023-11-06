import shutil
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Define source and destination folders
source_folder = '/var/lib/jenkins/workspace/Endcard/Email-Task/sample'  # Update with your source folder path
destination_folder = '/var/lib/jenkins/workspace/Endcard/Email-Task/output'  # Update with your destination folder path

# Define the filename you want to move and email
filename = 'file.txt'  # Update with your filename

# Move the file
try:
    shutil.move(f'{source_folder}/{filename}', f'{destination_folder}/{filename}')
    print(f"Moved '{filename}' from '{source_folder}' to '{destination_folder}'")
except Exception as e:
    print(f"Error moving the file: {str(e)}")

# Email the file
smtp_server = 'smtp.gmail.com'  # Update with your SMTP server
smtp_port = 587  # Update with your SMTP server port
sender_email = 'kishoreb@clouddestinations.com'  # Update with your email
recipient_email = 'kishorekumar.b99@gmail.com'  # Update with recipient's email
password = 'sszq cvxf ndiz ejqr'  # Update with your email password

subject = 'File Moved and Attached'
body = 'Please find the attached file.'

message = MIMEMultipart()
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

# Attach the file
attachment = open(f'{destination_folder}/{filename}', 'rb')
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', f'attachment; filename= {filename}')
message.attach(part)

# Connect to the SMTP server and send the email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, recipient_email, message.as_string())
    server.quit()
    print(f"Email sent to '{recipient_email}' with the file attached.")
except Exception as e:
    print(f"Error sending the email: {str(e)}")


