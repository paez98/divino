import reflex as rx


def body() -> rx.Component:
    return rx.box(
        rx.center(
            rx.heading(
                'Servicios',
                size='9'
            )
        ),
        color = '#ffff',
        bg = '#2979F3',
        width = '100%'
    )
       