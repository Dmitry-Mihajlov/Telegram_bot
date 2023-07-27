from telebot import types

def KEYBOARD_GUIDE_LINE(message):
    markup_line = types.InlineKeyboardMarkup()

    button_line_1 = types.InlineKeyboardButton('Сайт skysmart', url='https://skysmart.ru/articles/mathematic/grafik-linejnoj-funkcii?ysclid=lbrz9wgqhr237678774')
    button_line_2 = types.InlineKeyboardButton('Сайт yaklass', url='https://www.yaklass.ru/p/algebra/7-klass/lineinaia-funktciia-y-kx-m-9165/lineinaia-funktciia-y-kx-m-grafik-lineinoi-funktcii-9107/re-6bf40f08-aae0-443f-b0ec-de161575f7ee?ysclid=lbrzmxkg72942068140')
    button_line_3 = types.InlineKeyboardButton('YouTube', url='https://youtu.be/nbFbaio2xUg')
    markup_line.add(button_line_1, button_line_2, button_line_3)

    return markup_line

def KEYBOARD_GUIDE_SQUARE(message):
    markup_square = types.InlineKeyboardMarkup()

    button_square_1 = types.InlineKeyboardButton('Сайт skysmart', url='https://skysmart.ru/articles/mathematic/kvadratichnaya-funkciya-parabola?ysclid=lbs0fzvirb938387357')
    button_square_2 = types.InlineKeyboardButton('Сайт foxford',url='https://foxford.ru/wiki/matematika/grafikkvadratichnoyfunkzii?ysclid=lbs0ib7or8222590323')
    button_square_3 = types.InlineKeyboardButton('YouTube', url='https://youtu.be/hBICgw5YDyI')
    markup_square.add(button_square_1, button_square_2, button_square_3)

    return markup_square