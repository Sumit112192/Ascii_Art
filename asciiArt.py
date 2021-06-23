from PIL import Image
import sys
unicodeValues = ["\u2588","\u2589", "\u258A", 
"\u258B","\u258C","\u258D",
"\u258E", "\u258F"]
#These are block unicodes
def returnIndex(pixel):
	return int(pixel//32)

fileName = sys.argv[1]
im = Image.open(fileName)
(height, width) = im.size
newWidth = 60
im = im.resize((int(height/width*newWidth), newWidth))
(newHeight, newWidth) = im.size
imGrayScale = im.convert('L')
pixels = list(imGrayScale.getdata())


pixel = 0
for _ in range(newWidth):
	for _ in range(newHeight):
		print(unicodeValues[returnIndex(pixels[pixel])], end="")
		pixel+=1
	print()

