#import pillow
#Enter the name of the image we wants to convert with its extension
#open up the image we want to resize using python
#specify the size we want to change it to
#save the new resized image

from PIL import Image
image_name = input('Enter the name of the Image you want to resize with its extention: ')
size1 = int(input('Enter the width of the new image: '))
size2 = int(input('Enter the height of the new image: '))

def resize_image(size1, size2):
    image = Image.open(image_name)
    print(f'Previous Size: {image.size}')
    resized_image = image.resize((size1, size2))
    resized_image.save(f'{size1}x{size2} Coverted image.jpg')
    print (f'{image_name} Converted Successfully')

resize_image(size1, size2)
