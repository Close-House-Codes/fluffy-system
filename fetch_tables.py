import pandas as pd

for period in range(1,5):
    dfs = []
    for i in range (50):
        file_path = 'html/quarter-{}/{}'.format(period, i)
        df = pd.read_html(file_path)
        dfs.append(df[2])
    
    combined = pd.concat(dfs)
    combined.to_csv('csv/quarter-{}/combined.csv'.format(period), index=False)
    