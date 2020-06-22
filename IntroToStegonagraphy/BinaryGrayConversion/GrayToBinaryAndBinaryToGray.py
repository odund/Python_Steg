'''
Binary To Gray and Gray to Binary conversion to use in Stegonagrapy
Created on Jun 21, 2020
@author: olegg
'''

''' XOR two characters '''
def xor_c(a, b): 
    return '0' if(a == b) else '1'
  
''' Flip the bit '''
def flip(c): 
    return '1' if(c == '0') else '0'
  
''' Convert binary string to gray string '''
def binarytoGray(binary):
    gray = ""
  
    ''' Most Significant Bit (MSB) of gray code is same as binary code '''
    gray += binary[0]
  
    ''' Compute remaining bits, next bit is comuted by doing XOR of previous  
        and current in Binary '''
    for i in range(1,len(binary)):
          
        ''' Concatenate XOR of previous bit with current bit '''
        gray += xor_c(binary[i - 1],binary[i])
  
    return gray
  
''' Convert gray code string to binary string '''
def graytoBinary(gray): 
  
    binary = ""
  
    ''' MSB of binary code is same as gray code '''
    binary += gray[0]
  
    ''' Compute remaining bits '''
    for i in range(1, len(gray)): 
          
        ''' If current bit is 0, concatenate previous bit
            Otherwise, concatenate invert of previous bit '''
        if (gray[i] == '0'):
            binary += binary[i - 1]
        else:
            binary += flip(binary[i - 1]) 
  
    return binary
  
''' Driver Code '''
binary = "01001"
print("Gray code of", binary, "is", binarytoGray(binary))
  
gray = "01101"; 
print("Binary code of", gray, "is", graytoBinary(gray))
