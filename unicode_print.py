count = 0x0
while count <= 0xffff:
	try:
		print(chr(count), end='')
	except:
		pass
	count+=1
