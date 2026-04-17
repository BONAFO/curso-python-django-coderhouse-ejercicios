import json


class Events:
    def open_file(self,filename):
        try:
            with open(f"{filename}.json", "r") as file:
                return json.load(file)
        except ValueError:
            self.app.notify("Archivo Invalido", severity="error")
        except FileNotFoundError:
            self.app.notify("Archivo No encontrado", severity="error")
        except Exception as error:
            error = str(error)
            self.app.notify(f"Error: {error}", severity="error")

    def exit(self):
        self.app.exit()


