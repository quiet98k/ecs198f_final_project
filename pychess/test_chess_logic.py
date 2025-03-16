import pytest
from logic.chess_logic import ChessLogic

# Coordinate conversion tests
def test_array2grid():
    """Test the array2grid conversion function."""
    chess = ChessLogic()
    # Test valid indices
    grid = [
        ["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"],
        ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"],
        ["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6"],
        ["a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5"],
        ["a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4"],
        ["a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3"],
        ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"],
        ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"]
    ]
    for i in range(8):
        for j in range(8):
            assert chess.array2grid(i, j) == grid[i][j]
    
    # Test invalid indices
    assert chess.array2grid(-1, 0) == "-1"
    assert chess.array2grid(0, -1) == "-1"
    assert chess.array2grid(8, 0) == "-1"
    assert chess.array2grid(0, 8) == "-1"

def test_grid2array():
    """Test the grid2array conversion function."""
    chess = ChessLogic()

    grid_to_array = [
        [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)],
        [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)],
        [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7)],
        [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7)],
        [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7)],
        [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7)],
        [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7)],
        [(7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7)],
    ]
    positions = [
        ["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"],
        ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"],
        ["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6"],
        ["a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5"],
        ["a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4"],
        ["a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3"],
        ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"],
        ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"]
    ]
    
    # Test all valid positions
    for i in range(8):
        for j in range(8):
            assert chess.grid2array(positions[i][j]) == grid_to_array[i][j]
    
    assert chess.grid2array("a0") == (-1, -1)  
    assert chess.grid2array("a9") == (-1, -1)  
    assert chess.grid2array("`8") == (-1, -1)  
    assert chess.grid2array("i8") == (-1, -1)  
    assert chess.grid2array("i9") == (-1, -1)  

# Piece retrieval tests
def test_get_piece():
    """Test piece retrieval from the board."""
    chess = ChessLogic()
    
    assert chess.get_piece("a8") == "r"  # Black rook
    assert chess.get_piece("b8") == "n"  # Black knight
    assert chess.get_piece("c8") == "b"  # Black bishop
    assert chess.get_piece("d8") == "q"  # Black queen
    assert chess.get_piece("e8") == "k"  # Black king
    assert chess.get_piece("f8") == "b"  # Black bishop
    assert chess.get_piece("g8") == "n"  # Black knight
    assert chess.get_piece("h8") == "r"  # Black rook
    
    assert chess.get_piece("a7") == "p"  # Black pawn
    assert chess.get_piece("b7") == "p"  # Black pawn
    assert chess.get_piece("c7") == "p"  # Black pawn
    assert chess.get_piece("d7") == "p"  # Black pawn
    assert chess.get_piece("e7") == "p"  # Black pawn
    assert chess.get_piece("f7") == "p"  # Black pawn
    assert chess.get_piece("g7") == "p"  # Black pawn
    assert chess.get_piece("h7") == "p"  # Black pawn
    
    # White pieces (last and second-to-last rows)
    assert chess.get_piece("a1") == "R"  # White rook
    assert chess.get_piece("b1") == "N"  # White knight
    assert chess.get_piece("c1") == "B"  # White bishop
    assert chess.get_piece("d1") == "Q"  # White queen
    assert chess.get_piece("e1") == "K"  # White king
    assert chess.get_piece("f1") == "B"  # White bishop
    assert chess.get_piece("g1") == "N"  # White knight
    assert chess.get_piece("h1") == "R"  # White rook
    
    assert chess.get_piece("a2") == "P"  # White pawn
    assert chess.get_piece("b2") == "P"  # White pawn
    assert chess.get_piece("c2") == "P"  # White pawn
    assert chess.get_piece("d2") == "P"  # White pawn
    assert chess.get_piece("e2") == "P"  # White pawn
    assert chess.get_piece("f2") == "P"  # White pawn
    assert chess.get_piece("g2") == "P"  # White pawn
    assert chess.get_piece("h2") == "P"  # White pawn
    
    # Test empty squares
    assert chess.get_piece("a3") == ""  # Empty square
    assert chess.get_piece("b3") == ""  # Empty square
    assert chess.get_piece("e4") == ""  # Empty square
    assert chess.get_piece("h6") == ""  # Empty square
    

