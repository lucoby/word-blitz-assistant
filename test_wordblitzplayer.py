from wordblitz import Word_Blitz_Player
import unittest

class Test_Trie(unittest.TestCase):
    def setup_method(self, method):
        self.word_blitz_player = Word_Blitz_Player()


    def test_setup_trie(self):
        self.assertTrue(self.word_blitz_player.trie.is_word('cat'))
        self.assertTrue(self.word_blitz_player.trie.is_word('aardvarks'))
        self.assertTrue(self.word_blitz_player.trie.is_word('absterging'))

        self.assertTrue(self.word_blitz_player.trie.has_prefix('abstergi'))

        self.assertFalse(self.word_blitz_player.trie.is_word('abstergggg'))

        self.assertFalse(self.word_blitz_player.trie.has_prefix('absterq'))
