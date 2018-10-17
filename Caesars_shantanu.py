import string

def load_words(file_name):
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

def is_word(word_list, word):
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        return self.message_text

    def get_valid_words(self):
        return self.valid_words[:]
    def build_shift_dict(self, shift):
        dict1 = {}
        str1 = string.ascii_uppercase
        for s in str1:
            if (ord(s)+shift-65) < 26 :
                 dict1[s] = chr(ord(s)+shift)
            elif (ord(s)+shift-65) >= 26 :
                 dict1[s] = chr(ord(s)+shift-26)
    
        str1 = string.ascii_lowercase
        for s in str1:
            if (ord(s)+shift-97) < 26 :
                 dict1[s] = chr(ord(s)+shift)
            elif (ord(s)+shift-97) >= 26 :
                 dict1[s] = chr(ord(s)+shift-26)
    
        return dict1    
    
    def apply_shift(self, shift):
        msg = self.get_message_text()
        newMsg = ""
        dict1 = self.build_shift_dict(shift)
        for i in range(len(msg)):
            if msg[i] in dict1:
                newMsg += dict1.get(msg[i])
            else:
                newMsg += msg[i]
        return newMsg

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        Message.__init__(self, text)
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(self.get_shift())
        self.message_text_encrypted = self.apply_shift(self.get_shift())

    def get_shift(self):
        return self.shift

    def get_encrypting_dict(self):
        return dict(self.encrypting_dict)

    def get_message_text_encrypted(self):
        return self.message_text_encrypted

    def change_shift(self, shift):
        assert 0 <= shift < 26
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(self.shift)

class CiphertextMessage(Message):
    def __init__(self, text):
        Message.__init__(self, text)
        self.text = text

    def decrypt_message(self):
        final_shift = 0
        best_word_list = 0
        word_list = load_words('words.txt')
        for shift in range(27):
            decrypted_text = self.apply_shift(shift)
            wordlist = decrypted_text.split(' ')
            num_valid_words = 0
            for word in wordlist:
                if is_word(word_list, word):
                    num_valid_words += 1
            if num_valid_words > best_word_list:
                final_shift = shift
                best_word_list = num_valid_words

        return (final_shift, self.apply_shift(final_shift))
    

def decrypt_story():
    ciphertext = CiphertextMessage(get_story_string())
    return ciphertext.decrypt_message()

print(decrypt_story())
