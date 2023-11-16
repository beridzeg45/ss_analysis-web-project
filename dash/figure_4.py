from imports import *

df['Date Published']=pd.to_datetime(df['Date Published'],errors='coerce')

fig = make_subplots(rows=1, cols=2, 
                    specs=[[{"type": "box"}, {"type": "box"}]],
                    subplot_titles=['By Status','By Condition'],
                    )

trace_1=go.Box(x=df['Status'],y=df['Price Per SQMT'],showlegend=False)
trace_2=go.Box(x=df['Condition'],y=df['Price Per SQMT'],showlegend=False)

fig.add_trace(trace_1,col=1,row=1)
fig.add_trace(trace_2,col=2,row=1)

fig.update_layout(height=600,template='plotly_dark')
fig.update_layout(title=dict(text='Frequency Distribution Of Price Per SQMT',font_family='Arial Black',font_size=20,x=0.5,y=1))
fig.update_yaxes(range=[0, 2500], row=1, col=1)
fig.update_yaxes(range=[0, 2500], row=1, col=2)
fig4=fig