
file_1 = open("2022/Day_1/Calories.txt", "r")

#First Half

#x = 1
#elves = {}
#
#count = 0
#
#for line in (file_1): 
#
#    if line.strip():
#
#        count += int(line)
#        print(line)
#    else:
#        elves[x] = count
#        x +=1
#        count = 0
#
#if count:
#    elves[x] = count
#
#print(sorted(elves.values()))

#Second Half

x = 1
elves = {}

count = 0

for line in (file_1): 

    if line.strip():

        count += int(line)
        
    else:
        elves[x] = count
        x +=1
        count = 0

if count:
    elves[x] = count


elves_reversed = sorted(elves.values(),reverse=True)

top_3 = 0
second_count = 0

for x in elves_reversed:
    if second_count < 3:
        print (x)
        top_3 += x
        second_count += 1

print (top_3)


        