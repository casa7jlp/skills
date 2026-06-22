"""
Rode este arquivo UMA VEZ para fazer o login no Google.

Ele abre o navegador, você escolhe a conta adm@soucasa7.com.br e clica em
"Permitir". Depois disso ele cria um arquivo token.json e você não precisa
mais logar de novo.

    python authorize.py
"""

from server import _get_credentials

if __name__ == "__main__":
    _get_credentials()
    print("\n=================================================")
    print("  Autorizado com sucesso! O arquivo token.json foi criado.")
    print("  Agora pode ligar o conector no Claude (veja PASSO-A-PASSO.md).")
    print("=================================================\n")
