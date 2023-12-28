from os import path
from rich.console import Console
from rich.traceback import install
from customtkinter import *
import json

install()
console = Console()


def loadSettingsData():
    currentDir = path.dirname(path.abspath(__file__))
    settingsPath = path.join(currentDir, "..", "..", "data", "settings_cache.json")

    try:
        with open(settingsPath, "r") as settingsFile:
            return json.load(settingsFile)
    except Exception as e:
        console.log("[red]Failed to load settings file[/red]")
        return {
            "includeLetters": True,
            "includeUppercase": True,
            "includeNumbers": True,
            "includeSymbols": True,
            "autoCopy": False,
            "length": 32,
        }


def loadSettings(settings):
    data = loadSettingsData()
    (
        settings["includeLetters"],
        settings["includeUppercase"],
        settings["includeNumbers"],
        settings["includeSymbols"],
        settings["autoCopy"],
        settings["length"],
    ) = (
        data["includeLetters"],
        data["includeUppercase"],
        data["includeNumbers"],
        data["includeSymbols"],
        data["autoCopy"],
        data["length"],
    )


def setSettings(
    settings: dict,
    includeLetters: CTkCheckBox,
    includeUppercase: CTkCheckBox,
    includeNumbers: CTkCheckBox,
    includeSymbols: CTkCheckBox,
    autoCopy: CTkCheckBox,
    outputLength: CTkSlider,
):
    includeLetters.select() if settings["includeLetters"] else includeLetters.deselect()
    includeUppercase.select() if settings[
        "includeUppercase"
    ] else includeUppercase.deselect()
    includeNumbers.select() if settings["includeNumbers"] else includeNumbers.deselect()
    includeSymbols.select() if settings["includeSymbols"] else includeSymbols.deselect()
    autoCopy.select() if settings["autoCopy"] else autoCopy.deselect()
    outputLength.set(settings["length"])


def saveSettings(
    settings,
    includeLetters: CTkCheckBox,
    includeUppercase: CTkCheckBox,
    includeNumbers: CTkCheckBox,
    includeSymbols: CTkCheckBox,
    autoCopy: CTkCheckBox,
    outputLength: CTkSlider,
):
    settings["includeLetters"] = includeLetters.get()
    settings["includeUppercase"] = includeUppercase.get()
    settings["includeNumbers"] = includeNumbers.get()
    settings["includeSymbols"] = includeSymbols.get()
    settings["autoCopy"] = autoCopy.get()
    settings["length"] = int(outputLength.get())

    saveSettingsData(settings)


def saveSettingsData(settings):
    currentDir = path.dirname(path.abspath(__file__))
    settingsPath = path.join(currentDir, "..", "..", "data", "settings_cache.json")

    try:
        with open(settingsPath, "w") as settingsFile:
            json.dump(settings, settingsFile)
    except Exception as e:
        console.log("[red]Failed to save settings file[/red]")
