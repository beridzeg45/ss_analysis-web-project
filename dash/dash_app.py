from imports import *
from figure_1 import layout_section_1
from figure_2 import fig2
from figure_3 import fig3
from figure_4 import fig4

df['Date Published']=pd.to_datetime(df['Date Published'],errors='coerce')


df['Date Published']=pd.to_datetime(df['Date Published'],errors='coerce').dt.date
min_date=df['Date Published'].min().strftime('%B %d, %Y')
max_date=df['Date Published'].max().strftime('%B %d, %Y')


app.layout = html.Div([
        html.P([
        html.Span('ss.ge - Tbilisi Apartment Prices Analysis ', style={'color': 'red', 'font-size': '25px', 'font-family': 'Arial'}),
        html.Span(f'({min_date} - {max_date})', style={'color': 'white', 'font-size': '15px', 'font-family': 'Arial Black'})
]),
    html.Div('Created By Giorgi Beridze',style={'color':'white','margin-bottom': '50px','font-size':'15px','font-family':'Arial Black'}),
    html.Div([html.Div(html.Div(intro_text, style={'color':'white','margin-bottom': '50px', 'font-size': '15px', 'font-family': 'Arial'}))],style={'white-space': 'pre-line'}),   

    html.Div(style={'margin-top': '100px'}),
    layout_section_1,
    html.Div(style={'margin-top': '100px'}),
    dcc.Graph(figure=fig2),
    html.Div(style={'margin-top': '100px'}),
    dcc.Graph(figure=fig3),
    html.Div(style={'margin-top': '100px'}),
    dcc.Graph(figure=fig4),
],
style={"background-color": "#000000"}
)

if __name__ == '__main__':
    app.run_server()