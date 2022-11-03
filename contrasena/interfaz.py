import tkinter as tk
from tkinter import END, Listbox, Variable, ttk

try:
    import contra

    MAX_LENGTH = 64
    MIN_LENGTH = 4
    MAX_CONTRA = 20
    MIN_CONTRA =1

    ANCHO = 500
    ALTO = 200

    class VentanaSecundaria():

        def __init__(self, lista) -> None:
            self.ventana2= tk.Toplevel()
            self.ventana2.config(width=ANCHO, height=ALTO)
            self.ventana2.title("Contraseñas Generadas")
            self.list_box=tk.Listbox(self.ventana2, height=len(lista), )
            self.list_box.insert(END,*lista)
            self.list_box.pack()




    class Application(tk.Tk):

        def __init__(self) -> None:
            super().__init__()
            #APP
            self.title("Contra v1.0")
            self.geometry("400x300")
            self.resizable(0,0)

            #TEXTO
            self.text1 =ttk.Label(text=f"Longitud de la contraseña (Max {MAX_LENGTH}/ Min {MIN_LENGTH})")
            self.text1.place(x=20,y=20)

            self.text2 =ttk.Label(text=F"Cantidad de contraseñas (max {MAX_CONTRA})")
            self.text2.place(x=20, y=40)

            #INPUT
            self.text_input =ttk.Entry(width=4)
            self.text_input.place(x=270,y=20)

            self.text2_input =ttk.Entry(width=4)
            self.text2_input.place(x=270, y=40)

            #GUARDAR CONTRASEÑA
            #self.contra = tk.Listbox(listvariable=)
            self.msg =tk.StringVar()

            #BOTON
            self.button = ttk.Button(text="Generar contraseña", command=self.password_generator)
            self.button.place(x=20,y=60)



            #LABEL-CONTRASEÑA
            #self.text_contra = ttk.Label(self.app, textvariable= self.contra, font=("Courier New", 12))
            #self.text_contra.place(x=20, y=110)
        
            #MENSAJE GUARDADO
            #self.text_msg_porta = ttk.Label(self.app, textvariable= self.msg)

            #LOOP
            #self.app.mainloop()
            

        def clip(self, text):

            #COPIA EL PARÁMETRO ENVIADO 'TEXT' AL PORTAPAPELES
            self.clipboard_clear()
            self.clipboard_append(text)

        def abrir_ventana_secundaria (self, lista):
            self.ventana_secundaria = VentanaSecundaria(lista)

        def password_generator (self):
            try:
                longitud = abs(int(self.text_input.get()))
                cantidad = abs(int(self.text2_input.get()))

                if len(self.text_input.get()) and len(self.text2_input.get()):

                    if longitud < MAX_LENGTH:
                        self.contra_generada =(contra.generador_contraseñas2(longitud, cantidad))
                    else:
                        self.contra_generada =(contra.generador_contraseñas2(longitud, cantidad))
                elif not len(self.text_input.get()):
                    #NO SE INGRESO UNA LONGITUD. SE CREA CON LONGITUD 4.
                    self.contra_generada = contra.generador_contraseñas2(MIN_LENGTH, cantidad)
                elif not len(self.text2_input.get()):
                    #NO SE INGRESO UNA CANTIDAD. SE CREA CON CANTIDAD 1.
                    self.contra_generada = contra.generador_contraseñas2(longitud, MIN_CONTRA )
                else:
                    #NO SE INGRESO LONGITUD NI CANTIDAD. SE CREA CON LONGITUD 4, CANTIDAD 1
                    self.contra_generada =contra.generador_contraseñas2(MIN_LENGTH, MIN_CONTRA)

                self.abrir_ventana_secundaria(self.contra_generada)

            except Exception as e:
                #self.contra.set("ERROR. INGRESE UN NUMERO VALIDO")
                #self.msg.set("")
                print(f"ERROR: {e}")

    def main():
        mi_app = Application()
        mi_app.mainloop()
    
    if __name__ == '__main__':
        main()
except ImportError as e:
        print(f"Error al importar el módulo generador de contraseñas.\nERROR: {e}")
except Exception as e:
        print(f"Ha ocurrido un error inesperado.\nERROR: {e}")