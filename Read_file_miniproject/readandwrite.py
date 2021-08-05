#!/usr/bin/env python3

import pandas as pd

# these following two lines are for writing to file
# use this when you are not rendering to a window
import matplotlib
matplotlib.use('Agg')

# create some graphs
import matplotlib.pyplot as plt

def main():
    categories = [{"name": "point", "short": "pts"},
                    {"name": "assist", "short": "ast"},
                    {"name": "rebound", "short": "reb"}]
    for caterogy in categories:
        getHighest(caterogy)
        plot(caterogy)
    

def getHighest(category):
    data_file= 'all_seasons.csv'

    dataframeobj = pd.read_csv(data_file, index_col=0)
    start_year=1996
    end_year=1997
    category_name = category.get("name")
    category_short = category.get("short")
    file_name = f"{category_name}.xlsx"
    writer = pd.ExcelWriter(file_name)
    for i in range(25):
        current_season=str(start_year)+"-"+str(end_year)[-2:]
        current_season_DF=dataframeobj[dataframeobj["season"] == current_season]
        
        highest = current_season_DF.sort_values([f"{category_short}"], ascending=False).head(1)
        #print(highest)
        highest.to_excel(writer, startrow=i*2, startcol=0, index=False)
        start_year += 1
        end_year += 1
    writer.save()
    combined_DF = pd.read_excel(file_name, index_col=0)
    combined_DF.drop(index="player_name",inplace=True)    
    combined_DF.to_excel(file_name)

def plot(category):
    category_name = category.get("name")
    category_short = category.get("short")
    file_name = f"{category_name}.xlsx"
    combined_DF = pd.read_excel(file_name, index_col=0)
    #create a stacked bar graph
    combined_DF[f"{category_short}"].plot(kind="barh")
    plt.savefig(f"/Users/yun/Documents/Projects/Python/mycode/Read_file_miniproject/{category_name}.png", bbox_inches='tight')    

if __name__ == "__main__":
    main()