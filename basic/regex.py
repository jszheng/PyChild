import re  # This file can be used as a reference_use of regex


# 013
def valid_pass(pass_str):
    if len(pass_str) < 8:
        print('password length must >= 8')
        return False
    if not re.search(r'\d', pass_str):
        print('password must include digit')
        return False


phonenumberRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = phonenumberRegex.search('My number is 415-424-4242')
# mo.group(2)
print('Phone number found: ' + str(mo.groups()))
print(type(mo.groups()))
print(mo.groups())

# 002
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Tina Fey and Batman')
print(mo1.group())
mo2 = heroRegex.search('Batman and Tina Fey')
print(mo2.group())

# 003
BatRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = BatRegex.search('Batmobile lost a wheel.')
print(mo.group())

# 004
batRegex = re.compile(r'Batwoman|Batman')
mo = batRegex.findall('The Adventure of Batwoman and Batman')
print(mo)

# 005
nonegreedyhaRegex = re.compile(r'(ha){3,5}?')
mo = nonegreedyhaRegex.search('hahahahahahahaha')
print(mo.group())

# 006 *
songRegex = re.compile(r'me')
mo = songRegex.findall('Awesome me')
print(mo)

# 007
alphRedex = re.compile(r'[^aeiouAEIOU]')
mo = alphRedex.findall('RoboCop eat baby food. BABY FOOD')
print(mo)

# 008
lineRegex = re.compile('.*', re.DOTALL)
mo = lineRegex.search('serve the public.\nProtect the innocent.')
print(mo)

# 009
robocop = re.compile(r'robocop', re.I)
mo = robocop.search('Robocop is part man, part machine, all cop')
print(mo)

# 010
nameRegex = re.compile(r'Agent \w+')
mo = nameRegex.sub('CENSORED', 'Agent Alice gave the secret document to Agent Bob')
print(mo)

# 011
secretagentRegex = re.compile(r'Agent (\w)\w*')
mo = secretagentRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Bob was a double agent')
print(mo)


