STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]
STOP_WORDS.remove(('a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'))

def flatten_lol(lol):
  flat_list = []
  for sublist in lol:
    for item in sublist:
      flat_list.append(item)
  return flat_list



def print_word_freq(file):
  """Read in `file` and print out the frequency of words in that file."""
  # Your code will go here. You can write additional
  #  functions if you want, and call them inside this function.
  # first open the file
  with open(file) as f:
        lyrics = f.readlines()
        word_list = [line.split() for line in lyrics]
        word_list = flatten_lol(word_list)
  print(word_list)

# remove the puncuation
  word_count = {}
# keys be word value be freq.
# lower the words
  first_word = word_list[0].lower()
  print(first_word)
  word_count[first_word] = 1
  print(word_count)
  print(word_count.keys())


# This is an "incantation." You will not see it very often, and it needs to be here to be able to pass file names as arguments.
if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
