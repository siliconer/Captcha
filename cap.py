
from PIL import Image
import os


im =  Image.open("captcha.gif")
im2 = Image.new("P",im.size,255)
#print im.getpixel((1,0))
#  im.size[1] height ;  im.size[0] width

import time
#count = 0
#for position in position:
#	new_img = im2.crop((position[0],0,position[1],im2.size[1]))
#	new_img.save("./%s.gif"%count)
#	count = count + 1
##
import math
class VectorCompare:
	def magnati(self,concordance):
		total = 0
		for word,count in concordance.iteritems():
			total = total + count*2
		return math.sqrt(total)
	def relation(self,concordance1,concordance2):
		relevance = 0
		top = 0
		for word,count in concordance1.iteritems():
			if concordance2.has_key(word):
				top = count*concordance2[word] + top
		return top/(self.magnati(concordance1)*self.magnati(concordance2))
# change pic into vectors

def buildvector(im):
	dic = {}
	count = 0
	for i in im.getdata():
		dic[count]=i
		count = count + 1
	return dic

iconset = ['0','1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
imageset=[]
for letter in iconset:
	for img in os.listdir('./iconset/%s/'%letter):
		temp  = []
		if img != "Thumbs.db" and img != ".DS_Store":
			temp.append(buildvector(Image.open("./iconset/%s/%s"%(letter,img))))
		imageset.append({letter:temp})
count = 0

# get the pic
for x in range(im.size[1]):
	for y in range(im.size[0]):
		pix = im.getpixel((y,x))
		if pix == 227 or pix == 220:
			im2.putpixel((y,x),0)

#im2.show()

#get the start and end

found_letter = False
getin_letter = False
start = 0
end = 0
position = []
for y in range(im2.size[0]):
	for  x in range(im2.size[1]):
		pixel = im2.getpixel((y,x))
		if pixel != 255:  #not white
			getin_letter = True
	if found_letter == False and getin_letter == True:
			found_letter = True
			start = y
	if found_letter == True and getin_letter == False:
			end = y
			position.append((start,end))
			found_letter = False
	getin_letter = False
print position
# [(6, 14), (15, 25), (27, 35), (37, 46), (48, 56), (57, 67)]

for position in position: # each pic
	new_img = im2.crop((position[0],0,position[1],im2.size[1]))  #crop the crp
	g = []
	v = VectorCompare()
	for image in imageset:
		for x,y in image.iteritems():
			if len(y) != 0:
				g.append(((v.relation(y[0],buildvector(new_img))),x))
	g.sort(reverse=True)
	print "",g[0]




