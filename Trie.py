class Trie:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.word_finished = False

    def add(self, word):
        if len(word) == 0:
            self.word_finished = True
            return
        elif word[0] not in self.children:
            self.children[word[0]] = Trie(word[0])
        self.children[word[0]].add(word[1:])

    def has_prefix(self, prefix):
        if len(prefix) == 0:
            return True
        elif prefix[0] in self.children:
            return self.children[prefix[0]].has_prefix(prefix[1:])
        else:
            return False
    def is_word(self, word):
        node = self
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        return node.word_finished
