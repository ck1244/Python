#prints an introduction to the program
print("This program will convert Days, Hours, Minutes and Seconds to Seconds")
def ToSeconds(): #defining the function
    return #used to return the value
days = int(input("Please enter days:")) #asks user to input days
hours = int(input("Please enter hours:")) #asks user to input hours
mins = int(input("Please enter mins:")) #asks user to input minutes
seconds = int(input("Please enter seconds:")) #asks user to input seconds

#calculation to turn all values into seconds
tdays = days * 86400
thours = hours*3600
tmins = mins *60
tsecs = seconds
#adds up all values
total = tdays + thours +tmins +tsecs
#prints the result
print("ToSeconds =>","(",days,"Day(s),",hours,"Hour(s),",mins,"Minute(s),",seconds,"Second(s)) =>", total,"Seconds")
