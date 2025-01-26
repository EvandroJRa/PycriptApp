PyCryptApp

Um aplicativo de interface gráfica desenvolvido em Python com Kivy para criptografar e descriptografar arquivos e pastas de forma simples e intuitiva. 
O aplicativo oferece segurança na manipulação de arquivos ao utilizar criptografia AES com chaves derivadas de senhas fornecidas pelo usuário.

Funcionalidades

Criptografar Arquivos e Pastas:
Criptografa arquivos ou pastas inteiras, salvando-os com a extensão .enc.
Remove automaticamente os arquivos originais após a criptografia.
Descriptografar Arquivos:

Restaura arquivos criptografados ao estado original, removendo os arquivos .enc após a descriptografia.
Interface Gráfica:

Exibição de arquivos e pastas disponíveis no diretório atual.
Permite navegação entre unidades de disco e diretórios.
Indica o caminho atual de forma destacada para facilitar a navegação.
Validação:

Impede a criptografia de arquivos já criptografados.
Exibe mensagens de erro e sucesso em pop-ups.
Atualização Automática:

Atualiza a lista de arquivos e pastas após operações de criptografia ou descriptografia.

Pré-requisitos

Certifique-se de ter o Python 3.7 ou superior instalado. Além disso, instale as dependências necessárias usando o pip:

Tecnologias Utilizadas

Python 3: Linguagem de programação principal.
Kivy: Framework para desenvolvimento de interfaces gráficas.
Cryptography: Biblioteca para implementação de criptografia AES.
OS Module: Manipulação de arquivos e diretórios.

Como Funciona a Criptografia

O aplicativo utiliza AES (Advanced Encryption Standard) no modo CFB.
Uma senha fornecida pelo usuário é utilizada para derivar uma chave criptográfica segura por meio do algoritmo PBKDF2.
Arquivos criptografados possuem a extensão .enc e incluem uma assinatura para validação.

Contribuindo

Contribuições são bem-vindas! Para colaborar:

1-Faça um fork do repositório.

2-Crie uma branch para sua feature
  git checkout -b minha-feature
  
3-Faça o commit de suas alterações
  git commit -m 'Adiciona nova funcionalidade'
  
4-Envie para sua branch
  git push origin minha-feature
  
5-Abra um Pull Request.

Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

Autor

Evandro J. Ramos,
Análise e Desenvolvimento de Sistemas.

