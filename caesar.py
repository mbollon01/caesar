def main():
	print ("Welcome to Caesar shift\n")
	print ("=======================\n")
	print ("1.Encrypt\n2.Decrypt")
	option = int(input("please input an option:   "))

	message = input('Enter Message: ')
	shift = int(input("input the shift:  "))

	if option ==1:
		encrypt(message, shift)
	elif option ==2:
		decrypt(message, shift)
	else:
		print("incorrect input")



def encrypt(message, shift):
	encrypted = ''

	for i in range(len(message)):
		if message[i].isalpha():
			if message[i].islower():
				num = ord(message[i]) + shift
				if num > ord('z'):
					num -= 26
					encrypted += chr(num)
				else:
					encrypted += chr(num)
			elif message[i].isupper():
				num = ord(message[i])+shift
				if num > ord('Z'):
					num -= 26
					encrypted += chr(num)
				else:
					encrypted += chr(num)
		elif ord(message[i]) == 32:
			encrypted += ' '
		else:
			encrypted += chr(num)

	print (encrypted)

	f = open('encrypted.txt','w')
	f.write(encrypted)
	f.close

	print("This message has been successfully written to encrypted.txt")


def decrypt(message, shift):
	decrypted = ''
	for i in range(len(message)):
		if message[i].isalpha():
			if message[i].islower():
				num = ord(message[i]) - shift
				if num > ord('z'):
					num -= 26
					decrypted += chr(num)
				else:
					decrypted += chr(num)
			elif message[i].isupper():
				num = ord(message[i]) - shift
				if num > ord('Z'):
					num -= 26
					decrypted += chr(num)
				else:
					decrypted += chr(num)
		elif ord(message[i]) == 32:
			decrypted += ' '
		else:
			decrypted += chr(num)

	print(decrypted)
	fileWrite(decrypted)

def fileWrite(decrypted):
	file = open('decrypted.txt','w')
	file.write(decrypted)
	file.close
	print("This message has been successfully written to decrypted.txt")

def fileRead():
	message = ''
	file = open("encrypted.txt","r")
	message += file.readline()
	shift = int(input("Enter shift: "))
	file.close()
	decrypt(message, shift)

if __name__ == "__main__":
	main()