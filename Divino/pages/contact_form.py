import reflex as rx
from Divino.style.style import Size
from Divino.style.style import Size


@rx.page(
    '/contacto',
    title='U.E. Divino Niño | Contacto'
)
def contact_form() -> rx.Component:
    return rx.vstack(
        rx.form.root(
            rx.vstack(
                rx.form.field(
                    rx.vstack(
                        rx.form.label('Nombre'),
                        rx.form.control(
                            rx.input.input(
                                placeholder='Escriba su nombre...'
                            ),
                            as_child=True
                        ),
                        rx.form.label('Telefono'),
                        rx.form.control(
                            rx.input.input(
                                placeholder='Introduzca su numero de telefono...'
                            ),
                            as_child=True
                        ),
                        rx.form.label('Correo'),
                        rx.form.control(
                            rx.input.input(
                                placeholder='Escriba su correo...',
                                type='email',
                            ),
                            as_child=True,

                        ),
                        rx.form.submit(
                            rx.button('Enviar'),
                            as_child=True,
                            margin_top='0.5em'
                        ),
                    ),
                ),
                # spacing='9'
            ),
            border='1px solid',
            border_radius='10px',
            padding = Size.SAMLL.value
        ),
        width = '100%'
    )
