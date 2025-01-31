"""
Design a data structure that supports adding new words
and searching for existing words.

notes:
-----
I think the structure should be pretty similar to the Trie/Prefix Tree
structure, but the only thing to have in mind is that "." acts as a wildcard
when performing search operations.

search method design:
---------------------
now, if we have the wild card "." in our input search string. 
the string could be matched with any of the incorporated strings, 
at the end of the day what the wild card is doing is shifting 
the search level on the tree. 

the issue here is that we cant choose any child, we have to choose a 
child that its concatenation would have the same length as the input
string. 
   |
    -> this would need a recursive check

the recursive helper function would look for a deepness in the Tree that
matches the length of the input string and a possible route. this would allow us to 
move forward in the tree in the right direction
lets analyze an example.

lets say we have the word "baix" in our trie. and we insert the following search
"ba.x"
-> it would be ideal to compare the lengths, but we dont actually know what letter could "."
   be.
-> we could start our normal trie iteration and everything would be fine until we reach ".".
   now, we know the length of the input string and how far we have traversed. 
   the question here is:
                - WHAT NEXT CHARACTER SHOULD I CHOOSE?
   and the answer would be:
                - ANY CHARACTER THAT ALLOWS YOU TO KEEP MOVING DOWN THE TRIE
                  AND MATCHES YOUR LENGTH.
[KEY INSIGHT]: The fact of the matter is that we have to perform a combination of a brute-force/recursive approach.
      |
       --> "." --> this would trigger a recursive search on all of the current analyzed node.
      |
       --> if i had to pass the word to the recursive call, i would like to pass everything that is after the current value to the recursive
           call, and for that it is necessary to extract the index

"""
from typing import Optional

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.children[c] = True

    def search(self, word: str) -> bool:
        def dfs(word, root):
            for i, c in enumerate(word):
                if c == ".":
                    for child in root.children:
                        if dfs(word[i + 1:], child):
                            return True
                        return False
                if c not in root.children:
                    return False
                else:
                    root = root.children[c]
            return root.word
        return dfs(word, self.root)

 
        