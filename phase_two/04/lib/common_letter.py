def get_most_common_letter(text):
    counter = {}
    for char in text:
        counter[char] = counter.get(char, 0) + 1

    letter = sorted(counter.items(), key=lambda item: item[1], reverse=True)[1][0]
    
  # Error
  # letter = sorted(counter.items(), key=lambda item: item[1])[0][1]
  # 
  # sorted(counter.items()) returns a tupled list [('t', 3), ('s', 1), ('r', 4)...]
  #
  # sorted() will by default sort in an ascending order, to have the largest one you'd
  # want it in the opposite order, sort() has a parameter called reversed which when True
  # will do that.
  #
  # key=lambda item: item[1]
  #
  # we are creating a function that will fetch the item we'll want to base the sorting on.
  # in this case the tuple's second item (a, b) the sorted() will focus on the values of b
  #
  # sorted(counter.items(), key=lambda item: item[1]) will return an ordered list based on b
  # [('s', 1), ('n', 1), ('!', 1), (',', 2), ('i', 2), ('t', 3), ('h', 3)...]
  # 
  # we want the highest occurence we could just access the last element of the list but to make
  # it more simple and neater we can just reverse it by setting reversed=True
  #
  # sorted(counter.items(), key=lambda item: item[1], reverse=True)
  # now it will return us a list in descending order based on the element b of the tuple
  # [(' ', 8), ('o', 7), ('e', 4), ('r', 4), ('f', 4), ('t', 3)...]
  #
  # we know the biggest occurence will be the spaces so we'd skip it and go to the second one
  # sorted(counter.items(), key=lambda item: item[1], reverse=True)[1][0]
  #                                                                [a][b]
  # a is the tuple inside the list and b is the element inside the tuple

    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")