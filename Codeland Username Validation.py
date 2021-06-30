import re

def CodelandUsernameValidation(strParam):
    length = len(strParam) in range(1,26)
    first_letter = type(strParam[0]) == str
    alph_and_num = strParam.isalnum()
    contains_ = re.search("_", strParam)
    is__last = strParam[len(strParam)-1] == "_"
    if is__last:
        return "false"
    elif (length and first_letter and alph_and_num
        or length and first_letter and contains_):
        return "true"
    else:
        return "false"
  # code goes here

# keep this function call here 
print(CodelandUsernameValidation(input()))

