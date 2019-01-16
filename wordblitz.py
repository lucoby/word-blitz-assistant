import time
from PIL import Image
import pyautogui
import pytesseract
import pyscreenshot as ImageGrab
import os

from Trie import Trie


class Word_Blitz_Player:
    def __init__(self, box):
        self.setup_trie()
        self.r = 4
        self.c = 4
        self.found_words = set()
        self.found_words_positions = []
        self.setup_positions(box)
        self.wait = 0.03

    def setup_trie(self):
        self.trie = Trie('')
        for word in open('wordlist.txt').readlines():
            self.trie.add(word[:-1])

    def setup_positions(self, box):
        x0, y0, x1, y1 = box
        x_step = (x1 - x0) / self.c
        y_step = (y1 - y0) / self.r
        x_half = x_step / 2
        y_half = y_step / 2
        self.click_pos = [(int(x0 + x_half + i*x_step), int(y0 + y_half + j * y_step)) \
                for j in range(4) for i in range(4)]
        self.sc_pos = [(int(x0 + 33 + i*x_step), int(y0 + 29 + j*y_step), \
                int(x0 + 65 + i*x_step), int(y0 + 69 + j*y_step)) \
                for j in range(4) for i in range(4)]

    def main(self):
        self.get_board()
        print(self.board)
        self.to_board_arr()
        self.find_words()
        self.enter_words()

    def get_board(self):
        im = self.take_screenshot()
        ocr_im = self.process_img(im)
        filename = "temp.jpg"
        ocr_im.save(filename, dpi=(300,300))
        self.ocr(filename)
        self.process_text()
        os.remove(filename)

    def take_screenshot(self):
        return ImageGrab.grab()

    def process_img(self, im):
        im_out = Image.new('RGB', (32*16, 40))
        for i, box in enumerate(self.sc_pos):
            region = im.crop(box)
            paste_box = (i*32, 0, i*32 + 32, 40)
            im_out.paste(region, paste_box)
        return im_out

    def ocr(self, im_file):
        self.board = pytesseract.image_to_string(Image.open(im_file)).lower()

    def process_text(self):
        self.board.replace(" ", "").replace("|", "i")

    def to_board_arr(self):
      self.board_arr = [[c for c in self.board[self.c*i:self.c*i+self.c]] for i in range(self.r)]

    def find_words(self):
        explored = [[False for j in range(self.c)] for i in range(self.r)]

        for i in range(self.r):
            for j in range(self.c):
                self.__find_words_helper__(i, j, self.board_arr[i][j], [i * self.r + j], self.__explore__(i, j, explored))

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
                new_prefix = prefix + self.board_arr[i][j]
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
        pyautogui.moveTo(self.click_pos[position][0], self.click_pos[position][1])

if __name__ == '__main__':
    word_blitz_player = Word_Blitz_Player((566, 458, 1001, 892))
    word_blitz_player.main()
