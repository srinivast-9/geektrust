import random

runs_required = 40 #required to win
overs = 4 #overs left
balls = 6*overs #total balls left
players = ["Kirat Boli","NS Nodhi","R Rumrah","Shashi Henra"]
score = (0,1,2,3,4,5,6,'out') #range of score each player can hit

#initialize a tuple for each player with his weighted probability of hitting a score
kirat_prob = (5,30,25,10,15,1,9,5)
nodhi_prob = (10,40,20,5,10,1,4,10)
rumrah_prob = (20,30,15,5,5,1,4,20)
henra_prob = (30,25,5,0,5,1,4,30)

#form a list of player score probability
player_prob = [kirat_prob,nodhi_prob,rumrah_prob,henra_prob]
#initialize score of each player in dictionary
player_score = {"Kirat Boli":0, "NS Nodhi":0, "R Rumrah":0, "Shashi Henra":0}
#initialize balls played for each player in dictionary
player_balls = {"Kirat Boli":0, "NS Nodhi":0, "R Rumrah":0, "Shashi Henra":0}

#function to swap position of players for strike in list and their hit probabilities
#on over change or scoring (1,3,5) or getting out
def swap_players(player):
    newstrike = player[1]
    player[1] = player[0]
    player[0] = newstrike

#main function to begin the game
def play():
    teamscore = 0
    ball = 0
    over = 0
    ballinover = 0
    commentary = "%d overs left. %d runs to win\n" % (overs - over, runs_required - teamscore)
    while (ball != balls and teamscore < 40 and len(players) > 1):
        ball += 1
        ballinover += 1
        #choose a random score for player at strike from his weighted probability list
        hit = random.choices(score,player_prob[0])[0]
        player_balls[players[0]] += 1 #maintain count of balls played by each player

        isout = False
        if hit == 'out':
            isout = True
            commentary += "%d.%d %s is out\n" %(over,ballinover,players[0])
            #if player is out remove him from the list
            players.pop(0)
            player_prob.pop(0)
            hit = 0
            if not len(players) > 1:
                #if no players left for play then end the game
                break
        else:
            runs_string = "runs" if hit>1 else "run"
            commentary += "%d.%d %s scores %d %s\n" % (over,ballinover,players[0],hit,runs_string)

        if hit > 0:
            teamscore += hit #add the score to total teamscore
            player_score[players[0]] += hit #add the score to player at strike

        #if it's end of a over
        if ball % 6 == 0:
            over += 1
            ballinover = 0
            if teamscore<runs_required:
                overs_left = overs - over
                overs_string = "overs" if overs_left>1 else "over"
                runs_left = runs_required - teamscore
                runs_string = "runs" if runs_left>1 else "run"
                commentary += "\n%d %s left. %d %s to win\n" % (overs_left,overs_string,runs_left,runs_string)
            if not isout and hit not in (1,3,5):
                #swap position of player at strike if score is not 1,3,5 and none of players is out
                swap_players(players)
                swap_players(player_prob)
        else: #if it's mid of a over
            if hit in (1,3,5) or isout:
                #swap position of player at strike if score is 1,3,5 or if a player is out
                swap_players(players)
                swap_players(player_prob)

    #Announce the match result
    if teamscore>=runs_required:
        players_left = len(players)
        balls_left = balls - ball
        wickets_string = "wickets" if players_left>1 else "wicket"
        balls_string = "balls" if balls_left>1 else "ball"
        print("Lengaburu won by %d %s and %d %s remaining\n" % (len(players),wickets_string,balls_left,balls_string))
    elif teamscore==runs_required-1:
        printf("It's a tie!!\n")
    else:
        runs_left = runs_required - teamscore
        runs_string = "runs" if runs_left>1 else "run"
        print("Lengaburu lost by %d %s\n" % (runs_left,runs_string))

    #Announce the score of each player
    for player,pscore in player_score.items():
        balls_played = player_balls[player]
        balls_string = "balls" if balls_played>1 else "ball"
        if player in players:
            print("%s - %d* (%d %s)" % (player,pscore,balls_played,balls_string))
        else:
            print("%s - %d (%d %s)" % (player,pscore,balls_played,balls_string))

    #Print the match commentary ball by ball
    print('\n\nMatch Commentary:\n'+commentary)


if __name__ == '__main__':
    play()
