import pytest
from data_structures.trie import Trie


@pytest.fixture
def trie():
    trie = Trie()
    trie.insert("hello")
    trie.insert("hell")
    trie.insert("heaven")
    trie.insert("heavy")
    return trie


def test_insert_and_search(trie):
    assert trie.search("hello") == True
    assert trie.search("hell") == True
    assert trie.search("heaven") == True
    assert trie.search("heavy") == True
    assert trie.search("he") == False
    assert trie.search("helloo") == False


def test_starts_with(trie):
    assert trie.starts_with("hell") == True
    assert trie.starts_with("he") == True
    assert trie.starts_with("hea") == True
    assert trie.starts_with("ho") == False
    assert trie.starts_with("heav") == True


def test_find_words_with_prefix(trie):
    assert sorted(trie.find_words_with_prefix("he")) == sorted(
        ["hello", "hell", "heaven", "heavy"]
    )
    assert sorted(trie.find_words_with_prefix("hell")) == sorted(["hello", "hell"])
    assert sorted(trie.find_words_with_prefix("hea")) == sorted(["heaven", "heavy"])
    assert trie.find_words_with_prefix("ho") == []


def test_delete(trie):
    trie.delete("hello")
    assert trie.search("hello") == False
    assert trie.search("hell") == True
    assert trie.search("heaven") == True
    assert trie.search("heavy") == True

    trie.delete("hell")
    assert trie.search("hell") == False
    assert trie.search("heaven") == True
    assert trie.search("heavy") == True

    trie.delete("heaven")
    assert trie.search("heaven") == False
    assert trie.search("heavy") == True

    trie.delete("heavy")
    assert trie.search("heavy") == False

    trie.delete("he")


def test_get_value(trie):
    assert trie.get_value("hello") == "o"
    assert trie.get_value("hell") == "l"
    assert trie.get_value("heaven") == "n"
    assert trie.get_value("heavy") == "y"
    assert trie.get_value("he") == None
    assert trie.get_value("helloo") == None


if __name__ == "__main__":
    pytest.main()
