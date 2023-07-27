from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        # Creating the main layout (a BoxLayout in this case)
        layout = BoxLayout(orientation='vertical', padding=20)

        # Adding a Label widget to display a greeting message
        greeting_label = Label(text="Hello, welcome to my Kivy project!", font_size=24)
        layout.add_widget(greeting_label)

        # Adding two Button widgets for Snake and Pong games
        snake_button = Button(text="Play Snake", size_hint=(None, None), size=(150, 50), font_size=20)
        snake_button.bind(on_press=self.play_snake)  # Binding the Snake game method to the button
        layout.add_widget(snake_button)

        pong_button = Button(text="Play Pong", size_hint=(None, None), size=(150, 50), font_size=20)
        pong_button.bind(on_press=self.play_pong)  # Binding the Pong game method to the button
        layout.add_widget(pong_button)

        return layout

    def play_snake(self, instance):
        # Method to start the Snake game
        print("Starting Snake game...")

        # Call your Snake game method here or navigate to the Snake game screen

    def play_pong(self, instance):
        # Method to start the Pong game
        print("Starting Pong game...")
        import pong
        pong.main()
        # Call your Pong game method here or navigate to the Pong game screen

if __name__ == '__main__':
    MyApp().run()
