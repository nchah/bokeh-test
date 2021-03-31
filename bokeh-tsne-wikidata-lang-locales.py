# Bokeh test
import pandas as pd
import pickle
from bokeh.plotting import figure, output_file, show, curdoc
from bokeh.models import HoverTool, ColumnDataSource, Div, Label, LabelSet, Button, Dropdown, Select, CustomJS, CheckboxGroup, Paragraph
from bokeh.layouts import row, column
from bokeh.themes import built_in_themes, Theme


# def handler(event):
#     global runtime, source1, show_labels
#     # Load from source, then update data source on additional selections
#     print('source1 data: ' + event.item)
#     if runtime == 0:
#         source1_data = pickle.load(open('source1-data/' + event.item,'rb'))
#         source1_df = pd.DataFrame(source1_data, columns=source1_data.keys())
#         source1 = ColumnDataSource(source1_df)  # can also load directly from dict instead of pandas
#     elif runtime > 0:
#         source1.data = pickle.load(open('source1-data/' + event.item,'rb'))

#     # Scatter plot
#     p.scatter(source=source1, x="x", y="y", color="colors", fill_alpha=0.7, size=5)

#     # Add node labels
#     print("check: " + str(show_labels))
#     if show_labels == True:
#         labels = LabelSet(x='x', y='y', text='lang', text_font_size='12px',
#                 x_offset=5, y_offset=5, source=source1,
#                 render_mode='canvas') #render_mode='canvas')
#         p.add_layout(labels)
#     elif show_labels == False:
#         pass

#     runtime += 1


def button_handler(event):
    global runtime, source1, show_labels

    # Load from source, then update data source on additional selections
    sourcefile = "source1-" + s.value.replace(": ", "_").replace(", ", "-") + ".pickle"
    print('source1 data: ' + s.value)
    if runtime == 0:
        source1_data = pickle.load(open('source1-data/' + sourcefile,'rb'))
        source1_df = pd.DataFrame(source1_data, columns=source1_data.keys())
        source1 = ColumnDataSource(source1_df)  # can also load directly from dict instead of pandas
    elif runtime > 0:
        source1.data = pickle.load(open('source1-data/' + sourcefile,'rb'))

    # Scatter plot
    p.scatter(source=source1, x="x", y="y", color="colors", fill_alpha=0.7, size=5)
    p.add_tools(HoverTool(tooltips=[("language:", "@lang")]))

    # Add node labels
    print("show_labels: " + str(show_labels))
    if show_labels == True:
        labels = LabelSet(x='x', y='y', text='lang', text_font='helvetica', text_font_size='12px',
                x_offset=5, y_offset=5, source=source1,
                render_mode='canvas') #render_mode='canvas' or 'css')
        p.add_layout(labels)
    elif show_labels == False:
        pass

    runtime += 1


def checkbox_handler(event):
    global show_labels, runtime
    # print(attr, old, new)
    print(c.active)
    if 0 in c.active:
        show_labels = True
        c.labels = [' Node labels ON']
    if 0 not in c.active:
        show_labels = False
        c.labels = [' Node labels OFF']
    if runtime > 0:
        c.labels = [' (Please reload page to toggle again)']
        c.disabled = True



## Globals ##
TOOLS="wheel_zoom,hover,crosshair,pan,zoom_in,zoom_out,box_zoom,undo,redo,reset,save"
# TOOLS="wheel_zoom,zoom_in,zoom_out,reset,save"
runtime = 0
source1 = ColumnDataSource()
show_labels = True


# Figure and Dropdown menu
p = figure(title = "Clusters of language locales by P31_obj_set localization frequency",
           background_fill_color='whitesmoke',  # gainsboro
           # tools=TOOLS, 
           toolbar_location='below',
           aspect_ratio=2,
           # plot_height=1000,
           # plot_width=2000, 
           # width_policy='max',
           # max_width=5000,
           sizing_mode='stretch_both',
           tooltips=[("language:", "@lang")],
           active_scroll='wheel_zoom')

