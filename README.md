# bricademy

### como configurar e executar a aplicação em ambiente linux

1. Instale o pacote python3-venv.
   `sudo apt-get install python3-venv`
2. clone a aplicação.
   `git clone https://github.com/Projeto-de-Software-1/bricademy.git`
3. acesse o diretorio bricademy
   `cd bricademy`
4. crie o ambiente virtual
   `python3 -m venv myvenv`
   > isso criará um ambiente virtual e os pacotes do projeto serão instalados nele, não instalando "lixo" no seu computador nem gerando conflito com versões de aplicações distintas.
5. habilite o ambiente virtual com o comando
   `source ./myvenv/bin/activate`
   > para ter certeza que habilitou no terminal aparecerá (myvenv)
6. instale as dependencias do projeto com o comando
   `pip install -r requirements.pip`
7. gere o banco de dados
   `python manage.py migrate`
8. crie um superusuario do sistema
   `python manage.py createsuperuser`
9. se registre no [mapbox](https://account.mapbox.com/auth/signup/)
   > copie o Default public token
10. abra o arquivo /bricademy/settings.py e na variavel MAPBOX_TOKEN coloque o token registrado
11. rode o servidor
    `python manage.py runserver`
12. acesse o a pagina de administração
    > digite no navegador localhost:8000/admin -> logue com o usuário criado no passo 8
13. Crie subjects para pode testar a aplicação
    > vá até subjects e no canto superior direito clique em add subject e cadastre 1 ou 2
14. teste o sistema
    > pode clicar em viewsite no canto superior direito ou acesse diretamente localhost:8000
