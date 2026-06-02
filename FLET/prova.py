import flet as ft

def main(page: ft.Page):
    page.title = "Lista de tarefas"
    
    campo = ft.TextField(hint_text="Adicione uma tarefa: ")

    def adicionar_tarefa(e):
        lista.controls.append(
            ft.Row([
                ft.Checkbox(value=False),
                ft.Text(campo.value)
            ])
        )
        page.update()

    botao = ft.ElevatedButton("Adicionar", on_click=adicionar_tarefa)
    lista = ft.Column()

    page.add(
        ft.Row([campo, botao]),
        lista
    )

ft.app(target=main)