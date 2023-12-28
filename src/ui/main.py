from customtkinter import *

from util.misc import (
    bindSettingChangeEvent,
    copyGeneratedPassword,
    generatePassword,
    updatePasswordLength,
)
from util.settings import loadSettings, setSettings


def renderGenerateSection(root) -> tuple[CTkLabel, CTkEntry, CTkButton, CTkButton]:
    generatePasswordHeading = CTkLabel(
        root,
        text="Generate Secure Password",
        font=("Arial", 14, "bold"),
    )
    passwordOuputBox = CTkEntry(
        placeholder_text="Password will appear here",
        master=root,
        width=250,
    )
    generatePasswordButton = CTkButton(
        root, width=80, text="Generate", font=("Arial", 12, "bold")
    )
    copyPasswordButton = CTkButton(
        root, width=60, text="Copy", font=("Arial", 12, "bold")
    )

    generatePasswordHeading.place(x=0, y=0)
    passwordOuputBox.place(x=0, y=30)
    generatePasswordButton.place(x=255, y=30)
    copyPasswordButton.place(x=340, y=30)

    return (
        generatePasswordHeading,
        passwordOuputBox,
        generatePasswordButton,
        copyPasswordButton,
    )


def renderSettingsSection(
    root,
) -> tuple[
    CTkLabel, CTkCheckBox, CTkCheckBox, CTkCheckBox, CTkCheckBox, CTkLabel, CTkSlider
]:
    changeSettingsHeading = CTkLabel(
        root,
        text="Change Generation Settings",
        font=("Arial", 14, "bold"),
    )
    toggleLettersCheckbox = CTkCheckBox(
        root, text="Include letters", font=("Arial", 12, "bold")
    )
    toggleUppercaseCheckbox = CTkCheckBox(
        root, text="Include uppercase letters", font=("Arial", 12, "bold")
    )
    toggleNumbersCheckbox = CTkCheckBox(
        root, text="Include numbers", font=("Arial", 12, "bold")
    )
    toggleSpecialsCheckbox = CTkCheckBox(
        root, text="Include special characters", font=("Arial", 12, "bold")
    )
    automaticCopyCheckbox = CTkCheckBox(
        root, text="Automatically copy password", font=("Arial", 12, "bold")
    )
    passwordLengthHeading = CTkLabel(
        root, text="Password Length", font=("Arial", 12, "bold")
    )
    passwordLengthSlider = CTkSlider(
        root, from_=8, to=64, number_of_steps=56, width=400
    )

    changeSettingsHeading.place(x=0, y=70)
    toggleLettersCheckbox.place(x=0, y=100)
    toggleUppercaseCheckbox.place(x=0, y=130)
    toggleNumbersCheckbox.place(x=0, y=160)
    toggleSpecialsCheckbox.place(x=0, y=190)
    automaticCopyCheckbox.place(x=0, y=220)
    passwordLengthHeading.place(x=0, y=250)
    passwordLengthSlider.place(x=0, y=280)

    return (
        changeSettingsHeading,
        toggleLettersCheckbox,
        toggleUppercaseCheckbox,
        toggleNumbersCheckbox,
        toggleSpecialsCheckbox,
        automaticCopyCheckbox,
        passwordLengthHeading,
        passwordLengthSlider,
    )


def renderMainTab(root) -> None:
    (
        generatePasswordHeading,
        passwordOuputBox,
        generatePasswordButton,
        copyPasswordButton,
    ) = renderGenerateSection(root)

    (
        changeSettingsHeading,
        toggleLettersCheckbox,
        toggleUppercaseCheckbox,
        toggleNumbersCheckbox,
        toggleSpecialsCheckbox,
        automaticCopyCheckbox,
        passwordLengthHeading,
        passwordLengthSlider,
    ) = renderSettingsSection(root)

    # Update password length heading on slider movement
    sliderActionButtons = [
        "<Button-1>",
        "<B1-Motion>",
        "<ButtonRelease-1>",
    ]
    for action in sliderActionButtons:
        passwordLengthSlider.bind(
            action,
            lambda event: updatePasswordLength(
                slider=passwordLengthSlider,
                heading=passwordLengthHeading,
            ),
        )

    # Actions for generating and copying password
    generatePasswordButton.bind(
        "<Button-1>",
        lambda event: generatePassword(passwordOuputBox, *settingsElements),
    )
    copyPasswordButton.bind(
        "<Button-1>", lambda event: copyGeneratedPassword(passwordOuputBox)
    )

    # Group all the settings elements for easier access
    settingsElements = [
        toggleLettersCheckbox,
        toggleUppercaseCheckbox,
        toggleNumbersCheckbox,
        toggleSpecialsCheckbox,
        automaticCopyCheckbox,
        passwordLengthSlider,
    ]

    localSettings = dict()
    loadSettings(localSettings)
    setSettings(
        localSettings,
        *settingsElements,
    )
    updatePasswordLength(passwordLengthSlider, passwordLengthHeading)

    # Bind changing of each setting element to save settings
    for element in settingsElements:
        bindSettingChangeEvent(
            widget=element,
            settings=localSettings,
            settingsElements=settingsElements,
        )
