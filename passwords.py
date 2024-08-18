import random


def password(flag, count, answer):
    while len(answer) < count:
        if flag[0] == 0:
            n = random.randint(0, 9)
            answer.append(n)
        if flag[1] == 0:
            n = random.randint(97, 122)
            answer.append(chr(n))
        if flag[2] == 0:
            n = random.randint(65, 90)
            answer.append(chr(n))
        if flag[3] == 0:
            n = random.randint(33, 47)
            answer.append(chr(n))
    return answer


def create_flag(flag):
    print('Использовать цифры? да/нет')
    if input() == 'нет':
        flag[0] = 1
    print('Использовать строчные буквы? да/нет')
    if input() == 'нет':
        flag[1] = 1
    print('Использовать заглавные буквы? да/нет')
    if input() == 'нет':
        flag[2] = 1
    print('Использовать символы? да/нет')
    if input() == 'нет':
        flag[3] = 1
    return flag


def main():
    print('Введите длину пароля:')
    count = int(input())
    flag = [0, 0, 0, 0]
    answer = []
    flag = create_flag(flag)
    answer = password(flag, count, answer)
    random.shuffle(answer)
    print(*answer)


main()
