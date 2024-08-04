from django.shortcuts import render
from myapp.utils import send_with_attachment
from django.conf import settings

# Create your views here.

# This is without attachment
# def send_mail(request):
#     if send_mail_to_client():
#         msg = "Mail sent successfully"
#         return render(request, 'index.html',{'msg':msg})
#     else:
#         msg = "There was some error"
    
#     return render(request, 'index.html')


# this is with attachment

def send_mail(request):
    if request:
        subject = "Mail is sent from django server with attachment"
        message = "if you see attchment then task is successful"
        recepient_list = ['michealscottdrumroll@gmail.com',]
        file_path = f"{settings.BASE_DIR}/media/rename.jpg"
        send_with_attachment(subject, message, recepient_list, file_path)
        return render (request, 'index.html')
    else:
        return render (request, 'index.html')