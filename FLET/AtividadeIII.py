import flet as ft

def main(page: ft.Page):
    page.title = "Lista de tarefas"
    page.add(
        ft.Column([
            ft.Row([
                ft.TextField("Tarefa: "),
                ft.Checkbox(value=False)
            ]),
            ft.Row([
                ft.TextField("Tarefa: "),
                ft.Checkbox(value=False)
            ]),
            ft.Row([
                ft.TextField("Tarefa: "),
                ft.Checkbox(value=False)
            ]),
            ft.Row([
                ft.TextField("Tarefa: "),
                ft.Checkbox(value=False)
            ])
        ])
    )

ft.app(target=main)