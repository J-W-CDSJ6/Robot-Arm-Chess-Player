from stockfish import Stockfish

stockfish_path = "/Users/Guest/Documents/Robot thing/Robot-Arm-Chess-Player-1/stockfish_15_win_x64_avx2/stockfish_15_x64_avx2.exe"

def replace_piece_name_with_unicdoe_symbol(vis):
  newvis = vis
  newvis = newvis.replace("K", u"♔")
  newvis = newvis.replace("Q", u"♕")
  newvis = newvis.replace("R", u"♖")
  newvis = newvis.replace("B", u"♗")
  newvis = newvis.replace("N", u"♘")
  newvis = newvis.replace("P", u"♙")
  newvis = newvis.replace("k", u"♚")
  newvis = newvis.replace("q", u"♛")
  newvis = newvis.replace("r", u"♜")
  newvis = newvis.replace("b", u"♝")
  newvis = newvis.replace("n", u"♞")
  newvis = newvis.replace("p", u"♟︎")
  return newvis

def make_best_move_with_time_constraint(instance, time_constraint):
  move = instance.get_best_move_time(time_constraint)
  if move is None: return None
  instance.make_moves_from_current_position([move])
  return move

def make_best_move(instance):
  move = instance.get_best_move()
  if move is None: return None
  instance.make_moves_from_current_position([move])
  return move

def get_player_move(instance):
  while True:
    move = input("Please input your move ([from][to][promotion?] e.g. e6e7 e.g.2 e7e8q\n> ")
    if (instance.is_move_correct(move) or move == "best"): return (move if move != "best" else instance.get_best_move())
    else: print("Invalid move!")

def main():
<<<<<<< Updated upstream
  instance = Stockfish(path=stockfish_path)
  while True:
    vis = replace_piece_name_with_unicdoe_symbol(instance.get_board_visual())
    print(vis, instance.get_evaluation())
    if make_best_move(instance) is None: break
  print("gg")
=======
  stockfish = Stockfish(path=stockfish_path)
  while True:
    turnCounter = 1
    canPass = False
    player = input("Would you like to play as white or black? (w/b)\n> ")
    match player:
      case "w" | "b":
        canPass = True
      case _:
        print("Not a valid response!")
    if not canPass: continue
    canPass = False
    while True:
      print(replace_piece_name_with_unicode_symbol(stockfish.get_board_visual()))
      if turnCounter % 2 == 0:
        if player == "w":
          if make_best_move(stockfish) is None: break
        else:
          stockfish.make_moves_from_current_position([get_player_move(stockfish)])
      else:
        if player == "w":
          stockfish.make_moves_from_current_position([get_player_move(stockfish)])
        else:
          if make_best_move(stockfish) is None: break
      turnCounter += 1
    canPass = False
    replay = input("Game over. Replay? (y/n)\n> ")
    match replay:
      case "y": break
      case "n": continue
      case _:
        print("Not a valid response!")
    
>>>>>>> Stashed changes
  
if __name__ == "__main__":
  main()

