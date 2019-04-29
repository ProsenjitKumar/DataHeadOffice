from PIL import Image


# device count
print("How many devices are connected with Internet, Network----> Current")


# send image into devices


# open my image
open_image = input("To open my Image press 'P': ")
if open_image == 'p' or open_image == 'P':
    img = Image.open('prosenjit.jpg')
    img.show()
else:
    print("Something went Wrong")