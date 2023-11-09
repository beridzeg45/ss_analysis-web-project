import sys
main_path=r"C:\Users\berid\OneDrive\Documents\GitHub\ss_analysis-web-app_V2"
sys.path.append(main_path)
from imports import *
from groupby import all_time_grouped as df

#df=pd.read_csv('all_time_grouped.csv')
df['Date Published']=pd.to_datetime(df['Date Published'],errors='coerce')


periods={'By Day':'D','By Week':'W','By Month':'M'}

layout_section_1=html.Div([
    dcc.Dropdown(id='select-period_1',options=[{'label':period_name,'value':period_argument} for period_name,period_argument in periods.items()],value='D',placeholder='Choose Period'),
    dcc.Graph(id='figure-1')
])

@app.callback(
    Output('figure-1','figure'),
    [Input('select-period_1','value')]
)

def show_figure_1(selected_period):
    df['Date Published']=pd.to_datetime(df['Date Published'],errors='coerce')
    grouped=df.groupby(['Status',df['Date Published'].dt.to_period(f'{selected_period}')])['Price Per SQMT'].median().reset_index()
    grouped=grouped[grouped['Status'].isin(['ახალი აშენებული','მშენებარე','ძველი აშენებული'])]
    grouped['Date Published']=grouped['Date Published'].astype(str)
    
    fig=px.line(grouped,x='Date Published',y='Price Per SQMT',color='Status',markers=True,symbol='Status')
    fig.update_layout(height=600)
    fig.update_layout(title=dict(text='Change In Apartment Median Price Overtime By Construction Status',font_family='Arial Black',font_size=15))
    fig.update_xaxes(title_text='Time Period')
    fig.update_yaxes(title_text='Price Per SQMT')
    fig.update_traces(marker=dict(size=10))
    return fig

print('Finished Figure_1')