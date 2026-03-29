from rxconfig import config
from deep_translator import GoogleTranslator as Gt
import reflex as rx
from .NASA_API import imageToBirthDay, img_title_info

class State(rx.State):
    fecha_nacimiento: str = ""
    url_nasa: str = "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/9c64cfe3-bb3b-4ae8-b5a6-d2f39d21ff87/d3jme6i-8c702ad4-4b7a-4763-9901-99f8b4f038b0.png/v1/fill/w_600,h_400/fondo_transparente_png_by_imsnowbieber_d3jme6i-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NDAwIiwicGF0aCI6Ii9mLzljNjRjZmUzLWJiM2ItNGFlOC1iNWE2LWQyZjM5ZDIxZmY4Ny9kM2ptZTZpLThjNzAyYWQ0LTRiN2EtNDc2My05OTAxLTk5ZjhiNGYwMzhiMC5wbmciLCJ3aWR0aCI6Ijw9NjAwIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0._EzHYkfFGg43L1lkbnBwDnU4zb1QOFVmH29ZTO7ZrAc"
    titulo_nasa: str = "Descubre el cielo del dia en que naciste"
    info_nasa: str = "Introduce tu fecha de nacimiento para descubrir qué maravilla capturó la NASA ese día."
    
    def set_fecha_nacimiento(self, value: str):
        self.fecha_nacimiento = value
    
    def obtener_datos(self):
        df = imageToBirthDay(self.fecha_nacimiento)
        titulo, info, url = img_title_info(df)
        self.titulo_nasa = Gt(source='auto', target='es').translate(titulo)
        self.info_nasa = Gt(source='auto', target='es').translate(info)
        self.url_nasa = url
        
from .proyectPage2 import SecondPage

# Componentes

# Primera Page

estilo_fondo_estatico = {
    "background_image": "linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('/Stars.jpg')",
    "background_size": "cover",
    "background_position": "center",
    "background_repeat": "no-repeat",
    "background_attachment": "fixed", 
    "width": "100%",
}

estilosPricipalPage = {
    "width": "100%",
    "height": "100vh",
    "background_color": "transparent", 
    "align_items": "stretch",
}

estilosExplicationPage = {
    "width": "100%",
    "height": "100vh",
    "padding": "0",
    "align": "center",
    "justify": "center",
}

n = "\n"

def creditos():
    return rx.vstack(
        rx.text("By", color="#ffffff", size="2"),
        rx.icon(tag="star", color="#ffffff", size=15),
        rx.text("Luciano Y.", color="#ffffff", size="2"),
        align="center", 
        spacing="1",
        flex="0.5",
        justify="center"
        )
        
def title():
    return rx.flex(
        rx.heading(
            "Starry Image", 
            color="white",
            font_size=["2.5rem", "4rem", "6rem"],
            font_family="Anton",            
            font_weight="400",    
            text_shadow="0px 0px 20px rgba(255, 255, 255, 0.3)", 
            letter_spacing="0.08em",
            text_align="center",
            ),
        align="center",
        justify="center",
        flex="3",
        width="100%",
        padding_x="1em",
    )

def boton():
    return rx.flex(
        rx.button(
            "Descubre", 
            on_click=rx.redirect("/second"),
            background_color="rgba(255, 255, 255, 0.08)",
            border="1px solid rgba(255, 255, 255, 0.15)",
            backdrop_filter="blur(15px)",
            color="white",
            size="4", 
            radius="full", 
            padding="1.5em 3em",
            width="300px", 
            height="65px",                
            font_size="1.2rem",
            cursor="pointer",
            _hover={
                "background_color": "rgba(255, 255, 255, 0.15)",
                "transform": "translateY(-2px)",
                "box_shadow": "0px 10px 30px rgba(255, 255, 255, 0.2)", # Brillo
            },
            transition="all 0.3s ease-in-out",            
        ),
        align="center",
        justify="center",
        flex="1",
        padding_bottom="3em"
    )

def flechaAbajo():
    return rx.center(
        rx.icon(
            tag="chevron_down", 
            size=40,
            color="#e0e0e0ff", 
            style={
                "filter": "drop-shadow(0px 0px 5px #e0e0e0ff)",
            },
            ),
        align="center",
        justify="center",
        width="100%",
        padding_bottom="2em",
        )

# Segunda Page

def Explication():
    return rx.vstack(
        
        rx.flex(
            rx.heading(
                f"Crónicas del Cosmos: {n} Tu Día Cero", 
                size={
                    "initial": "6",  
                    "sm": "8",
                    "lg": "9"
                },
                font_weight="800",
                line_height="1.2",
                width=["100%", "100%", "40%"],
                text_transform="uppercase",
                letter_spacing="0.05em",
                text_shadow="0px 0px 30px rgba(255, 255, 255, 0.1)",
                text_align=["center", "center", "left"],
                margin=["1em", "1em"],
                margin_bottom=["0", "1em"],
            ),
            
            rx.text(
                "Explora el cosmos a través de tu propia historia. Esta aplicación conecta con los archivos de la NASA para revelar el evento astronómico exacto que capturó el universo el mismo día en que naciste.", 
                size={
                    "initial": "2", 
                    "sm": "3",
                    "lg": "5"
                },
                line_height="1.6",
                width=["100%", "100%", "50%"],
                font_weight="300",
                letter_spacing="0.01em",
                text_align=["center", "center", "left"],
                padding="0.5em",
                margin="0.5em",
            ),
            flex_direction=["column", "column", "row"],
            background_color="rgba(255, 255, 255, 0.06)", 
            backdrop_filter="blur(15px)", 
            border="1px solid rgba(255, 255, 255, 0.15)",
            border_radius="24px",
            width=["90%", "85%", "92%"], 
            justify="center",
            align="center",
            flex="0", 
            margin="0.5em",
        ),
        align="center",
        justify="center",
    )
    
def index() -> rx.Component:
    
    def pricipalPage():
        return rx.vstack(
            creditos(),
            title(),
            boton(),
            flechaAbajo(),
            **estilosPricipalPage
        )
        
    def explicationPage():
        return rx.flex(
            Explication(),
            **estilosExplicationPage
        )
    
    return rx.vstack(
        pricipalPage(), 
        explicationPage(),
        **estilo_fondo_estatico,
        spacing="0",)


app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Anton&display=swap",
    ],)
app.add_page(index, route="/")
app.add_page(SecondPage, route="/second")