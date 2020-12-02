
# Demonstrated Python Program 
# to read file character by character 
  
  
file = open('development_set_enroll.txt', 'r') 
fw=open("adrese.txt", 'w')
  
while 1: 

    char = file.read(1) 
    if char =='\\':
    	char = '/'
    if not char:  
        break
    fw.write(char)
          
  
file.close() 