from imports import *

df['Date Published']=pd.to_datetime(df['Date Published'],errors='coerce')

grouped=df.groupby('General Address')['Article ID'].sum().reset_index()
grouped['Percentage']=100*grouped['Article ID']/grouped['Article ID'].sum()
grouped=grouped[['General Address','Percentage']].sort_values('Percentage',ascending=False)

top=grouped[grouped['Percentage']>=2]
top=pd.concat([top,
               pd.DataFrame({'General Address':'Less Than 2%','Percentage':100-top['Percentage'].sum()},index=[len(top)+1])]
)
bottom=grouped[grouped['Percentage']<2].sort_values('Percentage')

pull_list=[0]*len(top)
pull_list[-1]=0.2


fig = make_subplots(rows=1, cols=2, 
                    specs=[[{"type": "pie"}, {"type": "bar"}]],
                    subplot_titles=['Share Above 2%','Share Below 2%'],
                    )

trace_1=go.Pie(labels=top['General Address'],values=top['Percentage'],textinfo='label+percent',showlegend=False,pull=pull_list,hoverinfo='label')
trace_2=go.Bar(y=bottom['General Address'],x=bottom['Percentage'],showlegend=False,text=bottom['Percentage'].apply(lambda x:f'{x:.2f} %'),hoverinfo='text',orientation='h')

fig.add_trace(trace_1,col=1,row=1)
fig.add_trace(trace_2,col=2,row=1)

fig.update_traces(selector=dict(type='pie'), patch=dict(rotation=120))

fig.update_layout(height=700,template='plotly_dark')
fig.update_layout(title=dict(text='Share Of Apartments Avaialble For Sale By City Part',font_family='Arial Black',font_size=20,x=0.5,y=1))
fig.update_yaxes(tickformat=".%")
fig.update_xaxes(title_text='Percentage',col=2,row=1)
fig3=fig