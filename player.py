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

	def show(self): # Ok
		self.clear()
		os.chdir(self.path)

		for file in os.listdir(self.path):
			if fnmatch.fnmatch(file, self.extention):
				image = Image.open(file)
				image.show()

	def photo_copy(self, path_d): # Ok
		self.clear()

		print('''
		-------- Choose ---------
		1 - One File (Copy)
		2 - All Files (Copy)
			''')
		
		self.path_destiny = path_d
		command = int(input('Your choice:'))
		if command == 1:			
			#path_o = input('Insert the path origin location (One File):')
			c = 0
			dicio = {}
			for file in os.listdir(self.path):
				c += 1
				dicio[c] = file

			for keys, value in dicio.items():
				print('{} -> {}'.format(keys, value))

			id_choice = int(input('Insert the id value:'))
			if id_choice in dicio.keys():
				path_final = os.path.join(self.path, dicio[id_choice])
				shutil.copy(path_final, self.path_destiny)

			else:
				print('Inform a valid id')

		elif command == 2:
			#path_o = input('Insert the path origin location (Multiple File):')
			for file in os.listdir(self.path):
				shutil.copy(os.path.join(self.path, file), self.path_destiny)

		else:
			print('Not valid')

	def photo_delete(self): # Ok
		self.clear()

		print('''
		-------- Choose ---------
		1 - One File (Delete)
		2 - All Files (Delete)
			''')

		choice = int(input('Your choice:'))
		if choice == 1:
			
			dicio = {}
			c = 0
			for file in os.listdir(self.path):
				c += 1
				dicio[c] = file

			for keys, values in dicio.items():
				print('{} -> {}'.format(keys, values))
			
			id_choice = int(input('Choose your id:'))
			if id_choice in dicio.keys():
				os.remove(os.path.join(self.path, dicio[id_choice]))

		elif choice == 2:
			
			for filefolder, subfolder, filenames in os.walk(self.path): #Will just remove the files not the folders
				for filename in filenames:
					path_created = os.path.join(filefolder, filename)
					os.remove(path_created)
			#shutil.rmtree(self.path) #This command will delete everything

		else:
			print('Not valid')

	def photo_rename(self):
		self.clear()
		os.chdir(self.path)
		counter = 0
		changes = ''

		for file in os.listdir(self.path):
			file_name, file_exte = os.path.splitext(file)
			new_name = 'Photo - {}'.format(str(counter).zfill(2))
			os.rename(file, (new_name + file_exte))

			changes += file_name + file_exte + ' >> ' + new_name + file_exte +'\n'
			counter += 1
		print('Changes:\n{}'.format(changes))

	def zip_photo(self): # Ok
		# The zip will be save in the project folder, not in the especific directory
		# Later: try to save in another path
		self.clear()
		with ZipFile('Zip_photo1.zip', 'w') as zip_obj:
			for folderName, _, filenames in os.walk(self.path):
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

	if choice == 1: # Ok
		path_insert = input('Path origin location:')
		object_photo = Photo_show(path_insert)
		object_photo.show()

	elif choice == 2: # Ok
		path_origin = input('Path origin location:')
		path_destiny = input('Path destiny location:')
		object_photo = Photo_show(path_origin)
		object_photo.photo_copy(path_destiny)

	elif choice == 3: # Ok
		path_origin = input('Path origin location:')
		object_photo = Photo_show(path_origin)
		object_photo.photo_delete()
	
	elif choice == 4: # Ok
		path_to_rename = input('Insert the path of the multiple files to rename:\n')
		object_photo = Photo_show(path_to_rename)
		object_photo.photo_rename()

	elif choice == 5:
		path_to_zip = input('Insert the path to zip:\n')
		object_photo = Photo_show(path_to_zip)
		object_photo.zip_photo()