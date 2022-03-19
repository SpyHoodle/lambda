from core import cursors, modes


def execute(instance, key):
    # Enter key
    if key == 27:
        # Switch to normal mode
        modes.activate(instance, "normal")


def activate(instance):
    # Switch the cursor to a line
    cursors.cursor_mode("line")
