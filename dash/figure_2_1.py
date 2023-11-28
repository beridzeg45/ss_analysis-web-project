import sys
sys.path.append('')
from imports import *


coordinates_grouped=pd.read_csv('data/coordinates_grouped.csv')
coordinates_grouped['Date Published']=coordinates_grouped['Date Published'].astype(str)

fig=px.scatter_mapbox(coordinates_grouped,lat='Lat',lon='Lon',
                      zoom=10.5,
                      size='Size',color='Price Per SQMT',color_continuous_scale='Plotly3',
                      hover_name='Street',
                      #animation_frame='Date Published'
                      )


fig.update_traces(marker=dict(size=[i * 5 for i in coordinates_grouped['Size']]))
fig.update_layout(mapbox_style='open-street-map')
fig.update_layout(height=700,template='plotly_dark')
fig.update_layout(title=dict(text='Dispersion Of Apartments Available For Sale By Street',font_family='Arial Black',font_size=20))
fig_2_1=fig