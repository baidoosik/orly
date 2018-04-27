from django.shortcuts import render, redirect, HttpResponse
from PIL import Image
from .forms import CoverForm
# Create your views here.

'''
index

설명:

image 생성에 필요한 데이터를 폼으로 받아서 처리
'''


def index(request):
    if request.method == 'POST':
        form = CoverForm(request.POST)
        if form.is_valid():
            return redirect('cover:index')
    else:
        form = CoverForm()
    return render(request, 'cover/index.html', {
        'form': form
    })
 

''''
image_generator


설명:

form 으로 받은 데이터를 통해서 이미지를 동적으로 생성.
'''


def image_generator(request):
    image = Image.new('RGB', (256, 256), color='yellow')
    response = HttpResponse()
    image.save(response, format='JPEG')
    return response
