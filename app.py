import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

df = pd.read_csv('StockData.csv')
print(df.columns)
print(df.head())

months = df['Month'].unique()

company_colors = {
    'Amazon': '#331EFA',
    'Apple': '#FF555B',
    'Google': '#02AC96',
    'Microsoft': '#BA22FF',
    'Tesla': '#252525'
}

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Stock Market Analysis Dashboard"), width=12)
    ], className="mt-4 mb-4"),
    
    dbc.Row([
        dbc.Col([
            html.Label("Select Month:"),
            dcc.Dropdown(
                id='month-dropdown',
                options=[{'label': m, 'value': m} for m in months],
                value=months[0],
                clearable=False
            )
        ], md=4),

        dbc.Col([
            html.Label("Select Stock Price Metric:"),
            dcc.RadioItems(
                id='metric-radio',
                options=[
                    {'label': 'Open', 'value': 'Open'},
                    {'label': 'Close', 'value': 'Close'},
                    {'label': 'High', 'value': 'High'},
                    {'label': 'Low', 'value': 'Low'}
                ],
                value='Open',
                inline=True
            )
        ], md=4),

        dbc.Col([
            html.Button(
                "Update Charts", 
                id='update-button', 
                n_clicks=0, 
                className="btn btn-primary"
            )
        ], md=4, style={'textAlign': 'center'})
    ], className="mb-4"),
    
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='bar-chart')
        ], md=6),
        dbc.Col([
            dcc.Graph(id='box-plot')
        ], md=6)
    ])
], fluid=True)

@app.callback(
    [Output('bar-chart', 'figure'),
     Output('box-plot', 'figure')],
    [Input('update-button', 'n_clicks')],
    [State('month-dropdown', 'value'),
     State('metric-radio', 'value')]
)
def update_charts(n_clicks, selected_month, selected_metric):
    filtered_df = df[df['Month'] == selected_month]

    avg_df = filtered_df.groupby('Company', as_index=False)[selected_metric].mean()

    bar_fig = px.bar(
        avg_df,
        x='Company',
        y=selected_metric,
        color='Company',
        color_discrete_map=company_colors,
        title=f"Average {selected_metric} Prices of Each Company"
    )
    bar_fig.update_layout(
        xaxis_title="Company",
        yaxis_title="Stock Price"
    )

    box_fig = px.box(
        filtered_df,
        x='Company',
        y=selected_metric,
        color='Company',
        color_discrete_map=company_colors,
        title=f"{selected_metric} Price Distribution"
    )
    box_fig.update_layout(
        xaxis_title="Company",
        yaxis_title="Stock Price"
    )

    return bar_fig, box_fig


if __name__ == '__main__':
    app.run_server(debug=True)
