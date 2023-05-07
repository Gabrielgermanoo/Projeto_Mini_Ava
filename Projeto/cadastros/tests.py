from datetime import date
from django.test import Client, TestCase
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Atividade, Classe, Question, Status, Progressao, Comment, Comprovante



class ClasseCreateTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.url = reverse_lazy('cadastrar-classe')

    def test_cadastro_de_classe(self):
        form_data = {'nome': 'Classe Teste', 'nivel': 1, 'descricao': 'Classe de teste para o sistema'}
        response = self.client.post(self.url, form_data)
        self.assertEqual(response.status_code, 302) 
        self.assertEqual(Classe.objects.count(), 1) # apenas um objeto Classe deve ter sido criado
        nova_classe = Classe.objects.first()
        self.assertEqual(nova_classe.nome, 'Classe Teste')
        self.assertEqual(nova_classe.nivel, 1.0)
        self.assertEqual(nova_classe.descricao, 'Classe de teste para o sistema')

class StatusCreateTest(TestCase):
    
        def setUp(self):
            self.user = User.objects.create_user(username='testuser', password='testpass')
            self.client.login(username='testuser', password='testpass')
            self.url = reverse_lazy('cadastrar-status')
    
        def test_cadastro_de_status(self):
            form_data = {'nome': 'Status Teste', 'descricao': 'Status de teste para o sistema'}
            response = self.client.post(self.url, form_data)
            self.assertEqual(response.status_code, 302) 
            self.assertEqual(Status.objects.count(), 1) # apenas um objeto Status deve ter sido criado
            novo_status = Status.objects.first()
            self.assertEqual(novo_status.nome, 'Status Teste')
            self.assertEqual(novo_status.descricao, 'Status de teste para o sistema')

class CommentCreateTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='johndoe', email='johndoe@example.com', password='secret')
        self.data = {'body': 'Um comentário de teste'}
        self.url = reverse_lazy('cadastrar-comentario')

    def test_comment_create(self):
        # Simula o login do usuário
        self.client.login(username='johndoe', password='secret')
        # Envia uma requisição POST com os dados do comentário
        response = self.client.post(self.url, data=self.data)
        # Verifica se a resposta redireciona para a página de sucesso
        self.assertRedirects(response, reverse('listar-comentario'))
        # Verifica se o comentário foi criado no banco de dados
        self.assertEqual(Comment.objects.count(), 1)
        comment = Comment.objects.first()
        self.assertEqual(comment.body, 'Um comentário de teste')
        self.assertEqual(comment.usuario, self.user)

class CommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Cria um usuário para usar como chave estrangeira em Comment
        User.objects.create_user(username='testuser', password='testpass')

        # Cria uma instância de Comment para testar
        Comment.objects.create(usuario=User.objects.get(id=1), body='Test comment')

    def test_str_representation(self):
        comment = Comment.objects.get(id=1)
        expected = 'Test comment'
        self.assertEqual(str(comment), expected)

class QuestionCreateTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.url = reverse_lazy('cadastrar-enquete')
        self.data = {
            'question_text': 'Qual sua linguagem de programação favorita?',
        }

    def test_create_question(self):
        response = self.client.post(self.url, data=self.data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cadastros/listar-question.html')
        self.assertContains(response, 'Enquete cadastrada com sucesso.')
        self.assertTrue(Question.objects.filter(question_text='Qual sua linguagem de programação favorita?').exists())

    def test_create_question_invalid_data(self):
        self.data['question_text'] = ''
        response = self.client.post(self.url, data=self.data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cadastros/form.html')
        self.assertFormError(response, 'form', 'question_text', 'Este campo é obrigatório.')
        self.assertFalse(Question.objects.filter(question_text='').exists())









