# Bokeh test
import pandas as pd
import pickle
from bokeh.plotting import figure, output_file, show, curdoc
from bokeh.models import HoverTool, ColumnDataSource, Div, Label, LabelSet, Button, Dropdown, Select, CustomJS, CheckboxGroup, Paragraph
from bokeh.layouts import row, column
from bokeh.themes import built_in_themes, Theme


# # # # # # # # # # # # # # 
# # Lang locales
# # # # # # # # # # # # # # 

def button_handler(event):
    global runtime, source1, show_labels

    # Load from source, then update data source on additional selections
    sourcefile = "source1-" + s.value.replace(": ", "_").replace(", ", "-") + ".pickle"
    print('source1 data: ' + s.value)
    if runtime == 0:
        source1_data = pickle.load(open('source1-data-langs/' + sourcefile,'rb'))
        source1_df = pd.DataFrame(source1_data, columns=source1_data.keys())
        source1 = ColumnDataSource(source1_df)  # can also load directly from dict instead of pandas
    elif runtime > 0:
        source1.data = pickle.load(open('source1-data-langs/' + sourcefile,'rb'))
    # print(source1_df)

    # Scatter plot
    p.scatter(source=source1, x="x", y="y", color="colors", fill_alpha=0.7, size=5)
    p.add_tools(HoverTool(tooltips=[("language", "@lang")]))

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
    'source1-tSNE-Langs-Perplexity_25-LearningRate_200-Iterations_12500-KmeansClusters_5-AvgSilhouette_0.7744107.pickle',
    '2021-11-04 data:',
    'source1-tSNE-Langs-Perplexity_30-LearningRate_250-Iterations_7500-KmeansClusters_5-AvgSilhouette_0.7843169.pickle',
    ' = = = = = = = = = = ',
    'source1-tSNE-Langs-Perplexity_5-LearningRate_100-Iterations_10000-KmeansClusters_5-AvgSilhouette_0.5356258.pickle',
    'source1-tSNE-Langs-Perplexity_5-LearningRate_100-Iterations_5000-KmeansClusters_5-AvgSilhouette_0.4785947.pickle',
    'source1-tSNE-Langs-Perplexity_5-LearningRate_100-Iterations_7000-KmeansClusters_5-AvgSilhouette_0.49775645.pickle',
    'source1-tSNE-Langs-Perplexity_5-LearningRate_200-Iterations_10000-KmeansClusters_5-AvgSilhouette_0.5187296.pickle',
    'source1-tSNE-Langs-Perplexity_5-LearningRate_200-Iterations_5000-KmeansClusters_5-AvgSilhouette_0.49838758.pickle',
    'source1-tSNE-Langs-Perplexity_5-LearningRate_200-Iterations_7000-KmeansClusters_5-AvgSilhouette_0.5186522.pickle'
    'source1-tSNE-Langs-Perplexity_10-LearningRate_100-Iterations_10000-KmeansClusters_5-AvgSilhouette_0.61021835.pickle',
    'source1-tSNE-Langs-Perplexity_10-LearningRate_100-Iterations_5000-KmeansClusters_5-AvgSilhouette_0.57772136.pickle',
    'source1-tSNE-Langs-Perplexity_10-LearningRate_100-Iterations_7000-KmeansClusters_5-AvgSilhouette_0.62639225.pickle',
    'source1-tSNE-Langs-Perplexity_10-LearningRate_200-Iterations_10000-KmeansClusters_5-AvgSilhouette_0.6511983.pickle',
    'source1-tSNE-Langs-Perplexity_10-LearningRate_200-Iterations_5000-KmeansClusters_5-AvgSilhouette_0.5979305.pickle',
    'source1-tSNE-Langs-Perplexity_10-LearningRate_200-Iterations_7000-KmeansClusters_5-AvgSilhouette_0.61925894.pickle',
    'source1-tSNE-Langs-Perplexity_20-LearningRate_100-Iterations_10000-KmeansClusters_5-AvgSilhouette_0.69702715.pickle',
    'source1-tSNE-Langs-Perplexity_20-LearningRate_100-Iterations_5000-KmeansClusters_5-AvgSilhouette_0.7157357.pickle',
    'source1-tSNE-Langs-Perplexity_20-LearningRate_100-Iterations_7000-KmeansClusters_5-AvgSilhouette_0.7004581.pickle',
    'source1-tSNE-Langs-Perplexity_20-LearningRate_200-Iterations_10000-KmeansClusters_5-AvgSilhouette_0.7106504.pickle',
    'source1-tSNE-Langs-Perplexity_20-LearningRate_200-Iterations_5000-KmeansClusters_5-AvgSilhouette_0.70806557.pickle',
    'source1-tSNE-Langs-Perplexity_20-LearningRate_200-Iterations_7000-KmeansClusters_5-AvgSilhouette_0.7114242.pickle',
    'source1-tSNE-Langs-Perplexity_25-LearningRate_300-Iterations_5000-KmeansClusters_4-AvgSilhouette_0.76430476.pickle',
    'source1-tSNE-Langs-Perplexity_30-LearningRate_100-Iterations_10000-KmeansClusters_5-AvgSilhouette_0.7391591.pickle',
    'source1-tSNE-Langs-Perplexity_30-LearningRate_100-Iterations_5000-KmeansClusters_5-AvgSilhouette_0.73832816.pickle',
    'source1-tSNE-Langs-Perplexity_30-LearningRate_100-Iterations_7000-KmeansClusters_5-AvgSilhouette_0.73323584.pickle',
    'source1-tSNE-Langs-Perplexity_30-LearningRate_200-Iterations_10000-KmeansClusters_5-AvgSilhouette_0.75128967.pickle',
    'source1-tSNE-Langs-Perplexity_30-LearningRate_200-Iterations_12500-KmeansClusters_5-AvgSilhouette_0.7766407.pickle',
    'source1-tSNE-Langs-Perplexity_30-LearningRate_200-Iterations_5000-KmeansClusters_5-AvgSilhouette_0.74823016.pickle',
    'source1-tSNE-Langs-Perplexity_30-LearningRate_200-Iterations_7000-KmeansClusters_5-AvgSilhouette_0.7375945.pickle',
    'source1-tSNE-Langs-Perplexity_40-LearningRate_100-Iterations_10000-KmeansClusters_5-AvgSilhouette_0.6665348.pickle',
    'source1-tSNE-Langs-Perplexity_40-LearningRate_100-Iterations_5000-KmeansClusters_5-AvgSilhouette_0.6475928.pickle',
    'source1-tSNE-Langs-Perplexity_40-LearningRate_100-Iterations_7000-KmeansClusters_5-AvgSilhouette_0.65679246.pickle',
    'source1-tSNE-Langs-Perplexity_40-LearningRate_200-Iterations_10000-KmeansClusters_5-AvgSilhouette_0.6557168.pickle',
    'source1-tSNE-Langs-Perplexity_40-LearningRate_200-Iterations_5000-KmeansClusters_5-AvgSilhouette_0.6544822.pickle',
    'source1-tSNE-Langs-Perplexity_40-LearningRate_200-Iterations_7000-KmeansClusters_5-AvgSilhouette_0.6542868.pickle'
]
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
          Select the following settings and click "Load Visualization":<br>(1) Node labels on or off, <br>(2) Dataset source
          <br> <hr> """, 
          width=500, height=100, style={'font-size': '14px'})

# row1 = row(div,c,s,b, align='center', cols='min')
row1 = column(div,c,s,b)

# para = Paragraph(text="""GitHub source: """, width=200, height=500)
para = Div(text="<br><br> GitHub source: TBA <br>", 
          width=500, height=150, style={})

theme = {
'attrs' : {
    'Title': {
        'text_font': 'helvetica',
        'text_font_size': '18px',
    }
}}









# # # # # # # # # # # # # # 
# # P31_obj_set
# # # # # # # # # # # # # # 

def button_handler2(event2):
    global runtime2, source2, show_labels2

    # Load from source, then update data source on additional selections
    sourcefile = "source1-tSNE-P31objset-" + s2.value.replace("NLP model: stsb-roberta-large", "NLP, stsb, roberta, large")\
                                                     .replace(": ", "_")\
                                                     .replace(", ", "-") + ".pickle"
    print('source2 data: ' + s2.value)
    if runtime2 == 0:
        source2_data = pickle.load(open('source1-data-P31objset/' + sourcefile,'rb'))
        source2_df = pd.DataFrame(source2_data, columns=source2_data.keys())
        source2 = ColumnDataSource(source2_df)  # can also load directly from dict instead of pandas
    elif runtime2 > 0:
        source2.data = pickle.load(open('source1-data-P31objset/' + sourcefile,'rb'))

    # Scatter plot
    p2.scatter(source=source2, x="x", y="y", color="colors", fill_alpha=0.7, size=5)
    p2.add_tools(HoverTool(tooltips=[("P31_obj_set (en)", "@P31_obj_set_id_label")]))

    # Add node labels
    print("show_labels: " + str(show_labels2))
    if show_labels2 == True:
        labels = LabelSet(x='x', y='y', text='P31_obj_set_id_label', text_font='helvetica', text_font_size='12px',
                x_offset=5, y_offset=5, source=source2,
                render_mode='canvas') #render_mode='canvas' or 'css')
        p2.add_layout(labels)
    elif show_labels2 == False:
        pass

    runtime2 += 1


def checkbox_handler2(event):
    global show_labels2, runtime2
    # print(attr, old, new)
    print(c2.active)
    if 0 in c2.active:
        show_labels2 = True
        c2.labels = [' Node labels ON']
    if 0 not in c2.active:
        show_labels2 = False
        c2.labels = [' Node labels OFF']
    if runtime2 > 0:
        c2.labels = [' (Please reload page to toggle again)']
        c2.disabled = True



## Globals ##
TOOLS="wheel_zoom,hover,crosshair,pan,zoom_in,zoom_out,box_zoom,undo,redo,reset,save"
# TOOLS="wheel_zoom,zoom_in,zoom_out,reset,save"
runtime2 = 0
source2 = ColumnDataSource()
show_labels2 = True


# Figure and Dropdown menu
p2 = figure(title = "Clusters of P31_obj_set by 1-hot encoded vectors and BERT sentence embeddings",
           background_fill_color='whitesmoke',  # gainsboro
           # tools=TOOLS, 
           toolbar_location='below',
           aspect_ratio=2,
           # plot_height=1000,
           # plot_width=2000, 
           # width_policy='max',
           # max_width=5000,
           sizing_mode='stretch_both',
           # tooltips=[("", "")],
           active_scroll='wheel_zoom')

menu_items2 = [' ',
    ' = = = = = = = = = = Top silhouette score:',
    ' = = = = = = = = = = = = 1 Hot Encoding: ',
    'source1-tSNE-P31objset-1Hot-Perplexity_2-LearningRate_150-Iterations_15000-KmeansClusters_65-AvgSilhouette_0.86559206.pickle',
    ' = = = = = = = = = = = = BERT Transformer Encoding: ',
    'source1-tSNE-P31objset-NLP-stsb-roberta-large-Perplexity_2-LearningRate_300-Iterations_2500-KmeansClusters_400-AvgSilhouette_0.71771604.pickle',
    # 'source1-tSNE-P31objset-NLP-stsb-roberta-large-Perplexity_2-LearningRate_200-Iterations_7500-KmeansClusters_325-AvgSilhouette_0.7104604.pickle',
    '',
    ' = = = = = = = = = = = = Misc. runs: ',
    'source1-tSNE-P31objset-NLP-Perplexity_2-LearningRate_200-Iterations_15000-KmeansClusters_90-AvgSilhouette_0.5741877.pickle',
    'source1-tSNE-P31objset-NLP-Perplexity_5-LearningRate_100-Iterations_5000-KmeansClusters_50-AvgSilhouette_0.500595.pickle',
    'source1-tSNE-P31objset-NLP-Perplexity_2-LearningRate_100-Iterations_12500-KmeansClusters_65-AvgSilhouette_0.5196672.pickle'
]
# Formatting text for readability in dropdown
menu_items2 = [ m.replace("source1-tSNE-P31objset-", "")
                .replace("-", ", ").replace("_", ": ")
                .replace(".pickle", "")
                .replace("NLP, stsb, roberta, large", "NLP model: stsb-roberta-large") for m in menu_items2]

c2 = CheckboxGroup(labels=["Show Node Labels"], active=[0])
c2.on_click(checkbox_handler2)

s2 = Select(title='Select dataset:', width=500, options=menu_items2)

b2 = Button(label="Load Visualization", button_type="primary")
b2.on_click(button_handler2)


div2 = Div(text="""
          Select the following settings and click "Load Visualization":<br>(1) Node labels on or off, <br>(2) Dataset source
          <br> <hr> """, 
          width=500, height=100, style={'font-size': '14px'})

# row1 = row(div,c,s,b, align='center', cols='min')
row2 = column(div2,c2,s2,b2)

# para = Paragraph(text="""GitHub source: """, width=200, height=500)
para2 = Div(text="<br><br> GitHub source: TBA <br><br><br><br><br><br><br>", 
          width=500, height=150, style={})



# # # # # # # # # # # # # # 
# # 
# # # # # # # # # # # # # # 

curdoc().title = "Bokeh Application"
curdoc().theme = Theme(json=theme) #"dark_minimal"
curdoc().add_root(p)
# curdoc().add_root(c)
# curdoc().add_root(d)
# curdoc().add_root(s)
# curdoc().add_root(b)
curdoc().add_root(row1)
curdoc().add_root(para)

curdoc().add_root(p2)
curdoc().add_root(row2)
curdoc().add_root(para2)



# # # # # # # # # # # # # # 
# # Heatmap
# # # # # # # # # # # # # # 

def dropdown_handler(event3):
    # global div_image
    heatmaps = {
        'Heatmap with subplots, by cluster': 'heatmap-P31-obj-sets-xlabel-top30langsW2E-count1K-subplots-all.png',
        'Heatmap with all in one, log-scale': 'heatmap-P31-obj-sets-xlabel-top30langsW2E-count1K.png',
        'Heatmap with all in one, percents': 'heatmap-P31-obj-sets-xlabel-top30langsW2E-count1K-percents.png'
    }
    div_image = Div(text="""
        <img src="">
        <br><br><br>""", 
        width=500, height=150
        )
    div_image.text = """<img src="https://github.com/nchah/bokeh-test/blob/main/images/{}?raw=true" >""".format(heatmaps[event3.item])
    curdoc().add_root(div_image)


heatmap_intro = Div(text="""<h3>Heatmaps</h3>

    Language Legend: <br>
    "'en': English, 'pt': Portuguese, 'es': Spanish, 'it': Italian, 'fr': French, 'de': Standard German, 'ru': Russian, 'tr': Turkish, 'ar': Standard Arabic, 'arz': Egyptian Spoken Arabic, 
    'ha': Hausa, 'ss': Swahili, 'fa': Iranian Persian, 'hi': Hindi, 'bn': Bengali, 'ur': Urdu, 'mr': Marathi, 
    'te': Telugu, 'pa': Western Punjabi, 'gu': Gujarati, 'ta': Tamil, 'th': Thai, 'vi': Vietnamese, 
    'id': Indonesian, 'jv': Javanese, 'zh': Mandarin Chinese, 'wuu': Wu Chinese, 'yue': Yue Chinese, 'ko': Korean, 'ja': Japanese"
    """,
    width=1500, height=150, style={'font-size': '14px'}
    )
heatmap_end = Div(text="""<br><br><br>""",
    width=500, height=10, style={'font-size': '18px'}
    )

menu_items3 = [
    'Heatmap with all in one, log-scale',
    'Heatmap with all in one, percents',
    'Heatmap with subplots, by cluster'
]
# dropdown menu that loads graph automatically
d = Dropdown(label='Load Heatmap', width=500, menu=menu_items3,
             button_type='primary',
             # background='blue',
             # margin=(5, 5, 5, 20)
             )
d.on_click(dropdown_handler)

div_image = Div(text="""
    <img src="" alt="div_image">
    <br><br><br>""", 
    width=500, height=150
    )

curdoc().add_root(heatmap_intro)
curdoc().add_root(d)
curdoc().add_root(heatmap_end)

