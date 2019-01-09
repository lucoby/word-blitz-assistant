from Trie import Trie
import unittest

class Test_Trie(unittest.TestCase):
    def setup_method(self, method):
        self.mytrie = Trie('')
        self.mytrie.add('cat')
        self.mytrie.add('cab')
        self.mytrie.add('dog')
        self.mytrie.add('what')
        self.mytrie.add('whatsup')

    def test_add(self):
        self.assertTrue('c' in self.mytrie.children)
        self.assertTrue('d' in self.mytrie.children)
        self.assertTrue('w' in self.mytrie.children)

        self.assertFalse('a' in self.mytrie.children)
        self.assertFalse('b' in self.mytrie.children)
        self.assertFalse('e' in self.mytrie.children)
        self.assertFalse('h' in self.mytrie.children)

        self.assertTrue('a' in self.mytrie.children['c'].children)

        self.assertFalse('h' in self.mytrie.children['c'].children)
        self.assertFalse('d' in self.mytrie.children['c'].children)

        self.assertFalse(self.mytrie.children['c'].word_finished)
        self.assertFalse(self.mytrie.children['c'].children['a'].word_finished)
        self.assertTrue(self.mytrie.children['c'].children['a'].children['t'].word_finished)

        self.assertFalse(self.mytrie.children['w'].children['h'].children['a'].word_finished)
        self.assertTrue(self.mytrie.children['w'].children['h'].children['a'].children['t'].word_finished)
        self.assertFalse(self.mytrie.children['w'].children['h'].children['a'].children['t'].children['s'].word_finished)
        self.assertTrue(self.mytrie.children['w'].children['h'].children['a'].children['t'].children['s'].children['u'].children['p'].word_finished)

    def test_has_prefix(self):
        self.assertTrue(self.mytrie.has_prefix('c'))
        self.assertTrue(self.mytrie.has_prefix('ca'))
        self.assertTrue(self.mytrie.has_prefix('w'))
        self.assertTrue(self.mytrie.has_prefix('what'))
        self.assertTrue(self.mytrie.has_prefix('whats'))

        self.assertFalse(self.mytrie.has_prefix('b'))
        self.assertFalse(self.mytrie.has_prefix('cb'))
        self.assertFalse(self.mytrie.has_prefix('cats'))

    def test_is_word(self):
        self.assertTrue(self.mytrie.is_word('cat'))
        self.assertFalse(self.mytrie.is_word('ca'))
        self.assertFalse(self.mytrie.is_word('cats'))
