import reflex as rx


def about() -> rx.Component:
    return rx.hstack(
        rx.spacer(),
        rx.box(
            rx.text(
                '''
              En Divino Niño queremos que nuestros estudiantes hagan preguntas profundas,
              exploren las fronteras disciplinarias y confronten las ideas convencionales del pensamiento.
              Explore nuestro sitio web y conozca todo lo que tenemos para ofrecer.
              ''',
                width='40em'
            ),
            border='1px solid',
            width='auto%',
            height='100%'
        ),
        rx.spacer(),
        rx.box(
            rx.image(src='logo.png'),
            border='1px solid'
        ),
        rx.spacer(),
        width='100%',
        align='center',
        justify='center'
    )
