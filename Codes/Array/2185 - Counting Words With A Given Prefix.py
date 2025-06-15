# Last Updated: 15-06-2025 - 05:29 PM
# Difficulty: Easy
# Status: Solved
# Tags: Array, String, String Matching

# Time Complexity: O(m*n)
# Space Complexity: O(n)
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        n = len(pref)
        for word in words:
            if word[:n] == pref:
                count += 1
        return count


# Time Complexity: O(m*n)
# Space Complexity: O(1)
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        N = len(pref)
        res = 0
        for w in words:
            inc = 1
            if len(w) < N:
                continue
            for i in range(N):
                if w[i] != pref[i]:
                    inc = 0
                    break
            res += inc
        return res


# Trie
# Time Complexity: O(m*n)
# Space Complexity: O(m*n)
class PrefixNode:
    def __init__(self):
        self.children = {}
        self.count = 0


class PrefixTree:
    def __init__(self):
        self.root = PrefixNode()

    def add(self, w):
        cur = self.root
        for c in w:
            if c not in cur.children:
                cur.children[c] = PrefixNode()
            cur = cur.children[c]
            cur.count += 1

    def count(self, pref):
        cur = self.root
        for c in pref:
            if c not in cur.children:
                return 0
            cur = cur.children[c]
        return cur.count


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        prefix_tree = PrefixTree()

        for w in words:
            if len(w) >= len(pref):
                prefix_tree.add(w)
        return prefix_tree.count(pref)
