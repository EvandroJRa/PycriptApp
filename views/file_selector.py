from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.boxlayout import BoxLayout

class FileSelector(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        # Código do FileChooser aqui...
