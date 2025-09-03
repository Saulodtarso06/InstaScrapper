import os
from datetime import datetime

def criar_pasta_saida(nome_usuario: str) -> str:
    """
    Cria (se não existir) a pasta de saída para salvar as fotos.
    Retorna o caminho da pasta.
    """
    pasta = os.path.join(os.getcwd(), nome_usuario)
    if not os.path.exists(pasta):
        os.makedirs(pasta)
        log_info(f"Pasta criada: {pasta}")
    return pasta


def log_info(mensagem: str) -> None:
    """
    Exibe uma mensagem de log no console com timestamp.
    """
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[INFO {agora}] {mensagem}")


def log_erro(mensagem: str) -> None:
    """
    Exibe uma mensagem de erro no console com timestamp.
    """
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[ERRO {agora}] {mensagem}")
