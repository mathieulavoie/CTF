import Image
import os
import re
import CTFHelpers

def generate_images(data):
	for width in range(100,400):
		height = (len(data)/3)/width +1
		data_seq = re.findall("...",data) #Take 3 byte to create a pixel RGB. (Bitmap 24 bits)
		data_seq = map(lambda x : (ord(x[0]),ord(x[1]),ord(x[2])),data_seq)
		img = Image.new('L', (width, height))
		img.putdata(data_seq)
		print "\tImage of width %d saved"%width
		img.save("image_formatted_width-%s.bmp"%width,"BMP")

def decrypt(data):
	#Looking at the file in a hex editor, we see a 16 byte pattern. The key should be 16 bytes long
	#In a QR Code the background is White and the Foreground Black. plain text should be FFFFFF representing a white pixel.
	# K1 = C1 ^ P1
	key = CTFHelpers.xor_strings([data[:16], "\xFF"]) 
	return CTFHelpers.xor_strings([key, data])

	
encrypted_data = open("encrypted","rb").read()
print "[-] Encrypted file loaded"
decrypted_data = decrypt(encrypted_data)
print "[-] File decrypted"
print "[-] Generating images"
generate_images(decrypted_data)
print "[-] Images generated"



