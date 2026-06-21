# nested loop are loops inside each other.Nested loops are used in python to break down
# the steps so the programm knows exactly what to do in what order to check it.
string = input("Please enter your own word :  ")
char = input("Please enter any alphabet:  ")
i = 0
count = 0
while(i < len(string)):
     if(string[i] == char):
          count = count + 1
     i = i +1 
print("The total Number of Times " , char , "has occured =" , count)      
#  This is a nested loop because it checks if that alphabet it in the first position if not
#  then moves on to the next one and it always adds one if the Character you entered  is MATCHES.