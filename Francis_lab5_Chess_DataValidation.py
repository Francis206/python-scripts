#IT280 Lab5 "“Data Validation Lab"

#Provided Data
board = {'2a': 'wP', '1a': 'wR', '1b': 'wQ', '1f': 'wN', '3a': 'wB',
         '5a': 'wK', '7d': 'wB', '4h': 'wN', '2d': 'wP', '7a': 'bR', '7c': 'bQ', '7e': 'bP',
         '7h': 'bP', '8a': 'bN', '8d': 'bK', '8f': 'bP', '6g': 'bN', '5d': 'bP', '5g': 'bP',
         '8h': 'bB', '2h': 'bN', '3h': 'bN'}

#Define Pieces
black_pieces = 0
white_pieces = 0
total_pieces = 0
white_king = 0
black_king = 0
white_queen = 0
black_queen = 0
white_rook = 0
black_rook = 0
white_knight = 0
black_knight = 0
white_pawn = 0
black_pawn = 0

#Validate tbe peice in board
for key, value in board.items():
#Define white pieces
    if value[0].lower() == 'w':
        white_pieces += 1
        if value[1].upper() == 'P':
            white_pawn += 1
        elif value[1].upper() == 'K':
            white_king += 1
        elif value[1].upper() == 'N':
            white_knight += 1
        elif value[1].upper() == 'R':
            white_rook += 1
        elif value[1].upper() == 'Q':
            white_queen += 1
            
#Define black pieces
    else:
        black_pieces += 1
        if value[1].upper() == 'P':
            black_pawn += 1
        elif value[1].upper() == 'K':
            black_king += 1
        elif value[1].upper() == 'N':
            black_knight += 1
        elif value[1].upper() == 'R':
            black_rook += 1
        elif value[1].upper() == 'Q':
            black_queen += 1
    total_pieces += 1
    
#Conditions to validates of pieces
if black_pieces <= 16:
    print('Pass: Number of black pieces - {} black pieces'.format(black_pieces))
else:
    print('Fail: Number of black pieces - {} black pieces'.format(black_pieces))

if white_pieces <= 16:
    print('Pass: Number of white piecess - {} white pieces'.format(white_pieces))
else:
    print('Fail: Number of white pieces - {} white pieces'.format(white_pieces))
if total_pieces <= 32:
    print('Pass: Number of all pieces - {} total pieces'.format(total_pieces))
else:
    print('Fail: Number of all pieces - {} total pieces'.format(total_pieces))
if white_king == 1 and black_king == 1:
    print('Pass: Kings - One of each color.')
else:
    print('Fail: Kings - One of each color.')
print()
