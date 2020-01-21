import os, fnmatch
from PIL import Image
import shutil

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

	def photo_copy(self, path_d):
		
		print('''
		-------- Choose ---------
		1 - One file
		2 - Multiple files
			''')
		
		self.path_destiny = path_d
		command = int(input('Your choice:'))

		if command == 1:			
			path_o = input('Insert the path origin location:')
			
			shutil.copy(path_o, self.path_destiny)
		
		elif command == 2:
			path_o = input('Insert the path origin location:')

			for file in os.listdir(path_o):
				shutil.copy(path_o + '\\' + file, self.path_destiny)

	def photo_delete(self):
		#To do
		pass


if __name__ == '__main__':

	print('''
		==============================================
--------------------- Photo Displayer ----------------------
		==============================================
	
	>> Options

	[1] -> Insert another path to your photos
	[2] -> Copy Photos from another path
	[3] -> Delete Photos	
		''')
	choice = int(input())

	if choice == 1:
		path_insert = input('Path Location:')
		path_location = path_insert
		
		object_photo = Photo_show(path_location)
		object_photo.show()

	elif choice == 2:

		path_d = input('Insert the path destiny location:')

		object_photo = Photo_show('')
		object_photo.photo_copy(path_d)

	elif choice == 3:
		pass
		#To do
	
	else:
		path_location = 'C:\\Users\\Pedro\\Desktop\\Photos'
		obj = Photo_show(path_location)
		obj.show()
	