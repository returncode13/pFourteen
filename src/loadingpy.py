from dash.dependencies import Input, Output
import dash
import dash_core_components as dcc
import dash_html_components as html
import time

app = dash.Dash()

app.layout = html.Div(children=[

    html.Div([dcc.Dropdown(id='category', placeholder='Select category', multi=False,
                           options=[{'label': 'giraffes', 'value': 'giraffes'},
                                    {'label': 'orangutans', 'value': 'orangutans'},
                                    {'label': 'monkeys', 'value': 'monkeys'}]
                           )
              ], style={'max-width': 260}),

    html.Div(id='load'),
    html.Div(id='output'),
])

@app.callback(Output('load', 'children'),
              [Input('category', 'value')])
def prepare_data(categ):
    if categ:
        return html.Div([dcc.Markdown(
                         '''Loading ...''')], id='output')

@app.callback(Output('output', 'children'),
              [Input('category', 'value')])
def prepare_data(categ):
    if categ:
        time.sleep(2)
        return html.Div([dcc.Markdown(
                         '''Output for {}'''.format(categ))])

if __name__ == '__main__':
    app.run_server(debug=True)