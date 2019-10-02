'''
Write a function definition for the following function and then invoke the function to test it
works. The function search_file(filename, searchword) should accept a
filename (a file fields.txt has been provided) and a user specified search
word. It searches every line in the file for an occurrence of the word and if it exists it prints
out the line preceded by the line number. Importantly it also writes the same output out to a
file called 'Inputfile'Modified.txt. This examines iteration, string examination,
accumulators, files and functions. Example test case below:
search_file("Fields-of-Athenry", "watched") ==>
9 - Where once we watched the small free birds fly.
21 - Where once we watched the small free birds fly.
26 - She watched the last star falling
33 - Where once we watched the small free birds fly.
'''

def search_file():
    x = input("Please enter the '.txt' filename excluding extension>>>")
    y = x + '.txt'
    search_file = open(y,'r')
    search_file1=open( x +'modified.txt','w')
    line_num = 0
    search_phrase = input("Please enter your keyword:") 
    for line in search_file.readlines():
        line_num += 1
        if line.find(search_phrase) >= 0:
            print("%s - %s"%(line_num,line))
            search_file1.writelines("%s - %s"%(line_num,line))
    print("Result written out to",x+"modified.txt")

search_file()
