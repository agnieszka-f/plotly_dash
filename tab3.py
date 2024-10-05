import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px

def render_chart_1(df):
    df['dayOfWeek'] = df['tran_date'].apply(lambda x: x.dayofweek)
    gr = df.groupby(['dayOfWeek', 'Store_type']).count()['transaction_id'].reset_index()
    gr.rename(columns={'transaction_id' : 'Number of transaction'}, inplace=True)

    fig = go.Figure()
    fig = px.bar(gr, x='dayOfWeek', y='Number of transaction', color='Store_type', barmode='group',
                labels={'dayOfWeek': 'Dzień tygodnia', 'transaction_id': 'Liczba transakcji'},
                title='Liczba transakcji w poszczególne dni tygodnia z podziałem na kanał sprzedaży')
    fig.update_layout(
        xaxis = dict(tickmode = 'array', tickvals = [0, 1, 2, 3, 4, 5, 6],
                    ticktext = ['Niedziela', 'Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota']),
        yaxis = dict(tickformat='d')
    )
    return fig

def render_tab(df):
    fig_1 = render_chart_1(df.copy())

    layout = html.Div([
        html.H1('Kanały sprzedaży',style={'text-align':'center'}),
        html.Div([
            html.Div([dcc.Graph(id='number-of-transaction_1', figure=fig_1)], style={'width' : '100%'}),
        ], 
        style={'width':'100%','text-align':'center'}),
        html.Div([
            html.Div([
                dcc.Dropdown(
                    id='clients_dropdown',
                    options = [{'label': 'Gender', 'value': 'Gender'}, {'label': 'Country', 'value': 'country'}],
                    value = 'Gender'
                ),
                dcc.Graph(id='clients_chart')], style={'width' : '100%'}),
        ], 
        style={'width':'100%','text-align':'center'}),
        html.Div(id='temp-out-clients')
    ])

    return layout