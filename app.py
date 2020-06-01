import constants

def clean_player(player):
    """
    Clean the data for a single player:
    1. Name: as is
    2. Guardians: Modify to a list of strings, remove 'and' between names
    3. Height: Convert to integer
    4. Experience: boolean value (True or False)
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
    Iterate over player data calling clean_player function for each to clean data
    """
    cleaned_players = [clean_player(player) for player in players]
    return cleaned_players


def balance_teams(players, teams):
    """
    balance the players across the three teams: Panthers, Bandits and Warriors.
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
    """
    Display program menu and get input from user
    """
    print("BASKETBALL TEAM STATS TOOL\n")
    print("---- MAIN MENU ----\n")
    print("Here are your choices:")
    print("\n  Display Team Stats:")
    for team in teams:
        print(f"    Enter {teams.index(team) + 1} for {team}")
    print("\n  Any other key - Quit")
    choice = input("Enter an option > ")
    try:
        return int(choice) - 1
    except ValueError:
        return -1


def print_team(teamname, filled_team):
    """
    Print stats for one team to console
    """
    print(f"\nTeam {teamname} Stats:")
    print('-----------------------------')
    print(f'Total Players = {len(filled_team)}')
    experienced = len([player for player in filled_team if player['experience']])
    inexperienced = len([player for player in filled_team if not player['experience']])
    print(f'Total Experienced: {experienced}')
    print(f'Total Inexperienced: {inexperienced}')
    height = sum([(player['height']) for player in filled_team]) / len(filled_team)
    print(f'Average height: {height:.1f} inches')
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
    input("Press ENTER to continue")
    print('\n')


if __name__ == "__main__":
    players = clean_data(constants.PLAYERS)
#    teams = assign_team_numbers(constants.TEAMS)
    filled_teams = balance_teams(players, constants.TEAMS)
    choice = main_menu_selection(constants.TEAMS)
    while choice in range(len(constants.TEAMS)):
        print_team(constants.TEAMS[choice], filled_teams[constants.TEAMS[choice]])
        choice = main_menu_selection(constants.TEAMS)
    print("Program finished, thank you and have a nice day")
