class GrammarStats:
    def __init__(self):
        self.num_checks = 0
        self.num_checks_passed = 0
        pass
  
    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        self.num_checks += 1

        if text[0].isupper() and text[-1] == '.': 
            self.num_checks_passed +=1 
            return True
        
        else: return False
  
    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        return int((self.num_checks_passed / self.num_checks) * 100)