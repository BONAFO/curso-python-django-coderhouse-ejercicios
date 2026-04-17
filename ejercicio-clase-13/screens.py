from textual import on
from events import Events
from textual.widgets import Header, Label, Input, Button, DataTable
from textual.screen import Screen
from textual.containers import Center


filename = ""


class ScreenChangers:
    def show_home_screen(self):
        self.app.push_screen(HomeScreen())

    def show_open_file_screen(self):
        self.app.push_screen(OpenFileSceen())


    def show_open_file_mod_screen(self):
        self.app.push_screen(OpenFileSceenWrite())

    def show_file_info_screen(self):
        self.app.push_screen(ShowFileInfo(self.filename))
        
    def show_mod_file_screen(self):
        return ""
        self.app.push_screen(ShowFileInfo(self.filename))



class AddDataFile(Screen, ScreenChangers, Events):

    def __init__(self, filename: str):
        self.filename = filename
        super().__init__()

    def compose(self):
        # data = self.open_file(self.filename)
        # Tabla = DataTable()
        # Tabla.add_columns(*[key.capitalize() for key in data[0].keys()])   
        # rows = [list(item.values()) for item in data]
        # Tabla.add_rows(rows)
        # yield Tabla


        with Center():
            yield Button(label="Volver", variant="error", id="back", classes= "input-button")
            yield Button(label="Salir", variant="error", id="exit", classes= "input-button")

    @on(Button.Pressed, "#exit")
    def handle_exit(self):
        self.exit()

    @on(Button.Pressed, "#back")
    def handle_exit(self):
        self.show_home_screen()




class ShowFileInfo(Screen, ScreenChangers, Events):

    def __init__(self, filename: str):
        self.filename = filename
        super().__init__()

    def compose(self):
        data = self.open_file(self.filename)
        Tabla = DataTable()
        Tabla.add_columns(*[key.capitalize() for key in data[0].keys()])   
        rows = [list(item.values()) for item in data]
        Tabla.add_rows(rows)
        yield Tabla

        with Center():
            yield Button(label="Volver", variant="error", id="back", classes= "input-button")
            yield Button(label="Salir", variant="error", id="exit", classes= "input-button")

    @on(Button.Pressed, "#exit")
    def handle_exit(self):
        self.exit()

    @on(Button.Pressed, "#back")
    def handle_exit(self):
        self.show_home_screen()



class OpenFileSceen(Screen, ScreenChangers, Events):

    filename: str

    def compose(self):
        yield Header("Menú de Comandos")
        yield Label("Nombre del Archivo: ")
        yield Input(id="filename")
        
        with Center():
            yield Button(label="Buscar", variant="success", id="search", classes= "input-button")
            yield Button(label="Salir", variant="error", id="exit", classes= "input-button")


    @on(Button.Pressed, "#exit")
    def handle_exit(self):
        self.exit()

    @on(Button.Pressed, "#search")
    def handle_showfile(self):
        self.show_file_info_screen()

    @on(Input.Changed, "#filename")
    def input_changed(self, event):
        self.filename = event.value


class OpenFileSceenWrite(OpenFileSceen):

    @on(Button.Pressed, "#search")
    def handle_showfile(self):
        self.show_mod_file_screen()



class HomeScreen(Screen, ScreenChangers, Events):
    def compose(self):
        yield Header("Menú de Comandos")
        yield Label("Selecciona una opción:")
        yield Button(label="Cargar Archivo", variant="success", id="openfile")
        yield Button(label="Modificar Archivo", variant="success", id="modfile")
        yield Button(label="Salir", variant="error", id="exit")

    @on(Button.Pressed, "#exit")
    def handle_exit(self):
        self.exit()

    @on(Button.Pressed, "#openfile")
    def handle_openfile(self):
        self.show_open_file_screen()

    @on(Button.Pressed, "#modfile")
    def handle_modfile(self):
        self.show_open_file_mod_screen()
