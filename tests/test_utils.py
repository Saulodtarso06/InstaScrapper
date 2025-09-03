import unittest
import os
import shutil
from src.utils import criar_pasta_saida, log_info, log_erro


class TestUtils(unittest.TestCase):

    def setUp(self):
        """Executado antes de cada teste"""
        self.usuario_teste = "usuario_teste"
        self.pasta_teste = os.path.join(os.getcwd(), self.usuario_teste)

    def tearDown(self):
        """Executado depois de cada teste"""
        if os.path.exists(self.pasta_teste):
            shutil.rmtree(self.pasta_teste)

    def test_criar_pasta_saida(self):
        """Testa se a função cria a pasta corretamente"""
        caminho = criar_pasta_saida(self.usuario_teste)
        self.assertTrue(os.path.exists(caminho))
        self.assertEqual(caminho, self.pasta_teste)

    def test_log_info(self):
        """Testa se o log_info exibe mensagem corretamente"""
        try:
            log_info("Mensagem de teste")
        except Exception as e:
            self.fail(f"log_info levantou exceção: {e}")

    def test_log_erro(self):
        """Testa se o log_erro exibe mensagem corretamente"""
        try:
            log_erro("Mensagem de erro")
        except Exception as e:
            self.fail(f"log_erro levantou exceção: {e}")


if __name__ == "__main__":
    unittest.main()
