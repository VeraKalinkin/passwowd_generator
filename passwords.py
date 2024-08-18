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
    print("Use numbers? y/n")
    if input() == 'n':
        flag[0] = 1
    print("Use lowercase letters? y/n")
    if input() == 'n':
        flag[1] = 1
    print("Use uppercase letters? y/n")
    if input() == 'n':
        flag[2] = 1
    print("Use punctuation? y/n")
    if input() == 'n':
        flag[3] = 1
    return flag


def main():
    print("What should be the length of your password?")
    count = int(input())
    flag = [0, 0, 0, 0]
    answer = []
    flag = create_flag(flag)
    answer = password(flag, count, answer)
    random.shuffle(answer)
    print(*answer)


main()
