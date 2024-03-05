import reflex as rx
from Divino.style.style import Size
from Divino.style.style import BASESTYLE, title_logo_style
from Divino.style.fonts import Font


@rx.page('/logo')
def logo() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.image(
                src='/logo.png'
            ),
            rx.divider(
                orientation='vertical',
                size='4',
                height='150px',
                border='1px solid',
                margin=Size.SAMLL.value
            ),
            rx.vstack(
                rx.heading(
                    'Unidad Educativa Divino Niño',
                    size= '7',
                    style= {
                        'font_family': Font.LOGO.value
                    }
                ),
                rx.text('38 Años Camino a la Excelencia en la Educación',
                        size='4',
                        font_family= Font.LOGO.value),
                align='start',
                justify='center',
                spacing='0'
            ),
            align='center',
            justify='center',
            margin_top=Size.NORMAL.value
            # border='1px solid '
        ),
        # style= title_logo_style
    )
