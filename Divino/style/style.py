import reflex as rx
from enum import Enum
from .fonts import Font

# General sizes
class Size(Enum):
    SAMLL = '0.5em'
    MID = '0.8em'
    NORMAL = '1em'
    BIG = '1.5em'
    

# STYLES

BASESTYLE= {
    'font_family': Font.DEFAULT.value
}


# STYLESHEETS = [
#     'https://fonts.googleapis.com/css2?family=Madimi+One&display=swap',
#     'https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap'
# ]

title_logo_style =dict(
    font_family = Font.LOGO.value
)

