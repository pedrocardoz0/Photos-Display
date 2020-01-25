import os, fnmatch
from PIL import Image
import shutil
from zipfile import ZipFile

class Photo_show:

	def __init__(self, path_location, user):
		self.path = path_location # Inser the path of your files
		self.extention = '*.jpg'
		self.user = user
		self.logg = []

	@staticmethod
	def clear():
		os.system('cls')

	def show(self): # Ok
		self.clear()
		operation = 'View'
		#Temp (test)
		'''
		Mirror
		self.logg['USER'] = self.user
		self.logg['OPERAÇÃO'] = 'View'
		self.logg['ORIGEM'] = self.path
		self.logg['DESTINO'] = 'NULL'
		self.logg['TYPE'] = 'Multiple'
		'''

		os.chdir(self.path)

		for file in os.listdir(self.path):
			if fnmatch.fnmatch(file, self.extention):
				image = Image.open(file)
				image.show()

		self.report(operation, destiny='')

	def photo_copy(self, path_d): # Ok
		self.clear()
		operation = 'Copy'

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
		
		self.report(operation, destiny = self.path_destiny)

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

	def photo_rename(self): # Ok
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

	def report(self, operation, destiny):
		'''
		To start doing the .txt its going to be necessary to identify if the file already exist in the directory
		if yes, just append the respective values intead of that creat a new file

		In this case in special there is a problem, becasue, when we re-run the scrpit i mean when whe choose another
		operation inside the program we creat a new object that means that new object will be constucted and the __init__
		function will re build again, that will delete every thing that it had stored at that moment
		|
		V
		'''
		self.logg.append(self.user)
		self.logg.append(self.path)
		self.logg.append(destiny)
		self.logg.append(operation)
		self.logg.append(' ')
		print(self.logg)


if __name__ == '__main__':
	user = input('Username:')
	
	while True:
		os.system('cls')
		print('''
		==============================================
--------------------- Photo Displayer ----------------------
		==============================================
	
	>> Options (0 -> Exit)

	[1] -> Insert another path to your photos (viewer)
	[2] -> Copy Photos from another path
	[3] -> Delete Photos
	[4] -> Rename Photos
	[5] -> Zip Photos
	[6] -> Generate Report	
		''')
	
		choice = int(input())

		if choice == 0:
			break

		if choice == 1: # Ok
			path_insert = input('Path origin location:')
			object_photo = Photo_show(path_insert, user)
			object_photo.show()
			#object_photo.report()
			os.system('PAUSE')

		elif choice == 2: # Ok
			path_origin = input('Path origin location:')
			path_destiny = input('Path destiny location:')
			object_photo = Photo_show(path_origin, user)
			object_photo.photo_copy(path_destiny)
			os.system('PAUSE')

		elif choice == 3: # Ok
			path_origin = input('Path origin location:')
			object_photo = Photo_show(path_origin, user)
			object_photo.photo_delete()
		
		elif choice == 4: # Ok
			path_to_rename = input('Insert the path of the multiple files to rename:\n')
			object_photo = Photo_show(path_to_rename, user)
			object_photo.photo_rename()

		elif choice == 5: # Ok
			path_to_zip = input('Insert the path to zip:\n')
			object_photo = Photo_show(path_to_zip, user)
			object_photo.zip_photo()

		elif choice == 6:
			#To do
			pass