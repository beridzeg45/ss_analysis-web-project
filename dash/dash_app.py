from imports import *
from figure_1 import layout_section_1
from figure_2 import fig2
from figure_3 import fig3
from figure_4 import fig4
from figure_2_1 import fig_2_1



df['Date Published']=pd.to_datetime(df['Date Published'],errors='coerce').dt.date
min_date=df['Date Published'].min().strftime('%B %d, %Y')
max_date=df['Date Published'].max().strftime('%B %d, %Y')


image_sources = ['https://thumbs.dreamstime.com/b/winter-tbilisi-8588952.jpg',
                'https://cdn2.wanderlust.co.uk/media/1033/w26n5h.jpg?anchor=center&mode=crop&width=1200&height=0&rnd=132143224270000000',
                 'https://thumbs.dreamstime.com/b/evening-view-tbilisi-colorful-sunset-georgia-summer-city-cityscape-photograph-visible-holy-trinity-cathedral-72801385.jpg',
                 'https://wander-lush.org/wp-content/uploads/2021/09/Emily-Lush-autumn-in-Tbilisi-river-bridge-hero.jpg'
                 ]

app.layout = html.Div([
    html.P([html.Span('ss.ge - Tbilisi Apartment Prices Analysis ', style={'color': 'red', 'font-size': '25px', 'font-family': 'Arial'}),
            html.Span(f'({min_date} - {max_date})', style={'color': 'white', 'font-size': '15px', 'font-family': 'Arial Black'})]),

    html.Div('Created By Giorgi Beridze', style={'color': 'white', 'margin-bottom': '50px', 'font-size': '15px', 'font-family': 'Arial Black'}),

    html.Div([html.Div(html.Div(intro_text, style={'color': 'white', 'margin-bottom': '50px', 'font-size': '15px', 'font-family': 'Arial', 'font-style': 'italic'}))], style={'white-space': 'pre-line', 'text-align': 'center'}),
    
    html.Div([html.Img(src=image_source,style={'width': '20%', 'height': 'auto', 'display': 'block', 'margin': 'auto'}) for image_source in image_sources],style={'display': 'flex'}),

    html.Div(style={'margin-top': '100px'}),
    layout_section_1,
    html.Div(style={'margin-top': '100px'}),
    dcc.Graph(figure=fig2),
    html.Div(style={'margin-top': '100px'}),
    dcc.Graph(figure=fig_2_1),
    html.Div(style={'margin-top': '100px'}),
    dcc.Graph(figure=fig3),
    html.Div(style={'margin-top': '100px'}),
    dcc.Graph(figure=fig4),
    ],
    
style={"background-color": "#000000"})

if __name__ == '__main__':
    app.run_server()