import smtplib

content = "Python script email"

mail = smtplib.SMTP('smtp.gmail.com',587)

mail.ehlo()

mail.starttls()

mail.login('aayushkothari11@gmail.com','your password')

mail.sendmail('aayushkothari11@gmail.com','aayushkothari11@yahoo.com',content)

mail.close()

print("email sent")
