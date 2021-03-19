# Bokeh test
# from sklearn.cluster import KMeans
# from sklearn.manifold import TSNE
# import matplotlib.pyplot as plt
# import matplotlib.patches as mpatches
# import pandas as pd
# import numpy as np
# import matplotlib.cm as cm
import pickle


colors = [(0.0, 0.0, 0.5, 1.0),
 (0.0, 0.503921568627451, 1.0, 1.0),
 (0.4901960784313725, 1.0, 0.4775458570524984, 1.0),
 (1.0, 0.5816993464052289, 0.0, 1.0),
 (0.5, 0.0, 0.0, 1.0)]

## Bokeh
from bokeh.plotting import figure, output_file, show
# from bokeh.io import curdoc
from bokeh.plotting import figure, curdoc
# from bokeh.io import output_notebook
# from bokeh.resources import INLINE, CDN
# output_notebook(INLINE)
from bokeh.models import ColumnDataSource, Label, LabelSet
from bokeh.colors import Color
from matplotlib.colors import to_hex

TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select"

source1_data = pickle.load(open('source1.pickle','rb'))
source1 = ColumnDataSource( source1_data )

p = figure(title = "Langs by set localization",
           tools=TOOLS, toolbar_location='below',
           plot_width=1500, plot_height=800,
           tooltips=[('lang', '@lang')] )
p.scatter(source=source1, x="x", y="y", color="colors", fill_alpha=0.7, size=5)
labels = LabelSet(x='x', y='y', text='lang', text_font_size='12px',
              x_offset=5, y_offset=5, source=source1, render_mode='canvas')
p.add_layout(labels)

curdoc().title = "Hello, world!"
curdoc().add_root(p)
# show(p)
