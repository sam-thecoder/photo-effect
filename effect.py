from PIL import Image

import string
import random
from sorl.thumbnail import get_thumbnail

def random_filename(path=None, length=None):
	text = string.uppercase + string.lowercase + string.digits

	if path == None:
		path = 'greyscale/'

	if length == None:
		guess = random.randrange(8,15)
		length = range(guess)

	return path + ''.join( [random.choice(text) for x in length] ) + '.png'

def processor(img_filename):
	original = Image.open(img_filename)
	greyscale = original.convert('1')

	grey_filename = random_filename()
	greyscale.save(grey_filename)

	return None