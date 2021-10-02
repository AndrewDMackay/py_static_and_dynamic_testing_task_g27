### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:  
    # Error.. Should be 'card.value == 1:'..
      return True
    else
    # Error.. Missing colon, should be 'else:'..
      return False
   

  dif highest_card(self, card1 card2):
  # Error.. Should be 'def', not 'dif'..
  # Error.. There is a comma missing, should be 'card1, card2'..
  # Error.. The 'if, else' code block below should be indented to the right..
  if card1.value > card2.value:
    return card
  # Error.. Should be 'card1', no 'card' input passed in..
  else:
    return card2
  

# Error.. This whole code block should be indented to the right..
def cards_total(self, cards):
  total
  # Error.. The 'total' variable above is not defined, it needs to = something..
  # Or, to be pulled from a class, eg. 'cards.total', etc..
  for card in cards:
    total += card.value
    return "You have a total of" + total
  # Error.. The return statement above, should be indented back to the left, parallel to the 'for' loop..
  # Error.. Also, the return above is missing a space, or could be better as an f string, set out as below..
  # 'return (f"You have a total of {total}")

```
