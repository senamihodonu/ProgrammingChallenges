import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
"""
Web scraping demostration using Pandas and ploting with seaborn
@snHD88
"""

MENU_PROMPT = """
Please choose one of these options:

1) display table
2) show points distribution
3) show goals distribution
4) best team
5) worst team
6) exit

Provide selection:
"""
url = 'https://www.premierleague.com/matchweek/6686/table'
try:
    df = pd.read_html(url, header=0)
    premier_league_table = df[1]
except:
    print(f"could not connect to the provided url: {url}")
    exit()

def menu():
    while(user_input:= input(MENU_PROMPT)) != "6":
        if user_input == "1":
            print(premier_league_table)
        
        elif user_input == '2':
            # # using seaborn
            # sns.barplot(x = 'Club',
            #             y = 'Pts',
            #             data = premier_league_table)
            # plt.xticks(rotation=90)
            # # using matplotlib
            premier_league_table.plot.bar(x='Club', y='Pts', rot=90)
            plt.show()

        elif user_input == '3':
             # # using seaborn
            # sns.barplot(x = 'Club',
            #             y = 'GD',
            #             data = premier_league_table)
            # plt.xticks(rotation=90)
            # # using matplotlib
            premier_league_table.plot.bar(x='Club', y='GD', rot=90)
            plt.show()

        elif user_input == '4':
            max_points_value = premier_league_table['Pts'].max()
            max_points = premier_league_table.loc[premier_league_table['Pts'] == max_points_value]
            max_gd_value = max_points['GD'].max()
            max_gd = max_points.loc[max_points['GD'] == max_gd_value]
            print(f"The best team from the 2021/2022 season was {max_gd['Club'].max()} finishing with {max_points_value} points and {max_gd_value} goal difference")

        elif user_input == '5':
            min_points_value = premier_league_table['Pts'].min()
            min_points = premier_league_table.loc[premier_league_table['Pts'] == min_points_value]
            min_gd_value = min_points['GD'].min()
            min_gd = min_points.loc[min_points['GD'] == min_gd_value]
            print(f"The worst team from the 2021/2022 season was {min_gd['Club'].min()} finishing with {min_points_value} points and {min_gd_value} goal difference")
        
        else:
            print(f"{user_input} is not a valid selection")

menu()



