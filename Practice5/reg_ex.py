import re



#=============================================================================================================

def match_a_followed_by_bs(s):
    pattern = r'a b*'
    return bool(re.search(pattern, s))

test_strings_1 = ["a", "ab", "abb", "abbb", "ac", "ba", "abc", "aabbcc"]
for t in test_strings_1:
    print(f"{t:12} → {match_a_followed_by_bs(t)}")
print()

#============================================================================================================= 


def match_a_2to3_bs(s):
    pattern = r'a b{2,3}'
    return bool(re.search(pattern, s))

test_strings_2 = ["abb", "abbb", "ab", "abbbb", "a", "abbbbb", "xacbbby"]
for t in test_strings_2:
    print(f"{t:12} → {match_a_2to3_bs(t)}")
print()

#============================================================================================================= 


def find_snake_case_words(s):
    pattern = r'[a-z]+_[a-z]+'
    return re.findall(pattern, s)

examples_3 = [
    "hello_world test_case python_is_fun",
    "no_underscore here_one_two three",
    "ALL_CAPS snake_case_example"
]
for ex in examples_3:
    print(f"{ex}")
    print("→", find_snake_case_words(ex))
print()

#============================================================================================================= 


def find_title_words(s):
    pattern = r'[A-Z][a-z]+'
    return re.findall(pattern, s)

examples_4 = [
    "Hello World PythonIsFun JavaScript TypeScript",
    "I Am Traveling To Almaty City",
    "XMLHttpRequest HTML CSS"
]
for ex in examples_4:
    print(f"{ex}")
    print("→", find_title_words(ex))
print()

#=============================================================================================================


def a_anything_b(s):
    pattern = r'^a.*b$'
    return bool(re.match(pattern, s))

test_5 = ["ab", "a123b", "axxxb", "a b", "abc", "ba", "axb", "abbbb"]
for t in test_5:
    print(f"{t:10} → {a_anything_b(t)}")
print()

#=============================================================================================================

def replace_to_colon(s):
    pattern = r'[ ,.]'
    return re.sub(pattern, ':', s)

examples_6 = [
    "hello, world. this is python",
    "one two,three.four",
    "a,b.c d,e.f"
]
for ex in examples_6:
    print(f"{ex:30} → {replace_to_colon(ex)}")
print()

#============================================================================================================= 

def snake_to_camel(s):
    components = s.split('_')
    return components[0] + ''.join(word.capitalize() for word in components[1:])

test_snake = [
    "user_name",
    "first_name_last_name",
    "http_response_code",
    "alreadyCamel",
    "single"
]
for t in test_snake:
    print(f"{t:25} → {snake_to_camel(t)}")
print()

#============================================================================================================= 


def split_at_uppercase(s):

    return re.findall(r'[A-Z]?[a-z]*', s)


def split_camel_case(s):
    return re.split(r'(?=[A-Z])', s)

examples_8 = [
    "HelloWorldPythonCode",
    "XMLHttpRequest",
    "ThisIsATestString",
    "Already Split"
]
for ex in examples_8:
    print(f"{ex:25} → {split_camel_case(ex)}")
print()

#============================================================================================================= 

def insert_spaces_before_caps(s):
    return re.sub(r'([A-Z])', r' \1', s).strip()

examples_9 = [
    "HelloWorldFromPython",
    "ThisIsVeryImportantMessage",
    "XMLHttpRequestFactory",
    "IDontHaveSpacesYet"
]
for ex in examples_9:
    print(f"{ex:30} → {insert_spaces_before_caps(ex)}")
print()

#===========================================================================================================

def camel_to_snake(s):
    s1 = re.sub(r'([A-Z])', r'_\1', s)
    return s1.lower().lstrip('_')

test_camel = [
    "HelloWorld",
    "HTTPRequest",
    "UserProfileService",
    "thisIsAlready_snake",
    "XMLHttpRequest"
]
for t in test_camel:
    print(f"{t:25} → {camel_to_snake(t)}")
print()

