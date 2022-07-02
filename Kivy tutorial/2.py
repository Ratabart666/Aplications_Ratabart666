import kivy
from kivy.app import App #Se debe importar en cualquier aplicacion que se cree
from kivy.uix.label import Label #Es un widget del tipo etiqueta
from kivy.uix.gridlayout import GridLayout #Grid Layout
from kivy.uix.textinput import TextInput #Input de texto
from kivy.uix.button import Button #Botones

class MyGridLayout(GridLayout): #Clase especifica para la interfaz
    # Initialize infinite keywords
    def __init__(self,**kwargs):
        # Call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)
        # Set columns
        self.cols = 2
        #Add widgets
        self.add_widget(Label(text="Name: "))
        #Add input box
        self.name= TextInput(multiline=False)
        self.add_widget(self.name)
        #Add widgets
        self.add_widget(Label(text="Favorite pizza: "))
        #Add input box
        self.pizza= TextInput(multiline=False)
        self.add_widget(self.pizza)
        #Add widgets
        self.add_widget(Label(text="Color : "))
        #Add input box
        self.color= TextInput(multiline=False)
        self.add_widget(self.color)
        #Create a submit button
        self.submit = Button(text="Submit",font_size=32)
        # Bind the button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)
    
    def press(self,instance):
        name = self.name.text
        pizza = self.pizza.text #La caracteristica text del text input nos retorna el texto que ha ingresado el usuario
        color = self.color.text
        #Print in the terminal
        #print(f"Hello {name} you like {pizza} and your favorite color is {color}")
        #Print in the screen
        self.add_widget(Label(text=f"Hello {name} you like {pizza} and your favorite color is {color}"))
        #clear inputs
        self.name.text=""
        self.pizza.text=""
        self.color.text=""
        
        

class Myapp(App): #Definimos la clase de app
    def build(self):
        return MyGridLayout() 
    
if __name__=="__main__":# Comando para que la app corra
    Myapp().run()