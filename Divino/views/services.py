import reflex as rx
from Divino.components.preescolar import preescolar
from Divino.components.primaria import primaria
from Divino.components.media_general import media_general


def services() -> rx.Component:
    return rx.hstack(
        preescolar(),
        primaria(),
        media_general(),
        justify='center',
        align='center',
        width= '100%'
    )
