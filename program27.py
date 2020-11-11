cnt, full_num, low_num = 0, 0, 10000
with open('C:\\Users\\zoomee\\Downloads\\27-A.txt', 'r') as inf:
    lines = inf.read().split('\n')
    first = lines.pop(0)
    while cnt < int(first):
        line = lines[cnt].split()
        if int(line[0]) > int(line[1]):
            full_num += int(line[0])
            diff_num = int(line[0]) - int(line[1])
            if not diff_num % 3 == 0:
                if low_num > diff_num:
                    low_num = diff_num
        else:
            full_num += int(line[1])
            diff_num = int(line[1]) - int(line[0])
            if not diff_num % 3 == 0:
                if low_num > diff_num:
                    low_num = diff_num
        cnt += 1

if full_num % 3 == 0:
    full_num = full_num - low_num
print(full_num)
