import sys

print("DSi Common Key Generator")
print("------------------------")
print("1) Generate Key")
print("2) Exit")
key = input("Choose an option: ")
if key == "1" or key == 1:
	common_key = "AF {0}B F5 {0}6 A8 07 D2 {0}A EA 45 98 4F 04 74 28 6{0}".format(key)
	print(common_key)
	file = open("dsikey.bin","wb")
	file.write(bytearray.fromhex(common_key))
	file.close()
	sys.exit()
else:
	sys.exit()