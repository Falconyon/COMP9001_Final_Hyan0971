import sys
import random
from maps import LEVEL1_MAPS, LEVEL2_MAPS, select_map
from question import QUESTION_1, QUESTION_2, QUESTION_3


def find_player(game_map):
    r = 0
    while r < len(game_map):
        c = 0
        while c < len(game_map[r]):
            if game_map[r][c] == 'P':
                return r, c
            c += 1
        r += 1
    return None, None


def render(game_map):
    r = 0
    while r < len(game_map):
        line = ''
        c = 0
        while c < len(game_map[r]):
            line = line + game_map[r][c]
            c += 1
        print(line)
        r += 1


def find_exit(game_map):
    r = 0
    while r < len(game_map):
        c = 0
        while c < len(game_map[r]):
            if game_map[r][c] == 'E':
                return (r, c)
            c += 1
        r += 1


def move_player(game_map, dx, dy, level, state, questions_pool=None, question_positions=None):
    x, y = find_player(game_map)
    nx, ny = x + dx, y + dy
    if not (0 <= nx < len(game_map) and 0 <= ny < len(game_map[0])):
        return
    if game_map[nx][ny] == '#':
        return

    # Level 1: push box 
    if level == 1 and game_map[nx][ny] == 'o':
        bx, by = nx + dx, ny + dy
        if game_map[bx][by] in (' ', 'E'):
            game_map[bx][by] = 'o'
            game_map[nx][ny] = ' '
        else:
            return

    # Level 2: trigger full question set on first '?' touch
    if level == 2 and game_map[nx][ny] == '?':
        state['answers'] = []
        state['correct_bits'] = []
        i = 0
        while i < len(questions_pool):
            prompt = questions_pool[i][0]
            standard = questions_pool[i][1]
            while True:

                ans = input(prompt).strip().upper()
                if ans in ('T', 'F'):
                    break
                print('Please input T or F')
            if ans == 'T':
                state['answers'].append('1')
            else:
                state['answers'].append('0')
            
            if standard.upper() == 'T':
                std_bit = '1'
            else:
                std_bit = '0'
            state['correct_bits'].append(std_bit)
            i += 1
        return
       
 

    if question_positions and (x, y) in question_positions:
        game_map[x][y] = '?'
    else:
        game_map[x][y] = ' '
    game_map[nx][ny] = 'P'


def level1():
    while True:
        print("\nLevel 1: Push the box to the exit")
        game_map = select_map(LEVEL1_MAPS)
        exit_pos = find_exit(game_map)
        while True:
            render(game_map)
            cmd = input("Move P by input single (W/A/S/D), 'R' to restart, or Q to quit: ").strip().upper()
            if cmd == 'Q':
                sys.exit()
            if cmd == 'R':
                print("Restarting Level 1...\n")
                break  

            if cmd == 'W':
                dx = -1
            elif cmd == 'S':
                dx = 1
            else:
                dx = 0
            if cmd == 'A':
                dy = -1
            elif cmd == 'D':
                dy = 1
            else:
                dy = 0

            px = find_player(game_map)[0]
            py = find_player(game_map)[1]


            if (px + dx, py + dy) == exit_pos and game_map[exit_pos[0]][exit_pos[1]] != 'o':
                print("The exit is too high — you need a box to reach it.")
                continue

            move_player(game_map, dx, dy, 1, {})

            ex = exit_pos[0]
            ey = exit_pos[1]

            if game_map[ex][ey] == 'o':
                print("You pushed the box into the exit! Level 1 cleared.\n")
                return level2()


def level2():
    while True:
        print("\nLevel 2: Binary Password Lock")
        game_map = select_map(LEVEL2_MAPS)
        questions_pool = random.choice([QUESTION_1, QUESTION_2, QUESTION_3])
        state = {'answers': []}
        question_positions = {
            (r, c)
            for r in range(len(game_map))
            for c in range(len(game_map[0]))
            if game_map[r][c] == '?'
        }
        exit_pos = find_exit(game_map)
        while True:
            render(game_map)
            cmd = input("Move P by input single (W/A/S/D), 'R' to restart, or Q to quit: ").strip().upper()
         
            if cmd == 'Q':
                sys.exit()
            if cmd == 'R':
                print("Restarting Level 2...\n")
                break

            if cmd == 'W':
                dx = -1
            elif cmd == 'S':
                dx = 1
            else:
                dx = 0
            if cmd == 'A':
                dy = -1
            elif cmd == 'D':
                dy = 1
            else:
                dy = 0
            px = find_player(game_map)[0]
            py = find_player(game_map)[1]   
            if (px + dx, py + dy) == exit_pos:
                if not state.get('correct_bits'):
                    print("You haven't answered any questions yet, find the hint '?' first!")
                    continue
                code = ''
                i = 0
                while i < len(state['correct_bits']):
                    code = code + state['correct_bits'][i]
                    i += 1
                attempt = input("T = 1, F = 0. Enter the bit-string you just collected (e.g. 010 ): ").strip()
                if attempt == code:
                    print("Password correct! Level 2 cleared. You win!\n")
                    return
                else:
                    print()
                    print("Password incorrect.\n")
                    continue

            move_player(game_map, dx, dy, 2, state, questions_pool, question_positions)



def main():
    level1()


if __name__ == '__main__':
    main()

