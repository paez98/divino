import reflex as rx
from Divino.style.style import Size




# Seccion de preescolar
def preescolar() -> rx.Component:
    return rx.box(
        rx.heading(
            'Preescolar',
            align='center',
            justify='center'
        ),
        rx.center(
            rx.vstack(
                rx.image(
                    src='preescolar.jpg',
                    align='center',
                    height='20em',
                    width='100%',
                    border_radius='4%'
                ),
                rx.divider(),
                rx.text(
                    'U.E  Divino Niño. Brindándole a tu pequeño las herramientas para un futuro brillante.',
                    width='22em',
                    padding_x=Size.MID.value,
                    margin_bottom = Size.MID.value
                ),
                direction='column',
                border='1px solid',
                border_radius='4%',
                margin_top=Size.SAMLL.value
            )
        ),
        margin_left=Size.SAMLL.value
    )



