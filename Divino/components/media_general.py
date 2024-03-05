import reflex as rx
from Divino.style.style import Size


def media_general() -> rx.Component:
    return rx.box(
        rx.heading(
            'Media General',
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
                    '''
                    Forjando bachilleres con alas para volar alto,
                    corazones llenos de valores y mentes preparadas para conquistar el futuro.
                    ''',
                    size='5',
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
