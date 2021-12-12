file1 = open(r'D:\20211\Introdution to ML and Data mining\Project\Preprocess data\Done.txt', 'r', encoding='utf-8')
file2 = open(r'D:\20211\Introdution to ML and Data mining\Project\Preprocess data\data.csv', 'a', encoding='utf-8')

for index, line in enumerate(file1):
    if index <= 1163:
        file2.write(f"{1}, {line}")
    elif index <= 2235:
        file2.write(f"{2}, {line}")
    elif index <= 4235:
        file2.write(f"{3}, {line}")
    elif index <= 6235:
        file2.write(f"{4}, {line}")
    elif index <= 8235:
        file2.write(f"{5}, {line}")
    elif index <= 10235:
        file2.write(f"{6}, {line}")
    elif index <= 12235:
        file2.write(f"{7}, {line}")
    elif index <= 13472:
        file2.write(f"{8}, {line}")
    elif index <= 15472:
        file2.write(f"{9}, {line}")
    else:
        file2.write(f"{10}, {line}")
    
file2.close()
file1.close()