# Pawn move validation tests
def test_white_pawn_valid_moves():
    """Test white pawn movement validation."""
    # check pawn first move one square
    chess = ChessLogic()
    chess.check_order = False
    for col in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
        assert chess.get_white_pawn_valid_moves(col+'2', 'P') == [col+'3', col+'4']
        assert chess.play_move(col+'2'+col+'3') == col+'2'+col+'3'
        assert chess.get_piece(col+'2') == ""
        assert chess.get_piece(col+"3") == "P"
        assert chess.get_white_pawn_valid_moves(col+'3', 'P') == [col+'4']
        
        
    # check pawn first move two square
    chess = ChessLogic()
    chess.check_order = False
    for col in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
        assert chess.get_white_pawn_valid_moves(col+'2', 'P') == [col+'3', col+'4']
        assert chess.play_move(col+'2'+col+'4') == col+'2'+col+'4'
        assert chess.get_piece(col+'2') == ""
        assert chess.get_piece(col+"4") == "P"
        assert chess.get_white_pawn_valid_moves(col+'4', 'P') == [col+'5']

def test_black_pawn_valid_moves():
    # check pawn first move one square
    chess = ChessLogic()
    chess.check_order = False
    for col in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:        
        assert chess.get_black_pawn_valid_moves(col+'7', 'p') == [col+'6', col+'5']
        assert chess.play_move(col+'7'+col+'6') == col+'7'+col+'6'
        assert chess.get_piece(col+'7') == ""
        assert chess.get_piece(col+"6") == "p"
        assert chess.get_black_pawn_valid_moves(col+'6', 'p') == [col+'5']
        
    # check pawn first move two square
    chess = ChessLogic()
    chess.check_order = False
    for col in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:        
        assert chess.get_black_pawn_valid_moves(col+'7', 'p') == [col+'6', col+'5']
        assert chess.play_move(col+'7'+col+'5') == col+'7'+col+'5'
        assert chess.get_piece(col+'7') == ""
        assert chess.get_piece(col+"5") == "p"
        assert chess.get_black_pawn_valid_moves(col+'5', 'p') == [col+'4']

def test_pawn_captures():
    # White pawn captures
    chess = ChessLogic()
    chess.check_order = False
    # Place a black piece to be captured
    assert chess.play_move("d7d5") == "d7d5"
    assert chess.play_move("e2e4") == "e2e4"
    assert "d5" in chess.get_white_pawn_valid_moves("e4", "P")
    assert chess.play_move("e4d5") == "e4xd5"
    assert chess.get_piece("d5") == "P"
    assert chess.get_piece("e4") == ""
    
    chess = ChessLogic()
    chess.check_order = False
    # Place a black piece to be captured
    assert chess.play_move("d7d5") == "d7d5"
    assert chess.play_move("c2c4") == "c2c4"
    assert "d5" in chess.get_white_pawn_valid_moves("c4", "P")
    assert chess.play_move("c4d5") == "c4xd5"
    assert chess.get_piece("d5") == "P"
    assert chess.get_piece("c4") == ""
    
    
    # Black pawn captures
    chess = ChessLogic()
    chess.check_order = False
    # Place a white piece to be captured
    assert chess.play_move("d2d4") == "d2d4"
    assert chess.play_move("e7e5") == "e7e5"
    assert "d4" in chess.get_black_pawn_valid_moves("e5", "p")
    assert chess.play_move("e5d4") == "e5xd4"
    assert chess.get_piece("d4") == "p"
    
    chess = ChessLogic()
    chess.check_order = False
    # Place a white piece to be captured
    assert chess.play_move("d2d4") == "d2d4"
    assert chess.play_move("c7c5") == "c7c5"
    assert "d4" in chess.get_black_pawn_valid_moves("c5", "p")
    assert chess.play_move("c5d4") == "c5xd4"
    assert chess.get_piece("d4") == "p"

