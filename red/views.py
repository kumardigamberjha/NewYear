from django.shortcuts import render, redirect
from red.models import FormModel, SaveImage
from red.forms import FormForm, SaveImageForm
from red import views
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
from io import BytesIO

from django.http import JsonResponse
# Create your views here.
import base64
import requests

from django.core.files.base import ContentFile

@csrf_exempt
def Index(request):
    form = FormForm()
    inv = FormModel.objects.all().order_by('invite_date')
    if request.method == 'POST':
        form = FormForm(request.POST, request.FILES)

        name = request.POST.get('name')
        phone = request.POST.get('phone')
        adult = request.POST.get('adult')
        child = request.POST.get('child')
        kid = request.POST.get('kid')

        data_url = request.POST.get('img')
        # img_file = request.FILES.get('img')

        print("Name: ", name, phone, adult, child, kid)

        encoded_data = data_url.split(',')[1]

        # Decode the base64 string to binary data
        binary_data = base64.b64decode(encoded_data)

        # Create a ContentFile from binary data
        img_file = ContentFile(binary_data, name='decoded_image.png')

        s = FormModel(name=name, phone=phone, adult=adult, child=child, kid=kid)
        s.img = img_file
        s.save()
        print("Form Saved")

        encoded_img_data = base64.b64encode(binary_data).decode('utf-8')
        api_url = 'http://web.cloudwhatsapp.com/wapp/api/send'
        api_key = '427870336a6d45359a394f7f89cf5cba'
        mobile_number = '7814574759'  # Replace XXXX with the actual number

        url = "http://web.cloudwhatsapp.com/wapp/api/send?apikey={}&mobile={}&msg={}&img1={}".format(
            api_key, phone, f'''Welcome to RedCarpet!

            Dear Guest,

            We extend a warm welcome and present your exclusive access pass. To ensure a seamless experience, please follow these instructions:

            To Check the current status of the pass:
            
            https://redcarpet.codingindia.co.in/CheckQRCode/{phone}/ 

            Pass Deactivation Instructions:

            Upon entry, your access pass will be activated. To deactivate the pass after entry, please use the following deactivation link:

            https://redcarpet.codingindia.co.in/HandleQRCode/{phone}/ 

            Important Note:
            Please refrain from clicking on the deactivation link before entering the venue to avoid premature deactivation of your pass.

            Thank you for choosing RedCarpet. We look forward to hosting you and hope you enjoy your time with us!

            Warm regards,

            {request.user}''', f"https://redcarpet.codingindia.co.in/media/{s.img}"
        )

        try:
            response = requests.get(url)
            if response.status_code == 201:
                print("Message sent successfully!")
            elif response.status_code == 200:
                print("Message sent successfully!")
            else:
                print("Error sending message:", response.text)

        except requests.exceptions.RequestException as e:
            print("Error:", e)
    context = {'form': form, 'inv':inv}
    return render(request, 'redcar/index.html', context)


@csrf_exempt
def handle_qr_scan(request, mobile):
    print("Mobile: ", mobile)

    data = FormModel.objects.get(phone=mobile)
    data.is_active = False
    data.save()
    return render(request, "redcar/deact.html")


@csrf_exempt
def Check_qr_scan(request, mobile):
    print("Mobile: ", mobile)

    data = FormModel.objects.get(phone=mobile)
    if data.is_active:
        cardis = "Active"
    else:
        cardis = "Not Active"
    # data.is_active = False
    # data.save()
    context = {'cardis': cardis}
    return render(request, "redcar/deact.html")
   