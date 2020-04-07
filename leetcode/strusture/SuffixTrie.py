class SuffixTrie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.Trie = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        curr = self.Trie
        for w in word:
            if w not in curr:
                curr[w] = {}
            curr = curr[w]
        curr['#'] = 1

    def isTail(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr = self.Trie
        for w in word:
            curr = curr[w]
        # 如果 len(curr) 等于 1 说明，作为单词的结尾有且只有一个的
        # 像 time  me 这两个单词 倒序放进来 t 节点 的值 是 #:1 但 m 除了 #:1 以外还有 ti 的内容所以 len 不是 1
        return len(curr) == 1