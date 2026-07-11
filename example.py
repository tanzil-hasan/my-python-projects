import os 
os.system('cls')






a = 'tanzil hasan is a GOOD boy'
print(a.capitalize())

"""
Syntax:

variable = string.capitalize() 

Definition:
capitalize() method একটি string-এর প্রথম character কে uppercase (Capital)
এবং বাকি সব character কে lowercase করে দেয়।

Output:
Tanzil hasan is a good boy
"""









b = 'hello worLD'
print(b.title())

""" 
Syntax:
variable = string.title()

Definition:
title() method একটি string-এর প্রতিটি word-এর প্রথম character কে uppercase (Capital)
এবং প্রতিটি word-এর বাকি character গুলোকে lowercase করে দেয়.

Output : 
Hello World
"""










c = "Python is my favourite language"
print( c.center(50 , '*' ) )


"""
Syntax:

variable = string.center(width, fillchar)

Definition:
center() method একটি string-কে নির্দিষ্ট width-এর মধ্যে মাঝখানে (center)
স্থাপন করে এবং প্রয়োজন হলে দুই পাশে space বা নির্দিষ্ট character যোগ করে।

Output:
----------Python is my favourite language----------
"""









d = 'my name is mohammad siam molla and my mother is a cool women and i am proud of my mom '
print(d.count('m'))
print(d.count('my'))

"""
Syntax:
variable = string.count(value)
or,,
variable = string.count(value, start)
or,,
variable = string.count(value, start, end)

Definition:
count() method একটি string-এর মধ্যে নির্দিষ্ট character, word বা substring
কতবার আছে তা গণনা (count) করে।

Output:
14
3

Explanation:

1. d.count('m')

   * পুরো string-এর মধ্যে 'm' character টি মোট 14 বার আছে।
   * তাই output = 14

2. d.count('my')

   * পুরো string-এর মধ্যে "my" word টি মোট 3 বার আছে।
   * "my" পাওয়া যায়:
     my name ...
     ... and my mother ...
     ... of my mom
   * তাই output = 3

"""









text = "Hello"
print(text.encode())

name = "বাংলাদেশ"
l = name.encode('utf-8')
print(l)

"""
Syntex:
variable = string.encode()

Definition:
encode() method একটি string কে bytes এ রূপান্তর করে।

Output:
b'Hello'
b'\xe0\xa6\xac\xe0\xa6\xbe\xe0\xa6\x82\xe0\xa6\xb2\xe0\xa6\xbe\xe0\xa6\xa6\xe0\xa7\x87\xe0\xa6\xb6'


Function:
encode() → String to Bytes

✅ Network Communication

Internet বা socket দিয়ে data সাধারণত bytes আকারে পাঠানো হয়। so ,, encode() is used .
"""










b = b'Hello'
print(b.decode())
print(l.decode('utf-8'))

"""
Basic Syntex:
variable = bytes.decode(encoding)

Definition:
decode() method একটি bytes object কে string এ রূপান্তর করে।

Output:
Hello
বাংলাদেশ

Function:
decode() → Bytes to String

✅ File Handling

ফাইলে data bytes আকারে থাকতে পারে। পড়ার সময় bytes কে string এ convert করতে decode() লাগে।

"""
