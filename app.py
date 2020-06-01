import constants

def clean_player(player):
    """
    Clean the data for a single player:
    1. Height: This should be saved as an integer
    2. Experience: This should be saved as a boolean value (True or False)
    :param player (dictionary, keys = name, guardians, height, experience):
    :return: cleaned_player (same format dict as player)
    """
    cleaned_player = {}
    cleaned_player['name'] = player['name']
    cleaned_player['guardians'] = player['guardians'].split(' and ')
    if player['experience'] == 'YES':
        cleaned_player['experience'] = True
    else:
        cleaned_player['experience'] = False
    cleaned_player['height'] = int(player['height'].replace(' inches', ''))
    return cleaned_player


def clean_data(players):
    """
    1) read the existing player data from the PLAYERS constants provided in constants.py
    2) clean the player data without changing the original data (see note below)
    3) save it to a new collection - build a new collection with what you have learned up to this point.

    Data to be cleaned:

    HINT: Think Lists with nested Dictionaries might be one way.

    NOTE: Ensure you **do not directly modify the data in PLAYERS or TEAMS constants.
    This data you should iterate and read from to build your own collection and would be
    ideal to clean the data as you loop over it building your new collection.
    """
    cleaned_players = [clean_player(player) for player in players]
    return cleaned_players


def assign_team_numbers(teamnames):
    """
    Copy team names into a list of tuples which contain team name plus allocation of a sequential number
    Used to populate menu options for user in the main_menu_selection function
    :param teamnames: (list of names of teams)
    :return: teams (list of tuples containing name of team plus allocated team number)
    """
    teams = []
    for index, team in enumerate(teamnames):
        teams.append((team, index))
    return teams

def balance_teams(players, teams):
    """
    balance the players across the three teams: Panthers, Bandits and Warriors.
    Make sure the teams have the same number of total players on them when your team balancing function has finished.
    HINT: To find out how many players should be on each team, divide the length of players
    by the number of teams. Ex: num_players_team = len(PLAYERS) / len(TEAMS)
    :param players:
    :param teams:
    :return:
    """
    experienced_players = [player for player in players if player['experience']]
    inexperienced_players = [player for player in players if not player['experience']]
    filled_teams = {}
    for index, team in enumerate(teams):
        filled_teams[team] = []
        for player in experienced_players[index::len(teams)]:
            filled_teams[team].append(player)
        for player in inexperienced_players[index::len(teams)]:
           filled_teams[team].append(player)
    return filled_teams

def main_menu_selection(teams):
    print("BASKETBALL TEAM STATS TOOL\n")
    print("---- MAIN MENU ----\n")
    print("Here are your choices:")
    for team in teams:
        print(f"{team[1]+1} - Display Team Stats - {team[0]}")
    choice = input("Any other key - Quit\n")
    try:
        return int(choice) - 1
    except (ValueError, KeyboardInterrupt):
        return -1


def print_team(teamname, filled_team):
    print(f"\nTeam {teamname} Stats:")
    print('-----------------------------')
    print(f'Total Players = {len(filled_team)}')
    experienced = len([player for player in filled_team if player['experience']])
    inexperienced = len([player for player in filled_team if not player['experience']])
    print(f'-- Experienced Players = {experienced}')
    print(f'-- Inexperienced Players = {inexperienced}')
    print('\nPlayers on Team:')
    print_string = ', '.join([player['name'] for player in filled_team])
    print(f'  {print_string}')
    print('\nGuardians:')
    guardians = []
    for player in filled_team:
        for guardian in player['guardians']:
            guardians.append(guardian)
    print_string = ', '.join(guardians)
    print(f"  {print_string}")
    print('\n\n')



if __name__ == "__main__":
    players = clean_data(constants.PLAYERS)
    teams = assign_team_numbers(constants.TEAMS)
    filled_teams = balance_teams(players, constants.TEAMS)
    choice = main_menu_selection(teams)
    while choice in range(len(teams)):
        print_team(teams[choice][0], filled_teams[teams[choice][0]])
        choice = main_menu_selection(teams)
    print("Program finished, thank you and have a nice day")
