from stockfish import Stockfish

stockfish_path = "stockfish_15_win_x64_avx2\stockfish_15_x64_avx2.exe"

def replace_piece_name_with_unicode_symbol(vis):
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

def main():
  white = Stockfish(path=stockfish_path, parameters={"Threads": 3, "Hash": 256})
  black = Stockfish(path=stockfish_path, parameters={"Ponder": "false"})
  historicalPos = {}
  drawCounter = 0
  counter = 0
  while True:
    instance = white if counter % 2 == 0 else black
    vis = replace_piece_name_with_unicode_symbol(instance.get_board_visual())
    print(vis, ("White" if counter % 2 == 0 else "Black") + " eval: ", instance.get_evaluation()["value"])
    if counter % 2 == 0:
      if make_best_move(instance) is None: break
    else:
      if make_best_move_with_time_constraint(instance, 1) is None: break
    if not (instance.get_fen_position() in historicalPos): historicalPos[instance.get_fen_position()] = 0
    historicalPos[instance.get_fen_position()] += 1
    if instance.get_evaluation()["value"] == 0: drawCounter += 1
    else: drawCounter = 0
    if drawCounter == 100: break
    (black if counter % 2 == 0 else white).set_fen_position(instance.get_fen_position())
    counter += 1
  print("gg")
  
if __name__ == "__main__":
  main()

