# Final Project - Pygym

Web-based application using JavaScript, Python, and SQL.

<p align="center">
  <img src="https://img.shields.io/github/downloads/ThayRibeiro0/project0.2/total?color=%2300ff00&logo=Github&style=plastic" />
  <img src="https://img.shields.io/github/repo-size/ThayRibeiro0/project0.2?style=plastic" />
  <img src="https://img.shields.io/github/languages/top/ThayRibeiro0/project0.2?style=plastic" />
  <img src="https://img.shields.io/github/last-commit/ThayRibeiro0/project0.2?style=plastic" />
</p>

<p align="center">
    <img src="https://img.shields.io/badge/-Javascript/total?logo=Javascript" />
    <img src="https://img.shields.io/badge/Html-purple"  />
    <img src="https://img.shields.io/badge/Css-darkred" />
    <img src="https://img.shields.io/badge/-Python/total?logo=Python" >
    <img src="https://img.shields.io/badge/SQL-pink" />
    <img src="https://img.shields.io/badge/-Flask/total?logo=Flask" />
</p>


## Video Demo: <https://youtu.be/UXD7D4jK85M>


## Description

This project has as purpose help one gym that make the control about him students with excel and need to be more technological and agile in your routine. The company can control the web page with three routes: Login(employees page), Sign-up(admin1 page) and Admin(admin2 page). The Login page only who have the email and password create can access the home page and to do the register of students and logout there. The sign up can register the employees and see them in the list of employees that can work in the home page. The Admin it's who control de access about everything deleting the employees or edit them for access the home page. Yes, I debated by my boyfriend and serch online themes and ways for to do and I make like this because it was the purpose that I received from my boyfrind for make and resolve on problem.

## Instalation

The file docker make all the installations that you will need, but if you will need it you can run [pip install flask], [pip install flask-admin], [pip install flask-login] and the configuration about the [.venv] that I keep the links about everything below and make this and have the [python], the project works.

Download get-pip.py Script: Open a web browser and navigate to:
  - https://bootstrap.pypa.io/get-pip.py. 

Right-click on the page and select "Save As" to save the file to your computer.

Run get-pip.py Script: Open a terminal and navigate to the directory where you downloaded get-pip.py. Then run the following command to install pip:

```bash
  'python get-pip.py'
```

If you have multiple Python versions installed, you may need to specify the Python version explicitly. For example:

```bash
'python3 get-pip.py'
```

Verify Installation: After the installation completes, you can verify that pip is installed by running:

```bash
'pip --version'
```
Navigate to the Correct Directory: `cd /Directory`

This should display the version number of pip, confirming that it's installed correctly.

Install Packages: Now that pip is installed, you can proceed to install Flask and other packages as needed:

```bash
  pip install flask
  pip install flask-admin
  pip install flask-login
```

Using curl Command:Open your terminal and use the curl command to download the get-pip.py script. Run the following command:

