import requests

# ISS position
# api_url = 'http://api.open-notify.org/iss-now.json'

# response = requests.get(api_url)
# if response.status_code == 200:
#     print(response.text)
# else:
#     print(response.status_code)


# Number API
# number = 43
# api_url = 'http://numbersapi.com/'+str(number)

# response = requests.get(api_url)
# if response.status_code == 200:
#     print(response.text)
# else:
#     print(response.status_code)

# Telegram Bot Test

bot_name: str = 'stepiktestbot11022023_bot'
token: str = 'bot6181239100:AAGqBfSe-0Y-Y1o_hoFwwBzbsevrz0gj_c4'

api_url = 'https://api.telegram.org/' + token + '/getUpdates'
print(api_url)

response = requests.get(api_url)

if response.status_code == 200:
    print(response.text)
else:
    print(response.status_code)

# def say_something(number: int, word: str) -> str:
#     word = word.capitalize()
#     return word*number



arr = [-2, -1, 0, 1, 2, 3, 6]
arr2 = []
# set_num = set()
# for num in arr:
#     if int(num) == num:
#         set_num.add(num*num)
# arr2 = list(set_num)
# arr2.sort()
# print(arr2)
lp = 0
rp = 0
for index, (ln, rn) in enumerate(zip(arr, arr[1:])):
    if ln < 0 and rn >=  0:
        lp = index
        rp = index + 1
        print(lp)
    while lp >= 0 and rp < len(arr):
        if arr[rp] >= abs(arr[lp]):
            arr2.append(arr[rp]*arr[rp])
            rp += 1
        else:
            arr2.append(arr[lp]*arr[lp])
            lp -= 1
print(arr2)

# put your python code here
year = int(2020)
if year%12 == 2000%12:
    print('Дракон')
elif year%12 == 2001%12:
    print('Змея')
elif year%12 == 2002%12:
    print('Лошадь')
elif year%12 == 2003%12:
    print('Овца')
elif year%12 == 2004%12:
    print('Обезьяна')
elif year%12 == 2005%12:
    print('Петух')
elif year%12 == 2006%12:
    print('Собака')
elif year%12 == 2007%12:
    print('Свинья')
elif year%12 == 2008%12:
    print('Крыса')
elif year%12 == 2009%12:
    print('Бык')
elif year%12 == 2010%12:
    print('Тигр')
elif year%12 == 2011%12:
    print('Заяц')

num = 567689
reversed_num = 0
beg_num = num//100000*100000
while num%100000 > 0:
    rem = num%10
    reversed_num = reversed_num * 10 + rem
    num = num%100000//10
print(beg_num + reversed_num)

num = int(567689)
str_num = str(num)
if len(str_num) <= 5:
    str_num = str_num[::-1]
else:
    str_num = str_num[:-5]+str_num[1:][::-1]
print(str(int(str_num)))