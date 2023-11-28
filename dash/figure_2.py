import sys
sys.path.append('')
from imports import *

df=pd.read_csv('dash/../data/all_time_grouped.csv')
df['Date Published']=pd.to_datetime(df['Date Published'],errors='coerce')


grouped=df.groupby([df['Date Published'].dt.to_period('M'),'General Address','Status'])['Price Per SQMT'].median().reset_index()\
    .sort_values(['Date Published','Price Per SQMT'],ascending=[True,False])
grouped['Date Published']=grouped['Date Published'].astype(str)


fig=px.bar(grouped,x='General Address',y='Price Per SQMT',
           color='Status',barmode='group',
           animation_frame='Date Published',
           text=grouped['Price Per SQMT'].round().astype(int).astype(str)+' $',
)
fig.update_layout(height=600,template='plotly_dark')
fig.update_layout(title=dict(text='Median Apartment Prices Per SQMT By Month And City Part',font_family='Arial Black',font_size=15))
fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 1500
fig['layout']['updatemenus'][0]['pad']=dict(r= 10, t= 150)
fig['layout']['sliders'][0]['pad']=dict(r= 10, t= 150,)
fig2=fig

print('Finished Figure_2')
