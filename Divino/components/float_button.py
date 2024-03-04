import reflex as rx 


class FloatButton(rx.Component):
    library = 'antd'
    tag = 'FloatButton.BackTop'
    visibilityHeight = '0'
    fontSizeSM = 12
    badge = {
        'dot':'true'
    }
    
    
floatB = FloatButton.create