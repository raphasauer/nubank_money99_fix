# Nubank Money99 Fix
Script de Python que converte os arquivos .oxf do Nubank para serem utilizados com o Money 99

## Como usar
O script foi feito utilizando o Python 3.10. É necessário ter uma instalação de Python >= 3.7 na sua máquina. Para rodar o aqruivo, utilize o Command Prompt e digite:

`$ python3 .\nubank_money99_fix.py .\nome_do_seu_extrato.ofx`

O script simplesmente modifica ou troca as linhas do .oxf que causam problema na leitura pelo Money 99. Retirei as informações sobre quais linhas podem dar problemas no [post](https://comunidade.nubank.com.br/t/falha-no-uso-do-ofx-gerado-pelo-nubank/224615/19) do fórum do Nubank sobre o problema. Utilizei o comentário do usuário BrenoMorozowski como base para as alterações.

