import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from db_wrapper import DBWrapper

sites = [
    "嘉義",
    "新竹",
    "彰化",
    "屏東",
    "苗栗",
    "雲林",
]

db_wrapper = DBWrapper()
data = {}
for site in sites:
    data[site] = db_wrapper.get_data(site)

all_sidebar = {}

for site in sites:
    cont = []
    for d in data[site]:
        temp = [
            html.P(d["p_location"]),
            html.P(d["p_time"]),
            html.P(d["p_content"]),
            html.Hr(),
            ]
        cont = cont + temp
    # qq = html.Div(cont)
    all_sidebar[site] = cont

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "22rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "24rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("FB 爬蟲內容", className="display-4"),
        html.Hr(),
        # html.P(
        #     "A simple sidebar layout with navigation links", className="lead"
        # ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink(sites[0], href="/page-1", active="exact"),
                dbc.NavLink(sites[1], href="/page-2", active="exact"),
                dbc.NavLink(sites[2], href="/page-3", active="exact"),
                dbc.NavLink(sites[3], href="/page-4", active="exact"),
                dbc.NavLink(sites[4], href="/page-5", active="exact"),
                dbc.NavLink(sites[5], href="/page-6", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.Div(html.P("This is the content of the home page!"), className="container")
    elif pathname == "/page-1":
        return html.Div(all_sidebar[sites[0]], className="container")
    elif pathname == "/page-2":
        return html.Div(all_sidebar[sites[1]], className="container")
    elif pathname == "/page-3":
        return html.Div(all_sidebar[sites[2]], className="container")
    elif pathname == "/page-4":
        return html.Div(all_sidebar[sites[3]], className="container")
    elif pathname == "/page-5":
        return html.Div(all_sidebar[sites[4]], className="container")
    elif pathname == "/page-6":
        return html.Div(all_sidebar[sites[5]], className="container")
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == "__main__":
    app.run_server(debug=True)