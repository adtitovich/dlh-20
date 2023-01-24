import sys

next(sys.stdin, None) # исключаем заголовок

for line in sys.stdin:
    for value in line.strip().split(',', 1)[0].split(' '):
        print(f'{value},1')