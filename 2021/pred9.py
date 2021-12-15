path= 'E:/Text/test.txt'

#Open/close file
f=open(path,'rt')
f.close()

#Try-except
try:
    f=open(path)
except IOError as e:
    print(e)
finally:
    f.close()

#With, more comfortable option
with open(path, 'rt') as f:

    #Read entire file
    data = f.read()
    print(data)

    #Read n bytes
    data1 = f.read(1)
    print(data1)
    data2 = f.read(5)
    data3 = f.read(10)
    
    #Browsing line by line
    for line in data:
        print(line)

    #Read 1 line
    line1 = f.readline()
    line2 = f.readline()

#Read file line by line
with open(path, 'rt+') as f:
    l = f.readline()
    while l: 
        l = f.readline()
        print(l)

#Read entire file into 2D list
with open(path, 'rt+') as f:
    lines = f.readlines()
    print(lines)

#Seek
with open(path, 'rt+') as f:
    f.seek(10, 0)     #Jump + 10 chars
    data = f.read(10)
    print(data)
    f.seek(5, 0)      #Jump + 5 chars
    data2 = f.read(10)
    print(data2)

#Write to text file, clear old content
path= 'E:/Text/test.txt'
with open(path,'w',) as f:    
   f.write("Monday\n")
   f.write("Tuesday\n")

#Write to text file, append
with open(path,'a',) as f:    
   f.write("Wednesday\n")   

#Read binary file
path= 'E:/Tomas/Text/Image.bmp'
with open(path,'rb',) as f:
   data = f.read() 
   print(data)

#Write to binary file
b = [0, 50, 100, 150]
ba = bytearray(b)
print(ba) #Print byte array

with open("data.shp",'xb',) as f:
   f.write(ba)