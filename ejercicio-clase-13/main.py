from textual.app import App
from screens import HomeScreen




# class CommandMenuApp(App, Events, BlockYield):
#     CSS = """
#     Screen { align: center middle; }
#     Button { margin: 1; width: 40% }
#     Input.-valid {
#         border: tall $success 60%;
#     }
#     Input.-valid:focus {
#         border: tall $success;
#     }
#     Input {
#         margin: 1 1;
#     }
#     Label {
#         margin: 1 2;
#     }
#     Pretty {
#         margin: 1 2;
#     }    
#     """

#     def compose(self):
#         yield Header("Menú de Comandos")
#         yield Label("Selecciona una opción:")
#         yield Button(
#             **{"label": "Cargar Archivo", "variant": "success"}, cb=self.open_file
#         )
#         yield Button(**{"label": "Salir", "variant": "error"}, cb=self.exit)
#         yield from Input().compose()
    
#         # yield Button("1. Cargar Archivo", id="cargar", variant="primary")
#         # yield Button("2. Opción 2", id="opcion2")
#         # yield Button("3. Salir", id="salir", variant="error")

# self.app.push_screen(CargarScreen())


class CommandMenuApp(App):
    CSS_PATH = "style.tcss" 

    CSS = """
    Screen { align: center top; }
    Button { margin: 1; width: 40% }
    Input.-valid {
        border: tall $success 60%;
    }
    Input.-valid:focus {
        border: tall $success;
    }
    Input {
        margin: 1 1;
    }
    Label {
        margin: 1 2;
    }
    Pretty {
        margin: 1 2;
    }    

    """    
    def on_mount(self):
        self.push_screen(HomeScreen())   

if __name__ == "__main__":
    pass
    app = CommandMenuApp()
    app.run()
