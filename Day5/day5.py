'''
Q:Declare an empty list
'''
empty_list = list()

'''
Q:Declare a list with more than 5 items
'''
list_item = ['Apple','Mango','Banana','Watermelon','Orange']

'''
Q:Find the length of your list
'''
print(len(list_item))


'''
Q:Get the first item, the middle item and the last item of the list
'''
print(f'first item:{list_item[0]}')
print(f'Middle item:{list_item[3]}')
print(f'last item:{list_item[-1]}')

'''
Q:Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
'''
mixed_data_types = ['VISHWA',24,str(180)+'cm','Unmarried','Patna']
print(mixed_data_types)


'''
Q:Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
'''
it_compaines = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle','Amazon']


'''
Q:Print the list using print()
'''
print(it_compaines)


'''
Q:Print the number of companies in the list
'''
print(len(it_compaines))


'''
Q:Print the first, middle and last company
'''
print('first:',it_compaines[0])
print('last:',it_compaines[-1])
middle_list = int(len(it_compaines)/2) #if its odd only 2
print(f'middle:{it_compaines[middle_list]}')


''''
Q:Print the list after modifying one of the companies
'''
print(it_compaines[0])
it_compaines[0]= 'Meta'
print(it_compaines[0])


'''
Q:Add an IT company to it_companies
'''
it_compaines.append('IT')
print(it_compaines)



'''
Q:Insert an IT company in the middle of the companies list
'''
it_compaines[middle_list] = 'AMD'   # middleList value found in the earlier problem


'''
Q:Change one of the it_companies names to uppercase (IBM excluded!)
'''
it_compaines[0] = it_compaines[0].upper()
print(it_compaines)


'''
Q:Join the it_companies with a string '#;
'''
add_sym = '# '.join(it_compaines)
print(add_sym)

'''
Q:Check if a certain company exists in the it_companies list.
'''
check = 'META' in it_compaines
print(check)


'''
Q:Sort the list using sort() method
'''
list_sort_ex = [5,7,3,2,64,11,88]
list_sort_ex.sort()
print(list_sort_ex)


'''
Q:Reverse the list in descending order using reverse() method
'''
list_sort_ex.sort(reverse=True)
print(list_sort_ex)



'''
Q:Slice out the first 3 companies from the list
'''
slice_it_com = it_compaines[0:3]
print(f'slice:{slice_it_com}')


'''
Q:Slice out the last 3 companies from the list
'''
slice_last = it_compaines[-3:]
print(f'Slice last:{slice_last}')


'''
Q:Slice out the middle IT company or companies from the list
'''
print(it_compaines)
midd_of_compa = (len(it_compaines) / 2)
midd_of_compa = int(midd_of_compa)
print(f'middle company:{it_compaines[midd_of_compa]}')


'''
Q:Remove the first IT company from the list
'''
it_compaines.pop(0)
print(it_compaines)


'''
Q:Remove the middle IT company or companies from the list
'''
it_company = [' Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
mid_company = len(it_company) / 2
mid_company = int(mid_company)
it_company.pop(mid_company)
print(it_company)


'''
Q:Remove the last IT company from the list
'''
print(it_company)
it_company.pop(-1) #removing the last item in the list.
print(it_company)



'''
Q:Remove all IT companies from the list
'''
print(it_company)
it_company.clear() #clear the item from the list
print(it_company)


'''
Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
'''
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
join_list = front_end + back_end
print(join_list)



'''
Q:After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
'''
full_stack = join_list.copy()
full_stack.insert(full_stack.index('MongoDB') + 1, 'Python')
full_stack.insert(full_stack.index('MongoDB') + 2, 'SQL')
full_stack.insert(full_stack.index('MongoDB') + 3, 'Redux')
print(full_stack)

'''
Q:The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

- Sort the list and find the min and max age
'''
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age = min(ages)
max_age = max(ages)
print(f'min age:{min_age}')  #min age
print(f'Max age:{max_age}') #max age

'''
Q:Add the min age and the max age again to the list
'''
max_age = min_age + max_age
ages.append(max_age)
print(f'New list after adding {max_age}:{ages}')


'''
Q:Find the median age (one middle item or two middle items divided by two)
'''
print(ages)
middle_item  = len(ages) / 2
print(ages[int(middle_item)])


'''
Q:Find the average age (sum of all items divided by their number )
'''
total_len= len(ages)
avg_age = (sum(ages) /total_len)
print(f'Avg age:{avg_age}')

'''
Q:Find the range of the ages (max minus min)
'''
range_max = max(ages)
range_min = min(ages)
range_max_min = range_max - range_min
print(f'Range of age:{range_max_min}')


'''
Q:Compare the value of (min - average) and (max - average), use abs() method
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
'''
tot_1 = range_min - avg_age
tot_2 = range_max_min - avg_age
val_0 = abs(tot_1)
val_1 = abs(tot_2)
if val_0 > val_1:
    print('min-average is greater')
if val_1 > val_0:
    print('max-average is greater')


'''
Q:Find the middle country(ies) in the countries list
'''
given_country = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
mid_country = len(given_country) / 2
mid_country = int(mid_country)
print(f'middle country:{given_country[mid_country]}')


'''
Q:Divide the countries list into two equal lists if it is even if not one more country for the first half.
'''
if mid_country % 2 == 0:
    first_half_country = given_country[0:mid_country]
    second_half_country = given_country[mid_country+1:]
    print(f'first half:{first_half_country}\nsecond half:{second_half_country}')
else:
    first_half_country = given_country[0:mid_country+1]
    second_half_country = given_country[mid_country+2:]
    print(f'first half:{first_half_country}\nsecond half:{second_half_country}')

