# to reach from (.) to (x)
# some path are blocked

print("""
    1     2      3     4     5     6     7     8    9     10    11    12   13     14
  _____________________________________________________________________________________
1 |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
  |_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|
2 |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
  |_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|
3 |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
  |_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|
4 |     |  >>>>>>↓  |  >>>>>>↓  |  >>>>>↓   |  >>>>>>↓  |  >>>>> ↓  |  >>>>>>↓  |     |
  |_____|__↑_____↓__|__↑_____↓__|__↑____↓___|__↑_____↓__|__↑_____↓__|__↑_____↓__|_____|
5 |   .>>>>↑  |  >>>>>>↑  |  >>>>>>↑  | >>>>>>>↑  |  >>>>>>↑  |  >>>>>>↑  |  x  |     |
  |_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|
    	
     
      
      """)


def mov():
    global m
    m = "Forward"
    
def left_mov():
    global l
    l ="Turn_Left "
   

def right_mov():
    global r
    r = "Turn_Right"
step = 0
c = 0
aa = ""
print("START")
for z in range (6):
    mov()
    step += 1
    print(step )
    print (m)
    
    left_mov()
    step += 1
    print(step)
    print(l)
    
    mov()
    step += 1
    print(step )
    print (m)
    
    for zz in range(2):
        right_mov()
        step += 1
        print(step)
        print(r)
       
        mov()
        step += 1
        print(step)
        print(m)
   
    left_mov()
    step += 1
    print(step)
    print(l)
    
print ("FNISH")
print(f"the total step took to complete is {step}")