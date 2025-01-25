from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from controllers.file_controller import FileController

class ViewManager(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.controller = FileController()  # Instância do controlador

        # Campo de entrada para senha
        self.add_widget(Label(text="Senha para criptografia:"))
        self.password_input = TextInput(password=True, multiline=False)
        self.add_widget(self.password_input)

        # FileChooser para seleção de arquivos
        self.file_chooser = FileChooserIconView(filters=["*.*"])
        self.add_widget(self.file_chooser)

        # Botão para criptografar
        self.encrypt_button = Button(text="Criptografar Arquivo")
        self.encrypt_button.bind(on_press=self.encrypt_file)
        self.add_widget(self.encrypt_button)

        # Botão para descriptografar
        self.decrypt_button = Button(text="Descriptografar Arquivo")
        self.decrypt_button.bind(on_press=self.decrypt_file)
        self.add_widget(self.decrypt_button)

        # Mensagem de status
        self.status_label = Label(text="Status: Aguarde...")
        self.add_widget(self.status_label)

    def encrypt_file(self, instance):
        selected_files = self.file_chooser.selection
        password = self.password_input.text
        print(f"Arquivos selecionados: {selected_files}")
        print(f"Senha fornecida: {password}")
        if not selected_files:
            self.status_label.text = "Erro: Nenhum arquivo selecionado!"
            return
        if not password:
            self.status_label.text = "Erro: Digite uma senha!"
            return
        try:
            self.controller.encrypt(selected_files[0], password)
            self.status_label.text = "Arquivo criptografado com sucesso!"
        except Exception as e:
            self.status_label.text = f"Erro ao criptografar: {e}"

    def decrypt_file(self, instance):
        selected_files = self.file_chooser.selection
        password = self.password_input.text
        print(f"Arquivos selecionados: {selected_files}")
        print(f"Senha fornecida: {password}")
        if not selected_files:
            self.status_label.text = "Erro: Nenhum arquivo selecionado!"
            return
        if not password:
            self.status_label.text = "Erro: Digite uma senha!"
            return
        try:
            self.controller.decrypt(selected_files[0], password)
            self.status_label.text = "Arquivo descriptografado com sucesso!"
        except Exception as e:
            self.status_label.text = f"Erro ao descriptografar: {e}"
