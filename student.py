import streamlit as st
import pandas as pd
import plotly.express as px
from st_aggrid import AgGrid

st.header('Students Performance Visualization')

df = pd.read_csv('Students_Performance_mv.csv')
df['total score'] = df['math score'] + df['reading score'] + df['writing score']
df['average score'] = round(df['total score'] / 3,2)
df1 = df.dropna()
st.write('Students Performance Dataset')
grid_table = AgGrid(df1)
st.dataframe(grid_table)

series = df1['race/ethnicity'].value_counts()
df_race = pd.DataFrame(series)
df_race = df_race.reset_index()  
df_race.columns = ['race/ethnicity', 'Total']

pie_chart = px.pie(df_race,
                   title = 'Total Students each group',
                   values = 'Total',
                   names = 'race/ethnicity')

st.plotly_chart(pie_chart)

dfavg = grid_table.groupby('race/ethnicity', as_index=False)['average score'].mean()
bar_chart = px.bar(dfavg, x="race/ethnicity", y="average score", title="Average Score each group")
st.plotly_chart(bar_chart)

dfavgmath = grid_table.groupby('race/ethnicity', as_index=False)['math score'].mean()
matbar_chart = px.bar(dfavgmath, x="race/ethnicity", y="math score", title="Average Math Score each group")
st.plotly_chart(matbar_chart)

dfavgreading = grid_table.groupby('race/ethnicity', as_index=False)['reading score'].mean()
readingbar_chart = px.bar(dfavgreading, x="race/ethnicity", y="reading score", title="Average Reading Score each group")
st.plotly_chart(readingbar_chart)

dfavgwriting = grid_table.groupby('race/ethnicity', as_index=False)['writing score'].mean()
writingbar_chart = px.bar(dfavgwriting, x="race/ethnicity", y="writing score", title="Average Writing Score each group")
st.plotly_chart(writingbar_chart)
