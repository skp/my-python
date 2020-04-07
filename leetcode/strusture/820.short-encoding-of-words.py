from typing import List

from leetcode.strusture.SuffixTrie import SuffixTrie


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = SuffixTrie()
        cnt = 0
        words = set(words)
        for word in words:
            trie.insert(word[::-1])
        for word in words:
            # {'e': {'m': {'#': 1, 'i': {'t': {'#': 1}}}}, 'l': {'l': {'e': {'b': {'#': 1}}}}}
            if trie.isTail(word[::-1]):
                cnt += len(word) + 1
        return cnt


if __name__ == '__main__':
    Solution().minimumLengthEncoding(['time', 'me', 'bell'])
