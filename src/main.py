from rich.console import Console
from rich.traceback import install
from customtkinter import *

from util.misc import *
from ui.main import *

install()
console = Console()


def configureApp():
    app = CTk()

    app.geometry("420x360")
    app.title("Secure Password Generator")
    app.resizable(False, False)
    app.bind("<Escape>", lambda event: closeApp(app, event=event))
    set_default_color_theme("dark-blue")

    return app


def configureTabsContainer(root):
    tabsContainer = CTkTabview(root)
    tabsContainer.add("Generate Password")
    tabsContainer.pack(fill="both", expand=True)

    return tabsContainer


def main():
    app = configureApp()

    tabsContainer = configureTabsContainer(app)
    mainTab = tabsContainer.tab("Generate Password")

    renderMainTab(mainTab)

    app.mainloop()


if __name__ == "__main__":
    main()
