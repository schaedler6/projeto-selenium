# Relatório de Teste

## Caso de Teste: TC-001 - Login bem-sucedido / TC-002 - Login mal-sucedido

## Objetivo:
- TC-001: Validar login com usuário válido (standard_user/secret_sauce) no site https://www.saucedemo.com/
- TC-002: Validar mensagem de erro ao tentar login com usuário inválido (invalid_user/wrong_password).

## Passos Executados:
1. Acessar o site https://www.saucedemo.com/
2. Inserir credenciais corretas e realizar login (TC-001).
3. Verificar presença da lista de produtos.
4. Acessar novamente o site, inserir credenciais inválidas e tentar login (TC-002).
5. Verificar presença da mensagem de erro.

## Dados de Entrada:
- Usuário válido: standard_user
- Senha válida: secret_sauce
- Usuário inválido: invalid_user
- Senha inválida: wrong_password

## Resultado Esperado:
- TC-001: Acesso à página de produtos após login válido.
- TC-002: Exibição da mensagem de erro informando falha no login.

## Resultado Obtido:
- TC-001: Página de produtos carregada com sucesso.
- TC-002: Mensagem de erro exibida corretamente.

## Status:
- TC-001: ✅ Passou
- TC-002: ✅ Passou

## Observações:
- Testes executados em: 27/04/2025
- Nenhum erro inesperado ocorreu.
- Screenshots seriam capturados apenas em caso de falhas (não necessários aqui).
