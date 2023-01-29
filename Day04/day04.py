'''
Q: Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
- Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
- Declare a variable named company and assign it to an initial value "Coding For All".
- Print the variable company using print().
- Print the length of the company string using len() method and print().
'''

word_0,word_1,word_2,word_3 = 'Thirty ', 'Days ', 'Of ', 'Python'
concat = word_0 + word_1 + word_2 + word_3
print(concat)

string_0, string_1, string_2 = 'Coding ', 'For ', 'All'
concat_str = string_0 + string_1 + string_2
print(concat_str)

company = 'Coding For All'
print(company)
print('Len of the str:',len(company))


'''
Q:Change all the characters to uppercase letters using upper() method.
Change all the characters to lowercase letters using lower() method.
Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
Cut(slice) out the first word of Coding For All string.
Check if Coding For All string contains a word Coding using the method index, find or other methods.
'''

print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[7:])
print(company.find('Coding'))

substring = 'Coding'
print(company.index(substring)) #if return 0 | True or if return -1: False | if(.index(substring,5)) #value error


'''
Q:Replace the word coding in the string 'Coding For All' to Python.
- Change Python for Everyone to Python for All using the replace method or other methods.
- Split the string 'Coding For All' using space as the separator (split()) .
- "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
- What is the character at index 0 in the string Coding For All.
'''
print(company.replace('Coding','Python'))
print(company.split())
word_ex = 'Facebook, Google, Microsoft, Apple, IBM, Oracle'
print(word_ex.split(','))
print(company[0])



'''
Q:What is the last index of the string Coding For All.
- What character is at index 10 in "Coding For All" string.
- Create an acronym or an abbreviation for the name 'Python For Everyone'.
- Create an acronym or an abbreviation for the name 'Coding For All'.
- Use index to determine the position of the first occurrence of C in Coding For All.
- Use index to determine the position of the first occurrence of F in Coding For All.
- Use rfind to determine the position of the last occurrence of l in Coding For All People.
'''
str_cod = 'Coding For All'
print(str_cod[-1])
print(str_cod[10])

acro = 'Python For Everyone'
acro = 'PY4E'
print(acro)

acro_1 = 'Coding for All'
acro_1 = 'C4A'
print(acro_1)

print(str_cod.index('C'))
print(str_cod.index('F'))
print(str_cod.rfind('l'))


'''
Q:Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
- Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
- Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
- Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
'''
first_occ = 'You cannot end a sentence with because because because is a conjunction'
print(first_occ.find('because'))
print(first_occ.rindex('conjunction'))

len_find = first_occ.find('because')
end = len_find + len('because ')*3
print(first_occ[len_find:end])

print(first_occ.find('because'))

'''
Q:Does ''Coding For All' start with a substring Coding?
- Does 'Coding For All' end with a substring coding?
'''

cod_ex= 'Coding For All'
print(cod_ex.startswith('Coding'))
print(cod_ex.endswith('coding'))



