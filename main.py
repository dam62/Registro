import flet as ft
import registroPage
import loginPage

def main(page: ft.Page):
    page.title = "APP DE REGISTROS"

    def route_change(e):
        page.views.clear()
        if page.route == "/login":
            page.views.append(
                ft.View(
                    route="/login",
                    controls=[loginPage.main(page)]
                )
            )
        elif page.route == "/registros":
            page.views.append(
                ft.View(
                    route="/registros",
                    controls=[registroPage.main(page)]
                )
            )

        page.update()

    page.on_route_change = route_change
    page.go("/login")


if __name__ == '__main__':
    ft.app(target=main, view=ft.WEB_BROWSER, port=30033)