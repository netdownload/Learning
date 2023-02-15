inp = 'hello'
let_dct = ''
full_let = ''
dct = {}
# for i in range(len(inp)):
#     for letter in inp:
#         let_dct += letter
#         full_let += ''.join(let_dct)
#     inp = inp[1:]
#     let_dct = ''


for letter in full_let:
    if dct.get(letter) is None:
        dct[letter] = 1
    else:
        dct[letter] += 1

for key in sorted(dct.keys()):
    print(f'{key}: {dct[key]}')
