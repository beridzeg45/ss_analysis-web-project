from imports import *

geo_df=pd.read_csv('dash/../data/coordinates_df.csv')
geo_df['Date Published']=pd.to_datetime(geo_df['Date Published'],errors='coerce')
geo_df['Size']=geo_df.index

g=geo_df.groupby([geo_df['Date Published'].dt.to_period('W'),'Lat','Lon','Street']).agg({'Size':'count','Price Per SQMT':'median'}).reset_index()
g['Date Published']=g['Date Published'].astype(str)

fig=px.scatter_mapbox(g,lat='Lat',lon='Lon',
                      zoom=10.5,
                      size='Size',color='Price Per SQMT',color_continuous_scale='Plotly3',
                      hover_name='Street',
                      #animation_frame='Date Published'
                      )


fig.update_traces(marker=dict(size=[i * 5 for i in g['Size']]))
fig.update_layout(mapbox_style='open-street-map')
fig.update_layout(height=700,template='plotly_dark')
fig.update_layout(title=dict(text='Dispersion Of Apartments Available For Sale By Street',font_family='Arial Black',font_size=20))
fig_2_1=fig