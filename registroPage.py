import flet as ft
import datetime
import ddbb

def main(page : ft.Page):
    page.title = "REGISTRAR"

    def abrir_selector(e):
        date_picker.open = True
        page.update()

    def seleccionar_fecha(mi):
        fecha_txt.value = f"{date_picker.value.day}/{date_picker.value.month}/{date_picker.value.year}"
        page.update()

    def crear_registro(mi):
        nombre = nombre_tf.value
        apellidos = apellidos_tf.value
        email = email_tf.value
        password = passwd_tf.value
        fecha_nacimiento = date_picker.value
        ddbb.insertar_registro(nombre, apellidos, email, password, fecha_nacimiento)

    def volver(e):
        page.go("/login")

    nombre_tf = ft.TextField(label="Nombre", width=300)
    apellidos_tf = ft.TextField(label="Apellidos", width=300)
    email_tf = ft.TextField(label="Email", width=300)
    passwd_tf = ft.TextField(label="Contraseña", width=300)
    date_picker = ft.DatePicker(on_change=seleccionar_fecha, value=datetime.datetime.now())
    fecha_txt = ft.Text(f"{date_picker.value.day}/{date_picker.value.month}/{date_picker.value.year}")
    volver_btn = ft.ElevatedButton(text="Volver", on_click=volver)

    columna_datos = ft.Column(
        controls=[ft.Text("USUARIO", size=40),
                  nombre_tf,
                  apellidos_tf,
                  email_tf,
                  passwd_tf,
                  fecha_txt,
                  ft.FilledButton("SELECCIONAR FECHA", on_click=abrir_selector),
                  ft.FilledButton("Registrarse", on_click=crear_registro),
                  volver_btn,],
    )
    page.overlay.append(date_picker)
    return columna_datos