import pygame
import math

from display.classes.Piece import Piece

class Square:
    def __init__(self, x: int, y: int, width: int, height: int):
        """
        Object representing one square of the chess board

        Args:
            x (int): Relative x position of this square with respect to other tiles
            y (int): Relative y position of this square with respect to other tiles
            width (int): The width of the square
            height (int): The height of the square
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.abs_x = x * width
        self.abs_y = y * width
        self.abs_pos = (self.abs_x, self.abs_y)
        self.pos = (x, y)
        if (x + y) % 2 == 0:
            self.color = "light"
            self.draw_color = (200, 208, 194)
            self.highlight_color = (100, 249, 83)
        else:
            self.color = "dark"
            self.draw_color = (53, 53, 53)
            self.highlight_color = (0, 228, 10)
        self.occupying_piece = None
        self.coord = self.get_coord()
        self.highlight = False
        self.rect = pygame.Rect(self.abs_x, self.abs_y, self.width, self.height)

    def get_coord(self) -> str:
        """
        Calculate the Chess Coordinate (i.e. a1) for Square

        Returns:
            str: The Chess Coordinate of Square
        """
        columns = "abcdefgh"
        return columns[self.x] + str(int(math.fabs(self.y - 8)))
    
    def set_occuping_piece(self, piece: Piece | None):
        """
        Set/Clear a Piece on Square

        Args:
            piece (Piece | None): piece to set to square, None to clear
        """
        self.occupying_piece = piece
    
    def draw(self, display):
        """
        Draw the Square on Pygame Screen

        Args:
            display: Pygame Screen Object
        """
        if self.highlight:
            pygame.draw.rect(display, self.highlight_color, self.rect)
        else:
            pygame.draw.rect(display, self.draw_color, self.rect)
        
        if self.occupying_piece != None:
            centering_rect = self.occupying_piece.img.get_rect()
            centering_rect.center = self.rect.center
            display.blit(self.occupying_piece.img, centering_rect.topleft)