menu_items = [' ',
     ' = = = = = = = = = = Top silhouette score:',
     'source1-tSNE_Perplexity_30-LearningRate_200-Iterations_10000-AvgSilhouette_0.75128967.pickle',
     ' = = = = = = = = = = ',
     'source1-tSNE_Perplexity_5-LearningRate_100-Iterations_5000-AvgSilhouette_0.4785947.pickle',
     'source1-tSNE_Perplexity_5-LearningRate_100-Iterations_7000-AvgSilhouette_0.49775645.pickle',
     'source1-tSNE_Perplexity_5-LearningRate_100-Iterations_10000-AvgSilhouette_0.5356258.pickle',
     'source1-tSNE_Perplexity_5-LearningRate_200-Iterations_5000-AvgSilhouette_0.49838758.pickle',
     'source1-tSNE_Perplexity_5-LearningRate_200-Iterations_7000-AvgSilhouette_0.5186522.pickle',
     'source1-tSNE_Perplexity_5-LearningRate_200-Iterations_10000-AvgSilhouette_0.5187296.pickle',
     'source1-tSNE_Perplexity_10-LearningRate_100-Iterations_5000-AvgSilhouette_0.57772136.pickle',
     'source1-tSNE_Perplexity_10-LearningRate_100-Iterations_7000-AvgSilhouette_0.62639225.pickle',
     'source1-tSNE_Perplexity_10-LearningRate_100-Iterations_10000-AvgSilhouette_0.61021835.pickle',
     'source1-tSNE_Perplexity_10-LearningRate_200-Iterations_5000-AvgSilhouette_0.5979305.pickle',
     'source1-tSNE_Perplexity_10-LearningRate_200-Iterations_7000-AvgSilhouette_0.61925894.pickle',
     'source1-tSNE_Perplexity_10-LearningRate_200-Iterations_10000-AvgSilhouette_0.6511983.pickle',
     'source1-tSNE_Perplexity_20-LearningRate_100-Iterations_5000-AvgSilhouette_0.7157357.pickle',
     'source1-tSNE_Perplexity_20-LearningRate_100-Iterations_7000-AvgSilhouette_0.7004581.pickle',
     'source1-tSNE_Perplexity_20-LearningRate_100-Iterations_10000-AvgSilhouette_0.69702715.pickle',
     'source1-tSNE_Perplexity_20-LearningRate_200-Iterations_5000-AvgSilhouette_0.70806557.pickle',
     'source1-tSNE_Perplexity_20-LearningRate_200-Iterations_7000-AvgSilhouette_0.7114242.pickle',
     'source1-tSNE_Perplexity_20-LearningRate_200-Iterations_10000-AvgSilhouette_0.7106504.pickle',
     'source1-tSNE_Perplexity_30-LearningRate_100-Iterations_5000-AvgSilhouette_0.73832816.pickle',
     'source1-tSNE_Perplexity_30-LearningRate_100-Iterations_7000-AvgSilhouette_0.73323584.pickle',
     'source1-tSNE_Perplexity_30-LearningRate_100-Iterations_10000-AvgSilhouette_0.7391591.pickle',
     'source1-tSNE_Perplexity_30-LearningRate_200-Iterations_5000-AvgSilhouette_0.74823016.pickle',
     'source1-tSNE_Perplexity_30-LearningRate_200-Iterations_7000-AvgSilhouette_0.7375945.pickle',
     'source1-tSNE_Perplexity_40-LearningRate_100-Iterations_5000-AvgSilhouette_0.6475928.pickle',
     'source1-tSNE_Perplexity_40-LearningRate_100-Iterations_7000-AvgSilhouette_0.65679246.pickle',
     'source1-tSNE_Perplexity_40-LearningRate_100-Iterations_10000-AvgSilhouette_0.6665348.pickle',
     'source1-tSNE_Perplexity_40-LearningRate_200-Iterations_5000-AvgSilhouette_0.6544822.pickle',
     'source1-tSNE_Perplexity_40-LearningRate_200-Iterations_7000-AvgSilhouette_0.6542868.pickle',
     'source1-tSNE_Perplexity_40-LearningRate_200-Iterations_10000-AvgSilhouette_0.6557168.pickle']
# Formatting text for readability in dropdown
menu_items = [ m.replace("source1-", "")
                .replace(".pickle", "")
                .replace("-", ", ").replace("_", ": ") for m in menu_items]

c = CheckboxGroup(labels=["Show Node Labels"], active=[0])
c.on_click(checkbox_handler)

# # Alternative: dropdown menu that loads graph automatically
# d = Dropdown(label='Load dataset...', width=500, menu=menu_items,
#              button_type='primary',
#              # background='blue',
#              # margin=(5, 5, 5, 20)
#              )
# d.on_click(handler)

s = Select(title='Select dataset:', width=500, options=menu_items)

b = Button(label="Load Visualization", button_type="primary")
b.on_click(button_handler)


div = Div(text="""
          Select settings and click "Load Visualization"<br>(1) Node labels on or off, <br>(2) Dataset source
          <br> <hr> """, 
          width=500, height=100, style={'font-size': '14px'})

# row1 = row(div,c,s,b, align='center', cols='min')
row1 = column(div,c,s,b)

# para = Paragraph(text="""GitHub source: """, width=200, height=500)
para = Div(text="<br><br><br><br><br> GitHub source:", 
          width=500, height=500, style={})

theme = {
'attrs' : {
    'Title': {
        'text_font': 'helvetica',
        'text_font_size': '18px',
    }
}}

curdoc().title = "Bokeh Application"
curdoc().theme = Theme(json=theme) #"dark_minimal"
curdoc().add_root(p)
# curdoc().add_root(c)
# curdoc().add_root(d)
# curdoc().add_root(s)
# curdoc().add_root(b)
curdoc().add_root(row1)
curdoc().add_root(para)




