# Bokeh test
import pickle
from bokeh.plotting import figure, output_file, show, curdoc
from bokeh.models import ColumnDataSource, Label, LabelSet, Dropdown

TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select"

def handler(event):
    print(event.item)
    if event.item == 'Test 1':
        print('source1 data')
        
        source1_data = pickle.load(open('source1.pickle','rb'))
        source1 = ColumnDataSource( source1_data )

        p.scatter(source=source1, x="x", y="y", color="colors", fill_alpha=0.7, size=5)

        labels = LabelSet(x='x', y='y', text='lang', text_font_size='12px',
              x_offset=5, y_offset=5, source=source1, render_mode='canvas')
        p.add_layout(labels)

    elif event.item == 'b':
        print('...')


p = figure(title = "Clusters of language locales by P31_obj_set localization frequency",
           tools=TOOLS, toolbar_location='below',
           aspect_ratio=2,
           # plot_width=1500, plot_height=800,
           sizing_mode='stretch_both',
           tooltips=[('lang', '@lang')] )
d = Dropdown(label='Load dataset', menu=['Test 1', None, '...', None])

d.on_click(handler)

curdoc().title = ""
curdoc().add_root(p)
curdoc().add_root(d)
