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

def make_best_move(instance):
  move = instance.get_best_move()
  if move is None: return None
  instance.make_moves_from_current_position([move])
  return move

def make_best_move_with_time_constraint(instance, time_constraint=1000):
  move = instance.get_best_move_time(time_constraint)
  if move is None: return None
  instance.make_moves_from_current_position([move])
  return move

def main():
  white = Stockfish(path="C:/Users/Administrator/Documents/GitHub/Robot-Arm-Chess-Player/stockfish_15_win_x64_avx2/stockfish_15_x64_avx2.exe")
  black = Stockfish(path="C:/Users/Administrator/Documents/GitHub/Robot-Arm-Chess-Player/stockfish_15_win_x64_avx2/stockfish_15_x64_avx2.exe")
  drawing_turns = 0
  while True:
    vis = replace_piece_name_with_unicdoe_symbol(white.get_board_visual())
    eval = white.get_evaluation()
    print(vis, eval)
    if eval["value"] == 0: drawing_turns += 1
    else: drawing_turns = 0
    if make_best_move(white) is None: break
    black.set_fen_position(white.get_fen_position())
    vis = replace_piece_name_with_unicdoe_symbol(black.get_board_visual())
    eval = black.get_evaluation()
    print(vis, eval)
    if eval["value"] == 0: drawing_turns += 1
    else: drawing_turns = 0
    if make_best_move(black) is None: break
    white.set_fen_position(black.get_fen_position())
    if drawing_turns > 50: break

  print("gg")
  
if __name__ == "__main__":
  main()

