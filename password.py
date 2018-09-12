import re

def passtest(s):
    password=''

    #checks whether length is more than or equal to 6

    if len(s)<6: 
        print "Password is less than 6 characters, hence invalid."
        return

    #checks for uppercase character
    
    for i in s:
        if i.isupper():
            break
    else:
        print "Password does not contain any upper case characters, hence invalid."
        return

    #checks for lowercase character

    for j in s:
        if j.islower():
            break
    else:
        print "Password does not contain any lower case characters, hence invalid."
        return

    #checks for numeric character

    for k in s:
        if k.isdigit():
            break
    else:
        print "Password does not contain any numeric characters, hence invalid."
        return

    #checks for special character

    if not re.search('\W',s):
        if not re.search('_',s):
            print "Password does not contain any special charcaters, hence invalid."
            return

    print "Password is appropriate."
    password=s
    return password

password=''
while not password:
    print
    passw=raw_input("Enter password")
    password=passtest(passw)
    



