with open('input_1.txt', "r") as file_1:
    text_1 = file_1.read()
    str_1 = text_1
with open('input_2.txt', "r") as file_2:
    text_2 = file_2.read()
    str_2 = text_2
  
def levenstein(str_1, str_2):
    n, m = len(str_1), len(str_2)
    if n > m:
        str_1, str_2 = str_2, str_1
        n, m = m, n

    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if str_1[j - 1] != str_2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    a = (m - current_row[n]) / m
    a = str(a)
    with open("scores.txt",'w') as file:
            file  = file.write(a)
