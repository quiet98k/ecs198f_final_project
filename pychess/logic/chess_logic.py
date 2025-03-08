from typing import List
from typing import Tuple  


class ChessLogic:
      
 
    def __init__(self):
        """
        Initalize the ChessLogic Object. External fields are board and result

        board -> Two Dimensional List of string Representing the Current State of the Board
            P, R, N, B, Q, K - White Pieces

            p, r, n, b, q, k - Black Pieces

            '' - Empty Square

        result -> The current result of the game
            w - White Win

            b - Black Win

            d - Draw

            '' - Game In Progress
        """
        self.board = [
			['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
			['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
			['','','','','','','',''],
			['','','','','','','',''],
			['','','','','','','',''],
			['','','','','','','',''],
			['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
			['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
		]
        self.result = "" 
    
    # given the array index, print the grid string    
    def array2grid(self, row: int, col: int) -> str:
        if(col<0 or col>7 or row<0 or row>7):
            return str(-1)
        return chr(col + ord('a')) + str(8 - row)
        
    # given the grid string, get the array index
    def grid2array(self, pos: str) -> Tuple[int, int]:
        col = ord(pos[0]) - ord('a')
        row = 8 - int(pos[1])
        if(col<0 or col>7 or row<0 or row>7):
            return (-1,-1)
        return (row, col)
        
    # get the name of the piece based on given position in the grid
    def get_piece(self, pos: str) -> str:
        
        row_index, col_index = self.grid2array(pos)
        
        return self.board[row_index][col_index]
    
    def get_valid_end_pos(self, pos: str, piece: str) -> List[str]:
        row_index, col_index = self.grid2array(pos)
        valid_moves_in_index = []
        valid_moves = []
        if piece == "P":
            # Implement logic for white pawn
            # if this is its first move, it can move 1 or 2    
            pos_at_front = self.array2grid(row_index-1, col_index)
            # if the piece is not at the top row
            if(pos_at_front != "-1"):
                piece_at_front = self.get_piece(pos_at_front)
                # if no piece at front
                if(piece_at_front == ''):
                    valid_moves.append(pos_at_front)
                    # can move twice
                    if(row_index == 6): 
                        pos_at_front_twice = self.array2grid(row_index-2, col_index)
                        if pos_at_front_twice != '-1':
                            valid_moves.append(pos_at_front_twice)
            # now check diagonally left and right
            pos_at_left_diag = self.array2grid(row_index-1, col_index-1)
            if pos_at_left_diag != '-1' and self.get_piece(pos_at_left_diag).islower():
                valid_moves.append(pos_at_left_diag)
            pos_at_right_diag = self.array2grid(row_index-1, col_index+1)
            if pos_at_right_diag != '-1' and self.get_piece(pos_at_right_diag).islower():
                valid_moves.append(pos_at_right_diag)

        elif piece == "R":
            # Implement logic for white rook
            
            for i in range(row_index-1, -1, -1):
                pos_up = self.array2grid(i, col_index)
                piece_up = self.get_piece(pos_up)
                if piece_up == '':
                    valid_moves.append(pos_up)
                elif piece_up.islower():
                    valid_moves.append(pos_up)
                    break
                else:
                    break

            for j in range(row_index+1, 8):
                pos_down = self.array2grid(j, col_index)
                piece_down = self.get_piece(pos_down)
                if piece_down == '':
                    valid_moves.append(pos_down)
                elif piece_down.islower():
                    valid_moves.append(pos_down)
                    break
                else:
                    break

            for k in range(col_index-1, -1, -1):
                pos_left = self.array2grid(row_index, k)
                piece_left = self.get_piece(pos_left)
                if piece_left == '':
                    valid_moves.append(pos_left)
                elif piece_left.islower():
                    valid_moves.append(pos_left)
                    break
                else:
                    break

            for l in range(col_index+1, 8):
                pos_right = self.array2grid(row_index, l)
                piece_right = self.get_piece(pos_right)
                if piece_right == '':
                    valid_moves.append(pos_right)
                elif piece_right.islower():
                    valid_moves.append(pos_right)
                    break
                else:
                    break
        
        elif piece == "N":
            pass  # Implement logic for white knight
        
        elif piece == "B":
            pass  # Implement logic for white bishop
        
        elif piece == "Q":
            pass  # Implement logic for white queen
        
        elif piece == "K":
            pass  # Implement logic for white king
        
        elif piece == "p":
            pass  # Implement logic for black pawn
            # if this is its first move, it can move 1 or 2    
            pos_at_front = self.array2grid(row_index+1, col_index)
            # if the piece is not at the top row
            if(pos_at_front != "-1"):
                piece_at_front = self.get_piece(pos_at_front)
                # if no piece at front
                if(piece_at_front == ''):
                    valid_moves.append(pos_at_front)
                    # can move twice
                    if(row_index == 1): 
                        pos_at_front_twice = self.array2grid(row_index+2, col_index)
                        if pos_at_front_twice != '-1':
                            valid_moves.append(pos_at_front_twice)
            # now check diagonally left and right
            pos_at_left_diag = self.array2grid(row_index+1, col_index-1)
            if pos_at_left_diag != '-1' and self.get_piece(pos_at_left_diag).isupper():
                valid_moves.append(pos_at_left_diag)
            pos_at_right_diag = self.array2grid(row_index+1, col_index+1)
            if pos_at_right_diag != '-1' and self.get_piece(pos_at_right_diag).isupper():
                valid_moves.append(pos_at_right_diag)
        
        elif piece == "r":
            # Implement logic for black rook
            for i in range(row_index-1, -1, -1):
                pos_up = self.array2grid(i, col_index)
                piece_up = self.get_piece(pos_up)
                if piece_up == '':
                    valid_moves.append(pos_up)
                elif piece_up.isupper():
                    valid_moves.append(pos_up)
                    break
                else:
                    break

            for j in range(row_index+1, 8):
                pos_down = self.array2grid(j, col_index)
                piece_down = self.get_piece(pos_down)
                if piece_down == '':
                    valid_moves.append(pos_down)
                elif piece_down.isupper():
                    valid_moves.append(pos_down)
                    break
                else:
                    break

            for k in range(col_index-1, -1, -1):
                pos_left = self.array2grid(row_index, k)
                piece_left = self.get_piece(pos_left)
                if piece_left == '':
                    valid_moves.append(pos_left)
                elif piece_left.isupper():
                    valid_moves.append(pos_left)
                    break
                else:
                    break

            for l in range(col_index+1, 8):
                pos_right = self.array2grid(row_index, l)
                piece_right = self.get_piece(pos_right)
                if piece_right == '':
                    valid_moves.append(pos_right)
                elif piece_right.isupper():
                    valid_moves.append(pos_right)
                    break
                else:
                    break            
        
        elif piece == "n":
            pass  # Implement logic for black knight
        
        elif piece == "b":
            pass  # Implement logic for black bishop
        
        elif piece == "q":
            pass  # Implement logic for black queen
        
        elif piece == "k":
            pass  # Implement logic for black king
        
        return valid_moves
        
    
    
    

    def play_move(self, move: str) -> str:
        """
        Function to make a move if it is a valid move. This function is called everytime a move in made on the board

        Args:
            move (str): The move which is proposed. The format is the following: starting_sqaure}{ending_square}
            
            i.e. e2e4 - This means that whatever piece is on E2 is moved to E4

        Returns:
            str: Extended Chess Notation for the move, if valid. Empty str if the move is invalid
        """
        
        #Implement this
        start_pos = move[:2]
        end_pos = move[2:]
        print("start_pos: ", start_pos, " = ", self.get_piece(start_pos))
        print("end_pos: ", end_pos, " = ", self.get_piece(end_pos))
        valid_end_pos = self.get_valid_end_pos(start_pos, self.get_piece(start_pos))
        print(valid_end_pos)
        return ""