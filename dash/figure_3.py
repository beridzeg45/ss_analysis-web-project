from imports import *

df['Date Published']=pd.to_datetime(df['Date Published'],errors='coerce')

grouped=df.groupby('General Address')['Article ID'].sum().reset_index()
grouped['Percentage']=100*grouped['Article ID']/grouped['Article ID'].sum()
grouped=grouped[['General Address','Percentage']].sort_values('Percentage',ascending=False)

top=grouped[grouped['Percentage']>=2]
top.iloc[-1]={'General Address':'Less Than 2%','Percentage':100-top['Percentage'].sum()}
bottom=grouped[grouped['Percentage']<2]


fig = make_subplots(rows=1, cols=2, 
                    specs=[[{"type": "pie"}, {"type": "bar"}]],
                    subplot_titles=['Share Above 2%','Share Below 2%'],
                    )

trace_1=go.Pie(labels=top['General Address'],values=top['Percentage'],textinfo='label+percent',showlegend=False)
trace_2=go.Bar(x=bottom['General Address'],y=bottom['Percentage'],showlegend=False)

fig.add_trace(trace_1,col=1,row=1)
fig.add_trace(trace_2,col=2,row=1)


fig.update_layout(height=600,template='plotly_dark')
fig.update_layout(title=dict(text='Share Of Apartments Avaialble For Sale By City Part',font_family='Arial Black',font_size=20,x=0.5,y=1))
fig.update_yaxes(tickformat=".%")
fig3=fig