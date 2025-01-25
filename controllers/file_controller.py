import hashlib
from cryptography.fernet import Fernet

class FileController:
    def generate_key(self, password):
        """
        Gera uma chave Fernet baseada em uma senha usando SHA-256.
        """
        key = hashlib.sha256(password.encode()).digest()
        return Fernet(key)

    def encrypt(self, file_path, password):
        """
        Criptografa um arquivo com base em uma senha.
        """
        try:
            fernet = self.generate_key(password)
            with open(file_path, "rb") as file:
                data = file.read()
            encrypted_data = fernet.encrypt(data)
            with open(file_path, "wb") as file:
                file.write(encrypted_data)
            print(f"Arquivo '{file_path}' criptografado com sucesso!")
        except Exception as e:
            print(f"Erro ao criptografar o arquivo: {e}")

    def decrypt(self, file_path, password):
        """
        Descriptografa um arquivo com base em uma senha.
        """
        try:
            fernet = self.generate_key(password)
            with open(file_path, "rb") as file:
                encrypted_data = file.read()
            data = fernet.decrypt(encrypted_data)
            with open(file_path, "wb") as file:
                file.write(data)
            print(f"Arquivo '{file_path}' descriptografado com sucesso!")
        except Exception as e:
            print(f"Erro ao descriptografar o arquivo: {e}")
