# 
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd
import numpy as np
import matplotlib.cm as cm

P31_obj_data1 = pd.read_csv('bokeh-test-data.tsv', sep='\t', index_col=[0])
print("data shape (LANGS x sets): " + str(P31_obj_data1.shape))

# t-SNE
TSNE_PERPLEXITY = 30
TSNE_LR = 200
TSNE_N_ITER = 9000
data_tSNE = TSNE(n_components=2, #early_exaggeration=30, init='pca',
                 perplexity=TSNE_PERPLEXITY,  # default=30
                 learning_rate=TSNE_LR,  # default=200.0
                 n_iter=TSNE_N_ITER,  # default=1000
                 verbose=True).fit_transform(P31_obj_data1)
print('=> Done t-SNE')
# K-means
num_clusters = 5
clustering_model = KMeans(n_clusters=num_clusters)  #verbose=True)
clustering_model.fit(data_tSNE)  # t-SNE reduced data
cluster_assignment = clustering_model.labels_

unique = list(set(cluster_assignment))
colors = [plt.cm.jet(i/float(len(unique)-1)) for i in range(num_clusters)]


## Bokeh
from bokeh.plotting import figure, output_file, show
from bokeh.io import curdoc
# from bokeh.io import output_notebook
# from bokeh.resources import INLINE, CDN
# output_notebook(INLINE)
from bokeh.models import ColumnDataSource, Label, LabelSet
from bokeh.colors import Color
from matplotlib.colors import to_hex

TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select"

source1 = ColumnDataSource(dict(x=data_tSNE[:,0], y=data_tSNE[:,1], lang=P31_obj_data1.index.tolist(), colors=[to_hex(colors[c][:3]) for c in cluster_assignment]) )

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
