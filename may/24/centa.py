# Prefix trees?
#
# For a dictionary with n words of maximum length L
# This solution has O(n * L) time and O(n * L) space complexity

class PrefixTree:
    def __init__(self):
        # keys are characters, values are dicts
        self.root = dict()

    def build_prefix_tree(self, dictionary):
        for word in dictionary:
            curr = self.root
        
            for letter in word:
                if letter not in curr:
                    curr[letter] = dict()
                curr = curr[letter]

            curr["\0"] = None
    
    def _extract_word(self, phrase, taken, wordlist):
        curr_word = []
        curr_node = self.root

        for i, letter in enumerate(phrase):
            if ("\0" in curr_node):
                curr_word = [ "".join(curr_word) ]

                if (curr_word[0] not in taken and
                    self._extract_word(phrase[i:], taken, wordlist)):
                  
                    wordlist.append(curr_word[0])
                    taken.add(curr_word[0])
                    
                    return True
                
            elif letter in curr_node:
                curr_word.append(letter)
                curr_node = curr_node[letter]

            else:
                return False


        last_word = "".join(curr_word)
        if ('\0' in curr_node and last_word not in taken):
            wordlist.append(last_word)
            return True

        return False

    def extract_words(self, phrase):
        wordlist = []
        taken = set()

        if not self._extract_word(phrase, taken, wordlist):
            return None
        
        wordlist.reverse()

        return wordlist
            

if __name__ == "__main__":
    pt = PrefixTree()

    dictionary = input().split()

    phrase = input()

    pt.build_prefix_tree(dictionary)
    print(pt.extract_words(phrase))
