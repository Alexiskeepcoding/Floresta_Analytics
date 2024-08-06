"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )

def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.heading(
                        "Floresta Analytics", size="7", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Inicio", "/"),
                    navbar_link("Mapa", "/mapa"),
                    navbar_link("Estadisticas", "/estadistica"),
                    navbar_link("Comparacion", "/comparacion"),
                    justify="end",
                    spacing="5",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon_button(
                            rx.icon("user"),
                            size="2",
                            radius="full",
                        ),
                    ),
                    rx.menu.content(
                        rx.menu.item(rx.link("Sign In", href="/signIn")),
                        rx.menu.separator(),
                        rx.menu.item("Log Out", href="/#"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),

        bg=rx.color("accent", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )
    
def inicio() -> rx.Component:
    return rx.box(
        navbar(),
        rx.heading(
            "Bienvenido a la Floresta Analytics", 
            color_scheme="indigo",
            weight="bold"
        ),
        rx.text(
            "Explora datos de negocios locales y eventos mediante un mapa interactivo y analisis de datos detallado."
        ),
        align_items="start",
    )

class FormState(rx.State):
    form_data = {}
    
    def handle_submit(self, form_data: dict):   
        """Handle form submission."""
        self.form_data = form_data

def signUp() -> rx.Component:
    return rx.box(
        rx.heading(
            "Registrarse",
            color_scheme="indigo",
            weight="bold"
        ),
        rx.flex(
            rx.form(
                rx.vstack(
                    rx.input(
                        placeholder="Nombre",
                        name="name",
                    ),
                    rx.input(
                        placeholder="Usuario",
                        name="user",
                    ),
                    rx.input(
                        placeholder="Correo",
                        name="email",
                    ),
                    rx.input(
                        placeholder="Contraseña",
                        name="password",
                    ),
                    rx.button("Submit", type="submit"),
                    rx.link(
                        "Tienes una cuenta? Inicia Sesión!",
                        href="/signIn",
                        align=""
                    )
                ),
                justify="center",
                on_submit=FormState.handle_submit,
                reset_on_submit=True,
            ),
        ),
        rx.divider(),
        rx.text(FormState.form_data.to_string()),
        center_content=True,
        center_on_page=True,
    )


def signIn() -> rx.Component:
    return rx.chakra.center(
        rx.box(
            rx.heading(
                "Iniciar Sesión",
                color_scheme="indigo",
                weight="bold"
            ),
            rx.form(
                rx.vstack(
                    rx.input(
                        placeholder="Usuario",
                        name="user",
                    ),
                    rx.input(
                        placeholder="Contraseña",
                        name="password",
                    ),
                    rx.button("Submit", type="submit"),
                    rx.link(
                        "Aun no tinees una cuenta? Registrate!",
                        href="/signUp"
                    )
                ),
                justify="center",
                on_submit=FormState.handle_submit,
                reset_on_submit=True,
            ),
            rx.divider(),
            rx.text(FormState.form_data.to_string()),
        )    
    )

        

def mapa () -> rx.Component:
    return rx.box(
        navbar(),
        rx.heading(
            "Mapa Interactivo de Negocios",
            color_scheme="indigo",
            weight="bold"
        ),
        rx.text(
            "Explora datos de negocios locales y eventos mediante un mapa interactivo y analisis de datos detallado."
        ),
    )

def estadistica () -> rx.Component:
    return rx.box(
        navbar(),
        rx.heading(
            "Estadisticas Generales",
            color_scheme="indigo",
            weight="bold"
        ),
        rx.recharts.pie_chart (
            rx.recharts.pie(
               data=[
                   {"name": "Rstaurantes", "value": 30},
                   {"name": "Bares", "value": 30},
                   {"name": "Hoteles", "value": 30},
               ],
               data_key="value",
               name_key="name",
               fill="#8884d8",
               label=True,
            ),
            width="100%",
            height=300,
            legend="Distribucion por Cateogría",
        ),
    )

""" def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Web de Python", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )
 """

app = rx.App()

app.add_page(navbar)
app.add_page(inicio, route="/")
app.add_page(signUp , route="/signUp")
app.add_page(signIn , route="/signIn")
app.add_page(mapa , route="/mapa")
app.add_page(estadistica , route="/estadistica")

