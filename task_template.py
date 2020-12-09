'''
author =
'''
TEXTS = ['''Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley.\n''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.\n''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

username_password = {
"bob" : "123",
"ann" : "pass123",
"mike" : "password123",
"liz" : "pass123"
        }

while True:
    username_password = {
        "bob": "123",
        "ann": "pass123",
        "mike": "password123",
        "liz": "pass123"
    }
    login_username = str(input("Please enter your username:\n"))
    login_password = str(input("Please enter your password:\n"))

    if login_username in username_password.keys() and login_password == username_password[login_username]:
        print("Logged on")
        break
    else:
        print("Wrong username or password")
print(70*"_")
print(*TEXTS, sep='\n- ')
print(70*"_")
#number of words total in chosen text
chosen_text=(input("Select text you prefer (1,2,3): "))
print(70*"_")
decay_number = (TEXTS[int(chosen_text) - 1].split())
print("Number of words in total: ", + len(decay_number))
print(70*"_")
#number of words starting with capital letter
capital_letters = []
n=0
while 0<=n<(len(decay_number)):
    decay_letters = (decay_number[n][0]) # with index "n" found
    if decay_letters.isupper():
        capital_letters.append(decay_letters)  #add first CAPITAL/BIG letters to the list
    n += 1
print("The number of words starting with capital letter ",len(capital_letters)) #counting all capital/big letters
print(70*"_")
#number of uppercase words
uppercase_words =sum(map(str.isupper,(TEXTS[int(chosen_text) - 1].split())))
print("The number of uppercase words found in the string is: ",uppercase_words)
print(70*"_")
#number of lowercase words
lowercase_words =sum(map(str.islower,(TEXTS[int(chosen_text) - 1].split())))
print("The number of lowercase words found in the string is: ",lowercase_words)
print(70*"_")
#number of numeric-only words (e.g. 100, not 100N)
res = [int(ele) if ele.isdigit() else ele for ele in decay_number]
number_count = len([val for val in res if isinstance(val, int)])
print("The number of numeric-only words found in the list is:", number_count)
print(70*"_")
i = 0
word_lenghts = [] #it will be a list of lengts numbers
while 0 <= i < len(TEXTS[int(chosen_text) - 1].split()):
    word_lenghts.append((len(TEXTS[int(chosen_text) - 1].split()[i])))
    i = i+1
ix = min(word_lenghts)
l= []
while min(word_lenghts) <= ix <= max(word_lenghts):
    l.append(word_lenghts.count(ix))
    ix = ix + 1

n=1
while 1 <= n <= max(word_lenghts):
    if word_lenghts.count(n) == 0:
        pass
    else:
        print(n,word_lenghts.count(n)*"*",word_lenghts.count(n))
    n=n+1
print(70*"_")
sum_numbers=sum(([val for val in res if isinstance(val, int)]))
print("If we summed all the numbers in this text we would get: ",sum_numbers)
