# input n divise
import pygtk
pygtk.require('2.0')
import gtk

def on_button_clicked(widget, data=None):
    print("Button clicked!")

def create_window():
    # Create a new window
    window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    window.set_title("GTK2 Test Window")
    window.set_size_request(300, 200)
    window.connect("delete_event", gtk.main_quit)

    # Create a button
    button = gtk.Button("Click Me")
    button.connect("clicked", on_button_clicked)

    # Add the button to the window
    window.add(button)

    # Display everything
    button.show()
    window.show()

def main():
    create_window()
    gtk.main()

if __name__ == "__main__":
    main()
