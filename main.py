from graphics import Canvas
import time
import random

ROWS = 20
COLS = 10
CELL_SIZE = 30

CANVAS_WIDTH = COLS * CELL_SIZE
CANVAS_HEIGHT = ROWS * CELL_SIZE

DELAY = 0.2


# BUILDINGS

HOUSE = [
    [1]
]

TOWER = [
    [1],
    [1],
    [1]
]

BLOCK = [
    [1, 1],
    [1, 1]
]

SKYSCRAPER = [
    [1],
    [1],
    [1],
    [1],
    [1]
]

BUILDINGS = [
    HOUSE,
    TOWER,
    BLOCK,
    SKYSCRAPER
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


def can_move_down(board, piece, piece_row, piece_col):

    if piece_row >= ROWS - len(piece):
        return False

    for row in range(len(piece)):
        for col in range(len(piece[row])):

            if piece[row][col] == 1:

                next_row = piece_row + row + 1
                next_col = piece_col + col

                if board[next_row][next_col] == 1:
                    return False

    return True


def main():

    canvas = Canvas(
        CANVAS_WIDTH,
        CANVAS_HEIGHT
    )

    canvas.set_canvas_background_color("black")

    board = []

    for row in range(ROWS):
        board.append([0] * COLS)

    current_piece = random.choice(BUILDINGS)

    piece_row = 0
    piece_col = 4

    while True:

        key = canvas.get_last_key_press()

        if (
            key == "LEFT_ARROW"
            and piece_col > 0
        ):
            piece_col -= 1

        if (
            key == "RIGHT_ARROW"
            and piece_col < COLS - len(current_piece[0])
        ):
            piece_col += 1

        canvas.clear()

        draw_board(canvas)

        draw_board_cells(canvas, board)

        draw_piece(
            canvas,
            current_piece,
            piece_row,
            piece_col
        )

        if can_move_down(
            board,
            current_piece,
            piece_row,
            piece_col
        ):
            piece_row += 1

        else:

            place_piece(
                board,
                current_piece,
                piece_row,
                piece_col
            )

            current_piece = random.choice(
                BUILDINGS
            )

            piece_row = 0

            piece_col = random.randint(
                0,
                COLS - len(current_piece[0])
            )

        time.sleep(DELAY)


if __name__ == "__main__":
    main()