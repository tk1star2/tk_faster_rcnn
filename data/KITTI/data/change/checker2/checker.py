import os
from PIL import Image

for filename in os.listdir('.'):
	with open(filename, 'r') as file :
		if(filename=='checker.py' or filename=='a.txt'):
			file.close()
			continue
		string_index = filename[:-4]
		index = int(filename[:-4])
		#print(filename)
		#print('--------------------------------------------\n')
		#data = file.read()
		
		im = Image.open(filename)
		width, height = im.size
			
		if(int(width)!=1242 or int(height)!=375):
			print('{} ---- width : {}, height : {}\n'.format(filename, width, height))
			#print(filename)
			
	file.close()

	
