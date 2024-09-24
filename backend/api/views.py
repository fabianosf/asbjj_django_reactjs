# views.py
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

class HomeView(APIView):
    def get(self, request):
        data = {
            "carousel": [
                {"img": "/media/image/imagem1.jpg", "title": "Guerreiros no Tatame", "description": "Prof. Alexandre Salgado"},
                {"img": "/media/image/imagem2.jpg", "title": "Guerreiras no Tatame", "description": "Profa. Anna Carolina"},
                {"img": "/media/image/imagem3.jpg", "title": "Criançada no Tatame", "description": "Prof. Alexandre Salgado e Anna Carolina"}
            ],
            "gallery": [
                "/media/image/pessoal1.jpg",
                "/media/image/pessoal2.jpg",
                "/media/image/pessoal3.jpg",
                "/media/image/pessoal4.jpg",
                "/media/image/pessoal5.jpg",
                "/media/image/pessoal6.jpg"
            ]
        }
        return Response(data)


class AboutView(APIView):
    def get(self, request):
        data = {
            "image": "/media/image/professores.jpeg",
            "description": (
                "Na nossa academia, estamos comprometidos em transformar vidas através do jiu-jítsu e do bem-estar. "
                "Com mais de 10 anos de experiência, nosso time de instrutores dedicados, liderado por Alexandre "
                "Salgado e sua esposa Anna Carolina, oferece um ambiente acolhedor e seguro para alunos de todas as "
                "idades e níveis de habilidade."
                "Além das aulas de jiu-jítsu, oferecemos sessões de yoga ministradas pela nossa instrutora Anna Carolina."
            ),
            "schedule": [
                {
                    "day": "Segunda",
                    "times": [
                        {"time": "7:00 - 8:00", "class": "Todos os níveis"},
                        {"time": "18:00 - 19:00", "class": "Jiu-Jitsu"},
                        {"time": "19:20 - 20:20", "class": "Jiu-Jitsu(Infantil)"},
                        {"time": "20:00 - 21:00", "class": "Todos os níveis"}
                    ]
                },
                {
                    "day": "Terça",
                    "times": [
                        {"time": "12:00 - 13:00", "class": "Iniciantes kimono"},
                        {"time": "18:00 - 19:00", "class": "Jiu-Jitsu"},
                        {"time": "19:20 - 20:20", "class": "Jiu-Jitsu(Infantil)"},
                        {"time": "20:00 - 21:00", "class": "Todos os níveis"}
                    ]
                },
                {
                    "day": "Quarta",
                    "times": [
                        {"time": "7:00 - 8:00", "class": "Todos os níveis"},
                        {"time": "18:00 - 19:00", "class": "Jiu-Jitsu"},
                        {"time": "19:20 - 20:20", "class": "Jiu-Jitsu(Infantil)"},
                        {"time": "20:00 - 21:00", "class": "Todos os níveis"}
                    ]
                },
                {
                    "day": "Quinta",
                    "times": [
                        {"time": "12:00 - 13:00", "class": "Iniciantes kimono"},
                        {"time": "18:00 - 19:00", "class": "Jiu-Jitsu"},
                        {"time": "19:20 - 20:20", "class": "Jiu-Jitsu(Infantil)"},
                        {"time": "20:00 - 21:00", "class": "Todos os níveis"}
                    ]
                },
                {
                    "day": "Sexta",
                    "times": [
                        {"time": "7:00 - 8:00", "class": "Todos os níveis"},
                        {"time": "18:00 - 19:00", "class": "Open Match"},
                        {"time": "Open Match", "class": "Open Match"}
                    ]
                }
            ],
            "testimonials": [
                {"name": "João Pereira", "text": "O que eu mais gosto nas aulas..."},
                {"name": "Carla Mendes", "text": "O jiu-jitsu não só me ajudou..."},
                {"name": "Beatriz Lima", "text": "Comecei a treinar jiu-jitsu..."}
            ]
        }
        return Response(data)
    

