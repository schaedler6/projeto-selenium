# Relatório de Teste

## Caso de teste: TC-001 - Login Bem-Sucedido

### Objetivo:
Validar que um usuário com credenciais corretas consegue realizar o login com sucesso no site [saucedemo.com](https://www.saucedemo.com/).

### Passos Executados:
1. Acessar o site [https://www.saucedemo.com/](https://www.saucedemo.com/).
2. Preencher o campo de usuário com standard_user.
3. Preencher o campo de senha com secret_sauce.
4. Clicar no botão de login.

### Dados de entrada:
- Usuário: standard_user
- Senha: secret_sauce

### Resultado Esperado:
- O sistema deve redirecionar o usuário para a página de produtos.

### Resultado Obtido:
- O usuário foi corretamente redirecionado para a página de produtos.

### Status:
✅ Passou

### Observações:
Nenhuma.

---

# Relatório de Teste

## Caso de teste: TC-002 - Login Mal-Sucedido

### Objetivo:
Validar que o sistema exibe uma mensagem de erro adequada quando o usuário tenta realizar login com credenciais inválidas.

### Passos Executados:
1. Acessar o site [https://www.saucedemo.com/](https://www.saucedemo.com/).
2. Preencher o campo de usuário com invalid_user.
3. Preencher o campo de senha com invalid_password.
4. Clicar no botão de login.

### Dados de entrada:
- Usuário: invalid_user
- Senha: invalid_password

### Resultado Esperado:
- O sistema deve exibir uma mensagem de erro informando sobre falha no login.

### Resultado Obtido:
- A mensagem de erro foi exibida corretamente na tela.

### Status:
✅ Passou

### Observações:
Nenhuma.
