#!/usr/bin/python3
multiple_returns = __import__('8-multiple_returns').multiple_returns

sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))
print("Length: {:d} - First character: {}".format(multiple_returns("")
      [0], multiple_returns("")[1]))
