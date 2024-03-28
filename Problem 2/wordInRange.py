'''
Name: Jayden Ly
Lab Time: 3/7/24 2:45 PM

Ex: If the input is:

    ./Problem 2/input1.txt
    ammoniated
    millennium
'''
def wordInRange():
    named = input()
    lower = input()
    upper = input()
    #Type your code here
    file = open(named, 'r')
    list = file.readlines()
    for i in range(len(list)):
        if (list[i].strip('\n') <= upper and list[i].strip('\n') >= lower):
            print(str(list[i].strip('\n')) + ' - in range')

        else:
            print(str(list[i].strip('\n')) + ' - not in range')
        
    return
        
if __name__ == '__main__':
    wordInRange()