class ServiceView(APIView):
    def get(self, request):
        data = {
            "services": [
                {
                    "name": "Jiu-Jitsu",
                    "benefits": [
                        "Melhora da Condição Física",
                        "Perda de Peso",
                        "Melhora da Resiliência Física",
                        "Redução do Estresse",
                        "Desenvolvimento do Autocontrole",
                        "Habilidades de Autodefesa"
                    ],
                    "cta": "/contato"
                },
                {
                    "name": "Defesa Pessoal",
                    "benefits": [
                        "Aumento da Confiança",
                        "Redução do Estresse e Ansiedade",
                        "Desenvolvimento do Autocontrole",
                        "Resiliência Mental",
                        "Empoderamento Pessoal",
                        "Independência"
                    ],
                    "cta": "/contato"
                },
                {
                    "name": "Yoga",
                    "benefits": [
                        "Aumento da Flexibilidade",
                        "Melhora da Postura",
                        "Melhora da Respiração",
                        "Redução do Estresse",
                        "Melhora do Sono",
                        "Sensação de Paz Interior"
                    ],
                    "cta": "/contato"
                }
            ],
            "faq": [
                {
                    "id": "collapseUm",
                    "question": "O que é jiu-jitsu?",
                    "answer": "O jiu-jítsu é uma arte marcial focada em técnicas de alavanca, imobilizações e submissões, permitindo que uma pessoa menor e mais fraca possa se defender de um oponente maior e mais forte."
                },
                {
                    "id": "collapseDois",
                    "question": "Preciso ter experiência para começar?",
                    "answer": "Não, nossa academia oferece aulas para todos os níveis, desde iniciantes até avançados. Todo mundo começa do zero, e estamos aqui para ajudar no seu progresso."
                },
                {
                    "id": "collapseTres",
                    "question": "Quais são os benefícios de praticar jiu-jítsu?",
                    "answer": "Os benefícios incluem melhora da forma física, autoconfiança, disciplina, aprendizado de autodefesa, além de ser uma excelente forma de aliviar o estresse."
                },
                {
                    "id": "collapseQuatro",
                    "question": "Quanto tempo leva para obter a faixa preta?",
                    "answer": "O tempo varia de pessoa para pessoa, dependendo da dedicação, frequência de treino e aprendizado. Geralmente, leva de 8 a 12 anos para obter a faixa preta."
                },
                {
                    "id": "collapseCinco",
                    "question": "Quais equipamentos são necessários?",
                    "answer": "Para iniciar, você precisará de um kimono (Gi). Oferecemos kimonos para venda na academia. Mais adiante, você pode adquirir outros equipamentos, como rashguards e protetores bucais."
                },
                {
                    "id": "collapseSeis",
                    "question": "Há um limite de idade para começar?",
                    "answer": "Não há limite de idade. Temos alunos de todas as idades, desde crianças até adultos mais velhos. O jiu-jitsu é uma arte marcial inclusiva para todas as idades."
                }
            ]
        }
        return Response(data)



class ContactView(APIView):
    def get(self, request):
        data = {
            "team": [
                {
                    "name": "Alexandre Salgado",
                    "role": "Professor",
                    "image": "/media/image/alexandre.jpg"
                },
                {
                    "name": "NoGi",
                    "role": "Alexandre Salgado",
                    "image": "/media/image/nogi.jpeg"
                },
                {
                    "name": "Anna Carolina",
                    "role": "Professora",
                    "image": "/media/image/ana.jpg"
                },
                {
                    "name": "Meninas",
                    "role": "Anna Carolina",
                    "image": "/media/image/meninas.jpeg"
                }
            ]
        }
        return Response(data)



class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')  # Opcional, dependendo da lógica de autenticação
        password = request.data.get('password')

        # Tentar autenticar o usuário
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({"message": "Login bem-sucedido"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Credenciais inválidas"}, status=status.HTTP_401_UNAUTHORIZED)
        



class SignupView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        confirm_password = request.data.get('confirmPassword')
        phone = request.data.get('phone')

        # Verificar se as senhas coincidem
        if password != confirm_password:
            return Response({"message": "As senhas não coincidem"}, status=status.HTTP_400_BAD_REQUEST)

        # Verificar se o nome de usuário já existe
        if User.objects.filter(username=username).exists():
            return Response({"message": "Nome de usuário já existe"}, status=status.HTTP_400_BAD_REQUEST)

        # Criar o novo usuário
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # Aqui, você pode adicionar mais lógica para salvar o número de telefone em um perfil de usuário, por exemplo.

        return Response({"message": "Registro bem-sucedido"}, status=status.HTTP_201_CREATED)

