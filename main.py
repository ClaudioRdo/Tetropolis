from graphics import Canvas
import time

ROWS = 20
COLS = 10
CELL_SIZE = 30

CANVAS_WIDTH = COLS * CELL_SIZE
CANVAS_HEIGHT = ROWS * CELL_SIZE

DELAY = 0.2

O_PIECE = [
    [1, 1],
    [1, 1]
]

def draw_board(canvas):
    for row in range(ROWS):
        for col in range(COLS):

            x1 = col * CELL_SIZE
            y1 = row * CELL_SIZE

            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE

            canvas.create_rectangle(
                x1,
                y1,
                x2,
                y2,
                "black",
                "gray"
            )

def draw_board_cells(canvas, board):

    for row in range(ROWS):
        for col in range(COLS):

            if board[row][col] == 1:

                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE

                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE

                canvas.create_rectangle(
                    x1,
                    y1,
                    x2,
                    y2,
                    "cyan"
                )

def draw_piece(canvas, piece, start_row, start_col):

    for row in range(len(piece)):
        for col in range(len(piece[row])):

            if piece[row][col] == 1:

                x1 = (start_col + col) * CELL_SIZE
                y1 = (start_row + row) * CELL_SIZE

                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE

                canvas.create_rectangle(
                    x1,
                    y1,
                    x2,
                    y2,
                    "yellow"
                )

def place_piece(board, piece, piece_row, piece_col):

    for row in range(len(piece)):
        for col in range(len(piece[row])):

            if piece[row][col] == 1:

                board[piece_row + row][piece_col + col] = 1

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.set_canvas_background_color("black")

    piece_row = 0
    piece_col = 4

    board = []

    for row in range(ROWS):
        board.append([0] * COLS)
        
    while True:
        canvas.clear()

        draw_board(canvas)

        draw_board_cells(canvas, board)

        draw_piece(
            canvas,
            O_PIECE,
            piece_row,
            piece_col
        )

        piece_row += 1

        if piece_row >= ROWS - len(O_PIECE):
            place_piece(
                board,
                O_PIECE,
                piece_row,
                piece_col
            )

            piece_row = 0
            piece_col = 4

        time.sleep(DELAY)

if __name__ == "__main__":
    main()