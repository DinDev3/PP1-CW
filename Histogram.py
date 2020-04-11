#Histogram for exam marks

count=0     #total students
range1=0    #mark 0-29
range2=0    #mark 30-39
range3=0    #mark 40-69
range4=0    #mark 70-100
stars = 0   #star count
total = 0    #total marks
count40 = 0  #no. of students with a pass mark (mark>40)
highest = 0   #lowest possible mark is 0. Therefore, highest mark is definitely greater than or equal to zero
lowest = 100    #highest possible mark is 100. Therefore, lowest mark is definitely less than or equal to 100
mark = 0

print("Enter -1 to display histogram")
print()     #to keep space(for clarity of output)

#receiving all acceptable inputs from user
while mark!=-1:
    try:                                        # for part C
          mark=float(input("Enter mark: "))

    except:
          print("This is not a number. Please enter a numeric character for mark")
          continue

    #catagorizing marks into ranges
    if mark<0 and mark!=-1:
        print("Please enter a positive mark")
    elif mark>=70 and mark<=100:
        range4 = range4 + 1
        count40 = count40 + 1       #for Part B
    elif mark>= 40 and mark<=69:
        range3 = range3 + 1
        count40 = count40 + 1       #for Part B
    elif mark>=30 and mark<=39:
        range2 = range2 + 1
    elif mark>=0 and mark<=29:
        range1 = range1 + 1

    if mark>=0 and mark<=100:       #verifying whether input is within the accepted range
        count = count + 1
        total = total + mark    #needed for part B
        if highest<mark:
            highest= mark       #assigning mark to highest mark. displayed as float because mark is in float. for part B
        if lowest>mark or count ==1:        #assigning mark to lowest mark either if the mark is less that the current lowest mark or 
            lowest= mark                    # or if the first mark has been entered. displayed as float because mark is in float. for part B
    elif mark>100:                     
        print("Please enter a mark which is less than or equal to 100")     #for part C
    
print()        #to keep space(for clarity of output)
print('-'*40)

#displaying the histogram
stars = range1                  #0-29 range stars
print("0-29\t", end="")
for stars in range (range1,0,-1):
    print("*",end="")
print()

stars = range2                  #30-39 range stars
print("30-39\t", end="")
for stars in range (range2,0,-1):
    print("*",end="")
print()

stars = range3                  #40-69 range stars
print("40-69\t", end="")
for stars in range (range3,0,-1):
    print("*",end="")
print()

stars = range4                  #70-100 range stars
print("70-100\t", end="")
for stars in range (range4,0,-1):
    print("*",end="")
print()

print('-'*40)           #for clarity of output
print()

print("Total number of students: ",count)


#part B

try:
    average= total/count
    average = round(average,2)                  #rounding off average to 2 decimal places, (if float values were entered as marks)
    print("The average mark is: ",average)

    print("Number of students with a pass mark: ",count40)

    print("The highest mark is: ",highest)

    print("The lowest mark is: ",lowest)

except ZeroDivisionError:
    print("\nEnter at least one number to display the average, highest/lowest mark and number of students with a pass mark.")                   #To avoid ZeroDivisionError, if no valid mark is entered before entering -1

print()     #to keep space(for clarity of output)
print("-"*40)


#vertical histogram, part D

print("0-29\t30-39\t40-69\t70-100")     #vertical histogram header

max_range= max(range1, range2, range3, range4)      #assigning the maximum value of the input variables to the variable, max_range
ranges = [range1, range2, range3]                   #list of first 3 ranges

for max_range in range(max_range,0,-1):
    for i in range(0,3):            #looping through first 3 ranges; i=index in list
        if ranges[i]>0:
            print(" * ", end="\t")
            ranges[i]-=1
        else:
            print("   ",end="\t")

    if range4>0:            #used out of 'for loop' to break line
        print(" * ")
        range4=range4-1
    else:
        print("   ")
