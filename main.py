from graphics import Canvas

ROWS = 20
COLS = 10
CELL_SIZE = 30

CANVAS_WIDTH = COLS * CELL_SIZE
CANVAS_HEIGHT = ROWS * CELL_SIZE

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
                "white",
                "black"
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
                    "yellow",
                    "black"
                )

  
def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    draw_board(canvas)

    draw_piece(
        canvas,
        O_PIECE,
        0,
        4
    )

if __name__ == "__main__":
    main()