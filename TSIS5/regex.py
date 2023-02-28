import re

# 1
# pattern = r'a[b]*'
# print(re.search(pattern, 'doiabbbbsioaosapo'))

# 2
# pattern = r'a[b]{2,3}'
# print(re.search(pattern, "doiabbbbsioabbsapo"))

# 3
# sample = "this_is_a_sample"
# pattern = r'[a-z]+_[a-z]+'
# print(re.findall(pattern, sample))

# 4
# sample = "AaAnnnnBBBBnnmUUUp"
# pattern = r'[A-Z][a-z]+'
# print(re.findall(pattern, sample))

# 5
# pattern = r'a.*b$'
# print(re.search(pattern, "acb"))
# print(re.search(pattern, "a1234567b8"))
# print(re.search(pattern, "aaaabbbb"))

# 6
# sample = "This, is.. a te,st string."
# print(re.sub(r'[ ,.]', ':', sample))

# 7
# def snake_to_camel(s):
#     s = re.sub(r'_([a-z])', lambda match: match.group(1).upper(), s)
#     return s

# print(snake_to_camel('my_good_example'))
# print(snake_to_camel('python_tsis_lab5'))

# 8
# print(re.findall('[A-Z][^A-Z]*', "OneTwoThreeFourFive"))
# print(re.findall('[A-Z][^A-Z]*', "KSaj;j;JDJA:A"))
# print(re.findall('[A-Z][^A-Z]*', "example"))

# 9
# def insert_spaces(s):
#     s = re.sub(r'([A-Z][a-z]+)', r' \1', s)
#     return s.strip()

# s = 'InsertSpacesBetweenWordsStartingWithCapitalLetters'
# print(insert_spaces(s))

# 10
# def camel_to_snake(s):
#     s = re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()
#     return s

# s = 'ConvertCamelCaseStringToSnakeCase'
# print(camel_to_snake(s))