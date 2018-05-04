import os
from PIL import Image

for filename in os.listdir('.'):
	with open(filename, 'r') as file :
		if(filename=='rename.py'):
			file.close()
			continue
		lines = file.readlines()
		#print(filename)
		print(filename[:-4])
		string_index = filename[:-4]
		index = int(filename[:-4])
	file.close()

	group = ['Pedestrian', 'Cyclist', 'Car'] 	

#----------------------------------------------------
	dir = os.path.join('../test2', string_index+'.txt')
	with open(dir, 'w') as f :
		f.write('# PASCAL Annotation Version 1.00\n\n')
		f.write('Image filename : "{}"\n'.format(filename))
#==============================
		im = Image.open(os.path.join('../checker', string_index+'.png'))
		width, height = im.size

#=======================

		f.write('Image size (X x Y x C) : {} x {} x 3\n'.format(width, height))
		#f.write('Database : "The INRIA Rh-one-Alpes Annotated Person Database"\n')
		f.write('Database : "KITTI Database"\n')
		f.write('Objects with ground truth : ')
		
		num_object = 0
		indexs = []
		for line in lines:
			obj = line.strip().split(' ')
			indexs.append(obj[0])
			num_object += 1
		
		f.write('{} '.format(num_object))
		f.write('{ ')

		for index in indexs:
			f.write('"{}" '.format(index))
		f.write('}\n\n')
		
		f.write('# Note that there might be other objects in the image\n')
		f.write('# for which ground truth data has not been provided.\n\n')
		f.write('# Top left pixel co-ordinates : (0, 0)\n\n')

		num_object = 1
		for line in lines:
			obj = line.strip().split(' ')

			if(obj[0] == 'Pedestrian'):
				name = 'pedestrian'
			elif (obj[0] == 'Cyclist'):
				name = 'cyclist'
			elif (obj[0] == 'Car'):
				name = 'car'
			

			name = obj[0].lower()
	
			xmin = int(float(obj[4]))
			ymin = int(float(obj[5]))
			xmax = int(float(obj[6]))
			ymax = int(float(obj[7]))
	
			assert xmin >= 0.0 and xmin <= xmax, \
            			'Invalid bounding box x-coord xmin {} or xmax {} at {}.txt' \
                			.format(xmin, xmax, index)
        		assert ymin >= 0.0 and ymin <= ymax, \
            			'Invalid bounding box y-coord ymin {} or ymax {} at {}.txt' \
                			.format(ymin, ymax, index)
			w = int(xmax - xmin + 1.0)
			h = int(ymax - ymin + 1.0)
			x = int(xmin + 0.5*w)
			y = int(ymin + 0.5*h)
        
			if not obj[0] in group :
				continue;
#--------------------------------------------------------

			f.write('# Details for object {} ("{}")\n'.format(num_object, name))
			f.write('# Center point -- not available in other PASCAL databases -- refers\n')
			f.write('# to person head center\n')
			f.write('Original label for object {} "{}" : "{}"\n'.format(num_object, name, name))
			f.write('Center point on object {} "{}" (X, Y) : (721, 185)\n'.format(num_object, name))
			f.write('Bounding box for object {} "{}" (Xmin, Ymin) - (Xmax, Ymax) : ({}, {}) - ({}, {})\n\n'.format(num_object, name, xmin, ymin, xmax, ymax))
		
			num_object += 1

	f.close()


	
	