def test_pawn_en_passant():
    """Test en passant capture for both pawns."""
    chess = ChessLogic()
    # Test white capturing black via en passant
    # check for right capture
    for col in ["a", "b", "c", "d", "e", "f", "g"]:
        chess = ChessLogic()
        chess.check_order = False
        assert chess.play_move(col+"2"+col+"4") == col+"2"+col+"4"
        assert chess.play_move(col+"4"+col+"5") == col+"4"+col+"5"
        assert chess.play_move(chr(ord(col) + 1)+"7"+chr(ord(col) + 1)+"5") == chr(ord(col) + 1)+"7"+chr(ord(col) + 1)+"5"
        assert chess.play_move(col+"5"+chr(ord(col) + 1)+"6") == col+"5"+'x'+chr(ord(col) + 1)+"6"
    # check for left capture
    for col in ["b", "c", "d", "e", "f", "g", "h"]:
        chess = ChessLogic()
        chess.check_order = False
        assert chess.play_move(col+"2"+col+"4") == col+"2"+col+"4"
        assert chess.play_move(col+"4"+col+"5") == col+"4"+col+"5"
        assert chess.play_move(chr(ord(col) - 1)+"7"+chr(ord(col) - 1)+"5") == chr(ord(col) - 1)+"7"+chr(ord(col) - 1)+"5"
        assert chess.play_move(col+"5"+chr(ord(col) - 1)+"6") == col+"5"+'x'+chr(ord(col) - 1)+"6"
        
    # Test black capturing white via en passant
    # check for right capture
    for col in ["a", "b", "c", "d", "e", "f", "g"]:
        chess = ChessLogic()
        chess.check_order = False
        assert chess.play_move(col+"7"+col+"5") == col+"7"+col+"5"
        assert chess.play_move(col+"5"+col+"4") == col+"5"+col+"4"
        assert chess.play_move(chr(ord(col) + 1)+"2"+chr(ord(col) + 1)+"4") == chr(ord(col) + 1)+"2"+chr(ord(col) + 1)+"4"
        assert chess.play_move(col+"4"+chr(ord(col) + 1)+"3") == col+"4"+'x'+chr(ord(col) + 1)+"3"
    # check for left capture
    for col in ["b", "c", "d", "e", "f", "g", "h"]:
        chess = ChessLogic()
        chess.check_order = False
        assert chess.play_move(col+"7"+col+"5") == col+"7"+col+"5"
        assert chess.play_move(col+"5"+col+"4") == col+"5"+col+"4"
        assert chess.play_move(chr(ord(col) - 1)+"2"+chr(ord(col) - 1)+"4") == chr(ord(col) - 1)+"2"+chr(ord(col) - 1)+"4"
        assert chess.play_move(col+"4"+chr(ord(col) - 1)+"3") == col+"4"+'x'+chr(ord(col) - 1)+"3"
        
    # Test invalid en passant attempts
    # check for right capture
    for col in ["a", "b", "c", "d", "e", "f", "g"]:
        chess = ChessLogic()
        chess.check_order = False
        assert chess.play_move(col+"2"+col+"4") == col+"2"+col+"4"
        assert chess.play_move(col+"4"+col+"5") == col+"4"+col+"5"
        assert chess.play_move(chr(ord(col) + 1)+"7"+chr(ord(col) + 1)+"5") == chr(ord(col) + 1)+"7"+chr(ord(col) + 1)+"5"
        assert chess.play_move("b1a3") == "nb1a3"
        assert chess.play_move(col+"5"+chr(ord(col) + 1)+"6") == ""
    # check for left capture
    for col in ["b", "c", "d", "e", "f", "g", "h"]:
        chess = ChessLogic()
        chess.check_order = False
        assert chess.play_move(col+"2"+col+"4") == col+"2"+col+"4"
        assert chess.play_move(col+"4"+col+"5") == col+"4"+col+"5"
        assert chess.play_move(chr(ord(col) - 1)+"7"+chr(ord(col) - 1)+"5") == chr(ord(col) - 1)+"7"+chr(ord(col) - 1)+"5"
        assert chess.play_move("b1a3") == "nb1a3"
        assert chess.play_move(col+"5"+chr(ord(col) - 1)+"6") == ""
        
    # Test black capturing white via en passant
    # check for right capture
    for col in ["a", "b", "c", "d", "e", "f", "g"]:
        chess = ChessLogic()
        chess.check_order = False
        assert chess.play_move(col+"7"+col+"5") == col+"7"+col+"5"
        assert chess.play_move(col+"5"+col+"4") == col+"5"+col+"4"
        assert chess.play_move(chr(ord(col) + 1)+"2"+chr(ord(col) + 1)+"4") == chr(ord(col) + 1)+"2"+chr(ord(col) + 1)+"4"
        assert chess.play_move("b8a6") == "nb8a6"
        assert chess.play_move(col+"4"+chr(ord(col) + 1)+"3") == ""
    # check for left capture
    for col in ["b", "c", "d", "e", "f", "g", "h"]:
        chess = ChessLogic()
        chess.check_order = False
        assert chess.play_move(col+"7"+col+"5") == col+"7"+col+"5"
        assert chess.play_move(col+"5"+col+"4") == col+"5"+col+"4"
        assert chess.play_move(chr(ord(col) - 1)+"2"+chr(ord(col) - 1)+"4") == chr(ord(col) - 1)+"2"+chr(ord(col) - 1)+"4"
        assert chess.play_move("b8a6") == "nb8a6"
        assert chess.play_move(col+"4"+chr(ord(col) - 1)+"3") == ""

