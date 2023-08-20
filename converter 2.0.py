from PIL import Image
import os

def one_frame(picture):
    pic_width = picture.size[0]
    pic_height = picture.size[1]
    for h in range(pic_height):
        for w in range(pic_width):
            #print((h,w))
            pixel_position = w,h
            pixel_inf = picture.getpixel(pixel_position)
            #print(pixel_inf[0],end='')
            if pixel_inf[0] != 255:
                #print('o', end='')
                text.write('o')
            else:
                #print(' ', end='')
                text.write(' ')
        #print()
        #text.write('|||')
        text.write('\n')


folder_path = 'Frame_sequence'




n = 0
limit = 1500


txt_path ='demo.txt'
text = open(txt_path, 'w')
for image_name in os.listdir(folder_path):
    print(image_name)
    image_path = os.path.join(folder_path, image_name)
    image_file = Image.open(image_path)
    image_file.thumbnail((image_file.size[0]*2 ,image_file.size[1]))
    # print(image_file.size)
    one_frame(image_file)
    text.write('\n'*20)
    n += 1

input('press enter to exit')

