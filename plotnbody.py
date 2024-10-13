import pandas as pd  # (version 1.0.0)
import plotly.express as px  # (version 4.7.0)
import plotly.io as pio
import numpy as np
import plotly.graph_objects as go

# Use for animation rotation at the end
x_eye = -1.25
y_eye = 2
z_eye = 0.5

df =pd.read_csv('/gpfs-home/sip14/software/N-body-master/output.nbody_122.500')
df.to_csv(r"/gpfs-home/sip14/software/N-body-master/csv1/122.500.csv",index=False)

df['resized_pop'] = df['vx'] / 100000000000000

fig = px.scatter_3d(
    data_frame=df,
    x=df['x'].values,
    y=df['y'].values,
    z=df['z'].values,
    size='resized_pop',
    size_max=10,
    opacity=0.3,
    template='plotly_dark',         # 'ggplot2', 'seaborn', 'simple_white', 'plotly',
                                # 'plotly_white', 'plotly_dark', 'presentation',
                                # 'xgridoff', 'ygridoff', 'gridon', 'none'
    title='N-body simulaiton',
    )

fig.update_layout(scene_camera_eye=dict(x=x_eye, y=y_eye, z=z_eye),
                  updatemenus=[dict(type='buttons',
                                    showactive=False,
                                    y=1,
                                    x=0.8,
                                    xanchor='left',
                                    yanchor='bottom',
                                    pad=dict(t=45, r=10),
                                    buttons=[dict(label='Play',
                                                  method='animate',
                                                  args=[None, dict(frame=dict(duration=30, redraw=True),
                                                                   transition=dict(duration=0),
                                                                   fromcurrent=True,
                                                                   mode='immediate'
                                                                   )]
                                                  )
                                             ]
                                    )
                               ]
                  )

#
def rotate_z(x, y, z, theta):
    w = x + 1j * y
    return np.real(np.exp(1j * theta) * w), np.imag(np.exp(1j * theta) * w), z


frames = []

for t in np.arange(0, 6.26, 0.1):
    xe, ye, ze = rotate_z(x_eye, y_eye, z_eye, -t)
    frames.append(go.Frame(layout=dict(scene_camera_eye=dict(x=xe, y=ye, z=ze))))
fig.frames = frames


fig.write_html("124.500.html")
fig.write_image"124.500.png")
pio.show(fig)