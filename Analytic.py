import pandas as pd
from pip.commands import completion

def loadPlayByPlayDataframe():
    '''
    
    '''
    
    df = pd.read_csv("./Data/reg_pbp_2009.csv")
    relevant_df = df[['posteam', 'play_type', 'pass_location', 'pass_length', 'air_yards', 'yards_after_catch', 'yards_gained']]
    return relevant_df

def completionPercentage(values):
    completions = len(values[values > 0].index)
    completion_percentage = completions/len(values.index)
    return completion_percentage


def aggregatePassBins(df):
    '''
    Takes the specified period of pass data, generates bins and creates performance aggregates
    for each
    
    First the data is binned by QB, then filtered by pass attempts
    
    Six basic bins are right, left, center by short (<=10 air yards) and long (> air yards)
    
    Three aggregate stats are completion percentage (completion/attempts), air yards, YAC yards, aggregate yards
    
    air yards per play, YAC yards per play,
    aggregate yards per play (air + YAC),  
    
    '''
    bins = df.groupby(['pass_location', 'pass_length'])
    binned_completion_per = bins['yards_gained'].apply(completionPercentage)
    
    completed_passes = df[df['yards_gained'] > 0] 
    bins = completed_passes.groupby(['pass_location', 'pass_length'])
    binned_YAC = bins['yards_after_catch'].sum()
    print(binned_YAC)
    
    

def main():
    print()
    df = loadPlayByPlayDataframe()
    baltimore_offensive_dataframe = df[df['posteam'] == 'BAL']
    print(len(baltimore_offensive_dataframe.index))
    baltimore_pass_dataframe = baltimore_offensive_dataframe[baltimore_offensive_dataframe['play_type'] == 'pass']
    print(len(baltimore_pass_dataframe.index))
    
    aggregatePassBins(baltimore_pass_dataframe)

if __name__ == "__main__":
    main()