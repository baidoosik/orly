COLOR_CODES = [
    (85, 19, 93, 255),
    (113, 112, 110, 255),
    (128, 27, 42, 255),
    (184, 7, 33, 255),
    (101, 22, 28, 255),
    (80, 61, 189, 255),
    (225, 17, 5, 255),
    (6, 123, 176, 255),
    (247, 181, 0, 255),
    (0, 15, 118, 255),
    (168, 0, 155, 255),
    (0, 132, 69, 255),
    (0, 153, 157, 255),
    (1, 66, 132, 255),
    (177, 0, 52, 255),
    (55, 142, 25, 255),
    (133, 152, 0, 255),
]

'''
adjust_text_positio

설명:

글자 수에 따라서 텍스트 위치를 조정.

'''


def adjust_text_position(title, top_text, author,
                         guide_text, guide_text_placement):
    right = 500
    center = 250
    title_text_size = 36
    top_text_size = 10
    author_text_size = 15
    guide_text_size = 18

    title_position = center - title_text_size*0.5*len(title)
    top_text_position = center - top_text_size*0.5*len(top_text)
    author_text_position = right - author_text_size*len(author)

    if guide_text_placement == 'bottom_right':
        guide_text_wposition = 500 - guide_text_size*len(guide_text)
        guide_text_hposition = 510
    elif guide_text_placement == 'bottom_left':
        guide_text_wposition = 10
        guide_text_hposition = 510
    elif guide_text_placement == 'top_right':
        guide_text_wposition = 500 - guide_text_size * len(guide_text)
        guide_text_hposition = 50
    else:
        guide_text_wposition = 10
        guide_text_hposition = 50

    return title_position, top_text_position, author_text_position, \
        guide_text_wposition, guide_text_hposition
