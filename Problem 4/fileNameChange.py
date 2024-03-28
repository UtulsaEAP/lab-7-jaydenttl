'''
Jayden Ly
6:09
./Problem 4/ParkPhotos.txt
'''
def fileNameChange():
    #type your code here
    file_name = input()
    file = open(file_name, 'r')
    data = file.readlines()
    for line in range(len(data)):
        data[line] = data[line].strip('\n')
     
    for i in range(len(data)):
        x = data[i].replace("_photo.jpg" ,"_info.txt")
        print(x) 
    
    
    
    return

if __name__ == '__main__':
    fileNameChange()