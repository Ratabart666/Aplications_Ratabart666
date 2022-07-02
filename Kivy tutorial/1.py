import kivy
from kivy.app import App #Se debe importar en cualquier aplicacion que se cree
from kivy.uix.label import Label #Es un widget del tipo etiqueta

class Myapp(App): #Definimos la clase de app
    def build(self):
        return Label(text="Hello world",font_size=72) #Podemos definir el texto y el tamano del texto
    
if __name__=="__main__":# Comando para que la app corra
    Myapp().run()