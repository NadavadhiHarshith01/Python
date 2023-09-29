import re
email="harshith@gmail.com"

if(re.search(".*gmail.*",email)):
    
    username=email[0:email.index("@")]
    domine=email[email.index("@")+1:]
    print("Username: ",username)
    print("Domine: ",domine)
else:
    print("Invlid email")

