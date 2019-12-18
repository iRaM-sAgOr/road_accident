import random

start = 0
end = 0
digit = ''
for i in range(1, 11):
    start = (start * 10) + 1
    end = (end * 10) + 9
    print("start and end is ", start, end)
    for j in range(1, 101):
        k = random.randint(start, end)
        print(j, k)
        digit=digit +'\n'+ str(k)
with open("number.txt", "w") as text_file:
     text_file.write(str(digit))