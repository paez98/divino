import reflex as rx
from .links import link, link_button, link2
from .icons import icon
from .float_button import floatB
from .logo import logo


def navbar() -> rx.Component:
    return rx.box(
        
    )
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
        #     rx.spacer(),
        #     rx.chakra.button(
        #         link('Inicio', '/', '#ffff'),
        #         variant='ghost'),
        #     rx.menu.root(
        #         rx.menu.trigger(rx.chakra.button(
        #             'Colegio',
        #             icon('icons/chevron-down.svg'),
        #             variant='ghost')),
        #         rx.menu.content(
        #             rx.menu.item(link('Quienes somos', '#', 'black')),
        #             rx.menu.separator(),
        #             rx.menu.item(link('Instalaciones', '#', 'black'))
        #         )
        #     ),
        #     rx.menu.root(
        #         rx.menu.trigger(
        #             rx.chakra.button(
        #                 'Servicios',
        #                 icon('icons/chevron-down.svg'),
        #                 variant='ghost'
        #             ),
        #         ),
        #         rx.menu.content(
        #             rx.menu.item(
        #                 link2('Preescolar', '#'),
        #                 _hover={
        #                     'text_color': '#ffff',
        #                     'color': '#ffff'
        #                 }
        #             ),
        #             rx.menu.separator(),
        #             rx.menu.item(
        #                 link2('Primaria', '#')
        #             ),
        #             rx.menu.separator(),
        #             rx.menu.item(
        #                 link2('Media general', '#'),
        #             ),
        #             _hover={
        #                 'text_color': ''
        #             }
        #         ),
        #     ),
        #     rx.chakra.button(
        #         link('Admision', '#', '#ffff'),
        #         variant='ghost'
        #     ),
        #     rx.chakra.button(
        #         link('Contacto', '#', '#ffff'),
        #         variant='ghost'
        #     ),
        #     rx.spacer(),
        #     align_items='center'
        # ),
        # floatB(),
        # bg="#2979F3")
