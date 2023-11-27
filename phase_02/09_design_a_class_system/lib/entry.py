class Entry():
    # Public properties:
    #   title:  a string
    #   content: a string

    def __init__(self, title, content):
        self.title = title
        self.content = content
    
    def count_words(self):
        words = self.content.split()
        return len(words)

    def parse_phone_number(self):
    #Will return the first phone number that appears and is 11 numbers long

        nums = "0123456789"
        num = ""
        num_len = 0
        for n, c in enumerate(self.content):
            if c == '0':
                if num_len <= 10:
                    num_len += 1
                    num += c
                    for i in range(1, len(self.content) - n):
                        if self.content[n + i] in nums:
                            num_len += 1
                            num += self.content[n + i]
                        if num_len > 10:
                            break

        if len(num) == 11:
            return num
        else:
            return None