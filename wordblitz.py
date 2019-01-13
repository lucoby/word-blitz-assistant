import pyautogui
import time

from Trie import Trie


class Word_Blitz_Player:
    def __init__(self):
        self.setup_trie()
        self.r = 4
        self.c = 4
        self.found_words = set()
        self.found_words_positions = []
        self.setup_positions(566, 458, 991, 878)
        self.wait = 0.03

    def setup_trie(self):
        self.trie = Trie('')
        for word in open('wordlist.txt').readlines():
            self.trie.add(word[:-1])

    def setup_positions(self, x0, y0, x1, y1):
        x_step_size = (x1 - x0) / self.c
        y_step_size = (y1 - y0) / self.r
        x_half_step = x_step_size / 2
        y_half_step = y_step_size / 2
        self.positions = [(int(x0 + x_half_step + i*x_step_size), int(y0 + y_half_step + j * y_step_size)) for j in range(4) for i in range(4)]

    def main(self, word):
        self.set_word(word)
        self.to_word_arr()
        self.find_words()
        self.enter_words()

    def set_word(self, word):
        self.word = word.lower()

    def to_word_arr(self):
      self.word_arr = [[c for c in self.word[self.c*i:self.c*i+self.c]] for i in range(self.r)]

    def find_words(self):
        explored = [[False for j in range(self.c)] for i in range(self.r)]

        for i in range(self.r):
            for j in range(self.c):
                self.__find_words_helper__(i, j, self.word_arr[i][j], [i * self.r + j], self.__explore__(i, j, explored))

    def __explore__(self, search_r, search_c, explored):
        return [[True if search_r == i and search_c == j else explored[i][j] for j in range(self.c)] for i in range(self.r)]

    def __find_words_helper__(self, search_r, search_c, prefix, positions, explored):
        steps = [(-1,-1), (-1, 0), (-1, 1),
                 ( 0,-1), ( 0, 0), ( 0, 1),
                 ( 1,-1), ( 1, 0), ( 1, 1)]
        for s in steps:
            i = search_r + s[0]
            j = search_c + s[1]
            if i >= 0 and i < self.r and j >= 0 and j < self.c and not explored[i][j]:
                new_prefix = prefix + self.word_arr[i][j]
                new_positions = positions + [i * self.r + j]
                if self.trie.is_word(new_prefix) and new_prefix not in self.found_words:
                    self.found_words.add(new_prefix)
                    self.found_words_positions.append(new_positions)

                if self.trie.has_prefix(new_prefix):
                    self.__find_words_helper__(i, j, new_prefix, new_positions, self.__explore__(i, j, explored))

    def enter_words(self):
        for word_positions in self.found_words_positions:
            self.enter_word(word_positions)

    def enter_word(self, positions):
        self.move_to(positions[0])
        pyautogui.mouseDown()
        for i in positions[1:]:
            self.move_to(i)
            time.sleep(self.wait)
        pyautogui.mouseUp()
        time.sleep(self.wait)

    def move_to(self, position):
        pyautogui.moveTo(self.positions[position][0], self.positions[position][1])

if __name__ == '__main__':
    word_blitz_player = Word_Blitz_Player()
    word_blitz_player.main('ZEACONITDAAOTSLU')
    # print(len(word_blitz_player.found_words))
