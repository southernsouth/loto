import random



def ex_random():
    ex = random.randint(0, 9)

    return ex

def random_int(x):
    global ex_lost, r_lost

    while True:
        ex = ex_random()

        if ex in ex_lost:
            ex = ex_random()
        else:
            ex_lost.append(ex)

            if ex == 0:
                while True:
                    r = random.randint(1, 9)

                    if r in r_lost:
                        r = random.randint(1, 9)
                    else:
                        r_lost.append(r)
                        r = ' ' + str(r)

                        break
            elif ex == 1:
                while True:
                    r = random.randint(10, 19)

                    if r in r_lost:
                        r = random.randint(10, 19)
                    else:
                        r_lost.append(r)
                        r = str(r)

                        break
            elif ex == 2:
                while True:
                    r = random.randint(20, 29)

                    if r in r_lost:
                        r = random.randint(20, 29)
                    else:
                        r_lost.append(r)
                        r = str(r)

                        break
            elif ex == 3:
                while True:
                    r = random.randint(30, 39)

                    if r in r_lost:
                        r = random.randint(30, 39)
                    else:
                        r_lost.append(r)
                        r = str(r)

                        break
            elif ex == 4:
                while True:
                    r = random.randint(40, 49)

                    if r in r_lost:
                        r = random.randint(40, 49)
                    else:
                        r_lost.append(r)
                        r = str(r)

                        break
            elif ex == 5:
                while True:
                    r = random.randint(50, 59)

                    if r in r_lost:
                        r = random.randint(50, 59)
                    else:
                        r_lost.append(r)
                        r = str(r)

                        break
            elif ex == 6:
                while True:
                    r = random.randint(60, 69)

                    if r in r_lost:
                        r = random.randint(60, 69)
                    else:
                        r_lost.append(r)
                        r = str(r)

                        break
            elif ex == 7:
                while True:
                    r = random.randint(70, 79)

                    if r in r_lost:
                        r = random.randint(70, 79)
                    else:
                        r_lost.append(r)
                        r = str(r)

                        break
            elif ex == 8:
                while True:
                    r = random.randint(80, 89)

                    if r in r_lost:
                        r = random.randint(80, 89)
                    else:
                        r_lost.append(r)
                        r = str(r)

                        break
            elif ex == 9:
                while True:
                    r = random.randint(90, 99)

                    if r in r_lost:
                        r = random.randint(90, 99)
                    else:
                        r_lost.append(r)
                        r = str(r)

                        break

            ex = ex * 2

            x = x.replace('.' + str(int(ex / 2)), r)
            
            break
    
    return x

def start():
    global ex_lost, r_lost, x, y
    
    x = '------------You--------------'
    
    x1 = '.0|.1|.2|.3|.4|.5|.6|.7|.8|.9'
    x2 = '.0|.1|.2|.3|.4|.5|.6|.7|.8|.9'
    x3 = '.0|.1|.2|.3|.4|.5|.6|.7|.8|.9'

    x4 = '-----------------------------'

    ex_lost = []
    r_lost = []
    
    for i in range(5):
        x1 = random_int(x1)

    for i in range(10):
        x1 = x1.replace('.' + str(i), '  ')
    
    x += '\n' + x1

    ex_lost = []

    for i in range(5):
        x2 = random_int(x2)

    for i in range(10):
        x2 = x2.replace('.' + str(i), '  ')

    x += '\n' + x2

    ex_lost = []

    for i in range(5):
        x3 = random_int(x3)

    for i in range(10):
        x3 = x3.replace('.' + str(i), '  ')

    x += '\n' + x3
    x += '\n' + x4

    print(x)


    y = '----------Computer-----------'

    y1 = '.0|.1|.2|.3|.4|.5|.6|.7|.8|.9'
    y2 = '.0|.1|.2|.3|.4|.5|.6|.7|.8|.9'
    y3 = '.0|.1|.2|.3|.4|.5|.6|.7|.8|.9'

    y4 = '-----------------------------'

    ex_lost = []
    r_lost = []
    
    for i in range(5):
        y1 = random_int(y1)

    for i in range(10):
        y1 = y1.replace('.' + str(i), '  ')
    
    y += '\n' + y1

    ex_lost = []

    for i in range(5):
        y2 = random_int(y2)

    for i in range(10):
        y2 = y2.replace('.' + str(i), '  ')

    y += '\n' + y2

    ex_lost = []

    for i in range(5):
        y3 = random_int(y3)

    for i in range(10):
        y3 = y3.replace('.' + str(i), '  ')

    y += '\n' + y3
    y += '\n' + y4

    print(y)

def game():
    global x, y

    b = []

    for i in range(99):
        if i < 9:
            b.append(' ' + str(i + 1))
        else:
            b.append(str(i + 1))

    while True:
        r = random.randint(0, len(b))

        print('\nNumber ' + b[r])

        ip = input('\nLock up or continue? (l/c)\n')

        while True:
            if ip == 'l' or ip == 'c':
                break
            else:
                ip = input('\nInvalid input.\nLock up or continue? (l/c)\n')

        if ip == 'l':
            if b[r] not in x:
                print('\nThis number is not on the card. You lost.')
                break
            else:
                x = x.replace(b[r], '  ')
                print('\n' + x)

                if b[r] in y:
                    y = y.replace(b[r], '  ')
                print(y)

                del b[r]

                if x.count('  ') == 10 * 3 and y.count('  ') == 10 * 3:
                    print('\nDraw.')
                    break
                elif x.count('  ') == 10 * 3:
                    print('\nYou win!')
                    break
                elif y.count('  ') == 10 * 3:
                    print('\nComputer win!')
                    break
        else:
            if b[r] in x:
                print('\nThis number was on the card. You lost.')
                break
            else:
                print('\n' + x)

                if b[r] in y:
                    y = y.replace(b[r], '  ')
                print(y)

                del b[r]

                if x.count('  ') == 10 * 3 and y.count('  ') == 10 * 3:
                    print('Draw.')
                    break
                elif x.count('  ') == 10 * 3:
                    print('You win!')
                    break
                elif y.count('  ') == 10 * 3:
                    print('Computer win!')
                    break

start()
game()
