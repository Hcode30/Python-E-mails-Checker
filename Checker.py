import re
# Add Path to your emails txt file
myMails = open(r"D:\Python Projects\My E-Mails Checker\E-mails.txt")
Mails = myMails.readlines()
ValidCount, InvalidCount = 0, 0
for line in Mails:
    myChecker = re.search(
        r"[A-z0-9\.]+@[A-z0-9]+\.([A-z]{,4})", line)
    if myChecker != None:
        print(f"===> {myChecker.string.strip()} <=== Is A Valid Email")
        ValidCount += 1
    else:
        print(f"===> {line.strip()} <=== Is Not A Valid Email")
        InvalidCount += 1
print(f"Number Of Emails: {len(Mails)}\
    \nNumber Of Valid Emails: {ValidCount}\
    \nNumber Of Invalid Emails: {InvalidCount}")
# Project Done Successfully :D
