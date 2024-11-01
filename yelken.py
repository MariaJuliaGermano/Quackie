from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc

# Inicialize o app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout da tela de login
app.layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                html.H2("Login", className="text-center"),
                width=12
            ),
            className="mb-4",
        ),
        dbc.Row(
            dbc.Col(
                dbc.Form(
                    [
                        dbc.Row(
                            [
                                dbc.Label("Usuário", html_for="username", width=4),
                                dbc.Col(
                                    dbc.Input(type="text", id="username", placeholder="Digite seu usuário"),
                                    width=8
                                ),
                            ],
                            className="mb-3"
                        ),
                        dbc.Row(
                            [
                                dbc.Label("Senha", html_for="password", width=4),
                                dbc.Col(
                                    dbc.Input(type="password", id="password", placeholder="Digite sua senha"),
                                    width=8
                                ),
                            ],
                            className="mb-3"
                        ),
                        dbc.Button("Login", id="login-button", color="primary", className="w-100"),
                        html.Div(id="login-message", className="mt-3"),
                    ]
                ),
                width=4,
                className="mx-auto"
            ),
        ),
    ],
    className="mt-5"
)

# Callback para verificar o login
@app.callback(
    Output("login-message", "children"),
    Input("login-button", "n_clicks"),
    State("username", "value"),
    State("password", "value"),
)
def check_login(n_clicks, username, password):
    if n_clicks:
        # Autenticação básica
        if username == "admin" and password == "1234":
            return dbc.Alert("Login bem-sucedido!", color="success")
        else:
            return dbc.Alert("Usuário ou senha incorretos.", color="danger")
    return ""

# Execute o app
if __name__ == "__main__":
    app.run_server(debug=True)
