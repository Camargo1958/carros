## Projeto de treinamento em Django

>virtualenv venv
>./venv/scripts/activate
>pip install django
>django-admin --version -> 5.0.6

# Criando projeto Django
>django-admin startproject app .

# Testando o projeto Django
>python .\manage.py runserver

Starting development server at http://127.0.0.1:8000/

# Django Admin help
>django-admin --help

# Testando a aplicação
>python .\manage.py test

# Criando um app
>python .\manage.py startapp cars

# Ativando a app no Django
No settings.py gerla do projeto (app): INSTALLED_APPS -> incluir 'cars'

# Inicializar o BD
- Gestão de usuários e gestão de sessão estão previamente iniciliazadas no BD
    # manage.py makemigrations: varre o projeto e montas migrations (rodar sempre que houver uma alteração nas estruturas de dados da aplicação)
    >python manage.py makemigrations
    # manage.py migrate: executa as alterações capturadas pelas migrations no BD
    >python manage.py migrate

# Criando um superuser
>python manage.py createsuperuser
Username (leave blank to use 'aldrovando'): admin
Email address: aldrovcamargo@gmail.com
Password: admin#2024
Password (again): 
Superuser created successfully.

# Criando modelo 'Car'
models.py -> django ORM
>python manage.py makemigrations
Migrations for 'cars':
  cars\migrations\0001_initial.py
    - Create model Car

>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, cars, contenttypes, sessions
Running migrations:
  Applying cars.0001_initial... OK

# Configurando tabela Car para ser acessada pelo admin
admin.py -> nova classe CarAdmin(admin.ModelAdmin)

# Configurando Django para operar em Portugues
settings.py -> LANGUAGE_CODE = 'en-us' => LANGUAGE_CODE = 'pt-br'

# Configurando Time Zone
settings.py -> TIME_ZONE = 'UTC' => TIME_ZONE = 'America/Sao_Paulo'

# Nomes de objetos no User Interface (Car object (3) -> Marea 20v)
models.py:
    def __str__(self):
        return self.model

# Criando modelo Brand
Car.brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
>python manage.py makemigrations
Migrations for 'cars':
  cars\migrations\0003_brand_alter_car_brand.py
    - Create model Brand
    - Alter field brand on car

>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, cars, contenttypes, sessions
Running migrations:
  Applying cars.0003_brand_alter_car_brand... OK

Alterar admin.py -> 

# Inserir propriedade de Placa (Plate) e Foto (Photo) na tabela de carros
>python -m pip install Pillow
Installing collected packages: Pillow
Successfully installed Pillow-10.3.0
>python manage.py makemigrations
Migrations for 'cars':
  cars\migrations\0004_car_photo_car_plate.py
    - Add field photo to car
    - Add field plate to car
>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, cars, contenttypes, sessions
Running migrations:
  Applying cars.0004_car_photo_car_plate... OK

- Configurar app/settings.py:
MEDIA_ROOT = os.path.JOIN(BASE_DIR, 'media')
MEDIA_URL = '/media/'

- app/urls;.py:
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Criando nova rota/url para /cars
- Editar arquivo app/urls e inserir a nova url (criada uma função view provisória cars_view para satisfazer o interface de path())
- Mover função view provisória cars_view para cars/views

# Inciando o servidor
>python manage.py runserver
localhost:8000/admin
localhost:8000/register
localhost:8000/login
admin + admin#2024
hazak + lobo1958

# Documentação da linguagem de templates do Django: 
https://docs.djangoproject.com/pt-br/4.1/ref/templates/language/

# Documentação models e ORM: 
https://docs.djangoproject.com/pt-br/4.2/topics/db/

    #cars = Car.objects.all() # get all objects as QuerySet using ORM
    #cars = Car.objects.filter(brand__name='Fiat')
    #cars = Car.objects.filter(model='Chevette Tubarão')

# Documentação de Forms no Django: 
https://docs.djangoproject.com/pt-br/4.1/topics/forms/

# 11 - Autenticação:
  Usar a infraestrutura do Django
  1- Criar tela para registro de usuário
  2- Criar tela de Login
  
  - Uma nova app -> Accounts: 
  >python manage.py startapp accounts

  - app/settings.py - INSTALLED_APPS : adicionar 'accounts'
  - app/urls.py:criar nova rota > register/
  - criar register_view em accounts/views.py
  - importar a register_view em app/urls.py
  - criar pasta templates em /accounts
  - criar resgister.html em accounts/templates
  - criar um botão submit em resgister.html
  - tratar o método post na register_view

  Criar a tela de Login:
  - app/urls.py:criar nova rota > login/
  - criar login_view em accounts/views.py
  - importar a login_view em app/urls.py
  - criar login.html em accounts/templates
  - tratar o método post na login_view
  - trocar o redirecionamento de register_view de /cars_view para /login

  Criar rota para Logout
  - app/urls.py:criar nova rota > logout/
  - criar logout_view em accounts/views.py
  - importar a logout_view em app/urls.py
  
  Em app/templates/base.html
  - Criar mensagem de saudação ao usuário logado
  - Condicionar o item de menu 'Cadastrar carro' ao usuário estar logado
  - Criar e condicionar o item de menu 'Cadastre-se' ao usuário não estar logado
  - Criar e condicionar o item de menu 'Login' ao usuário não estar logado
  - Criar e condicionar o item de menu 'Sair' (logout) ao usuário estar logado

# 12 - Class Based Views (CBVs):
Documentação oficial de CBVs: https://docs.djangoproject.com/pt-br/4.2/ref/class-based-views/
  - Introdução: 
    - Não foram feitas para subistuir Function Based Views, é uma alternativa e as dus apodem ser ussadas juntas no mesmo projeto
    - ListView - Lista de objetos
    - DetailView - Detalhe de um item
    - CreateView - Criar um objeto
    - UpdateView - Atualizar um objeto
    - DeleteView - Deletar um objeto
  
  - Reescrever cars_view

  