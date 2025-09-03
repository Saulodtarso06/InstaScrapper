import instaloader
## from utils import
from .utils import criar_pasta_saida, log_info, log_erro

import getpass  # Para senha segura

def baixar_fotos(usuario: str, login_usuario: str = None, login_senha: str = None):
    """
    Baixa todas as fotos de um perfil do Instagram.
    Para perfis privados ou evitar 401, é necessário login.
    """
    try:
        # Cria o objeto instaloader
        loader = instaloader.Instaloader(
            download_videos=False,
            download_video_thumbnails=False,
            save_metadata=False,
            post_metadata_txt_pattern=""
        )

        # LOGIN opcional
        if login_usuario and login_senha:
            log_info(f"Fazendo login com {login_usuario}")
            loader.login(login_usuario, login_senha)

        # Criar pasta de saída personalizada
        pasta_saida = criar_pasta_saida(usuario)

        log_info(f"Iniciando download das fotos do perfil: {usuario}")

        # Obter perfil
        profile = instaloader.Profile.from_username(loader.context, usuario)

        # Loop pelos posts e baixar
        for index, post in enumerate(profile.get_posts(), start=1):
            log_info(f"Baixando foto {index}...")
            loader.download_post(post, target=pasta_saida)

        log_info("Download concluído com sucesso!")

    except Exception as e:
        log_erro(f"Ocorreu um erro: {str(e)}")


if __name__ == "__main__":
    nome_usuario = input("Digite o @ do perfil (sem o @): ").strip()
    logar = input("Deseja fazer login para evitar bloqueios? (s/n): ").strip().lower()

    if logar == 's':
        usuario_login = input("Digite seu usuário do Instagram: ").strip()
        senha_login = getpass.getpass("Digite sua senha: ")
        baixar_fotos(nome_usuario, usuario_login, senha_login)
    else:
        baixar_fotos(nome_usuario)
