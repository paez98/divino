import reflex as rx


def news() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.heading('Taller Virtual'),
            rx.text('5 de enero-13 de junio de 2024'),
            border='1px solid',
            padding = '0.5em',
            #bg = 'url(descargar.jpg)',
            background = 'center/cover url(descargar.jpg)',
            widht='100%',
            height='100%',
            border_radius = '10px'
            
        ),
        rx.divider(
            #border = '2px solid',
            color_scheme='crimson',
            orientation= 'vertical',
            margin = '0 15',
            width = '0.05em',
            height= '8em'
            ),
        rx.box(
            rx.heading(
                'Feria Vocacional'
            ),
            rx.text(
                'Del 26 al 28 de Febrero del 2024',
            ),
            border='1px solid',
            padding = '0.5em',
            bg = 'rgba(26,144,255,0.84)',
            widht='100%',
            height='100%',
            border_radius = '10px'
        ),
        spacing='9',
        align='center',
        justify='center',
        width = '100%'
        
    )
