N = int(input("Enter random number : "))
output = ""
factors = ""

for i in range (2,N+1):
    divide = 0     
    if N%i == 0:    
        for j in range (1,i+1):    
            if i%j == 0:
                divide += 1
        if divide == 2:           
            factors += str(i) + ","

if N>1:
    output = "Prime factor(s) : " + faktor 
    l = len(output) - 1
    print(output[:l] + ".")

