from collections import defaultdict, deque

def print_game(index, marble_game):
    output = ""
    for count, value in enumerate(marble_game):
        if count != index:
            output += str(value)
            output += " "
        else:
            output += "("+str(value)+") "
    print(output)
    
def marbling_game(marbles, max_players, debug=False):
    score = defaultdict(int)

    playing = 0
    current_marble = 0
    marble_game = []

    for lowest_marble in range(marbles+1):
        if lowest_marble == 0:
            marble_game.append(lowest_marble)
            playing = playing%max_players + 1  
            current_marble=0
        else:
            if not lowest_marble%23 == 0:
                index = (current_marble + 1) % len(marble_game)
                lower = marble_game[0:index+1]
                lower.append(lowest_marble)
                current_marble = index+1
                lower.extend(marble_game[index+1:])
                marble_game = lower
                playing = playing%max_players + 1          
            else:
                score[playing] += lowest_marble
                index = (current_marble - 7 + len(marble_game)) % len(marble_game)
                lower = marble_game[0:index]
                score[playing] += marble_game[index]
                lower.extend(marble_game[index+1:])
                marble_game = lower
                playing = playing%max_players + 1  
                current_marble = index
        if debug:
            print_game(current_marble, marble_game)
    winner = sorted(score.items(), key=lambda s:s[1], reverse=True)[0]
    print(str(winner[0]) + " : " + str(winner[1]))

def marbling_game_rewrite(marbles, max_players):
    score = defaultdict(int)

    playing = 0
    marble_game = deque([0])

    for lowest_marble in range(1, marbles+1):
        if not lowest_marble%23 == 0:
            marble_game.rotate(-1)
            marble_game.append(lowest_marble)
            playing = playing%max_players + 1          
        else:
            score[playing] += lowest_marble
            marble_game.rotate(7)
            score[playing] += marble_game.pop()
            marble_game.rotate(-1)
            playing = playing%max_players + 1  
    winner = sorted(score.items(), key=lambda s:s[1], reverse=True)[0]
    print(str(winner[0]) + " : " + str(winner[1]))


marbling_game(72103, 459)
marbling_game_rewrite(72103, 459)
marbling_game_rewrite(7210300, 459)
            
