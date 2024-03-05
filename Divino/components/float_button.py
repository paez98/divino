import reflex as rx
from .icons import icon

class FloatButton(rx.Component):
    library = 'antd'
    tag = 'FloatButton.BackTop'
    visibilityHeight = '0'
    fontSizeSM = 12,
    fontSizeIcon = 12,
    _hover = {
        'color':'rgba(120,440, 0, 0.4)',
        'background-color':'rgba(120,440, 0, 0.4)'
    }
    badge = {
        'dot': 'true'
    }


floatB = FloatButton.create

def float_button()-> rx.Component:
    return rx.box(
        rx.link(
            rx.button(
                icon('icons/chevron-up-solid.svg')
            )
        )
    )