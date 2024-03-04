from rxconfig import config
import reflex as rx
from .pages.index import index
from .pages.contact_form import contact_form
from .components.logo import logo
from .style.style import BASESTYLE

# docs_url = "https://reflex.dev/docs/getting-started/introduction"
# filename = f"{config.app_name}/{config.app_name}.py"




app = rx.App(
    style= BASESTYLE
)

