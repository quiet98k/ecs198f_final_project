import pygame

from display.classes.Square import Square
from display.classes.Piece import Piece

from logic.chess_logic import ChessLogic

class Board:
    def __init__(self, width: int, height: int, logic: ChessLogic):
        """
        Object representing the Chess Board

        Args:
            width (int): The width of the Chess Board
            height (int): The height of the Chess Board
            logic (ChessLogic): ChessLogic object which implements the Chess Game Logic 
                (i.e. Board Representation, Move Making Logic)
        """
        self.width = width
        self.height = height
        self.tile_width = width // 8
        self.tile_height = height // 8
        self.selected_piece = None

        self.logic = logic
        self.squares: list[Square] = self.generate_squares()

        self.start_pos = ""
        self.end_pos = ""

    def generate_squares(self):
        """
        Construct all Square Objects of the Chess Board and place pieces based on the ChessLogic Board Representation
        """
        output = []
        for y in range(8):
            for x in range(8):
                piece = None
                if self.logic.board[y][x] != "":
                    piece = Piece(self.logic.board[y][x], self.tile_width, self.tile_height)
                square = Square(x, y, self.tile_width, self.tile_height)
                square.set_occuping_piece(piece)
                output.append(square)
        return output

    def get_square_from_pos(self, pos: tuple[int, int]) -> Square | None:
        """
        Get Square Object from Relative Position of Square

        Args:
            pos (tuple[int, int]): (x, y) coordinates of the Square
        
        Returns:
            Square | None: Square Object for Relative Position or None if invalid coordinates supplied
        """ 
        for square in self.squares:
            if (square.x, square.y) == (pos[0], pos[1]):
                return square
    
    def handle_click(self, mx: int, my: int):
        """
        Pygame Event Handler for when user clicks the board. 
        
        Calls the ChessLogic play_move function if a move has been parsed

        Args:
            mx (int): Absolute x coordinate of click
            my (int): Absolute y coordinate of click
        """
        x = mx // self.tile_width
        y = my // self.tile_height
        clicked_square = self.get_square_from_pos((x, y))
        if clicked_square is not None:
            if self.start_pos == "":
                self.start_pos = clicked_square.get_coord()
            elif self.end_pos == "":
                self.end_pos = clicked_square.get_coord()
                if self.start_pos != self.end_pos:
                    self.logic.play_move(f"{self.start_pos}{self.end_pos}")
                self.start_pos = ""
                self.end_pos = ""
    
    def draw(self, display, font):
        """
        Draws the Board, with result message if applicable, on Pygame Screen

        Args:
            display: Pygame Screen Object
            font: Pygame Font Object
        """
        self.squares = self.generate_squares()
        for square in self.squares:
            square.draw(display)
        if self.logic.result != "":
            white = (255, 255, 255)
            black = (0, 0, 0)
            red = (255, 0, 0)
            gray = (200, 200, 200)

            message = "Draw"
            if self.logic.result == "w":
                message = "White wins"
            elif self.logic.result == "b":
                message = "Black wins"
            text_surface = font.render(message, True, white)
            text_rect = text_surface.get_rect(center=(self.width // 2, self.height // 2))
            rect_width = text_rect.width + 40
            rect_height = text_rect.height + 20
            rect_x = text_rect.x - 20
            rect_y = text_rect.y - 10

            pygame.draw.rect(display, gray, (rect_x, rect_y, rect_width, rect_height))
            pygame.draw.rect(display, red, (rect_x, rect_y, rect_width, rect_height), 3)

            display.blit(text_surface, text_rect)