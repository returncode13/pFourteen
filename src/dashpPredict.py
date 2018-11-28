import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import  Input,Output,State

import numpy as np
import pandas as pd
import plotly.graph_objs as go
import jsonpickle as jsp
import numpy as np
import keras
from keras.models import  load_model

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# #external_stylesheets=['https://codepen.io/maxwshen/pen/GGGGNR']
#external_stylesheets=['https://codepen.io/chriddyp/pen/brPBPO.css']
#x=np.random.rand(4501,648)

x=np.loadtxt('/home/sharath/programming/python/pycharmProjects/proto-14/data/filtered_shot.txt')
xx=np.loadtxt('/home/sharath/programming/python/pycharmProjects/proto-14/data/shot.txt')

print('Loading data and labels')

TOTAL_SAMPLES_IN_FIELD_DATA=198
NUMBER_OF_SAMPLES=1126
NUMBER_OF_CHANNELS=648

field_data=np.loadtxt('/home/sharath/programming/python/pycharmProjects/proto-14/data/csv_for_proto-14/data.csv')
field_labels=np.loadtxt('/home/sharath/programming/python/pycharmProjects/proto-14/data/csv_for_proto-14/labels.csv')


field_data=field_data.reshape(TOTAL_SAMPLES_IN_FIELD_DATA,NUMBER_OF_SAMPLES,NUMBER_OF_CHANNELS)
print('Done loading data.')
print('Now loading model')
loaded_model=load_model('/home/sharath/programming/python/pycharmProjects/proto-14/models/tagging_model-v0.h5')
print('Done loading model')

shots=[x,xx]
NUMBER_OF_SHOTS=len(shots)
n1=x.shape[0]           #time
n2=x.shape[1]           #offset
print(x.shape)
app=dash.Dash(__name__,external_stylesheets=external_stylesheets)
colors = {
    'background': '#ffffff',
    'text': '#7FDBFF'
}
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[

    html.Div(children=[

        dcc.Graph(
        id='shot-view',
        figure={
            'data': [go.Heatmap(z=shots[0],
                                colorscale='Greys')],
            'layout':{
                'title': 'Dash Data Visualization',
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                },
                'yaxis':dict(autorange='reversed'),
                'autosize':False,
                #'height':1000,
                #'width':1000

            }
        }
        
        ),
        html.Div(id="update"),
        html.Div(id='hidden',style={'display': 'none'}),


        html.Div([html.Button('Random Shot', id='button'),
                  html.H1(children='Prediction')]),

        html.Div(id='prediction')

    ]),


    ])


class Shot:
    def __init__(self):
        self.shot_n=np.random.randint(NUMBER_OF_SHOTS,size=1)

@app.callback(
    Output(component_id='prediction',component_property='children'),
    [Input(component_id='shot-view',component_property='figure')],
     [State(component_id='hidden',component_property='children')]
)
def predict_after_figure(f,json_encoded):
    for i in range(1,100000):
        pass
    shot = jsp.decode(json_encoded)
    print('decoded shot ', shot.shot_n)
    shot_pred=field_data[shot.shot_n[0]].reshape(1,NUMBER_OF_SAMPLES,NUMBER_OF_CHANNELS,1)
    print('shape of shot to be predicted',shot_pred.shape)
    preds=loaded_model.predict_classes(shot_pred)
    print('preds shape: ',preds.shape)
    print(preds)

    return "Pred result for shot "+str(shot.shot_n)



@app.callback(
    Output(component_id='hidden',component_property='children'),
    [Input(component_id='button',component_property='n_clicks')]
)
def get_random_shot(inv):
    """

    :param inv:
    :return: JSON encoded Shot object
    """
    shot=Shot()
    print('encoding shot: ',shot.shot_n)
    return jsp.encode(shot)


@app.callback(
    Output(component_id='shot-view',component_property='figure'),
    [Input(component_id='hidden',component_property='children')]
)
def update_fig(json_encoded):
    """

    :param json_encoded:
    :return: the 'figure' param of dcc.Graph
    """
    shot=jsp.decode(json_encoded)
    print('decoded shot ',shot.shot_n)
    return {
        'data': [go.Heatmap(z=shots[shot.shot_n[0]],
                            colorscale='Greys')],
        'layout': {
            'title': 'Dash Data Visualization',
            'plot_bgcolor': colors['background'],
            'paper_bgcolor': colors['background'],
            'font': {
                'color': colors['text']
            },
            'yaxis': dict(autorange='reversed'),
            'autosize': False,
             #'height':1000,
             #'width':1000

        }
    }



if __name__=='__main__':
    app.run_server(debug=True)

