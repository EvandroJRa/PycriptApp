from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from controllers.file_controller import FileController


class ViewManager(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.padding = 20  # Espaçamento interno
        self.spacing = 10  # Espaçamento entre widgets

        self.controller = FileController()

        # Campo de entrada para senha
        self.add_widget(Label(text="Senha para criptografia:", size_hint=(1, None), height=30))
        self.password_input = TextInput(password=True, multiline=False, size_hint=(1, None), height=40)
        self.add_widget(self.password_input)

        # FileChooser para seleção de arquivos
        self.file_chooser = FileChooserIconView(filters=["*.*"], size_hint=(1, 0.6))
        self.add_widget(self.file_chooser)

        # Botão para criptografar
        self.encrypt_button = Button(text="Criptografar Arquivo", size_hint=(1, None), height=50)
        self.encrypt_button.bind(on_press=self.encrypt_file)
        self.add_widget(self.encrypt_button)

        # Botão para descriptografar
        self.decrypt_button = Button(text="Descriptografar Arquivo", size_hint=(1, None), height=50)
        self.decrypt_button.bind(on_press=self.decrypt_file)
        self.add_widget(self.decrypt_button)

    def show_popup(self, title, message):
        popup = Popup(
            title=title,
            content=Label(text=message),
            size_hint=(0.8, 0.4)
        )
        popup.open()

    def encrypt_file(self, instance):
        selected_files = self.file_chooser.selection
        password = self.password_input.text
        if not selected_files:
            self.show_popup("Erro", "Nenhum arquivo selecionado!")
            return
        if not password:
            self.show_popup("Erro", "Digite uma senha para criptografar!")
            return
        try:
            self.controller.encrypt(selected_files[0], password)
            self.show_popup("Sucesso", "Arquivo criptografado com sucesso!")
        except Exception as e:
            self.show_popup("Erro", f"Erro ao criptografar: {e}")

    def decrypt_file(self, instance):
        selected_files = self.file_chooser.selection
        password = self.password_input.text
        if not selected_files:
            self.show_popup("Erro", "Nenhum arquivo selecionado!")
            return
        if not password:
            self.show_popup("Erro", "Digite uma senha para descriptografar!")
            return
        try:
            self.controller.decrypt(selected_files[0], password)
            self.show_popup("Sucesso", "Arquivo descriptografado com sucesso!")
        except Exception as e:
            self.show_popup("Erro", f"Erro ao descriptografar: {e}")
