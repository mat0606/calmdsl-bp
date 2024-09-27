strValue = '@@{PC_IP}@@'
n = 2
replacementStr = '37'
# Replace last 3 characters in string with 'XXX'
strValue = strValue[:-n] + replacementStr
print (strValue)