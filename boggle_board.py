# Check if 4 letter word is on the random board
# 1. Check if first letter is on the board, go to first instance
# 2. Check if second letter is around the first
# 3. Check if third letter is around the second
# 4. Same with fourth
# 5. If yes to all, return True
# 6. If not, continue looping through all letters
# 7. If none, return False
# This allows the word to snake around in any direction

import random

class BoggleBoard:
  dice = [
    ["AAEEGN", "ELRTTY", "AOOTTW", "ABBJOO"],
    ["EHRTVW", "CIMOTU", "DISTTY", "EIOSST"],
    ["DELRVY", "ACHOPS", "HIMNQU", "EEINSU"],
    ["EEGHNW", "AFFKPS", "HLNNRZ", "DEILRX"]
  ]
    
  def __init__(self):
    self.board = [
      "----",
      "----",
      "----",
      "----"
    ]
      
  def print_board(self):
    for row in self.board:
      print("".join(row))
    
  def shake(self):
    new_board = []
    for row in self.dice:
      letters_lst=[]
      for die in row:
        randindex = random.randint(0,len(row[0])-1)
        if die[randindex] == "Q":
          letters_lst.append("Qu")
        else:
          letters_lst.append(die[randindex])  
      new_board.append(letters_lst)
    self.board = new_board
    self.print_board()

  def check_around(self, i, j, word):
    if len(word) == 0:
      return True
    ans = []
    if (self.board[i-1][j] == word[0] if i>0 else False):
      ans.append([i-1, j])
    if (self.board[i+1][j] == word[0] if i<len(self.board)-1 else False):
      ans.append([i+1, j])
    if (self.board[i][j-1] == word[0] if j>0 else False):
      ans.append([i, j-1])
    if (self.board[i][j+1] == word[0] if j<len(self.board[0])-1 else False):
      ans.append([i, j+1])
    print(ans)
    if len(ans) == 0:
      return False
    for item in ans:
      print(item)
      if self.check_around(item[0], item[1], word[1:]):
        return True
    return False
      

  def include_word(self, word):
    word = word.upper()
    for i,row in enumerate(self.board):
      for j, die in enumerate(row):
        if die == word[0]:
          if self.check_around(i, j, word[1:]):
            return True
          else:
            continue
    return False
          
              
      
  
board = BoggleBoard()
board.print_board()
board.shake()
# Check using the randomly generated letters to ensure a True answer
print(board.include_word(board.board[0][0] + board.board[1][0] + board.board[2][0] + board.board[3][0]))
print(board.include_word("boat"))