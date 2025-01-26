import os
import base64
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.primitives.hmac import HMAC
from cryptography.hazmat.primitives.kdf.concatkdf import ConcatKDFHash
from os import urandom


class FileController:
    ENCRYPTION_SIGNATURE = b"ENCRYPTED"

    def __init__(self):
        print("Inicializando FileController...")

    def derive_key(self, password: str, salt: bytes, length=32) -> bytes:
        """
        Deriva uma chave criptográfica a partir de uma senha e um salt.
        """
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=length,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        return kdf.derive(password.encode())

    def encrypt(self, file_path: str, password: str):
        """
        Criptografa um arquivo e o salva com a extensão .enc.
        """
        try:
            # Gera o salt e IV
            salt = os.urandom(16)
            iv = os.urandom(16)

            # Deriva a chave de criptografia
            key = self.derive_key(password, salt)

            # Lê o conteúdo do arquivo
            with open(file_path, 'rb') as f:
                plaintext = f.read()

            # Criptografa o conteúdo
            cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
            encryptor = cipher.encryptor()
            ciphertext = encryptor.update(plaintext) + encryptor.finalize()

            # Cria o arquivo criptografado
            encrypted_path = f"{file_path}.enc"
            with open(encrypted_path, 'wb') as f:
                f.write(self.ENCRYPTION_SIGNATURE + salt + iv + ciphertext)

            print(f"Arquivo '{file_path}' criptografado como '{encrypted_path}'.")

            # Remove o arquivo original
            os.remove(file_path)
            print(f"Arquivo original '{file_path}' excluído.")

        except Exception as e:
            print(f"Erro ao criptografar: {e}")
            raise

    def decrypt(self, file_path: str, password: str):
        """
        Descriptografa um arquivo criptografado e o restaura ao estado original.
        """
        try:
            # Lê o conteúdo do arquivo criptografado
            with open(file_path, 'rb') as f:
                data = f.read()

            # Verifica a assinatura
            if not data.startswith(self.ENCRYPTION_SIGNATURE):
                raise Exception(f"O arquivo '{file_path}' não está criptografado!")

            # Extrai salt, IV e ciphertext
            salt = data[len(self.ENCRYPTION_SIGNATURE):len(self.ENCRYPTION_SIGNATURE) + 16]
            iv = data[len(self.ENCRYPTION_SIGNATURE) + 16:len(self.ENCRYPTION_SIGNATURE) + 32]
            ciphertext = data[len(self.ENCRYPTION_SIGNATURE) + 32:]

            # Deriva a chave de descriptografia
            key = self.derive_key(password, salt)

            # Descriptografa o conteúdo
            cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
            decryptor = cipher.decryptor()
            plaintext = decryptor.update(ciphertext) + decryptor.finalize()

            # Cria o arquivo descriptografado
            decrypted_path = file_path.replace(".enc", "")
            with open(decrypted_path, 'wb') as f:
                f.write(plaintext)

            print(f"Arquivo '{file_path}' descriptografado como '{decrypted_path}'.")

            # Remove o arquivo criptografado
            os.remove(file_path)
            print(f"Arquivo criptografado '{file_path}' excluído.")

        except Exception as e:
            print(f"Erro ao descriptografar: {e}")
            raise
