from models.encryption_model import EncryptionModel

class FileController:
    def __init__(self):
        self.model = EncryptionModel()

    def encrypt(self, file_path, password):
        fernet = self.model.generate_key(password)
        self.model.encrypt_file(file_path, fernet)

    def decrypt(self, file_path, password):
        fernet = self.model.generate_key(password)
        self.model.decrypt_file(file_path, fernet)
