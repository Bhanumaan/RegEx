import re

txt=("The Rain in Spain")
x=re.search("^The.*Spain$",txt)    #
print(x)

x=re.findall("[a-m]",txt)  #Find all lower case characters alphabetically between "a" and "m":
print(x)

trt=("he11o , he had 598 Dollars")

x=re.findall("\d",trt)    #Find all Digit Characters
print(x)

x=re.findall("he..o",trt)   #search for  sequence that starts with he and ends with o after any 2 characters in between
print(x)

x=re.findall("^he.*Dollars$",trt) #'.*' accepts zero to all value in between and
                                  # in case of '.+' there should be atleast one occurace
print(x)

x=re.findall("^he.?o",trt)    #  '.?' looks for 0 or 1 in between he and o , just one character
print(x)

x=re.findall("he.{2}o",trt)   #allows exactly 2 character in between he and o
print(x)

new=("The rain in ain spain falls mainly in the plains")
x=re.findall("rait|japan",new)    #checks wheather either one of rain or spain are in the given string or not
print(x)

if x:
    print("yes")
else:
    print("Nomatch ")

x=re.findall("\AThe",new)  #checks if string starts with "The" or not
                           #If yes it returns "The"
print(x)

x=re.findall(r"\brain",new)  #checks wheather a word exist staring with rain in the given string
                             # r before"\b" means relative string
print(x)

x=re.findall(r"ain\b",new)  #checks if a word exist that end with "ain" in the string
print(x)                       # In output one ain is from rain and one from spain

x=re.findall(r"\Bain",new)  #checks if ain exist in the sring anywhere expect in begining of any word
print(x)                    #word should not start with ain

x=re.findall(r"ain\B",new)   #checks if ain exist in the sring anywhere expect in end of any word
print(x)                    #word should not end with ain

x=re.findall("\D",new)  #return for every Non-digit charcter
print(x)

x=re.findall("\s",new) #return for every white space character
print(x)

x=re.findall("\S",new)   #return all non white space charcters
print(x)

x=re.findall("plains\Z",new)   #check if the string end with plains
print(x)

x = re.findall("\w", new)   #return all characters including alphabets , digits and underscore"_"
print(x)

x=re.findall("[0-9]",trt)          #return digits between 0 - 9
print(x)

x=re.findall("[0-5][0-9]",trt)     #return 2 digit number from 00 to 59
print(x)

x=re.findall("[a-zA-z]",trt)      #return Lower case character from a-z and upper case character from A-Z
print(x)

x=re.findall("[+]",trt)     #finds if there is any +character in string
if x: print("yes there is a + character")
else: print("No + character")

neew=("The rain in Spain ")
x=re.search("\s",neew)         #Finds the first white space character
print(x)
print(x.start())       #we use x.start to acces the first value from the return of x which is in a tuple format


x=re.split("\s",neew)    #this will retun where the string has been split with spaces
print(x)

x=re.split("\s",neew,1)          #Split the string at only at the first occurance 1 is putting limit
print(x)

x=re.sub("\s","-",neew)       #Substitute the white spaces with '-'
print(x)

x=re.sub("\s","+",neew,2)            #to control the number of substutions
print(x)                            #space was replaced by '+' only 2 times

x=re.search("ai",neew)
print(x)
print(x.span())                       #The span on the values
print(x.string)                       #This retrun the whole string
print(x.group())                      #This return the group we are searching

print("\n \n xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \n\n ")

x=re.search(r"\bS\w+",neew)         # \b means begins with , \w+ means till the end and S is to be found
print(x)
print(x.span())
print(x.string)
print(x.group())



