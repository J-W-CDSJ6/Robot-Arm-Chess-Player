emptyBoardFEN = "8/8/8/8/8/8/8/8 w - - 0 1"

class Board:
  # Rudimentary class for one single turn of a game.
  # Does not contain functions to progress the game in any way.
  def __init__(self, FEN="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"):
    self.FEN = FEN

  @property
  def listedBoard(self):
    # A formatted version of the current FEN.
    listed = self.FEN.split("/")
    infos = listed[7].split()
    listed[7] = infos[0]
    boardedObj = {
      "board": listed,
      "turn": int(infos[5]),
      "player": infos[1],
      "castles": infos[2],
      "passantable": infos[3],
      "half_move": int(infos[4])
    }
    return boardedObj
  
  def setpiece(self, position, piece):
    # Sets a piece at the position, overriding any piece that was already on it.
    File = ord(position[0])-97
    Rank = int(position[1])
    infoed = self.listedBoard
    board = infoed["board"]
    rankStr = board[8-Rank]
    listed = list(rankStr)
    listed[File] = piece
    rankStr = "".join(listed)
    args = {}
    for i, rank in enumerate(board):
      args[i] = rank
    for key, value in infoed.items():
      if key == "board": continue
      args[key] = value
    newFEN = "{0}/{1}/{2}/{3}/{4}/{5}/{6}/{7} {turn} {castles} {passantable} {half_move} {turn}".format(**args)
    self.FEN = newFEN
    return True
  
  def getpiece(self, position):
    # Get the piece sititng on the position given
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

class Game:
  # A nice game of chess. Que le meilleur gagne.
  def __init__(self, initBoard=Board()):
    self.history = [ Board(emptyBoardFEN) ]           # The history of the entire game.
    formatted = initBoard.listedBoard                 
    self.turn = formatted["turn"]                        # Which turn it is
    self.player = formatted["player"]                   # Who is currently playing
    self.castle = formatted["castles"]                 # What castles are available
    self.timeSinceLastPawnMove = formatted["half_move"]  # Used for 50-moves-rule
    self.whiteCapturedPieces = []                     # What pieces have *black lost*?
    self.blackCapturedPieces = []                     # What pieces have *white lost*?
    self.history.insert(1, initBoard)
    self.moveHistory = [""]                           # The move history of the entire game (1. e4 e5 etc.)
  
  @property
  def currentBoard(self):
    # The current board.
    return self.history[self.turn]

  def __capturePiece(self, position):
    # Internal function used to mark a captured piece.
    if self.player == "w": self.whiteCapturedPieces.insert(self.currentBoard.getpiece(toPos))
    else: self.blackCapturedPieces.insert(self.currentBoard.getpiece(toPos))

  def __moveAndCapture(self, fromPos, toPos, piece):
    # Internal function used to capture a piece (e.g. Nxf4)
    self.currentBoard.setpiece(fromPos, "1"),
    self.__capturePiece(toPos)
    self.currentBoard.setpiece(position, piece)

  def move(self, move):
    fromPos = move[0:2]
    toPos = move[2:4]
    promotion = move[4] if len(move) > 4 else ""
    pieceToMove = self.currentBoard.getpiece(fromPos)
    isWhite = pieceToMove.isupper()
    if isWhite != (self.player == "w"): return False
    deltaX = (ord(fromPos[0])-ord(toPos[0]))
    deltaY = (int(fromPos[1])-int(toPos[1]))
    match pieceToMove.lower():
      case "n":
        # The knight
        if (abs(deltaX) + abs(deltaY) == 3) and (deltaX != 0) and (deltaY != 0): self.__moveAndCapture(fromPos, toPos, pieceToMove)
        else: return False
      case "r":
        # The rook
        moveDir = "vertical" if deltaY > 0 else "horizontal"
        if moveDir == "vertical":
          for offset in range(1 if deltaY > 0 else deltaY + 1, deltaY if deltaY > 0 else 0):
            posToCheck = "{0}{1}".format(fromPos[0], str(int(fromPos[1])+offset))
            piece = self.currentBoard.getpiece(posToCheck)
            print(piece)
            if piece != "1": return False
          self.__moveAndCapture(fromPos, toPos, pieceToMove)
        else:
          for offset in range(1 if deltaX > 0 else deltaX + 1, deltaX if deltaX > 0 else 0):
            posToCheck = "{0}{1}".format(chr(ord(fromPos[0])+offset), fromPos[1])
            piece = self.currentBoard.getpiece(posToCheck)
            print(piece)
            if piece != "1": return False
          self.__moveAndCapture(fromPos, toPos, pieceToMove)


def main():
  testGame = Game()
  testGame.move("e2e4")

  
if __name__ == "__main__":
  main()

