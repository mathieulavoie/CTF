import CTFHelpers

offset_palette_duplication = 0xB5
offset_start_image_data = 0x435
nb_images = 86
images_directory = "frames"
green_color_byte_string = "\x00\x00\xFF\x00"
nb_palette_index_changes = 0x20


def change_palette(header):
    return header[:offset_palette_duplication] +\
        "".join(green_color_byte_string*nb_palette_index_changes) +\
        header[offset_palette_duplication + len(green_color_byte_string) * nb_palette_index_changes:]


def write_file(name, header, data):
    fo = open(name , "wb")
    fo.write(header)
    fo.write(data)
    fo.close()


xor_data = "\x00"
image_header = None

print "[-] Xoring images data from directory %s" % images_directory

for i in range(1, nb_images):
    image_path = "%s/%02d.bmp" % (images_directory,i)
    print "\t processing image %s" % image_path
    image = open(image_path, "rb").read()
    if image_header is None:
        image_header = image[:offset_start_image_data]

    xor_data = CTFHelpers.xor_strings([xor_data, image[offset_start_image_data:]])

write_file("xored_image.bmp",image_header,xor_data)
print "[-] Modifing Palette"
image_header = change_palette(image_header)
print "[-] Done! Writing image to disk"
write_file("xored_image_palette_edit.bmp",image_header,xor_data)