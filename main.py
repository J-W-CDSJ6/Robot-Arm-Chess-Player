from stockfish import Stockfish

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

def make_best_move(instance, time_constraint):
  move = instance.get_best_move_time(time_constraint)
  if move is None: return None
  instance.make_moves_from_current_position([move])
  return move

def main():
  instance = Stockfish(path="C:/Users/Administrator/Documents/GitHub/Robot-Arm-Chess-Player/stockfish_15_win_x64_avx2/stockfish_15_x64_avx2.exe")
  while True:
    vis = replace_piece_name_with_unicdoe_symbol(instance.get_board_visual())
    print(vis, instance.get_evaluation())
    if make_best_move(instance, 50) is None: break
  print("gg")
  
if __name__ == "__main__":
  main()

