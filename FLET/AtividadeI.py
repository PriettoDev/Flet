import flet as ft

def main(page: ft.Page):
    page.title = "Minha primeira aplicação flet"
    page.add(
        ft.Text("Bem vindo ao flet!"),
        ft.ElevatedButton("Clique aqui!", on_click=lambda _: page.add(ft.Text("Botão Clicado!")))
    )

ft.app(target=main)