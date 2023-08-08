from enum import Enum

class Move(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

def move_from_letter(letter: str) -> Move:
    match letter:
        case 'A' | 'X':
            return Move.ROCK
        case 'B' | 'Y':
            return Move.PAPER
        case 'C' | 'Z':
            return Move.SCISSORS
        case _:
            raise ValueError(f'Invalid letter: {letter}')

class Result(Enum):
    WIN = 6
    DRAW = 3
    LOSE = 0
    
def result_from_letter(letter: str) -> Result:
    match letter:
        case 'X':
            return Result.LOSE
        case 'Y':
            return Result.DRAW
        case 'Z':
            return Result.WIN
        case _:
            raise ValueError(f'Invalid letter: {letter}')

def get_player_1_result(player_1_move: Move, player_2_move: Move) -> Result:
    if player_1_move == player_2_move:
        return Result.DRAW

    match player_1_move:
        case Move.ROCK:
            return Result.WIN if player_2_move == Move.SCISSORS else Result.LOSE
        case Move.PAPER:
            return Result.WIN if player_2_move == Move.ROCK else Result.LOSE
        case Move.SCISSORS:
            return Result.WIN if player_2_move == Move.PAPER else Result.LOSE

def move_from_result(result: Result, opponent_move: Move) -> Move:
    match result:
        case Result.DRAW:
            return opponent_move
        case Result.WIN:
            match opponent_move:
                case Move.ROCK:
                    return Move.PAPER
                case Move.PAPER:
                    return Move.SCISSORS
                case Move.SCISSORS:
                    return Move.ROCK
        case Result.LOSE:
            match opponent_move:
                case Move.ROCK:
                    return Move.SCISSORS
                case Move.PAPER:
                    return Move.ROCK
                case Move.SCISSORS:
                    return Move.PAPER

            

def part_1() -> int:
    with open('input.txt', 'r') as f:
        moves = [tuple(line.split()) for line in f.readlines()]

    opponent_moves = [move_from_letter(move[0]) for move in moves]
    my_moves = [move_from_letter(move[1]) for move in moves]

    score = 0
    for opponent_move, my_move in zip(opponent_moves, my_moves):
        score += get_player_1_result(my_move, opponent_move).value
        score += my_move.value

    return score

def part_2() -> int:
    with open('input.txt', 'r') as f:
        moves = [tuple(line.split()) for line in f.readlines()]
        
    opponent_moves = [move_from_letter(move[0]) for move in moves]
    results = [result_from_letter(move[1]) for move in moves]
    
    score = 0
    for opponent_move, results in zip(opponent_moves, results):
        my_move = move_from_result(results, opponent_move)
        score += my_move.value
        score += results.value
        
    return score
    
def main() -> None:
    print(f'Part one: {part_1()}')
    print(f'Part two: {part_2()}')


if __name__ == '__main__':
    main()