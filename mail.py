# Importing simple mail transfer protocol library
import smtplib

# server address, port number i.e, gmail server here
server = smtplib.SMTP('smtp.gmail.com',587)

# transport layer security
server.starttls()

# sender's mail id and password
server.login('sender_id@gmail.com','password')

# sending a mail with message
server.sendmail('sender_id@gmail.com','receiver_id@gmail.com','This mail is sent using python')

print("mail sent successfully")

# before running this code make sure that you have turned on "less secure app access" option
# in security settings of sender's account...