# Rook move validation tests
def test_white_rook_valid_moves():
    """Test white rook movement validation."""
    chess = ChessLogic()
    chess.check_order = False
    assert chess.play_move("a1a2") == ""
    assert chess.play_move("a1a3") == ""
    assert chess.play_move("a1b1") == ""
    assert chess.play_move("a1c1") == ""
    assert chess.play_move("a2a4") == "a2a4"
    assert chess.play_move("")
    
    
    # Test horizontal and vertical movements
    # Test captures
    # Test blocked paths
    

def test_black_rook_valid_moves():
    """Test black rook movement validation."""
    chess = ChessLogic()
    # Similar tests as white rook

# Knight move validation tests
def test_white_knight_valid_moves():
    """Test white knight movement validation."""
    chess = ChessLogic()
    # Test L-shaped moves
    # Test edge cases (near board edges)
    # Test captures

def test_black_knight_valid_moves():
    """Test black knight movement validation."""
    chess = ChessLogic()
    # Similar tests as white knight

# Bishop move validation tests
def test_white_bishop_valid_moves():
    """Test white bishop movement validation."""
    chess = ChessLogic()
    # Test diagonal movements
    # Test captures
    # Test blocked paths

def test_black_bishop_valid_moves():
    """Test black bishop movement validation."""
    chess = ChessLogic()
    # Similar tests as white bishop

# Queen move validation tests
def test_white_queen_valid_moves():
    """Test white queen movement validation."""
    chess = ChessLogic()
    # Test horizontal, vertical, and diagonal movements
    # Test captures
    # Test blocked paths

def test_black_queen_valid_moves():
    """Test black queen movement validation."""
    chess = ChessLogic()
    # Similar tests as white queen

# King move validation tests
def test_white_king_valid_moves():
    """Test white king movement validation."""
    chess = ChessLogic()
    # Test one square moves in all directions
    # Test invalid moves into check
    # Test captures

def test_black_king_valid_moves():
    """Test black king movement validation."""
    chess = ChessLogic()
    # Similar tests as white king

# Castling tests
def test_white_castling():
    """Test white castling mechanics."""
    
    # Test kingside castling

    # valid castling
    chess = ChessLogic()
    chess.check_order = False
    assert chess.play_move("a2a4") == "a2a4"
    assert chess.play_move("b2b4") == "b2b4"
    assert chess.play_move("c2c4") == "c2c4"
    assert chess.play_move("d2d4") == "d2d4"
    assert chess.play_move("b1c3") == "nb1c3"
    assert chess.play_move("c1a3") == "bc1a3"
    assert chess.play_move("d1b3") == "qd1b3"
    assert chess.play_move("e1c1") == "0-0-0"
    assert chess.get_piece("c1") == "K"
    assert chess.get_piece("d1") == "R"
    
    
    
    
    
    # some piece in the middle
    # thread start pos(for king? rook?)
    # thread middle pos
    # thread end pos(king? rook?)
    
    
    
    # Test queenside castling
    # Test invalid castling (pieces in way, king/rook moved, etc.)
    # Test castling through check

def test_black_castling():
    """Test black castling mechanics."""
    chess = ChessLogic()
    # Similar tests as white castling

