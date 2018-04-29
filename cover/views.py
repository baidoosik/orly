from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings
from PIL import Image, ImageFont, ImageDraw
from .forms import CoverForm
from orly.utiis import COLOR_CODES
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
    # receive args
    title = request.GET['title']
    top_text = request.GET['top_text']
    author = request.GET['author']
    animal_code = request.GET['animal_code']
    color_index = request.GET['color_code']
    guide_text = request.GET['guide_text']
    guide_text_placement = request.GET['guide_text_placement']
    ttf_path = settings.ROOT('assets', 'fonts', 'NanumGothicCoding.ttf')
    font = ImageFont.truetype(ttf_path, 30)

    animal_path = settings.ROOT('orly', 'static', 'img', 'animal_img', '{}.png'.format(animal_code))
    animal_img = Image.open(animal_path)
    animal_img = animal_img.resize((300, 300))

    color_number = COLOR_CODES[int(color_index)]
    canvas_img = Image.new('RGB', (500, 700), color_number)
    canvas_img.paste(animal_img, (100, 100))

    # get a drawing context
    d = ImageDraw.Draw(canvas_img)
    # draw text, half opacity
    d.text((100, 10), title, font=font, fill=(0, 255, 255, 128))
    # draw text, full opacity
    d.text((100, 60), top_text, font=font, fill=(255, 0, 255, 255))
    # draw text, full opacity
    d.text((400, 500), author, font=font, fill=(255, 0, 255, 255))
    response = HttpResponse(content_type='image/png')
    canvas_img.save(response, format='PNG')
    return response
