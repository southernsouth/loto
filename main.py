import numbers
from random import randint


class Loto():
    def __init__(self):
        self.numbers = []
        for i in range(90):
            self.numbers.append(i + 1)

        self.sort_numbers = []
        index_1 = 0
        index_2 = 9
        for i in range(9):
            self.sort_numbers.append(self.numbers[index_1:index_2])
            index_1 = index_2
            index_2 += 10
        self.sort_numbers[8].append(90)

        Loto.player_card(self)
        Loto.pc_card(self)
        Loto.game(self)
    
    def player_card(self):
        self.player_numbers_list = []  
        for i in range(9):
            numbers_for_indexs = []
            for x in range(len(self.sort_numbers[i])):
                numbers_for_indexs.append(x)
            indexs = []
            for x in range(3):
                index = randint(0, len(numbers_for_indexs) - 1)
                indexs.append(numbers_for_indexs[index])
                del numbers_for_indexs[index]
            self.player_numbers_list.append([self.sort_numbers[i][indexs[0]], self.sort_numbers[i][indexs[1]], self.sort_numbers[i][indexs[2]]])

        indexs = [[], [], []]
        for i in range(3):
            numbers_for_indexs = [0, 1, 2, 3, 4, 5, 6, 7, 8]
            for x in range(5):
                random_index = randint(0, len(numbers_for_indexs) - 1)
                indexs[i].append(numbers_for_indexs[random_index])
                del numbers_for_indexs[random_index]
            indexs[i].sort()

        self.player_numbers_in_game = [[[], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], []]]
        for i in range(3):
            for x in range(5):
                list_index = indexs[i][x]
                self.player_numbers_in_game[i][list_index].append(self.player_numbers_list[list_index][i])
        
        self.player_card_row1 =  '\n|.1|.2|.3|.4|.5|.6|.7|.8|.9|\n'
        for i in range(9):
            list = self.player_numbers_in_game[0]
            if len(list[i]) == 0:
                list[i] = ['  ']
            if len(str(list[0][0])) == 1:
                list[i][0] = ' ' + str(list[i][0])
            self.player_card_row1 = self.player_card_row1.replace('.%s' % (i + 1), str(list[i][0]))
        self.player_card_row2 =  '|.1|.2|.3|.4|.5|.6|.7|.8|.9|\n'
        for i in range(9):
            list = self.player_numbers_in_game[1]
            if len(list[i]) == 0:
                list[i] = ['  ']
            if len(str(list[0][0])) == 1:
                list[i][0] = ' ' + str(list[i][0])
            self.player_card_row2 = self.player_card_row2.replace('.%s' % (i + 1), str(list[i][0]))
        self.player_card_row3 =  '|.1|.2|.3|.4|.5|.6|.7|.8|.9|\n'
        for i in range(9):
            list = self.player_numbers_in_game[2]
            if len(list[i]) == 0:
                list[i] = ['  ']
            if len(str(list[0][0])) == 1:
                list[i][0] = ' ' + str(list[i][0])
            self.player_card_row3 = self.player_card_row3.replace('.%s' % (i + 1), str(list[i][0]))

        self.player_card_text =  '           [You]            \n'
        self.player_card_text += '+--+--+--+--+--+--+--+--+--+'    
        self.player_card_text += self.player_card_row1     
        self.player_card_text += self.player_card_row2    
        self.player_card_text += self.player_card_row3
        self.player_card_text += '+--+--+--+--+--+--+--+--+--+'

    def pc_card(self):
        self.pc_numbers_list = []  
        for i in range(9):
            numbers_for_indexs = []
            for x in range(len(self.sort_numbers[i])):
                numbers_for_indexs.append(x)
            indexs = []
            for x in range(3):
                index = randint(0, len(numbers_for_indexs) - 1)
                indexs.append(numbers_for_indexs[index])
                del numbers_for_indexs[index]
            self.pc_numbers_list.append([self.sort_numbers[i][indexs[0]], self.sort_numbers[i][indexs[1]], self.sort_numbers[i][indexs[2]]])

        indexs = [[], [], []]
        for i in range(3):
            numbers_for_indexs = [0, 1, 2, 3, 4, 5, 6, 7, 8]
            for x in range(5):
                random_index = randint(0, len(numbers_for_indexs) - 1)
                indexs[i].append(numbers_for_indexs[random_index])
                del numbers_for_indexs[random_index]
            indexs[i].sort()

        self.pc_numbers_in_game = [[[], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], []]]
        for i in range(3):
            for x in range(5):
                list_index = indexs[i][x]
                self.pc_numbers_in_game[i][list_index].append(self.pc_numbers_list[list_index][i])
        
        self.pc_card_row1 =  '\n|.1|.2|.3|.4|.5|.6|.7|.8|.9|\n'
        for i in range(9):
            list = self.pc_numbers_in_game[0]
            if len(list[i]) == 0:
                list[i] = ['  ']
            if len(str(list[0][0])) == 1:
                list[i][0] = ' ' + str(list[i][0])
            self.pc_card_row1 = self.pc_card_row1.replace('.%s' % (i + 1), str(list[i][0]))
        self.pc_card_row2 =  '|.1|.2|.3|.4|.5|.6|.7|.8|.9|\n'
        for i in range(9):
            list = self.pc_numbers_in_game[1]
            if len(list[i]) == 0:
                list[i] = ['  ']
            if len(str(list[0][0])) == 1:
                list[i][0] = ' ' + str(list[i][0])
            self.pc_card_row2 = self.pc_card_row2.replace('.%s' % (i + 1), str(list[i][0]))
        self.pc_card_row3 =  '|.1|.2|.3|.4|.5|.6|.7|.8|.9|\n'
        for i in range(9):
            list = self.pc_numbers_in_game[2]
            if len(list[i]) == 0:
                list[i] = ['  ']
            if len(str(list[0][0])) == 1:
                list[i][0] = ' ' + str(list[i][0])
            self.pc_card_row3 = self.pc_card_row3.replace('.%s' % (i + 1), str(list[i][0]))

        self.pc_card_text =  '            [PC]            \n'
        self.pc_card_text += '+--+--+--+--+--+--+--+--+--+'    
        self.pc_card_text += self.pc_card_row1     
        self.pc_card_text += self.pc_card_row2    
        self.pc_card_text += self.pc_card_row3
        self.pc_card_text += '+--+--+--+--+--+--+--+--+--+'

    def game(self):
        check = True
        while True:
            random_index = randint(0, len(self.numbers) - 1)
            number = str(self.numbers[random_index])
            del self.numbers[random_index]
            if len(number) == 1:
                number = ' ' + number

            print(self.player_card_text)
            print(self.pc_card_text)
            if self.player_card_text.count(' ') == 77:
                print('You win!')
                break
            if self.pc_card_text.count(' ') == 78:
                print('You lose')
                break
            print('\n+------+--+\n|Number|%s|\n+------+--+' % (number))
            
            while True:
                answer = input('Select or skip? (Y/n): ').upper()

                if answer == 'Y':
                    if number in self.player_card_text:
                        self.player_card_text = self.player_card_text.replace(number, '  ')
                        if number in self.pc_card_text:
                            self.pc_card_text = self.pc_card_text.replace(number, '  ')
                        break
                    else:
                        print('You lose. The number is not on the card.')
                        check = False
                        break
                elif answer == 'N':
                    if number in self.player_card_text:
                        print('You lose. The number was on the card.')
                        check = False
                        break
                    else:
                        if number in self.pc_card_text:
                            self.pc_card_text = self.pc_card_text.replace(number, '  ')
                        break

            if check == False:
                break

Loto()