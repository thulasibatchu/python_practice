fp1=open('data.txt','r')
data=fp1.read()
fp2=open('xyz.txt','a')
fp2.write(data)

print("new file created")
fp1.close()
fp2.close()