# Bokeh test
import pickle
from bokeh.plotting import figure, output_file, show, curdoc
from bokeh.models import ColumnDataSource, Label, LabelSet, Dropdown

TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select"

def handler(event):
    print('source1 data: ' + event.item)
        
    source1_data = pickle.load(open(event.item,'rb'))
    source1 = ColumnDataSource( source1_data )

    p.scatter(source=source1, x="x", y="y", color="colors", fill_alpha=0.7, size=5)

    labels = LabelSet(x='x', y='y', text='lang', text_font_size='12px',
          x_offset=5, y_offset=5, source=source1, render_mode='canvas')
    p.add_layout(labels)

    if event.item == 'b':
        print('...')


p = figure(title = "Clusters of language locales by P31_obj_set localization frequency",
           background_fill_color='lightgrey',
           tools=TOOLS, toolbar_location='below',
           aspect_ratio=2,
           # plot_width=1500, plot_height=800,
           sizing_mode='stretch_both',
           tooltips=[('lang', '@lang')] )

menu_items = ['source1-tsnePerp5-LRate100-Iters5000-AvgSilhouette0.52310336.pickle',
 'source1-tsnePerp5-LRate100-Iters7000-AvgSilhouette0.52552533.pickle',
 'source1-tsnePerp5-LRate100-Iters10000-AvgSilhouette0.46690762.pickle',
 'source1-tsnePerp5-LRate200-Iters5000-AvgSilhouette0.5385952.pickle',
 'source1-tsnePerp5-LRate200-Iters7000-AvgSilhouette0.5313827.pickle',
 'source1-tsnePerp5-LRate200-Iters10000-AvgSilhouette0.48490345.pickle',
 'source1-tsnePerp10-LRate100-Iters5000-AvgSilhouette0.60337734.pickle',
 'source1-tsnePerp10-LRate100-Iters7000-AvgSilhouette0.6300929.pickle',
 'source1-tsnePerp10-LRate100-Iters10000-AvgSilhouette0.6096842.pickle',
 'source1-tsnePerp10-LRate200-Iters5000-AvgSilhouette0.6392452.pickle',
 'source1-tsnePerp10-LRate200-Iters7000-AvgSilhouette0.6297343.pickle',
 'source1-tsnePerp10-LRate200-Iters10000-AvgSilhouette0.65313894.pickle',
 'source1-tsnePerp20-LRate100-Iters5000-AvgSilhouette0.6989243.pickle',
 'source1-tsnePerp20-LRate100-Iters7000-AvgSilhouette0.68160737.pickle',
 'source1-tsnePerp20-LRate100-Iters10000-AvgSilhouette0.7143117.pickle',
 'source1-tsnePerp20-LRate200-Iters5000-AvgSilhouette0.72331315.pickle',
 'source1-tsnePerp20-LRate200-Iters7000-AvgSilhouette0.7051578.pickle',
 'source1-tsnePerp20-LRate200-Iters10000-AvgSilhouette0.7044447.pickle',
 'source1-tsnePerp30-LRate100-Iters5000-AvgSilhouette0.73119795.pickle',
 'source1-tsnePerp30-LRate100-Iters7000-AvgSilhouette0.7394427.pickle',
 'source1-tsnePerp30-LRate100-Iters10000-AvgSilhouette0.73571587.pickle',
 'source1-tsnePerp30-LRate200-Iters5000-AvgSilhouette0.7336306.pickle',
 None,
 'source1-tsnePerp30-LRate200-Iters7000-AvgSilhouette0.75937724.pickle',
 None,
 'source1-tsnePerp30-LRate200-Iters10000-AvgSilhouette0.747867.pickle',
 'source1-tsnePerp40-LRate100-Iters5000-AvgSilhouette0.64692277.pickle',
 'source1-tsnePerp40-LRate100-Iters7000-AvgSilhouette0.65720874.pickle',
 'source1-tsnePerp40-LRate100-Iters10000-AvgSilhouette0.65109044.pickle',
 'source1-tsnePerp40-LRate200-Iters5000-AvgSilhouette0.6542307.pickle',
 'source1-tsnePerp40-LRate200-Iters7000-AvgSilhouette0.65836734.pickle',
 'source1-tsnePerp40-LRate200-Iters10000-AvgSilhouette0.6608401.pickle']

d = Dropdown(label='Load dataset', menu=menu_items) #, menu=['Test 1', None, '...', None])


# source1_data = pickle.load(open('source1.pickle','rb'))
# source1 = ColumnDataSource( source1_data )

# p.scatter(source=source1, x="x", y="y", color="colors", fill_alpha=0.7, size=5)

# labels = LabelSet(x='x', y='y', text='lang', text_font_size='12px',
#       x_offset=5, y_offset=5, source=source1, render_mode='canvas')
# p.add_layout(labels)

d.on_click(handler)

curdoc().title = "Bokeh Application"
curdoc().add_root(p)
curdoc().add_root(d)
