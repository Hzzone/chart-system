
'''
传入文件路径，返回一个LIST
'''
def read_file(path):
	data = []
	with open(path, "rb") as f:
		while True:
			chunk = f.read(1)
			if not chunk:
				break
			data.append(ord(chunk.decode()))
	return data

if __name__ == "__main__":
	print(read_file("/Users/HZzone/Desktop/test.py"))