import reflex as rx


def services() -> rx.Component:
    return rx.hstack(
        rx.center(
            rx.box(
                rx.center(
                    rx.vstack(
                    rx.heading('Preescolar'),
                    rx.image(src='descargar.jpg'),
                    direction='column'
                    )
                ),
                rx.vstack(
                    rx.divider(),
                    rx.text(
                        '''rem Ipsum is simply dummy text of the printing and typesetting industry.
                        Lorem Ipsum has been the industrys standard dummy text ever since the 1500s,
                        when an unknown printer took a galley of type and scrambled it to make a type specimen book''',
                    ),
                ),
                border='1px solid',
                padding='10px',
                margin_left = '15px',
                background_image = "linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)"
                # width = '600px'
            ),
            rx.spacer(),
            rx.box(
                rx.center(
                    rx.vstack(
                    rx.heading('Primaria'),
                    rx.image(src='logo.png'),
                    direction='column'
                    )
                ),
                rx.vstack(
                    rx.divider(),
                    rx.text(
                        '''rem Ipsum is simply dummy text of the printing and typesetting industry.
                        Lorem Ipsum has been the industrys standard dummy text ever since the 1500s,
                        when an unknown printer took a galley of type and scrambled it to make a type specimen book'''
                    )
                ),
                border='1px solid',
                padding='10px',
                #margin_X='15px'
                # width = '600px'
                background = "linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)"
            ),
            rx.spacer(),
            rx.box(
                rx.center(
                    rx.vstack(
                    rx.heading('Media general'),
                    rx.image(src='logo.png'),
                    direction='column'
                    )
                ),
                rx.vstack(
                    rx.divider(),
                    rx.text('''
                            lorem Ipsum is simply dummy text of the printing and typesetting industry.
                            Lorem Ipsum has been the industrys standard dummy text ever since the 1500s,
                            when an unknown printer took a galley of type and scrambled it to make a type specimen book
                            ''')
                ),
                border='1px solid',
                padding='10px',
                margin_right='15px',
                background = "linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)"
                # widht ='600px'
            ),
            spacing='2'
        ),
        width='100%',

    )
