from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings
from PIL import Image, ImageFont, ImageDraw
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
            form.cleaned_data
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
    image = Image.new('RGB', (256, 256), color='green')
    title = request.GET['title']
    top_text = request.GET['top_text']
    author = request.GET['author']

    ttf_path = settings.ROOT('assets', 'fonts', 'NanumGothicCoding.ttf')
    font = ImageFont.truetype(ttf_path, 30 )
    # get a drawing context
    d = ImageDraw.Draw(image)
    # draw text, half opacity
    d.text((10, 10), title, font=font, fill=(0, 255, 255, 128))
    # draw text, full opacity
    d.text((10, 60), top_text, font=font, fill=(255, 0, 255, 255))
    # draw text, full opacity
    d.text((60, 200), author, font=font, fill=(255, 0, 255, 255))
    response = HttpResponse(content_type='image/png')
    image.save(response, format='PNG')
    return response
