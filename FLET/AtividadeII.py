import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Text("Bem-Vindo a minha página!"),
        ft.TextField("Nome: "),
        ft.TextField("Sobrenome: "),
        ft.TextField("Email: "),
        ft.ElevatedButton("Enviar")
    )

ft.app(target = main)