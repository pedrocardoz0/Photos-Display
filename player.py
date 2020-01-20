import os, fnmatch
from PIL import Image


class Photo_show:

	def __init__(self, path_location):
		self.path = path_location # Inser the path of your files
		self.extention = '*.jpg'

	def show(self):
		os.chdir(self.path)

		for file in os.listdir(self.path):

			if fnmatch.fnmatch(file, self.extention):
				image = Image.open(file)
				image.show()


if __name__ == '__main__':

	print('''
		==============================================
--------------------- Photo Displayer ----------------------
		==============================================
	
	>> Options

	[1] -> Insert another path to your photos
		''')
	choice = int(input())

	if choice == 1:
		path_insert = input('Path Location:')
		path_location = path_insert
		object_photo = Photo_show(path_location)
		object_photo.show()

	else:
		path_location = 'C:\\Users\\Pedro\\Desktop\\Photos'
		obj = Photo_show(path_location)
		obj.show()
	