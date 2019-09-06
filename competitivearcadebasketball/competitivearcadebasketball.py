import sys

def competitivearcadebasketball(lines):
    info = lines[0].split(" ")
    num_players = int(info[0])
    win_score = int(info[1])

    scoreboard = {}
    for i in lines[1:num_players+1]:
        scoreboard[i] = 0

    lines = lines[num_players+1:]
    for score in lines:
        score_parts = score.split(" ")
        player = score_parts[0]
        points = int(score_parts[1])
        scoreboard[player] += points

    winners = []
    for player in scoreboard.keys():
        if scoreboard[player] >= win_score:
            winners.append(player)

    if len(winners) > 0:
        return " wins!\n".join(winners) + " wins!"
    
    return "No winner!"


def main():
    lines = [line.strip() for line in sys.stdin]
    print(competitivearcadebasketball(lines))
main()
