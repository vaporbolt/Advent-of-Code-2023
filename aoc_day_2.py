import sys
import functools

def main():
    input_file = sys.argv[1]
    input_text = open(input_file, "r").read()
    input_list = input_text.split("\n")
    possible_games = find_possible_games(input_list)
    answer = sum(possible_games)
    print(answer)



def find_possible_games(list):

    #list of IDs of the possible games
    possible_games = []
    for game in list:
        game_id = None
        # find digits 
        game_id_text = game.replace("Game ", "")
        id_digits = ""
        for char in game_id_text:
            if char.isdigit():
                id_digits += char
            else:
                break
        game_id = int(id_digits)
        game_text = game_id_text.replace(id_digits + ":", "")
        # gives us a list of each sub game
        sub_game_list = game_text.split(";")
        is_possible_game = True
        max_colors = {}
        max_colors["red"] = 0
        max_colors["green"] = 0
        max_colors["blue"] = 0
        for sub_game in sub_game_list:
           sub_picks = sub_game.split(",")
           for pick in sub_picks:
                # remove leading space from pick
                pick = pick[1:]
                count_digits = ""
                for char in pick:
                    if char.isdigit():
                        count_digits += char
                    else:
                        break  
                pick_count = int(count_digits)
                pick_color = pick.replace(count_digits + " ", "")
                if pick_count > max_colors[pick_color]:
                    max_colors[pick_color] = pick_count
        possible_games.append(max_colors["red"] * max_colors["blue"] * max_colors["green"])

        
          
    return possible_games       
main()
