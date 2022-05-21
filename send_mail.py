import smtplib
from email.mime.text import MIMEText

def send_mail(customer, dealer, rating, comments):
    port = 2525 
    smtp_server = 'smtp.mailtrap.io'
    login = '34a3e246246b1e'
    password = 'e19fa17d5c0ff3'
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Commets: {comments}</li></ul>"
    sender_email = 'email1@example.com'
    receiver_email = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'E-Lifestyle Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send Mail  
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())