import csv

def read_csv(file_name):
    with open(file_name, 'r') as file:
        csv_reader = csv.DictReader(file)
        data = []
        for row in csv_reader:
            data.append(row)
    return data

def get_wins(data: list[dict]): 

    # Put each row into a dict for its year

    teams = {row['hteam'] for row in data}
    years = {row['season'] for row in data}
    
    out_dict = {}
    for year in years:
        out_dict[year] = {}
        for team in teams:
            out_dict[year][team] = 0

    for row in data:
        if row['winner'] == '':
            continue
        # Find the location of the correct year and the winning team
        out_dict[row['season']][row['winner']] += 1
    
    return out_dict
        

data = read_csv('historical_games.csv')


winners = get_wins(data)
print(winners)