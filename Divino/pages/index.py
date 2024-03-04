import reflex as rx
from Divino.components.navbar import navbar
from Divino.views.body import body
from Divino.views.services import services
from Divino.sections.about import about
from Divino.sections.news import news
from Divino.sections.events import events
from Divino.components.logo import logo

@rx.page(
    "/",
    title='U.E. Divino Niño'
)
def index() -> rx.Component:
    return rx.box(
        logo(),
        navbar(),
        rx.vstack(
            about(),
            news(),
            rx.divider(color_scheme='crimson'),
            events(),
            body(),
            services()
        )
    )
