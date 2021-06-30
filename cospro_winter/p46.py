string = "this is string constant"
char = 't'

char_count = 0
i = 0
while i < len(string):
    print(string[i], end='')
    if string[i] == char:
        char_count += 1
    i += 1
print("")
print(char + "s count : ", char_count)
