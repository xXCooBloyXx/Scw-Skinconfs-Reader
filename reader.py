import os
import string

folder_path = './input'

if not os.path.exists('input'):
	os.makedirs('input')

for file_name in os.listdir(folder_path):
	if file_name.endswith('.scw'):
		file_path = os.path.join(folder_path, file_name)
		with open(file_path, 'rb') as file:
			data = file.read()
			geoms = []
			while b'GEOM' in data:
				offset = data.index(b'GEOM') + 6
				geom_text = ''
				while True:
					bytes = data[offset:offset+1]
					if bytes == b'\x00':
						break
					try:
						geom_text += bytes.decode()
					except UnicodeDecodeError:
						break
					offset += 1
				geom_text = ''.join(char for char in geom_text if char in string.printable)
				geom_text = geom_text.strip()
				geoms.append(geom_text)
				data = data[offset:]
		print(f'{file_name}:{"+".join(geoms)}')
print("Done!")
os.system("pause")