import reflex as rx
from .links import link, link_button, link2
from .icons import icon
from .float_button import floatB
from .logo import logo
from Divino.style.style import Size


def navbar() -> rx.Component:
    return rx.box(
        floatB(),
        rx.hstack(
            rx.chakra.button(
                link('Inicio', '/', '#ffff'),
                variant='ghost'
            ),
            rx.menu.root(
                rx.menu.trigger(rx.chakra.button(
                    'Colegio',
                    icon('icons/chevron-down.svg'),
                    variant='ghost')),
                rx.menu.content(
                    rx.menu.item(link2('Quienes somos', '#')),
                    rx.menu.separator(),
                    rx.menu.item(link2('Instalaciones', '#'))
                )
            ),
            rx.menu.root(
                rx.menu.trigger(
                    rx.chakra.button(
                        'Servicios',
                        icon('icons/chevron-down.svg'),
                        variant='ghost'
                    ),
                ),
                rx.menu.content(
                    rx.menu.item(
                        link2('Preescolar', '#'),
                        _hover={
                            'text_color': '#ffff',
                            'color': '#ffff'
                        }
                    ),
                    rx.menu.separator(),
                    rx.menu.item(
                        link2('Primaria', '#')
                    ),
                    rx.menu.separator(),
                    rx.menu.item(
                        link2('Media general', '#'),
                    ),
                    _hover={
                        'text_color': ''
                    }
                ),
            ),
            rx.chakra.button(
                link('Admision', '#', '#ffff'),
                variant='ghost'
            ),
            rx.chakra.button(
                link('Contacto', '#', '#ffff'),
                variant='ghost',
                style={
                    'opacity': 1
                }
            ),
            width='100%',
            background='rgb(59 130 246 / 1)',
            justify='center',
            margin_top=Size.SAMLL.value,

        ),
        position='sticky',
        z_index='999',
        top='0',
    )

    #
    #
    #     rx.spacer(),
    #     align_items='center'
    # ),

    # )
