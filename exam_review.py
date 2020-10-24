#WHILE statement examples
#Counting up to 10 from 1
i = 1
while i <= 10:
    print(i)
    i = i + 1
    
#Counting down from 10 to 1

i = 10
while i > 0:
    priint(i)
    i = i - 1


#FOR I IN RANGE statments    

for i in range(1,11):
    print(i)

for i in range(10,0,-1):
    print(i)


#COUNTER statement (count to 20 from 0 increasing by 2 each time)

counter = 0

while (counter != 20):
    counter += 2
    print(counter)


#ACCUMULATOR statement

counter = 0
sum = 0

while (counter != 10):
    counter += 2
    print(counter, end='')
    if (counter !=10):
        print("+", end='')
    sum += counter
print(" =", sum)


#How to neatly aline columes (table) - see other code animal lab / money one

#\t = tab
#\n = new line
#\' = single quote
#\" = double quote
#\\ = backslash
#-=     *=   /=


#Adding strings

s = "sam"

s += "smith"

print(s)#"sam smith"


