emptyBoardFEN = "8/8/8/8/8/8/8/8 w - - 0 1"

class Move:
  def __init__(self, moveStr):
    assert type(moveStr) == str, "Cannot make move from non-string!"
    self.moveFrom = moveStr[0:1]
    self.moveTo = moveStr[2:3]
    self.promotion = moveStr[4] if len(moveStr) > 4 else ""

class Board:
  def __init__(self, FEN="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"):
    self.FEN = FEN

  @property
  def listedBoard(self):
    listed = self.FEN.split("/")
    infos = listed[7].split()
    listed[7] = infos[0]
    boardedObj = {
      "board": listed,
      "turn": infos[5],
      "player": infos[1],
      "castles": infos[2],
      "passantable": infos[3],
      "half_move": infos[4]
    }
    return boardedObj
  
  def getpiece(self, position):
    File = ord(position[0])-97
    Rank = int(position[1])
    boardObj = self.listedBoard
    rankStr = boardObj["board"][8-Rank]
    expandedRankStr = ""
    for char in rankStr:
      try:
        expandedRankStr += int(char)*"1"
      except:
        expandedRankStr += char
    return expandedRankStr[File]

  def move(self, move):
    pass

class Game:
  def __init__(self):
    self.history = []

def main():
  empty = Board()
  print(empty.getpiece("e7"))

  
if __name__ == "__main__":
  main()

