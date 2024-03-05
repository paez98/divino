import reflex as rx 


class FloatButton(rx.Component):
    library = 'antd'
    tag = 'FloatButton.BackTop'
    visibilityHeight = '0'
    fontSizeSM = 12,
    fontSizeIcon = 12,
    controlItemBgHover = 'rgba(120,440, 0, 0.4)'
    badge = {
        'dot':'true'
    }
    
    
floatB = FloatButton.create