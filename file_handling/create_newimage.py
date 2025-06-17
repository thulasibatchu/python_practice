fp1=open('logo.jfif','rb')
img_data=fp1.read()

fp2=open('new_logo1.png','wb')
fp2.write(img_data)

print("new image created")

fp1.close()
fp2.close()