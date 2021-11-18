"Doc string"

import random

# Some comment
# more

def primary():
    "primary function"
    print("Keep it logically awesome.")

    quote_file = open("quotes.txt", encoding="latin-1")
    quotes = quote_file.readlines()
    quote_file.close()

    last = 13
    rnd = random.randint(0, last)

    print(quotes[rnd])

if __name__== "__main__":
    primary()
