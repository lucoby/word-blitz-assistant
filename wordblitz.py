from Trie import Trie

class Word_Blitz_Player:
    def __init__(self):
        self.setup_trie()

    def setup_trie(self):
        self.trie = Trie('')
        for word in open('wordlist.txt').readlines():
            self.trie.add(word[:-1])



if __name__ == '__main__':
    self.word_blitz_player = Word_Blitz_Player('sreyuesibniuenah')