```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

To run the app Activate Virtual Environment (if applicable):
```bash
source venv/bin/activate
python3 -m venv venv
pip install -r requirements.txt
python app.py
```

Generate Secret Key in __init__.py and you can then run this script from your terminal:
```bash
python generate_secret_key.py
```

## What each of the files you wrote for the project contains and does?

The project the flask, docker, venv, docker-compose, env,gitignore, requirements, setup and installation, (Terminal, Folders .venv, __pycache__, dockers(automatic setup the packages), .gitignore(ignore files to upload in github), requirements(libs), env(to hidden the secret_key), set(set flask), flask and venv(to load the servidor)); Created a flask app(function that factory the application in the __init__.py and app.py) ; The routes/views, (the way to see and map URL's to Controllers/Actions and generation URL's inside the Views and Auth); Used the jinja templating language and HTML templates (Jinja template is simply a text file that can generate any text-based format (HTML, XML, CSV, LaTeX, etc) and became more easy the setup the page's code using as base the to setup inside in other documentation{% ... %}; Realized the sign up, login, home, logout, works page HTML and stylization with the CSS file(Creating the page's structure with the Hyper Text Markup Language(HTML) in base, base1, funcionarios, home, login, sign_up, update html's and the stylization with the base.cc); The HTTP requests (POST, GET,...)(views and auth to take datas for user and user inside the pages and show for the user and admin); The handling POST requests (step by step); Wrote the message flashing (messages in the html's red and green with the use the Flash that show alert message similar the javascript); Setup the flask SQLAlchemy, (terminal and documentation views); The Database and Models, (views, models, auth, __init__.py and app.py); Incremented new users and students accounts, (views, auth); Logged in users and looked the client view, (html's); Maked the flask login module, (views); Checked if user and admin is logged in, (views and auth) ; Registers control HTML, (home, employees; Added and deleted the user and the students registers. (buttons html's home, employees and base, base1); 16: And for less the setup the flask-admin and flask-login(__init__.py, views, auth) and all the structed based in searches and datas from class, friends and internet and that help me in my study and learn each day more thanks for all the contributions because finally I'm feel ready.


## Referência
- [CS50]
- [Stackoverflow]
- [Clipchamp]
- [Python Documentation]
- [Learn JavaScript] - Full Course for Beginners: (https://www.youtube.com/watch?v=PkZNo7MFNFg)
- [Pyhon packages] https://packaging.python.org/pt_BR/latest/tutorials/installing-packages/)
- [Flask Documentation]
- [Flask Tutorial in Visual Studio Code] (https://code.visualstudio.com/docs/python/tutorial-flask)
- [How to Create a User Login Web System in Python] (https://www.section.io/engineering-education/user-login-web-system/)
- [Construindo um sistema de login com Python Flask e MySQL para iniciantes] (https://pt.quish.tv/building-login-system-with-python-flask)
- [Login & Registration with SQLite Database Using Flask | Tamil] (https://www.youtube.com/watch?v=RrtzalGsPFk)
- [Register & login using python flask] (https://www.youtube.com/watch?v=d04xxdrc7Yw&t=1572s)
- [Aplicativo Flask + Banco de dados - Ativando o Botão CADASTRAR no Python] (https://www.youtube.com/watch?v=1Yu9V8iyvL4&t=9s)
- [Cadastro e Login com Python - #05 Login] (https://www.youtube.com/watch?v=nHG5zwVJ07M)
- [TELA DE LOGIN COM TEMA DARK | HTML + CSS] (https://www.youtube.com/watch?v=69-WfrVBli8)
- [Aprenda como ligar um FORMULÁRIO com BANCO DE DADOS #01] (https://www.youtube.com/watch?v=QOeDE7nPDq0&t=262s)
- [Animated Login and Registration Form in HTML CSS & JavaScript] (https://www.youtube.com/watch?v=V8PU_geaCCU)
- [Python Flask Authentication Tutorial - Learn Flask Login] (https://www.youtube.com/watch?v=71EU8gnZqZQ)
- [Run Python Script Clicking Html Button | Latest 2021] (https://www.youtube.com/watch?v=0meTbQQaosU)
- [Learn Python : Create Login Page Using Python Flask & Bootstrap | Render Template | Static Files] (https://www.youtube.com/watch?v=U7g-TcIKLB4)
- [Python Website Full Tutorial - Flask, Authentication, Databases & More] (https://www.youtube.com/watch?v=dam0GPOAvVI&t=1776s)
- [Responsive Login and Registration Form in HTML CSS & JavaScript] (https://www.youtube.com/watch?v=VP0DS6iXbXY)
- [Animated Login and Registration Form in HTML CSS & JavaScript] (https://www.youtube.com/watch?v=V8PU_geaCCU&t=48s)
- [Picabay videos particles] (https://pixabay.com/videos/search/particle/)
- [How to Create a Video Background With CSS] (https://blog.hubspot.com/website/video-background-css)
- [JavaScript & jQuery the missing manual by David Sawyer Mcfarland]
- [HTML and Css Design and Build Websites by Jon Duckett]
- [Javascript and JQuery Interactive Front-End by Jon Duckett]
