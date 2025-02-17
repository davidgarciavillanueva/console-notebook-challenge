# TODO: Agrega el código de las clases del modelo aquí. Borra este comentario al terminar.
from datetime import datetime


class Note:
    HIGH: str = "HIGH"
    MEDIUM: str = "MEDIUM"
    LOW: str = "LOW"


    def __init__(self,code:str,title: str, text :str,importance :str,creation_date :datetime,tags :list[str] ):
        self.code = code
        self.title = title
        self.text = text
        self.importance = importance
        self.tags :list[str] = tags

    def add_tag(self,tag:str):
        if tag not in self.tags:
            self.tags.append(tag)
        else:
            print(f"ya exite la etiqueta {tag}")


    def __str__(self):
        Date: {creation_date}
        {title}: {text: }
        pass

class Notebook:
    def __init__(self,notes :list[Note] ):
        self.notes :list[Note] = []
