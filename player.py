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
		1 - One File (Copy)
		2 - All Files (Copy)
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

		else:
			print('Not valid')

	def photo_delete(self):
		print('''
		------- Choose --------
		1 - One File (delete)
		2 - All Files (delete)
			''')

		choice = int(input('Insert:'))

		if choice == 1:
			path_to_delete = input('Path and file:')

			os.remove(path_to_delete)

		elif choice == 2:

			path_to_delete = input('Path to delete everything:')

			for file in os.listdir(path_to_delete):
				os.remove(path_to_delete + '\\' + file)

		else:
			print('Not valid')

	def photo_rename(self):
		path_to_rename = input('Insert the path of the multiple files to rename:')
		os.chdir(path_to_rename)
		counter = 0

		for file in os.listdir(path_to_rename):
			file_name, file_exte = os.path.splitext(file)
			new_name = 'Photo - {}'.format(str(counter).zfill(2))
			os.rename(file, (new_name + file_exte))
			
			counter += 1

if __name__ == '__main__':

	print('''
		==============================================
--------------------- Photo Displayer ----------------------
		==============================================
	
	>> Options

	[1] -> Insert another path to your photos (viewer)
	[2] -> Copy Photos from another path
	[3] -> Delete Photos
	[4] -> Rename Photos	
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
		object_photo = Photo_show('')
		object_photo.photo_delete()
	
	elif choice == 4:
		object_photo = Photo_show('')
		object_photo.photo_rename()

	else:
		path_location = 'C:\\Users\\Pedro\\Desktop\\Photos'
		obj = Photo_show(path_location)
		obj.show()