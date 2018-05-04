import os

for filename in os.listdir('.'):
	with open(filename, 'r') as file :
		if(filename=='reading.py'):
			file.close()
			continue
		print(filename)
		print('--------------------------------------------\n')
		data = file.read()
		
		import re
		
		objs = re.findall('\(\d+, \d+\)[\s\-]+\(\d+, \d+\)', data)
        	objs2 = re.findall(r'(\(\"[\w]+\"\))',data)	
		for ix2, obj2 in enumerate(objs2):
			print('inx1 {} : {}'.format(ix2, obj2[2:-2]))

		for ix, obj in enumerate(objs):
	   	     # Make pixel indexes 0-based
        		coor = re.findall('\d+', obj)
     			x1 = float(coor[0])
       			y1 = float(coor[1])
            		x2 = float(coor[2])
                	y2 = float(coor[3])
			
			print('inx2 {} : {} {} {} {}\n'.format(ix, x1, y1, x2, y2))
	file.close()

	
