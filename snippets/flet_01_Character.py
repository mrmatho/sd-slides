import flet as ft

def main(page: ft.Page):
    page.title = "Character Creator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    input_name = ft.TextField(label="Hero Name", width=200)
    input_level = ft.Slider(min=0, max=100, value=50, step=5, label="Level", width=200)
    
    page.add(
        ft.Column(
            controls=[
                input_name,
                input_level,
                ft.Row(
                    controls=[
                        ft.ElevatedButton("Save Hero", on_click=lambda _: page.snackbar(f"Saved {input_name.value}")),
                        ft.ElevatedButton("Reset", bgcolor=ft.colors.RED)
                    ],
                    alignment=ft.MainAxisAlignment.END
                )
                    
            ]
        )
    )
    