import random

overs = 1 #overs left
balls = 6*overs #total balls left
lengaburu_players = ["Kirat Boli","NS Nodhi"]
enchai_players = ["DB Vellyers","H Mamla"]
score = (0,1,2,3,4,5,6,'out') #range of score each player can hit

#initialize a tuple for each player with his weighted probability of hitting a score
#Lengaburu team
kirat_prob = (5,10,25,10,25,1,14,10)
nodhi_prob = (5,15,15,10,20,1,19,15)
#Enchai team
vellyers_prob = (5,10,25,10,25,1,14,10)
mamla_prob = (10,15,15,10,20,1,19,10)

#for a list of player score probability
lengaburu_player_prob = [kirat_prob,nodhi_prob]
enchai_player_prob = [vellyers_prob,mamla_prob]
#initialize score of each player in dictionary
lengaburu_player_score = {"Kirat Boli":0, "NS Nodhi":0}
enchai_player_score = {"DB Vellyers":0, "H Mamla":0}
#initialize balls played for each player in dictionary
lengaburu_player_balls = {"Kirat Boli":0, "NS Nodhi":0}
enchai_player_balls = {"DB Vellyers":0, "H Mamla":0}

commentary = ""
match_result = ""
match_summary = ""


#function to swap position of players for strike in list and their hit probabilities on scoring (1,3,5)
def swap_players(player):
    newstrike = player[1]
    player[1] = player[0]
    player[0] = newstrike

#Function to simulate play innings of the game
def play(team,players,player_prob,player_balls,player_score,opponent_score):
    global commentary
    global match_result
    global match_summary

    commentary += '\n' + team + " innings\n"
    teamscore = 0

    ball = 0
    while (ball != balls and len(players) > 1):
        ball += 1
        #choose a random score for player at strike from his weighted probability list
        hit = random.choices(score,player_prob[0])[0]
        player_balls[players[0]] += 1 #maintain count of balls played by each player

        if hit == 'out':
            commentary += "0.%d %s gets out! \n" %(ball,players[0])
            #if player is out remove him from the list
            players.pop(0)
            player_prob.pop(0)
            break
        else:
            runs_string = "runs" if hit>1 else "run"
            exclaim = '!' if hit>3 else ''
            commentary += "0.%d %s scores %d %s%s\n" % (ball,players[0],hit,runs_string,exclaim)

        if hit > 0:
            teamscore += hit #add the score to total teamscore
            player_score[players[0]] += hit #add the score to player at strike

        if hit in (1,3,5):
            #swap position of player at strike if score is 1,3,5
            swap_players(players)
            swap_players(player_prob)

        #end game if Enchai scores more than lengaburu in 2nd innings
        if team == "Enchai" and teamscore>opponent_score:
            break

    #decide match result on completion of 2nd innings
    if team == "Enchai":
        balls_left = balls - ball
        balls_string = "balls" if balls_left > 1 else "ball"
        if teamscore > opponent_score:
            match_result = "Enchai won with %d %s remaining\n" %(balls_left,balls_string)
        elif teamscore == opponent_score:
            match_result = "It's a tie again!\n"
        else:
            runs_left = opponent_score - teamscore
            runs_string = "runs" if runs_left>1 else "run"
            match_result = "Enchai lost by %d %s\n" % (runs_left,runs_string)

    #populate match summary for each player
    match_summary += '\n'+team+'\n'
    for player,pscore in player_score.items():
        balls_played = player_balls[player]
        balls_string = "balls" if balls_played>1 else "ball"
        if player in players:
            match_summary += "%s - %d* (%d %s)\n" % (player,pscore,balls_played,balls_string)
        else:
            match_summary += "%s - %d (%d %s)\n" % (player,pscore,balls_played,balls_string)

    return teamscore


if __name__ == '__main__':
    #play 1st innings for lengaburu
    lengaburu_score = play("Lengaburu", lengaburu_players, lengaburu_player_prob, lengaburu_player_balls, lengaburu_player_score,
         0)
    #play 2nd innings for Enchai
    enchai_score = play("Enchai", enchai_players, enchai_player_prob, enchai_player_balls, enchai_player_score,
         lengaburu_score)
    #print match result and summary
    print(match_result,match_summary)
    # Print the match commentary ball by ball for both innings
    print('\nMatch Commentary:\n' + commentary)
