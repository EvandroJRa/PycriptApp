from cryptography.fernet import Fernet

class EncryptionModel:
    @staticmethod
    def generate_key(password: str) -> Fernet:
        """Gera uma chave de criptografia com base na senha."""
        key = Fernet.generate_key()
        return Fernet(key)

    @staticmethod
    def encrypt_file(file_path: str, fernet: Fernet):
        """Criptografa um arquivo."""
        with open(file_path, "rb") as file:
            data = file.read()
        encrypted_data = fernet.encrypt(data)
        with open(file_path, "wb") as file:
            file.write(encrypted_data)

    @staticmethod
    def decrypt_file(file_path: str, fernet: Fernet):
        """Descriptografa um arquivo."""
        with open(file_path, "rb") as file:
            encrypted_data = file.read()
        data = fernet.decrypt(encrypted_data)
        with open(file_path, "wb") as file:
            file.write(data)
