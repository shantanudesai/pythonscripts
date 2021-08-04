#! python3

import re, pyperclip

#  Create a regex for Phone numbers

phoneRegex=re.compile(r'''
# examples 415-555-0000, 555-0000, (415) 555-0000, 5555-0000 ext 12345, ext. 12345, x12345
(
(((\d\d\d)|(\(\d\d\d)))?    #area code ( optional)

(\s|-)    #first seperator

\d\d\d    #first 3 digits

- #seperator

\d\d\d\d  #last 4 digits

(((ext(\.)?\s)|x)      # extension word part (optoinal)

(\d{2,5}))?  # extension number part (optoinal)
)
''', re.VERBOSE)

# Create a regex for email Addresses

emailRegex=re.compile(r'''
[a-zA-Z0-9_.+]+      # name part
@# at symbol
[a-zA-Z0-9_.+]+ # domain name part

''', re.VERBOSE)


# TODO: Get the text off clipboard

text = pyperclip.paste()

# TODO: Extract email / phone number from this text

extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append((phoneNumber[0]))


#print(extractedEmail)
#print(allPhoneNumbers)

# TODO: Copy the extracted data to clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
print(results)
