from  django.core.mail import send_mail,EmailMessage
from django.conf import settings

def send_mail_to_client():
    subject = "Sending mail from django"
    message = "If recieved then the task has been completed successfully."
    from_email = settings.EMAIL_HOST_USER
    recepient_list = ['michealscottdrumroll@gmail.com']
    send_mail(subject, message, from_email, recepient_list)


def send_with_attachment(subject, message, recepient_list, file_path):
    mail = EmailMessage(subject=subject, body= message, from_email=settings.EMAIL_HOST_USER, to=recepient_list)
    mail.attach_file(file_path)
    mail.send()
