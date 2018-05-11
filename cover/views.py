from django.conf import settings
from django.shortcuts import render, HttpResponse
from PIL import Image, ImageFont, ImageDraw
from .utiis import COLOR_CODES, adjust_text_position
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
    anymal_list = [i for i in range(1, 41)]
    return render(request, 'cover/index.html', {
        'form': form,
        'anymal_list': anymal_list,
        'color_list': ["#%02x%02x%02x" % (color[0], color[1], color[2])
                       for color in COLOR_CODES]
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

    animal_path = settings.ROOT('orly', 'static', 'img', 'animal_img',
                                '{}.png'.format(animal_code))
    animal_img = Image.open(animal_path)
    animal_img = animal_img.resize((400, 400))

    color_number = COLOR_CODES[int(color_index)]
    canvas_img = Image.new('RGB', (500, 700), 'white')
    canvas_img.paste(animal_img, (50, 30))

    # get a drawing context
    d = ImageDraw.Draw(canvas_img)
    d.rectangle(((0, 0), (500, 15)), fill=color_number)
    d.rectangle(((0, 430), (500, 510)), fill=color_number)

    # draw text
    title_position, top_text_position, author_text_position, \
    guide_text_wposition, guide_text_hposition = adjust_text_position(
        title, top_text, author, guide_text, guide_text_placement)
    font = ImageFont.truetype(ttf_path, 70)
    d.text((title_position, 430), title, font=font, fill=(255, 255, 255, 128))
    font = ImageFont.truetype(ttf_path, 20)
    d.text((top_text_position, 15), top_text, font=font, fill=(0, 0, 0, 255))
    font = ImageFont.truetype(ttf_path, 35)
    d.text((guide_text_wposition, guide_text_hposition),
           guide_text, font=font, fill=(0, 0, 0, 255))
    font = ImageFont.truetype(ttf_path, 30)
    d.text((author_text_position, 600), author, font=font,
           fill=(0, 0, 0, 255))
    response = HttpResponse(content_type='image/png')
    canvas_img.save(response, format='PNG')
    return response
