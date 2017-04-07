import string

poem = open('camuflauged.txt', 'r')
poem_header = open('camuflauged_header.txt', 'r')
book = open('Emma.txt', 'r')
word_dict = open('words.txt', 'r')

def file_to_list(txt_file):
    """
    This function moves words from file to list.
    """
    lst = []
    for line in txt_file:
        lines = line.strip().lower()
        words = lines.split()
        for word in words:
            lst.append(word)
    return lst       

list_file = file_to_list(poem)
dict_lst = file_to_list(word_dict)

def remove_header(book):
    """
    Removes header and puts words from file from words to list.
    Use only if text file has headers from gutenberg.org.
    """
    lst = []
    flag = False
    signal = "*END*THE SMALL PRINT!"
    for line in book:
        if flag == True:
            for word in line.split():
                lst.append(word)
        elif (signal in line) and (flag == False):
            flag = True
        else:
            pass
    lst = [element.lower() for element in lst]
    return lst
    
no_header = remove_header(poem_header)
no_header2 = remove_header(book)
    
def strip_words(text):
    """
    Removes punctuation.
    """
    lst = []
    del_punctuation = [s.translate(None, string.punctuation) for s in text]
    for word in del_punctuation:
        lst.append(word)
    return lst
		
stripped_words3 = strip_words(list_file)
stripped_words = strip_words(no_header)
stripped_words2 = strip_words(no_header2)

def print_words(text):
    """
    Prints words in newlines.
    """
    for word in text:
        print word
        

def histogram(word_list):
    """
    Looks at number of words in text and appends the same words
    to dictionary under the same value that increments.
    This is how we can find most repeated words.
    """
    dictionary = {}
    lst = []
    for word in word_list:
        dictionary[word] = dictionary.get(word, 0) + 1
        
    for key, value in dictionary.iteritems():
        lst.append((value, key))
        
    lst.sort(reverse = True)
    
    return lst
    
histogram = histogram(stripped_words2)

def histogram_to_list(histogram):
    """
    Turns histogram into list.
    """
    lst = []
    for numbers, words in histogram:
        lst.append(words)
    
    return lst
    
histo_lst = histogram_to_list(histogram)


def count_words(words):
    """
    Counts words in list.
    """
    count = 0
    for x in words:
        count += 1
    return 'There are {} words in the text.'.format(count)
    

def most_frequently_used_words(lst):
    """
    Prints top 20 most used words in text.
    """
    for x in lst[:20]:
        print x
        

def compare_with_dictionary(lst, words_dict):
    """
    Compared words from the book with words from dictionary
    to find the words that are not in the book.
    """
    for x in lst:
        if x not in words_dict:
            print x

    
if __name__ == '__main__':
    print count_words(no_header2)
    print count_words(histogram)       
    most_frequently_used_words(histogram)
