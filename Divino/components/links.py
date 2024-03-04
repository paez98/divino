import reflex as rx


def link(text: str, url: str, color: str) -> rx.Component:
    return rx.link(
        text,
        href=url,
        color=color,
        _hover={'text_decoration': 'None',
                'color': '#ffff'}
    )


def link2(text: str, url: str) -> rx.Component:
    return rx.link(
        text,
        href=url,
        _hover={
            'text_decoration': 'None',
            'color':'#ffff'
        }
    )


def link_button(text: str, url: str,  var: str) -> rx.Component:
    return rx.link(
        rx.button(text, variant=var),
        href=url,
    )
