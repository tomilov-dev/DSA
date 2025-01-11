class TrieNode:
    def __init__(self, value: str | None = None) -> None:
        self.value = value
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)
            node = node.children[char]
        node.end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def get_value(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        if node.end:
            return node.value
        return None

    def delete(self, word: str) -> bool:
        def _delete(node, word, depth):
            if not node:
                return False

            if depth == len(word):
                if not node.end:
                    return False
                node.end = False
                return len(node.children) == 0

            char = word[depth]
            if char not in node.children:
                return False

            should_delete_child = _delete(node.children[char], word, depth + 1)

            if should_delete_child:
                del node.children[char]
                return not node.end and len(node.children) == 0

            return False

        return _delete(self.root, word, 0)

    def find_words_with_prefix(self, prefix: str) -> list[str]:
        def _find_words(node, prefix):
            words = []
            if node.end:
                words.append(prefix)
            for char, child_node in node.children.items():
                words.extend(_find_words(child_node, prefix + char))
            return words

        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return _find_words(node, prefix)
