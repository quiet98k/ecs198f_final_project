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
        self.last_move = None
        self.white_king_moved = False
        self.black_king_moved = False
        self.white_left_rook_moved = False
        self.white_right_rook_moved = False
        self.black_left_rook_moved = False
        self.black_right_rook_moved = False
        
        
        
        
        
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
    
    def get_white_pawn_valid_moves(self, pos: str, piece: str) -> List[str]:
        row_index, col_index = self.grid2array(pos)
        valid_moves = []
        if piece != "P":
            return valid_moves
        
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
                    if pos_at_front_twice != "-1":
                        valid_moves.append(pos_at_front_twice)
        # now check diagonally left and right
        pos_at_left_diag = self.array2grid(row_index-1, col_index-1)
        if pos_at_left_diag != "-1" and self.get_piece(pos_at_left_diag).islower():
            valid_moves.append(pos_at_left_diag)
        pos_at_right_diag = self.array2grid(row_index-1, col_index+1)
        if pos_at_right_diag != "-1" and self.get_piece(pos_at_right_diag).islower():
            valid_moves.append(pos_at_right_diag)
            
            
        if self.last_move != None:
            last_piece, last_start_pos, last_end_pos = self.last_move
            if piece == 'P' and last_piece == 'p':
                # if I'm white pawn and last move is black pawn
                # I want to check
                # 1. Does the last pawn move twice ahead?
                # 2. Am I at the correct pos
                # with both is true, do I want to move at the correct position?
                # If I do want to move at the correct position, then eat it
                if abs(int(last_start_pos[1]) - int(last_end_pos[1])) == 2:
                    if pos[1] == "5":
                        valid_moves.append(last_end_pos[0] + str(int(last_end_pos[1]) + 1))
        
        return valid_moves

    def get_black_pawn_valid_moves(self, pos: str, piece: str) -> List[str]:
        row_index, col_index = self.grid2array(pos)
        valid_moves = []
        if piece != "p":
            return valid_moves
        # Implement logic for black pawn
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
                    if pos_at_front_twice != "-1":
                        valid_moves.append(pos_at_front_twice)
        # now check diagonally left and right
        pos_at_left_diag = self.array2grid(row_index+1, col_index-1)
        if pos_at_left_diag != "-1" and self.get_piece(pos_at_left_diag).isupper():
            valid_moves.append(pos_at_left_diag)
        pos_at_right_diag = self.array2grid(row_index+1, col_index+1)
        if pos_at_right_diag != "-1" and self.get_piece(pos_at_right_diag).isupper():
            valid_moves.append(pos_at_right_diag)
        
        if self.last_move != None:
            last_piece, last_start_pos, last_end_pos = self.last_move
            if piece == 'p' and last_piece == 'P':
                if abs(int(last_start_pos[1]) - int(last_end_pos[1])) == 2:
                    if pos[1] == "4":
                        valid_moves.append(last_end_pos[0] + str(int(last_end_pos[1]) - 1))
        return valid_moves

    def get_white_rook_valid_moves(self, pos: str, piece: str) -> List[str]:
        row_index, col_index = self.grid2array(pos)
        valid_moves = []
        if piece != "R":
            return valid_moves
        
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
        return valid_moves
    
    def get_black_rook_valid_moves(self, pos: str, piece: str) -> List[str]:
        row_index, col_index = self.grid2array(pos)
        valid_moves = []
        if piece != "r":
            return valid_moves
        
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
        return valid_moves

    def get_white_knight_valid_moves(self, pos: str, piece: str) -> List[str]:
        row_index, col_index = self.grid2array(pos)
        valid_moves = []
        if piece != "N":
            return valid_moves
        
        # Implement logic for white knight
        knight_moves = [
        (row_index - 2, col_index - 1),
        (row_index - 2, col_index + 1),
        (row_index - 1, col_index + 2),
        (row_index + 1, col_index + 2),
        (row_index + 2, col_index + 1),
        (row_index + 2, col_index - 1),
        (row_index + 1, col_index - 2),
        (row_index - 1, col_index - 2)
        ]
        for move in knight_moves:
            new_pos = self.array2grid(move[0], move[1])
            if new_pos != "-1" and (self.get_piece(new_pos) == "" or self.get_piece(new_pos).islower()):
                valid_moves.append(new_pos)
                
        return valid_moves
    
    def get_black_knight_valid_moves(self, pos: str, piece: str) -> List[str]:
        row_index, col_index = self.grid2array(pos)
        valid_moves = []
        if piece != "n":
            return valid_moves
        # Implement logic for black knight
        knight_moves = [
            (row_index - 2, col_index - 1),
            (row_index - 2, col_index + 1),
            (row_index - 1, col_index + 2),
            (row_index + 1, col_index + 2),
            (row_index + 2, col_index + 1),
            (row_index + 2, col_index - 1),
            (row_index + 1, col_index - 2),
            (row_index - 1, col_index - 2)
        ]
        for move in knight_moves:
            new_pos = self.array2grid(move[0], move[1])
            if new_pos != "-1" and (self.get_piece(new_pos) == "" or self.get_piece(new_pos).isupper()):
                valid_moves.append(new_pos)
        return valid_moves

    def get_black_bishop_valid_moves(self, pos: str, piece: str) -> List[str]:
        row_index, col_index = self.grid2array(pos)
        valid_moves = []
        if piece != "b":
            return valid_moves
        # Implement logic for black bishop
        for i in range(1, 8):
            pos_up_right = self.array2grid(row_index - i, col_index + i)
            if pos_up_right == "-1":
                break
            piece_up_right = self.get_piece(pos_up_right)
            if piece_up_right == '':
                valid_moves.append(pos_up_right)
            elif piece_up_right.isupper():
                valid_moves.append(pos_up_right)
                break
            else:
                break
        for i in range(1, 8):
            pos_up_left = self.array2grid(row_index - i, col_index - i)
            if pos_up_left == "-1":
                break
            piece_up_left = self.get_piece(pos_up_left)
            if piece_up_left == '':
                valid_moves.append(pos_up_left)
            elif piece_up_left.isupper():
                valid_moves.append(pos_up_left)
                break
            else:
                break
        for i in range(1, 8):
            pos_down_right = self.array2grid(row_index + i, col_index + i)
            if pos_down_right == "-1":
                break
            piece_down_right = self.get_piece(pos_down_right)
            if piece_down_right == '':
                valid_moves.append(pos_down_right)
            elif piece_down_right.isupper():
                valid_moves.append(pos_down_right)
                break
            else:
                break
        for i in range(1, 8):
            pos_down_left = self.array2grid(row_index + i, col_index - i)
            if pos_down_left == "-1":
                break
            piece_down_left = self.get_piece(pos_down_left)
            if piece_down_left == '':
                valid_moves.append(pos_down_left)
            elif piece_down_left.isupper():
                valid_moves.append(pos_down_left)
                break
            else:
                break
        return valid_moves

    def get_white_bishop_valid_moves(self, pos: str, piece: str) -> List[str]:
        row_index, col_index = self.grid2array(pos)
        valid_moves = []
        if piece != "B":
            return valid_moves
        
        for i in range(1, 8):
            pos_up_right = self.array2grid(row_index - i, col_index + i)
            if pos_up_right == "-1":
                break
            piece_up_right = self.get_piece(pos_up_right)
            if piece_up_right == '':
                valid_moves.append(pos_up_right)
            elif piece_up_right.islower():
                valid_moves.append(pos_up_right)
                break
            else:
                break
        for i in range(1, 8):
            pos_up_left = self.array2grid(row_index - i, col_index - i)
            if pos_up_left == "-1":
                break
            piece_up_left = self.get_piece(pos_up_left)
            if piece_up_left == '':
                valid_moves.append(pos_up_left)
            elif piece_up_left.islower():
                valid_moves.append(pos_up_left)
                break
            else:
                break
        for i in range(1, 8):
            pos_down_right = self.array2grid(row_index + i, col_index + i)
            if pos_down_right == "-1":
                break
            piece_down_right = self.get_piece(pos_down_right)
            if piece_down_right == '':
                valid_moves.append(pos_down_right)
            elif piece_down_right.islower():
                valid_moves.append(pos_down_right)
                break
            else:
                break
        for i in range(1, 8):
            pos_down_left = self.array2grid(row_index + i, col_index - i)
            if pos_down_left == "-1":
                break
            piece_down_left = self.get_piece(pos_down_left)
            if piece_down_left == '':
                valid_moves.append(pos_down_left)
            elif piece_down_left.islower():
                valid_moves.append(pos_down_left)
                break
            else:
                break
            
        return valid_moves
    
    def get_black_bishop_valid_moves(self, pos: str, piece: str) -> List[str]:
        row_index, col_index = self.grid2array(pos)
        valid_moves = []
        if piece != "b":
            return valid_moves
        # Implement logic for black bishop
        for i in range(1, 8):
            pos_up_right = self.array2grid(row_index - i, col_index + i)
            if pos_up_right == "-1":
                break
            piece_up_right = self.get_piece(pos_up_right)
            if piece_up_right == '':
                valid_moves.append(pos_up_right)
            elif piece_up_right.isupper():
                valid_moves.append(pos_up_right)
                break
            else:
                break
        for i in range(1, 8):
            pos_up_left = self.array2grid(row_index - i, col_index - i)
            if pos_up_left == "-1":
                break
            piece_up_left = self.get_piece(pos_up_left)
            if piece_up_left == '':
                valid_moves.append(pos_up_left)
            elif piece_up_left.isupper():
                valid_moves.append(pos_up_left)
                break
            else:
                break
        for i in range(1, 8):
            pos_down_right = self.array2grid(row_index + i, col_index + i)
            if pos_down_right == "-1":
                break
            piece_down_right = self.get_piece(pos_down_right)
            if piece_down_right == '':
                valid_moves.append(pos_down_right)
            elif piece_down_right.isupper():
                valid_moves.append(pos_down_right)
                break
            else:
                break
        for i in range(1, 8):
            pos_down_left = self.array2grid(row_index + i, col_index - i)
            if pos_down_left == "-1":
                break
            piece_down_left = self.get_piece(pos_down_left)
            if piece_down_left == '':
                valid_moves.append(pos_down_left)
            elif piece_down_left.isupper():
                valid_moves.append(pos_down_left)
                break
            else:
                break
        return valid_moves

    def get_white_queen_valid_moves(self, pos: str, piece: str) -> List[str]:
        row_index, col_index = self.grid2array(pos)
        valid_moves = []
        if piece != "Q":
            return valid_moves
        # Implement logic for white queen
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
        for i in range(1, 8):
            pos_up_right = self.array2grid(row_index - i, col_index + i)
            if pos_up_right == "-1":
                break
            piece_up_right = self.get_piece(pos_up_right)
            if piece_up_right == '':
                valid_moves.append(pos_up_right)
            elif piece_up_right.islower():
                valid_moves.append(pos_up_right)
                break
            else:
                break
        for i in range(1, 8):
            pos_up_left = self.array2grid(row_index - i, col_index - i)
            if pos_up_left == "-1":
                break
            piece_up_left = self.get_piece(pos_up_left)
            if piece_up_left == '':
                valid_moves.append(pos_up_left)
            elif piece_up_left.islower():
                valid_moves.append(pos_up_left)
                break
            else:
                break
        for i in range(1, 8):
            pos_down_right = self.array2grid(row_index + i, col_index + i)
            if pos_down_right == "-1":
                break
            piece_down_right = self.get_piece(pos_down_right)
            if piece_down_right == '':
                valid_moves.append(pos_down_right)
            elif piece_down_right.islower():
                valid_moves.append(pos_down_right)
                break
            else:
                break
        for i in range(1, 8):
            pos_down_left = self.array2grid(row_index + i, col_index - i)
            if pos_down_left == "-1":
                break
            piece_down_left = self.get_piece(pos_down_left)
            if piece_down_left == '':
                valid_moves.append(pos_down_left)
            elif piece_down_left.islower():
                valid_moves.append(pos_down_left)
                break
            else:
                break
        return valid_moves
    
    def get_black_queen_valid_moves(self, pos: str, piece: str) -> List[str]:
        row_index, col_index = self.grid2array(pos)
        valid_moves = []
        if piece != "q":
            return valid_moves
        # Implement logic for black queen
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
        for i in range(1, 8):
            pos_up_right = self.array2grid(row_index - i, col_index + i)
            if pos_up_right == "-1":
                break
            piece_up_right = self.get_piece(pos_up_right)
            if piece_up_right == '':
                valid_moves.append(pos_up_right)
            elif piece_up_right.isupper():
                valid_moves.append(pos_up_right)
                break
            else:
                break
        for i in range(1, 8):
            pos_up_left = self.array2grid(row_index - i, col_index - i)
            if pos_up_left == "-1":
                break
            piece_up_left = self.get_piece(pos_up_left)
            if piece_up_left == '':
                valid_moves.append(pos_up_left)
            elif piece_up_left.isupper():
                valid_moves.append(pos_up_left)
                break
            else:
                break
        for i in range(1, 8):
            pos_down_right = self.array2grid(row_index + i, col_index + i)
            if pos_down_right == "-1":
                break
            piece_down_right = self.get_piece(pos_down_right)
            if piece_down_right == '':
                valid_moves.append(pos_down_right)
            elif piece_down_right.isupper():
                valid_moves.append(pos_down_right)
                break
            else:
                break
        for i in range(1, 8):
            pos_down_left = self.array2grid(row_index + i, col_index - i)
            if pos_down_left == "-1":
                break
            piece_down_left = self.get_piece(pos_down_left)
            if piece_down_left == '':
                valid_moves.append(pos_down_left)
            elif piece_down_left.isupper():
                valid_moves.append(pos_down_left)
                break
            else:
                break
        return valid_moves

    def get_white_king_valid_moves(self, pos: str, piece: str) -> List[str]:
        row_index, col_index = self.grid2array(pos)
        valid_moves = []
        if piece != "K":
            return valid_moves
        # Implement logic for white king
        king_moves = [
            (row_index - 1, col_index - 1),  
            (row_index - 1, col_index),      
            (row_index - 1, col_index + 1), 
            (row_index, col_index + 1),      
            (row_index + 1, col_index + 1),  
            (row_index + 1, col_index),      
            (row_index + 1, col_index - 1),  
            (row_index, col_index - 1)   
        ]

        for move in king_moves:
            new_pos = self.array2grid(move[0], move[1])
            if new_pos != "-1":
                piece_at_pos = self.get_piece(new_pos)
                # if (piece_at_pos == '' or piece_at_pos.islower()) and new_pos not in opponent_moves:
                if (piece_at_pos == '' or piece_at_pos.islower()):
                    valid_moves.append(new_pos)
        
        if self.white_king_moved == False:
            if self.white_left_rook_moved == False:
                valid_moves.append("c1")
            if self.white_right_rook_moved == False:
                valid_moves.append("g1")
        
        return valid_moves  

    def get_black_king_valid_moves(self, pos: str, piece: str) -> List[str]:
        row_index, col_index = self.grid2array(pos)
        valid_moves = []
        if piece != "k":
            return valid_moves
        # Implement logic for black king
        king_moves = [
            (row_index - 1, col_index - 1),  
            (row_index - 1, col_index),      
            (row_index - 1, col_index + 1), 
            (row_index, col_index + 1),      
            (row_index + 1, col_index + 1),  
            (row_index + 1, col_index),      
            (row_index + 1, col_index - 1),  
            (row_index, col_index - 1)   
        ]
        
        for move in king_moves:
            new_pos = self.array2grid(move[0], move[1])
            if new_pos != "-1":
                piece_at_pos = self.get_piece(new_pos)
                # if (piece_at_pos == '' or piece_at_pos.islower()) and new_pos not in opponent_moves:
                if (piece_at_pos == '' or piece_at_pos.islower()):
                    valid_moves.append(new_pos)
                    
        if self.black_king_moved == False:
            if self.black_left_rook_moved == False:
                valid_moves.append("c8")
            if self.black_right_rook_moved == False:
                valid_moves.append("g8")
                
        return valid_moves    
    
    # get the array of valid ending position
    def get_valid_end_pos(self, pos: str, piece: str) -> List[str]:
        row_index, col_index = self.grid2array(pos)
        valid_moves = []
        
        
        
        
        if piece == "P":
            valid_moves = self.get_white_pawn_valid_moves(pos, piece)
        
        elif piece == "R":
            valid_moves = self.get_white_rook_valid_moves(pos, piece)
        
        elif piece == "N":
            valid_moves = self.get_white_knight_valid_moves(pos, piece)
        
        elif piece == "B":
            valid_moves = self.get_white_bishop_valid_moves(pos, piece)
            
        elif piece == "Q":
            valid_moves = self.get_white_queen_valid_moves(pos, piece)
        
        elif piece == "K":
            valid_moves = self.get_white_king_valid_moves(pos, piece)
             
        elif piece == "p":
            valid_moves = self.get_black_pawn_valid_moves(pos, piece)

        elif piece == "r":
            valid_moves = self.get_black_rook_valid_moves(pos, piece)
        
        elif piece == "n":
            valid_moves = self.get_black_knight_valid_moves(pos, piece)
        
        elif piece == "b":
            valid_moves = self.get_black_bishop_valid_moves(pos, piece)
        
        elif piece == "q":
            valid_moves = self.get_black_queen_valid_moves(pos, piece)
        
        elif piece == "k":
            valid_moves = self.get_black_king_valid_moves(pos, piece)
        
        return valid_moves  
    
    def check_winning_status(self):
        # get all moves for white pieces
        white_moves = set()
        white_king_pos = ""
        for col in range(ord('a'), ord('h') + 1):
            for row in range(1, 9):
                square = chr(col) + str(row)
                if self.get_piece(square) == 'K':
                    white_king_pos = square
                if self.get_piece(square).isupper():
                    white_moves.update(self.get_valid_end_pos(square, self.get_piece(square)))
        # get all moves for black pieces
        black_moves = set()
        black_king_pos = ""
        for col in range(ord('a'), ord('h') + 1):
            for row in range(1, 9):
                square = chr(col) + str(row)
                if self.get_piece(square) == 'k':
                    black_king_pos = square
                if self.get_piece(square).islower():
                    black_moves.update(self.get_valid_end_pos(square, self.get_piece(square)))
                    
        # Check if either king is in check
        white_in_check = white_king_pos in black_moves
        black_in_check = black_king_pos in white_moves
        
        # Check if white pieces has any legal moves
        white_has_legal_moves = False
        for col in range(ord('a'), ord('h') + 1):
            for row in range(1, 9):
                pos = chr(col) + str(row)
                piece = self.get_piece(pos)
                if piece.isupper():
                    for move in self.get_valid_end_pos(pos, piece):
                        temp_board = [row[:] for row in self.board]
                        temp_result = self.result
                        temp_last_move = self.last_move
                        temp_white_king_moved = self.white_king_moved
                        temp_black_king_moved = self.black_king_moved
                        temp_white_left_rook_moved = self.white_left_rook_moved
                        temp_white_right_rook_moved = self.white_right_rook_moved
                        temp_black_left_rook_moved = self.black_left_rook_moved
                        temp_black_right_rook_moved = self.black_right_rook_moved
                        
                        move_result = self.simulate_move(pos + move)
                        
                        self.board = temp_board
                        self.result = temp_result
                        self.last_move = temp_last_move
                        self.white_king_moved = temp_white_king_moved
                        self.black_king_moved = temp_black_king_moved
                        self.white_left_rook_moved = temp_white_left_rook_moved
                        self.white_right_rook_moved = temp_white_right_rook_moved
                        self.black_left_rook_moved = temp_black_left_rook_moved
                        self.black_right_rook_moved = temp_black_right_rook_moved
                        
                        if move_result != "":
                            white_has_legal_moves = True
                            break
                if white_has_legal_moves:
                    break
            if white_has_legal_moves:
                break
                        
        # Check for black now
        black_has_legal_moves = False
        for col in range(ord('a'), ord('h') + 1):
            for row in range(1, 9):
                pos = chr(col) + str(row)
                piece = self.get_piece(pos)
                if piece.islower():
                    for move in self.get_valid_end_pos(pos, piece):
                        temp_board = [row[:] for row in self.board]
                        temp_result = self.result
                        temp_last_move = self.last_move
                        temp_white_king_moved = self.white_king_moved
                        temp_black_king_moved = self.black_king_moved
                        temp_white_left_rook_moved = self.white_left_rook_moved
                        temp_white_right_rook_moved = self.white_right_rook_moved
                        temp_black_left_rook_moved = self.black_left_rook_moved
                        temp_black_right_rook_moved = self.black_right_rook_moved
                        
                        move_result = self.simulate_move(pos + move)
    
                        self.board = temp_board
                        self.result = temp_result
                        self.last_move = temp_last_move
                        self.white_king_moved = temp_white_king_moved
                        self.black_king_moved = temp_black_king_moved
                        self.white_left_rook_moved = temp_white_left_rook_moved
                        self.white_right_rook_moved = temp_white_right_rook_moved
                        self.black_left_rook_moved = temp_black_left_rook_moved
                        self.black_right_rook_moved = temp_black_right_rook_moved
                        
                        if move_result != "":
                            black_has_legal_moves = True
                            break
                        
                if black_has_legal_moves:
                    break
            if black_has_legal_moves:
                break
        
        if white_in_check and not white_has_legal_moves:
            self.result = "b"
        elif black_in_check and not black_has_legal_moves:
            self.result = "w"
        elif not white_has_legal_moves and not black_has_legal_moves:
            self.result = "d"
        else:
            self.result = ""
        print("Current Winning Status is: " + self.result)
        
    
    

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
        piece = self.get_piece(start_pos)
        promotion = False
        capture = False
        
        if self.last_move != None:
            if piece.isupper() and self.last_move[0].isupper():
                print("Invalid Order, should be black's move now")
                return ""
            if piece.islower() and self.last_move[0].islower():
                print("Invalid Order, should be white's move now")
                return ""
        else:
            if piece.islower():
                print("First move should be white")
                return ""
        

        opponent_moves = set()
        my_king_pos = ""
        if piece != "-1" and piece.isupper():
            # get opponent's possible moves
            for col in range(ord('a'), ord('h') + 1):
                for row in range(1, 9):
                    square = chr(col) + str(row)
                    if self.get_piece(square) == 'K':
                        my_king_pos = square
                    if self.get_piece(square).islower():
                        opponent_moves.update(self.get_valid_end_pos(square, self.get_piece(square)))
                        
        elif piece != "-1" and piece.islower():
            # get opponent's possible moves
            for col in range(ord('a'), ord('h') + 1):
                for row in range(1, 9):
                    square = chr(col) + str(row)
                    if self.get_piece(square) == 'k':
                        my_king_pos = square
                    if self.get_piece(square).isupper():
                        opponent_moves.update(self.get_valid_end_pos(square, self.get_piece(square)))
        if piece == 'k' or piece == 'K':
            if end_pos in opponent_moves:
                print("This move will leave King in Check")
                self.check_winning_status()
                return ""
        if my_king_pos in opponent_moves:
            print("This move will leave King in Check")
            self.check_winning_status()
            return ""
        
        # check for castling
        if(piece == "K" and self.white_king_moved == False):
            start_row_index, start_col_index = self.grid2array(start_pos)
            end_row_index, end_col_index = self.grid2array(end_pos)
            if(start_row_index == end_row_index == 7 and start_col_index == 4 ):
                if(end_col_index == 2 and self.white_left_rook_moved == False):
                    # move to the left
                    if(self.board[7][1] == self.board[7][2] == self.board[7][3] == "" and 
                       "b1" not in opponent_moves and "c1" not in opponent_moves and  "d1" not in opponent_moves and "e1" not in opponent_moves):
                        # then it's a valid castling
                        print("Is valid castling for white king to the left")
                        print(self.get_piece("b1"))
                        self.board[7][4] = ""
                        self.board[7][0] = ""
                        self.board[7][2] = "K"
                        self.board[7][3] = "R"
                        self.white_king_moved = True
                        self.white_left_rook_moved = True
                        self.last_move = piece, start_pos, end_pos
                        extended_chess_notation = "0-0-0"
                        print("extended_chess_notation: " + extended_chess_notation)
                        self.check_winning_status()
                        return extended_chess_notation
                    else:
                        print("Invalid Castling")
                        self.check_winning_status()
                        return ""
                if(end_col_index == 6 and self.white_right_rook_moved == False):
                    # move to the right
                    if(self.board[7][5] == self.board[7][6] == "" and 
                       "e1" not in opponent_moves and "f1" not in opponent_moves and  "g1" not in opponent_moves):
                        # then it's a valid castling
                        print("Is valid castling for white king to the right")
                        self.board[7][4] = ""
                        self.board[7][7] = ""
                        self.board[7][6] = "K"
                        self.board[7][5] = "R"
                        self.white_king_moved = True
                        self.white_right_rook_moved = True
                        self.last_move = piece, start_pos, end_pos
                        extended_chess_notation = "0-0"
                        print("extended_chess_notation: " + extended_chess_notation)
                        self.check_winning_status()
                        return extended_chess_notation
                    else:
                        print("Invalid Castling")
                        self.check_winning_status()
                        return ""
        elif(piece == "k" and self.black_king_moved == False):
            start_row_index, start_col_index = self.grid2array(start_pos)
            end_row_index, end_col_index = self.grid2array(end_pos)
            if(start_row_index == end_row_index == 0 and start_col_index == 4 ):
                if(end_col_index == 2 and self.black_left_rook_moved == False):
                    # move to the left
                    if(self.board[0][1] == self.board[0][2] == self.board[0][3] == "" and 
                       "b8" not in opponent_moves and "c8" not in opponent_moves and  "d8" not in opponent_moves and "e8" not in opponent_moves):
                        # then it's a valid castling
                        print("Is valid castling for black king to the left")
                        self.board[0][4] = ""
                        self.board[0][0] = ""
                        self.board[0][2] = "k"
                        self.board[0][3] = "r"
                        self.black_king_moved = True
                        self.black_left_rook_moved = True
                        self.last_move = piece, start_pos, end_pos
                        extended_chess_notation = "0-0-0"
                        print("extended_chess_notation: " + extended_chess_notation)
                        self.check_winning_status()
                        return extended_chess_notation
                    else:
                        print("Invalid Castling")
                        self.check_winning_status()
                        return ""
                if(end_col_index == 6 and self.black_right_rook_moved == False):
                    # move to the right
                    if(self.board[0][5] == self.board[0][6] == "" and 
                       "e8" not in opponent_moves and "f8" not in opponent_moves and  "g8" not in opponent_moves):
                        # then it's a valid castling
                        print("Is valid castling for black king to the right")
                        self.board[0][4] = ""
                        self.board[0][7] = ""
                        self.board[0][6] = "k"
                        self.board[0][5] = "r"
                        self.black_king_moved = True
                        self.black_right_rook_moved = True
                        self.last_move = piece, start_pos, end_pos
                        extended_chess_notation = "0-0"
                        print("extended_chess_notation: " + extended_chess_notation)
                        self.check_winning_status()
                        return extended_chess_notation
                    else:
                        print("Invalid Castling")
                        self.check_winning_status()
                        return ""
        valid_end_pos = self.get_valid_end_pos(start_pos, piece)
        print("Valid End Pos: ", valid_end_pos)
        
        # now check for En Passant Capture
        if self.last_move != None:
            last_piece, last_start_pos, last_end_pos = self.last_move
            if piece == 'P' and last_piece == 'p':
                # if I'm white pawn and last move is black pawn
                # I want to check
                # 1. Does the last pawn move twice ahead?
                # 2. Am I at the correct pos
                # with both is true, do I want to move at the correct position?
                # If I do want to move at the correct position, then eat it
                
                if abs(int(last_start_pos[1]) - int(last_end_pos[1])) == 2:
                    if start_pos[1] == "5":
                        if end_pos == last_end_pos[0] + str(int(last_end_pos[1]) + 1):
                            start_index = self.grid2array(start_pos)
                            end_index = self.grid2array(end_pos)
                            last_end_index = self.grid2array(last_end_pos)
                            self.board[end_index[0]][end_index[1]] = self.board[start_index[0]][start_index[1]]
                            self.board[start_index[0]][start_index[1]] = ""
                            self.board[last_end_index[0]][last_end_index[1]] = ""
                            capture = True
                            self.last_move = piece, start_pos, end_pos
                            if end_pos[1] == "8":
                                self.board[end_index[0]][end_index[1]] = "Q"
                            extended_chess_notation = (piece.lower() if piece.lower() != "p" else "") + start_pos + "x" + end_pos
                            print("extended_chess_notation: " + extended_chess_notation)
                            self.check_winning_status()
                            return extended_chess_notation
            elif piece == 'p' and last_piece == 'P':
                if abs(int(last_start_pos[1]) - int(last_end_pos[1])) == 2:
                    if start_pos[1] == "4":
                        if end_pos == last_end_pos[0] + str(int(last_end_pos[1]) - 1):
                            start_index = self.grid2array(start_pos)
                            end_index = self.grid2array(end_pos)
                            last_end_index = self.grid2array(last_end_pos)
                            self.board[end_index[0]][end_index[1]] = self.board[start_index[0]][start_index[1]]
                            self.board[start_index[0]][start_index[1]] = ""
                            self.board[last_end_index[0]][last_end_index[1]] = ""
                            capture = True
                            self.last_move = piece, start_pos, end_pos
                            if end_pos[1] == "1":
                                self.board[end_index[0]][end_index[1]] = "q"
                            extended_chess_notation = (piece.lower() if piece.lower() != "p" else "") + start_pos + ("x" if capture else "") + end_pos + ("=Q" if promotion else "")
                            print("extended_chess_notation: " + extended_chess_notation)
                            self.check_winning_status()
                            return extended_chess_notation
        if end_pos in valid_end_pos:   
            start_index = self.grid2array(start_pos)
            end_index = self.grid2array(end_pos)
 
            self.board[end_index[0]][end_index[1]] = self.board[start_index[0]][start_index[1]]
            if(self.board[start_index[0]][start_index[1]] != ""):
                capture = True
            self.board[start_index[0]][start_index[1]] = ""
            self.last_move = piece, start_pos, end_pos
            
            if piece == 'P' and end_pos[1] == "8":
                self.board[end_index[0]][end_index[1]] = "Q"
                promotion = True
            if piece == 'p' and end_pos[1] == "1":
                self.board[end_index[0]][end_index[1]] = "q"
                promotion = True
            if piece == "K" and self.white_king_moved == False:
                self.white_king_moved = True
            if piece == "k" and self.black_king_moved == False:
                self.black_king_moved = True
            if piece == "R" and start_pos == "a1" and self.white_left_rook_moved == False:
                self.white_left_rook_moved = True
            if piece == "R" and start_pos == "h1" and self.white_right_rook_moved == False:
                self.white_right_rook_moved = True
            if piece == "r" and start_pos == "a8" and self.black_left_rook_moved == False:
                self.black_left_rook_moved = True
            if piece == "r" and start_pos == "h8" and self.black_right_rook_moved == False:
                self.black_right_rook_moved = True
            
            
            
            extended_chess_notation = (piece.lower() if piece.lower() != "p" else "") + start_pos + ("x" if capture else "") + end_pos + ("=Q" if promotion else "")
            print("extended_chess_notation: " + extended_chess_notation)
            self.check_winning_status()
            return extended_chess_notation
        
        print("Invalid Moves")
        self.check_winning_status()
        return ""

    def simulate_move(self, move: str) -> str:
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

        piece = self.get_piece(start_pos)
        promotion = False
        capture = False
        

        if self.last_move != None:
            if piece.isupper() and self.last_move[0].isupper():
                return ""
            if piece.islower() and self.last_move[0].islower():
                return ""
        else:
            if piece.islower():
                return ""

        opponent_moves = set()
        my_king_pos = ""
        if piece != "-1" and piece.isupper():
            # get opponent's possible moves
            for col in range(ord('a'), ord('h') + 1):
                for row in range(1, 9):
                    square = chr(col) + str(row)
                    if self.get_piece(square) == 'K':
                        my_king_pos = square
                    if self.get_piece(square).islower():
                        opponent_moves.update(self.get_valid_end_pos(square, self.get_piece(square)))
                        
        elif piece != "-1" and piece.islower():
            # get opponent's possible moves
            for col in range(ord('a'), ord('h') + 1):
                for row in range(1, 9):
                    square = chr(col) + str(row)
                    if self.get_piece(square) == 'k':
                        my_king_pos = square
                    if self.get_piece(square).isupper():
                        opponent_moves.update(self.get_valid_end_pos(square, self.get_piece(square)))
        if piece == 'k' or piece == 'K':
            if end_pos in opponent_moves:

                return ""
        if my_king_pos in opponent_moves:
            return ""
        
        # check for castling
        if(piece == "K" and self.white_king_moved == False):
            start_row_index, start_col_index = self.grid2array(start_pos)
            end_row_index, end_col_index = self.grid2array(end_pos)
            if(start_row_index == end_row_index == 7 and start_col_index == 4 ):
                if(end_col_index == 2 and self.white_left_rook_moved == False):
                    # move to the left
                    if(self.board[7][1] == self.board[7][2] == self.board[7][3] == "" and 
                       "b1" not in opponent_moves and "c1" not in opponent_moves and  "d1" not in opponent_moves and "e1" not in opponent_moves):
                        # then it's a valid castling
                        self.board[7][4] = ""
                        self.board[7][0] = ""
                        self.board[7][2] = "K"
                        self.board[7][3] = "R"
                        self.white_king_moved = True
                        self.white_left_rook_moved = True
                        self.last_move = piece, start_pos, end_pos
                        extended_chess_notation = "0-0-0"
                        return extended_chess_notation
                    else:
                        return ""
                if(end_col_index == 6 and self.white_right_rook_moved == False):
                    # move to the right
                    if(self.board[7][5] == self.board[7][6] == "" and 
                       "e1" not in opponent_moves and "f1" not in opponent_moves and  "g1" not in opponent_moves):
                        # then it's a valid castling
                        self.board[7][4] = ""
                        self.board[7][7] = ""
                        self.board[7][6] = "K"
                        self.board[7][5] = "R"
                        self.white_king_moved = True
                        self.white_right_rook_moved = True
                        self.last_move = piece, start_pos, end_pos
                        extended_chess_notation = "0-0"
                        return extended_chess_notation
                    else:
                        return ""
        elif(piece == "k" and self.black_king_moved == False):
            start_row_index, start_col_index = self.grid2array(start_pos)
            end_row_index, end_col_index = self.grid2array(end_pos)
            if(start_row_index == end_row_index == 0 and start_col_index == 4 ):
                if(end_col_index == 2 and self.black_left_rook_moved == False):
                    # move to the left
                    if(self.board[0][1] == self.board[0][2] == self.board[0][3] == "" and 
                       "b8" not in opponent_moves and "c8" not in opponent_moves and  "d8" not in opponent_moves and "e8" not in opponent_moves):
                        # then it's a valid castling
                        self.board[0][4] = ""
                        self.board[0][0] = ""
                        self.board[0][2] = "k"
                        self.board[0][3] = "r"
                        self.black_king_moved = True
                        self.black_left_rook_moved = True
                        self.last_move = piece, start_pos, end_pos
                        extended_chess_notation = "0-0-0"
                        return extended_chess_notation
                    else:
                        return ""
                if(end_col_index == 6 and self.black_right_rook_moved == False):
                    # move to the right
                    if(self.board[0][5] == self.board[0][6] == "" and 
                       "e8" not in opponent_moves and "f8" not in opponent_moves and  "g8" not in opponent_moves):
                        # then it's a valid castling
                        self.board[0][4] = ""
                        self.board[0][7] = ""
                        self.board[0][6] = "k"
                        self.board[0][5] = "r"
                        self.black_king_moved = True
                        self.black_right_rook_moved = True
                        self.last_move = piece, start_pos, end_pos
                        extended_chess_notation = "0-0"
                        return extended_chess_notation
                    else:
                        return ""
        valid_end_pos = self.get_valid_end_pos(start_pos, piece)
        
        # now check for En Passant Capture
        if self.last_move != None:
            last_piece, last_start_pos, last_end_pos = self.last_move
            if piece == 'P' and last_piece == 'p':
                # if I'm white pawn and last move is black pawn
                # I want to check
                # 1. Does the last pawn move twice ahead?
                # 2. Am I at the correct pos
                # with both is true, do I want to move at the correct position?
                # If I do want to move at the correct position, then eat it
                
                if abs(int(last_start_pos[1]) - int(last_end_pos[1])) == 2:
                    if start_pos[1] == "5":
                        if end_pos == last_end_pos[0] + str(int(last_end_pos[1]) + 1):
                            start_index = self.grid2array(start_pos)
                            end_index = self.grid2array(end_pos)
                            last_end_index = self.grid2array(last_end_pos)
                            self.board[end_index[0]][end_index[1]] = self.board[start_index[0]][start_index[1]]
                            self.board[start_index[0]][start_index[1]] = ""
                            self.board[last_end_index[0]][last_end_index[1]] = ""
                            capture = True
                            self.last_move = piece, start_pos, end_pos
                            if end_pos[1] == "8":
                                self.board[end_index[0]][end_index[1]] = "Q"
                            extended_chess_notation = (piece.lower() if piece.lower() != "p" else "") + start_pos + "x" + end_pos
                            return extended_chess_notation
            elif piece == 'p' and last_piece == 'P':
                if abs(int(last_start_pos[1]) - int(last_end_pos[1])) == 2:
                    if start_pos[1] == "4":
                        if end_pos == last_end_pos[0] + str(int(last_end_pos[1]) - 1):
                            start_index = self.grid2array(start_pos)
                            end_index = self.grid2array(end_pos)
                            last_end_index = self.grid2array(last_end_pos)
                            self.board[end_index[0]][end_index[1]] = self.board[start_index[0]][start_index[1]]
                            self.board[start_index[0]][start_index[1]] = ""
                            self.board[last_end_index[0]][last_end_index[1]] = ""
                            capture = True
                            self.last_move = piece, start_pos, end_pos
                            if end_pos[1] == "1":
                                self.board[end_index[0]][end_index[1]] = "q"
                            extended_chess_notation = (piece.lower() if piece.lower() != "p" else "") + start_pos + ("x" if capture else "") + end_pos + ("=Q" if promotion else "")
                            return extended_chess_notation
        if end_pos in valid_end_pos:   
            start_index = self.grid2array(start_pos)
            end_index = self.grid2array(end_pos)
 
            self.board[end_index[0]][end_index[1]] = self.board[start_index[0]][start_index[1]]
            if(self.board[start_index[0]][start_index[1]] != ""):
                capture = True
            self.board[start_index[0]][start_index[1]] = ""
            self.last_move = piece, start_pos, end_pos
            
            if piece == 'P' and end_pos[1] == "8":
                self.board[end_index[0]][end_index[1]] = "Q"
                promotion = True
            if piece == 'p' and end_pos[1] == "1":
                self.board[end_index[0]][end_index[1]] = "q"
                promotion = True
            if piece == "K" and self.white_king_moved == False:
                self.white_king_moved = True
            if piece == "k" and self.black_king_moved == False:
                self.black_king_moved = True
            if piece == "R" and start_pos == "a1" and self.white_left_rook_moved == False:
                self.white_left_rook_moved = True
            if piece == "R" and start_pos == "h1" and self.white_right_rook_moved == False:
                self.white_right_rook_moved = True
            if piece == "r" and start_pos == "a8" and self.black_left_rook_moved == False:
                self.black_left_rook_moved = True
            if piece == "r" and start_pos == "h8" and self.black_right_rook_moved == False:
                self.black_right_rook_moved = True
            
            
            
            extended_chess_notation = (piece.lower() if piece.lower() != "p" else "") + start_pos + ("x" if capture else "") + end_pos + ("=Q" if promotion else "")
            return extended_chess_notation
        

        return ""