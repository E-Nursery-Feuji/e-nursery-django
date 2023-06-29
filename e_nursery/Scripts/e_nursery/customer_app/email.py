from django.core.mail import send_mail
import random
from django.conf import settings
import logging as log

#for the log level & file & formate
log.basicConfig(filename='e_nursery_log.log', level=log.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# for send otp
def send_opt_via_email(email):
    log.info("Send_otp_via_mail:starts")
    subject="forget password otp" #subject for email
    otp=random.randint(100000,999999) #otp genrate
    log.info("OTP genrated")
    message=f"Your opt is : {otp}" #message for email
    log.info(otp)
    email_from=settings.EMAIL_HOST #host email
    log.info(otp)
    send_mail(subject,message,email_from,[email]) #the send mail fiunction
    log.info("Email send")
    return otp