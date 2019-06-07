s1=input()
s2=s1.split()
s3=''
for i in range(0,len(s2)):
   s3=s3+(s2[i][-1::-1])+' '
print(s3)   
   
