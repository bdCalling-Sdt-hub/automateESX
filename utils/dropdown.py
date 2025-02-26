import autoit
import time

def select_dropdown_option(button_text, option_text):
    """
    Finds the currently active window, clicks a button with the given text to open a dropdown, 
    and selects the specified option.

    :param button_text: Visible text of the button to open the dropdown
    :param option_text: The dropdown option to select
    """

    # Get the currently active window
    window_title = autoit.win_get_title("")
    if not window_title:
        print("No active window found.")
        return

    print(f"Detected active window: {window_title}")

    # # Click the button (uses visible text)
    # autoit.control_click(window_title, button_text)
    # time.sleep(1)  # Wait for dropdown to open

    # Select the correct option from the dropdown
    autoit.control_command(window_title, "ComboBox1", "SelectString", option_text)
    time.sleep(1)  # Ensure selection happens

    # Press Enter to confirm selection (if required)
    autoit.send("{ENTER}")

    print(f"Selected '{option_text}' from dropdown in '{window_title}'")


