class PrefixTreeNode:
    def __init__(self, character):
        self.character = character
        self.children = dict()


class AutoComplete:
    def __init__(self, dictionary):
        self.root = PrefixTreeNode('\0')

        for word in dictionary:
            self.preproccess_word(word)
        
    def preproccess_word(self, word):
        curr = self.root

        for character in word:
            if character in curr.children.keys():
                curr = curr.children[character]
            else:
                child = PrefixTreeNode(character)
                curr.children[character] = child
                curr = child
        
        curr.children['*'] = None

    def get_words(self, node):
        if not node:
            return ['*']

        words = []

        for character, child in node.children.items():
            words.extend(map(lambda w: character+w,
                             self.get_words(child)))

        return words
    
    def autocomplete(self, word):
        curr = self.root

        for character in word:
            if character in curr.children.keys():
                curr = curr.children[character]
            else:
                return []

        return list(map(lambda w: word+w[:-2],
                        self.get_words(curr)))

if __name__ == "__main__":
    # read dictionary of words on the first line of input
    dictionary = input().split()

    # read the word to be autocompleted on the second line
    word = input()

    ac = AutoComplete(dictionary)

    # print the autocomplete possibilities
    print(ac.autocomplete(word))
