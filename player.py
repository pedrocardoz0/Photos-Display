import os, fnmatch
from PIL import Image
import shutil
from zipfile import ZipFile

class Photo_show:

	def __init__(self, path_location):
		self.path = path_location # Inser the path of your files
		self.extention = '*.jpg'
	
	@staticmethod
	def clear():
		os.system('cls')

	def show(self):
		self.clear()
		os.chdir(self.path)

		for file in os.listdir(self.path):

			if fnmatch.fnmatch(file, self.extention):
				image = Image.open(file)
				image.show()

	def photo_copy(self, path_d):
		self.clear()

		print('''
		-------- Choose ---------
		1 - One File (Copy)
		2 - All Files (Copy)
			''')
		
		self.path_destiny = path_d
		command = int(input('Your choice:'))

		if command == 1:			
			path_o = input('Insert the path origin location (One File):')
			shutil.copy(path_o, self.path_destiny)
		
		elif command == 2:
			path_o = input('Insert the path origin location (Multiple File):')

			for file in os.listdir(path_o):
				shutil.copy(path_o + '\\' + file, self.path_destiny)

		else:
			print('Not valid')

	def photo_delete(self):
		self.clear()
		print('''
		------- Choose --------
		1 - One File (delete)
		2 - All Files (delete)
			''')

		choice = int(input('Insert:'))

		if choice == 1:
			file_to_delete = input('Path and file:')

			os.remove(file_to_delete)

		elif choice == 2:

			path_to_delete = input('Path to delete everything:')

			for file in os.listdir(path_to_delete):
				os.remove(path_to_delete + '\\' + file)

		else:
			print('Not valid')

	def photo_rename(self):
		self.clear()
		path_to_rename = input('Insert the path of the multiple files to rename:\n')
		os.chdir(path_to_rename)
		counter = 0
		changes = ''

		for file in os.listdir(path_to_rename):
			file_name, file_exte = os.path.splitext(file)
			

			new_name = 'Photo - {}'.format(str(counter).zfill(2))
			changes += file_name + file_exte + ' >> ' + new_name + file_exte +'\n'
			os.rename(file, (new_name + file_exte))
			counter += 1

		print('Changes:\n{}'.format(changes))

	def zip_photo(self):
		# The zip will be save in the project folder, not in the especific directory
		# Later: try to save in another path
		self.clear()
		path_to_zip = input('Insert the path to zip:\n')
		
		with ZipFile('Zip_photo.zip', 'w') as zip_obj:
			for folderName, _, filenames in os.walk(path_to_zip):
				for filename in filenames:
					file_path = os.path.join(folderName, filename)
					zip_obj.write(file_path)

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
	[5] -> Zip Photos	
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

	elif choice == 5:
		object_photo = Photo_show('')
		object_photo.zip_photo()

	else:
		path_location = 'C:\\Users\\Pedro\\Desktop\\Photos'
		obj = Photo_show(path_location)
		obj.show()