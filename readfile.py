# 이것은 파일읽기 입니다.

fp = open("lesson2.srt", "r", encoding="utf-8")

lines = fp.readlines()

str_list = []
str_1st = []
list = []

for line in lines:
    if(line != '\n'):
        str_list.append(line)
    elif(len(str_list) == 4):
        str = str_list[2].replace('\n', ' ') + str_list[3]
        str_1st.append(str)
        str_list.clear()
    else:
        str_1st.append(str_list[2])
        str_list.clear()

# print(str_1st)
str = ''
for str2 in str_1st:
    if str2[-2:-1] != '.':
        str3 = str2.replace('\n', ' ')
        str += str3
    else:
        str += str2
        list.append(str)
        str = ''

print(list)
fp.close()
