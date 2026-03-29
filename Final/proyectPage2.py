import reflex as rx

from .Final import State

estilo_fondo_estatico = {
    "background_image": "linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('/BlurStar.jpg')",
    "background_size": "cover",
    "background_position": "center",
    "background_repeat": "no-repeat",
    "background_attachment": "fixed",
}

estilosSecundPage = {
    "width": "100%",
    "min_height": "100vh", 
    "align": "center",
    "align_items": "center",
    "padding": ["2em 1em", "5%"], 
    "spacing": "7",
}

def title():
    return rx.heading(
        "Introduzca su fecha de nacimiento", 
        color="white", 
        size={
            "initial": "7", 
            "sm": "8",      
            "lg": "9"       
        },
        font_family="Anton",
        font_weight="400",
        letter_spacing="0.08em",
        text_align="center",
        width="100%"
    )

def date_input():
    return rx.input(
        on_change=State.set_fecha_nacimiento,
        placeholder="YYYY-MM-DD",
        width="100%",
        max_width="300px",
        height="55px",
        
        style={
            "background_color": "#FFFFFF14", 
            "border": "1px solid #FFFFFF26", 
            "backdrop_filter": "blur(15px)",
            "border_radius": "9999px",
            "outline": "none !important",
            "transition": "all 0.3s ease-in-out",
            "font_size": "1.2rem",
        },
        
        text_align="center",
        
        _focus={
            "outline": "none !important",
            "border": "1px solid #FFFFFF40", 
            "background_color": "#FFFFFF26", 
            "transform": "translateY(-2px)",
        },
        
        _placeholder={
            "color": "#FFFFFF66",
            "font_size": "1.1rem",
        },
        
        cursor="pointer",
        _hover={
            "background_color": "rgba(255, 255, 255, 0.15)",
            "transform": "translateY(-2px)",
            "box_shadow": "0px 10px 30px rgba(255, 255, 255, 0.2)",
        },
        transition="all 0.3s ease-in-out",    
    )

def image_container():
    return rx.box(
        rx.image(
            src=State.url_nasa, 
            width="100%", 
            height="100%", 
            object_fit="cover",
            border_radius="20px",
        ),
        width=["95%", "80%", "35%"],
        height=["300px", "350px", "400px"], 
        style={
            "background_color": "rgba(255, 255, 255, 0.03)",
            "backdrop_filter": "blur(25px)", 
            "border": "1px solid rgba(255, 255, 255, 0.1)",
            "border_radius": "24px",
            "padding": "1.5em", 
        },
    )
    
def divider():
    return rx.divider(
        style={
            "border_width": "0.5px",
            "border_color": "#FFFFFF73",
            "width": "100%",
            "margin_y": "1em", 
        }
    )
    
def info_container():
    return rx.vstack(
        api_title(),
        divider(),
        rx.scroll_area(
            rx.text(State.info_nasa, color="#E2E8F0", size="3"),
            width="100%",
            height="100%",
        ),
        width=["95%", "80%", "35%"],
        height=["300px", "350px", "400px"],
        style={
            "background_color": "rgba(255, 255, 255, 0.03)",
            "backdrop_filter": "blur(25px)", 
            "border": "1px solid rgba(255, 255, 255, 0.1)",
            "border_radius": "24px",
            "padding": "2em", 
        },
    )
  
def api_title():
    return rx.heading(
        State.titulo_nasa, 
        color="white", 
        size="6",
        font_weight="bold",
        margin_bottom="0.2em",
        width="100%",
        text_align="left"
    )
    
def imgInfoContainer():
    return rx.flex(
        image_container(), 
        info_container(),
        flex_direction=["column", "column", "row"], 
        spacing="5",
        width="100%", 
        justify="center",
        align="center",
        padding_x=["1em", "2em", "0"],
    )


def boton():
    return rx.flex(
        rx.button(
            "Star", 
            on_click=State.obtener_datos,
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

def SecondPage() -> rx.Component:
    return rx.vstack(
        title(),
        date_input(),
        imgInfoContainer(),
        boton(),
        **estilosSecundPage,
        **estilo_fondo_estatico,
        )
