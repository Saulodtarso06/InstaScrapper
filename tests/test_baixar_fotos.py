import unittest
from unittest.mock import patch, MagicMock
import os
import shutil

from src.baixar_fotos import baixar_fotos
from src.utils import criar_pasta_saida


class TestBaixarFotos(unittest.TestCase):

    def setUp(self):
        """Executado antes de cada teste"""
        self.usuario_teste = "usuario_fake"
        self.pasta_teste = criar_pasta_saida(self.usuario_teste)

    def tearDown(self):
        """Executado depois de cada teste"""
        if os.path.exists(self.pasta_teste):
            shutil.rmtree(self.pasta_teste)

    @patch("src.baixar_fotos.instaloader.Instaloader")
    @patch("src.baixar_fotos.instaloader.Profile")
    def test_baixar_fotos(self, mock_profile, mock_instaloader):
        # Simular posts do perfil
        mock_post = MagicMock()
        mock_profile.from_username.return_value.get_posts.return_value = [mock_post, mock_post]

        # Simular loader
        mock_loader = MagicMock()
        mock_instaloader.return_value = mock_loader

        # Executar função
        baixar_fotos(self.usuario_teste)

        # Verificar se a pasta foi criada
        self.assertTrue(os.path.exists(self.pasta_teste))

        # Verificar se download_post foi chamado duas vezes (2 posts mockados)
        self.assertEqual(mock_loader.download_post.call_count, 2)


if __name__ == "__main__":
    unittest.main()
