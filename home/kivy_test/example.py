from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.core.window import Window

#/////////////////////////////////////////////////////////////////#
#// In this section we manipulate the actual window of the app. //#
#// See docs for more capabilities                              //#
#/////////////////////////////////////////////////////////////////#

# Set initial window size
Window.size = (700, 350)

# Turn off ability to exit screen
Window.borderless = True

# Turn background clear
Window.clearcolor = (1, 1, 1, 1)

#////////////////////////////////////#
#// Function to print out response //#
#////////////////////////////////////#

def printout_feeling(feeling_response):

    # Printout the response once button is pushed
    print('I am feeling very {}'.format(feeling_response))


#//////////////////////////////////////////////////////////////////#
#// In this section we define the widgets that will be displayed //#
#//////////////////////////////////////////////////////////////////#

# A happy image that is designed further in the .kv file
class SadFaceWidget(Image):

    # This function is called when this widget is pressed
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            printout_feeling('sad..')

# A sad image that is designed further in the .kv file
class HappyFaceWidget(Image):

    # This function is called when this widget is pressed
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            printout_feeling('happy!!')


# Base root widget that is the parent of the two face widgets
class RootWidget(Widget):
    pass

# This is the actual app class
class ExampleApp(App):

    # This builds the rootwidget as the base of the app
    def build(self):
        return RootWidget()

#///////////////////#
#// Start the app //#
#///////////////////#

if __name__ == '__main__':
    ExampleApp().run()
