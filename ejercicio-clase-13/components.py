from textual.app import App, ComposeResult
from textual.widgets import Button as Btn, Header, Label, Input as Inp, Pretty 
from textual.screen import Screen
from textual import on
from events import Events


class Button(Btn):
    """
    label: str
    Texto mostrado en el botón

    name: str
    Nombre interno del botón.

    id: str
    Identificador único.

    classes: str
    Clases CSS aplicadas.

    disabled: bool
    Indica si el botón está deshabilitado.

    flat: bool
    Si es True, el botón no tendrá sombra.
    """

    def __init__(self, cb=lambda: None, *args, **kwargs):
        self.cb = cb
        super().__init__(**kwargs)

    def on_click(self):
        self.cb()



    
class Input(Events):

    def __init__(self):
        self.value = ""  # Valor inicial

    def compose(self, input_id , label_text=""):
        yield Label(label_text)
        yield Inp(id=input_id) 

        
    def on_input_changed(self, event):
        if event.input.id == self.input_id:
            self.value = event.value 