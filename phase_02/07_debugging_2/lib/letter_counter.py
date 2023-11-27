class LetterCounter:
    def __init__(self, text):
        self.text = text

    def calculate_most_common_solved(self):
        counter = {}
        most_common = None
        most_common_count = 0
        for char in self.text:
            if not char.isalpha():
                continue
            counter[char] = counter.get(char, 0) + 1
            if counter[char] > most_common_count:
                most_common = char
                most_common_count += 1
        return [most_common_count, most_common]
    
    def calculate_most_common_original(self):
        counter = {}
        most_common = None
        most_common_count = 1
    #   Error 1: There is no most common letter yet so the count should
    #   be set a 0.

        for char in self.text:
            if not char.isalpha():
                continue
            counter[char] = counter.get(char, 1) + 1
        #   Error 2: The dict.get(a, b) if the key(a) does not exist it will add a default value(b)
        #   if the key does not exist we would want the inital value to be 0, as the we did not encounter the letter
        #   before and we are adding 1 to it once we encountered it.

            if counter[char] > most_common_count:
                most_common = char
                most_common_count += counter[char]
            #   Error 3: Anytime we enter the if statement means we encountered a letter that appears more than
            #   the one before it, so to keep track of how many times we have entered the if we would want to set
            #   the most_common_count to +1 every time.
            
        return [most_common_count, most_common]


counter = LetterCounter("Digital Punk")
print(counter.calculate_most_common_solved())
print(counter.calculate_most_common_original())

# Intended output:
# [2, "i"]