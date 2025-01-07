import flet as ft
from models import Usuario
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

CONN = 'sqlite:///BancoDeDados_Formulario.db'

engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()


def main(page: ft.Page):
    page.title = "Fromulário de Cadastro"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    def cadastrar(e):
        novo_usuario = Usuario(
            name=nome.value,
            email=email.value,
            password=senha.value
        )
        session.add(novo_usuario)
        session.commit()
        print("Usuário cadastrado com sucesso!")
    
    txt_titulo = ft.Text("Formulário de Cadastro")
    nome = ft.TextField(label="Nome", width=300)
    email = ft.TextField(label="Email", width=300)
    senha = ft.TextField(label="Senha", width=300, password=True)
    btn_cadastrar = ft.ElevatedButton("Cadastrar", width=300, on_click=cadastrar)
    
    page.add(
        txt_titulo,
        nome,
        email,
        senha,
        btn_cadastrar
    )

ft.app(target=main)


