import smtplib


def send_email(message):
    host = "smpt.gmail.com"
    port = 465

    sender = 'catastudent.32@gmail.com'
    password = 'dhenhscrkhymvozk'
    receiver = 'catastudent.32@gmail.com'



    with smtplib.SMTP("smtp.gmail.com",) as server:
        server.starttls() and server.login(user=sender, password=password)
        server.sendmail(from_addr=sender,
                        to_addrs=receiver,
                        msg=message)

