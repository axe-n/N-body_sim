import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import pandas as pd
from IPython.display import HTML
import random
from pathlib import Path as p

directory = '/gpfs-home/sip14/software/N-body-master/outputs2/autput/test1/s2'

files= p(directory).glob('*',)

#df1 = pd.DataFrame(np.random.random_integers(3,13 + 1, size=len(df.index)), columns=list('i'))
# df1.to_csv(r"/content/size.csv",index=False)

colors = ['#66560c','#612008','#a88f00'] 

for file in files:
 df =pd.read_csv(file)
# df.to_csv(r"/content/110.000.csv",index=False)

 s=(len(df.index))
 print(s)
 print(type(df),"\n")

 x=df['x'].values
 y=df['y'].values
 z=df['z'].values
# sizes=df1['i'].values

 fig=plt.figure()
 ax=fig.add_subplot(projection='3d')

 part_colors= [colors[i % len(colors)] for i in range(s)]

 ax.scatter(x,y,z,marker='.', c= part_colors)#, s= sizes)


# fig.set_size_inches(15,15)
 ax.set_facecolor('black')
 fig.set_facecolor('black')
 ax.grid(False)
 ax.axis('off')
 ax.xaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
 ax.yaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
 ax.zaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))

# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')

 plt.title("N-Body Simulation", loc='left', fontdict={'color': 'grey'})

# ax.set_xlim([300,500])
# ax.set_ylim([300,500])
# ax.set_zlim([300,500])

 def animate1(i):
  ax.view_init(20,50+i/15,20)
  plt.pause(0.001)
  return fig
 def animate2(i):
  x_lim = ax.set_xlim([1800,i*5])
  y_lim = ax.set_ylim([1800,i*5])
  z_lim = ax.set_zlim([1800,i*5])
  plt.pause(0.001)
  return fig


 def animate(i):
  animate1(i)
  animate2(i)
  plt.pause(0.001)
  return fig

 anim = animation.FuncAnimation(fig, animate, frames=150, interval=50)
 HTML(anim.to_html5_video())
 anim.save(f'{file}.mp4', fps=30, dpi=300, extra_args=['-vcodec', 'libx264'])