def test_wining_status():
    """Test white win with one move"""
    # chess.board = [
    #     ['', '', '', '', '', '', '', ''],
    #     ['', '', '', '', '', '', '', ''],
    #     ['', '', '', '', '', '', '', ''],
    #     ['', '', '', '', '', '', '', ''],
    #     ['', '', '', '', '', '', '', ''],
    #     ['', '', '', '', '', '', '', ''],
    #     ['', '', '', '', '', '', '', ''],
    #     ['', '', '', '', '', '', '', ''],
    # ]
    
    chess = ChessLogic()
    chess.check_order = False
    chess.board = [
        ['', '', '', '', '', '', '', ''],
        ['k', 'p', 'p', 'N', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', 'P', '', '', '', '', '', ''],
        ['', 'K', 'P', '', '', '', '', ''],
        ['', '', 'R', '', '', '', '', ''],
    ]
    assert chess.play_move("c1a1") == "rc1a1"
    assert chess.result == "w"
    
    chess = ChessLogic()
    chess.check_order = False
    chess.board = [
        ['', '', '', '', 'k', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', 'K', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['R', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
    ]
    assert chess.play_move("a2a8") == "ra2a8"
    assert chess.result == "w"
    
    chess = ChessLogic()
    chess.check_order = False
    chess.board = [
        ['', '', '', '', '', '', 'k', ''],
        ['', '', '', '', '', 'p', 'p', 'p'],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', 'P', ''],
        ['', '', '', '', '', 'P', 'K', ''],
        ['R', '', '', '', '', '', '', ''],
    ]
    assert chess.play_move("a1a8") == "ra1a8"
    assert chess.result == "w"
    
    chess = ChessLogic()
    chess.check_order = False
    chess.board = [
        ['', '', '', '', '', '', 'k', ''],
        ['', '', '', '', '', 'p', 'p', 'p'],
        ['p', '', '', '', '', '', '', ''],
        ['p', '', '', '', '', '', '', ''],
        ['', '', '', '', '', 'b', '', ''],
        ['', '', '', '', '', '', '', 'P'],
        ['', '', '', '', '', 'P', 'P', ''],
        ['', '', '', 'R', '', '', 'K', ''],
    ]
    assert chess.play_move("d1d8") == "rd1d8"
    assert chess.result == "w"
    
    chess = ChessLogic()
    chess.check_order = False
    chess.board = [
        ['r', '', 'b', 'q', 'k', 'b', '', 'r'],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        ['','','n','','','n','',''],
        ['','','','Q','','','',''],
        ['','','B','','P','','',''],
        ['','','','','','','',''],
        ['P', 'B', '', '', '', 'P', 'P', 'P'],
        ['R', 'N', '', '', 'K', '', 'N', 'R'],
    ]
    assert chess.play_move("d5f7") == "qd5xf7"
    assert chess.result == "w"
    
    chess = ChessLogic()
    chess.check_order = False
    chess.board = [
        ['r', 'n', '', 'k', '', 'b', 'b', 'r'],
        ['p', 'p', '', '', 'n', 'q', 'p', 'p'],
        ['','','','p','','p','',''],
        ['','N','p','','p','','',''],
        ['','','','','P','P','',''],
        ['','','','P','','N','P',''],
        ['P', 'P', 'P', 'B', '', '', '', 'P'],
        ['', 'K', 'R', '', 'Q', 'B', '', 'R'],
    ]
    assert chess.play_move("f7a2") == "qf7xa2"
    assert chess.result == "b"
    
    chess = ChessLogic()
    chess.check_order = False
    chess.board = [
        ['', '', 'r', '', '', 'r', 'k', ''],
        ['p', '', '', '', '', 'p', 'p', ''],
        ['', 'p', '', '', '', 'n', '', 'p'],
        ['', '', '', '', 'p', 'N', '', ''],
        ['', '', '', '', 'P', '', '', ''],
        ['', '', 'q', '', 'P', '', '', ''],
        ['n', '', 'P', 'R', 'Q', '', 'P', 'P'],
        ['', '', '', 'K', '', 'R', '', ''],
    ]
    assert chess.play_move("c3a1") == "qc3a1"
    assert chess.result == "b"
    
    
def test_draw_status():
    # chess = ChessLogic()
    # chess.board = [
    #     ['', '', '', '', '', '', 'K', ''],
    #     ['r', '', '', '', '', '', '', ''],
    #     ['', '', '', '', '', '', '', ''],
    #     ['', '', '', '', '', '', '', ''],
    #     ['', '', '', '', '', '', '', ''],
    #     ['', '', '', '', '', '', '', ''],
    #     ['', '', '', '', '', '', '', ''],
    #     ['', '', '', '', '', 'r', '', ''],
    # ]
    # assert chess.play_move("g8h8") == "kg8h8"
    # assert chess.result == ""
    # assert chess.play_move("f1g1") == "rf1g1"
    # assert chess.result == "d"
    
    chess = ChessLogic()
    chess.board = [
        ['', '', '', '', '', '', '', 'k'],
        ['R', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', 'R', '', ''],
    ]
    # assert chess.play_move("g8h8") == "kg8h8"
    assert chess.play_move("f1g1") == "rf1g1"
    assert chess.result == "d"