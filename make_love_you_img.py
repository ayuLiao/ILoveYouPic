from PIL import Image, ImageDraw, ImageFont



def character_generator(text):
    while True:
        for i in range(len(text)):
            yield text[i]

def gen_love_you_img(img_path, savepath):
    '''生成文字拼接而成的图片'''
    font_size = 7
    text = "我喜欢你！"
    # img_path = "header.jpeg"

    img_raw = Image.open(img_path)
    img_array = img_raw.load()

    img_new = Image.new("RGB", img_raw.size, (0, 0, 0))
    draw = ImageDraw.Draw(img_new)
    font = ImageFont.truetype('SimHei.ttf', font_size)
    ch_gen = character_generator(text)

    for y in range(0, img_raw.size[1], font_size):
        for x in range(0, img_raw.size[0], font_size):
            draw.text((x, y), next(ch_gen), font=font, fill=img_array[x, y], direction=None)

    # img_new.convert('RGB').save("save.jpeg")
    img_new.convert('RGB').save(savepath)

if __name__ == "__main__":
    gen_love_you_img('header.jpeg', 'save1.jpeg')