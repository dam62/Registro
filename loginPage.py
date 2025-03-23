import datetime
import flet as ft

import ddbb

def main(page : ft.Page):
    page.title = "LOGIN"

    def loguear(e):
        usuario = usuario_tf.value
        passwd = passwd_tf.value

        resultado = ddbb.buscar_usuario(usuario)

        if resultado:
            email_db, passwd_db = resultado[0]
            if usuario == email_db and passwd == passwd_db:
                ddbb.actualizarFechaLogin(email_db)
                print("Logueado con éxito")
            else:
                print("El email o la contraseña es incorrecto")
        else:
            print("El usuario no está registrado")

        page.update()

    def volver(e):
        page.go("/registros")

    usuario_tf = ft.TextField(label="Usuario/Email", width=300)
    passwd_tf = ft.TextField(label="Contraseña", width=300)
    volver_btn = ft.ElevatedButton(text="Registrarse", on_click=volver)

    columna_datos = ft.Column(
        controls=[ft.Text("USUARIO", size=40),
                  usuario_tf,
                  passwd_tf,
                  ft.FilledButton("LOGIN", on_click=loguear),
                  volver_btn,],
    )
    return columna_datos