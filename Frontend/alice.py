filename = 'alice.txt'

# NEXT 2 LINES ARE CODE path = "/Users/user/downloads/programming/python_work/text_files"
# myFile = path + filename

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")

    #had not indented contents = etc. Pay attention to indentation
    # I only get 'sorry, the file alice.txt does not exist This code is only PARTIALLY WORKING
    #moving on, got stuck on this file analysis for too long and all explanations online Windows!!




