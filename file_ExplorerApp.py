import os
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner  # Para seleção de discos
from kivy.app import App


class FileExplorerApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10, **kwargs)

        # Define a pasta raiz do sistema operacional
        self.root_path = self.get_root_path()

        # Layout para exibir o caminho atual
        self.path_box = BoxLayout(
            orientation='horizontal',
            size_hint=(1, None),
            height=50,
            padding=5,
            spacing=5
        )
        self.add_widget(self.path_box)

        # Fundo para o caminho atual (background)
        self.current_path_display = Label(
            text=self.root_path,
            size_hint=(0.8, 1),
            color=(1, 1, 1, 1),  # Cor do texto
            bold=True
        )
        self._create_background_instruction(self.current_path_display, "#444444")
        self.path_box.add_widget(self.current_path_display)
        
        # Spinner para seleção de discos
        self.disk_selector = Spinner(
            text="Selecionar Disco",
            values=self.get_available_drives(),
            size_hint=(0.2, 1)
        )
        self.disk_selector.bind(text=self.change_drive)
        self.path_box.add_widget(self.disk_selector)

        # FileChooser para seleção de arquivos/pastas
        self.file_chooser = FileChooserIconView(
            path=self.root_path,
            show_hidden=True,
            size_hint=(1, 0.7),
            dirselect=False,
            multiselect=True
        )
        self.file_chooser.bind(path=self.update_current_path)
        self.add_widget(self.file_chooser)

        # Botão para alternar entre modos
        self.toggle_mode_button = Button(
            text="Modo: Seleção de Arquivos",
            size_hint=(1, None),
            height=50
        )
        self.toggle_mode_button.bind(on_press=self.toggle_mode)
        self.add_widget(self.toggle_mode_button)

        # Campo de entrada para senha
        self.add_widget(Label(text="Senha:", size_hint=(1, None), height=30))
        self.password_input = TextInput(password=True, multiline=False, size_hint=(1, None), height=40)
        self.add_widget(self.password_input)

        # Botões para criptografar e descriptografar
        self.encrypt_button = Button(text="Criptografar Seleção", size_hint=(1, None), height=50)
        self.encrypt_button.bind(on_press=self.encrypt_selection)
        self.add_widget(self.encrypt_button)

        self.decrypt_button = Button(text="Descriptografar Seleção", size_hint=(1, None), height=50)
        self.decrypt_button.bind(on_press=self.decrypt_selection)
        self.add_widget(self.decrypt_button)

    def _create_background_instruction(self, widget, color_hex):
        """
        Adiciona uma cor de fundo ao widget.
        """
        from kivy.graphics import Color, Rectangle
        from kivy.utils import get_color_from_hex

        color = get_color_from_hex(color_hex)

        with widget.canvas.before:
            bg_color = Color(*color)  # Define a cor
            bg_rect = Rectangle(size=widget.size, pos=widget.pos)

        # Atualiza o tamanho e a posição dinamicamente
        widget.bind(size=lambda instance, value: setattr(bg_rect, 'size', value),
                    pos=lambda instance, value: setattr(bg_rect, 'pos', value))

    def get_root_path(self):
        """
        Retorna a pasta raiz do sistema operacional.
        """
        if os.name == 'nt':  # Windows
            return "C:/"
        else:  # Linux/Mac
            return "/"

    def get_available_drives(self):
        """
        Retorna os discos disponíveis no sistema.
        """
        if os.name == 'nt':  # Windows
            import string
            from ctypes import windll
            drives = []
            bitmask = windll.kernel32.GetLogicalDrives()
            for letter in string.ascii_uppercase:
                if bitmask & 1:
                    drives.append(f"{letter}:/")
                bitmask >>= 1
            return drives
        else:  # Linux/Mac
            return ["/"]

    def change_drive(self, spinner, text):
        """
        Altera o drive atual no FileChooser.
        """
        if os.path.exists(text):
            self.file_chooser.path = text
            self.update_current_path(None)

    def update_current_path(self, instance, value=None):
        """
        Atualiza o campo exibindo o caminho atual.
        """
        current_path = self.file_chooser.path
        print(f"Atualizando caminho no display: {current_path}")  # Depuração
        self.current_path_display.text = current_path

    def toggle_mode(self, instance):
        """
        Alterna entre seleção de arquivos ou pastas.
        """
        if self.file_chooser.dirselect:
            self.file_chooser.dirselect = False
            self.toggle_mode_button.text = "Modo: Seleção de Arquivos"
        else:
            self.file_chooser.dirselect = True
            self.toggle_mode_button.text = "Modo: Seleção de Pastas"

    def encrypt_selection(self, instance):
        """
        Exibe mensagem fictícia para criptografia.
        """
        selected_files = self.file_chooser.selection
        if not selected_files:
            self.show_popup("Erro", "Nenhum arquivo ou pasta selecionada!")
            return
        self.show_popup("Ação", f"Criptografando seleção: {selected_files}")

    def decrypt_selection(self, instance):
        """
        Exibe mensagem fictícia para descriptografia.
        """
        selected_files = self.file_chooser.selection
        if not selected_files:
            self.show_popup("Erro", "Nenhum arquivo ou pasta selecionada!")
            return
        self.show_popup("Ação", f"Descriptografando seleção: {selected_files}")

    def show_popup(self, title, message):
        """
        Exibe um popup com título e mensagem.
        """
        popup = Popup(
            title=title,
            content=Label(text=message),
            size_hint=(0.8, 0.4)
        )
        popup.open()


class MyApp(App):
    def build(self):
        return FileExplorerApp()


if __name__ == "__main__":
    MyApp().run()
