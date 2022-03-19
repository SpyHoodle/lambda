from core import utils
import curses


class StatusBar:
    def __init__(self, instance):
        self.instance = instance
        self.mode = instance.mode.upper()
        self.file = instance.buffer.name or "[No Name]"
        self.icon = instance.config["icon"] or "λ"
        self.colors = (7, 5, 13)
        self.components = [self.icon, self.mode, self.file]

    def render(self):
        x = 1
        utils.clear(self.instance, self.instance.height - 2, 0)
        for count, component in enumerate(self.components):
            self.instance.screen.addstr(self.instance.height - 2, x, component,
                                        curses.color_pair(self.colors[count]) | curses.A_BOLD)
            x += len(component) + 1


class Components:
    def __init__(self, components: dict = None):
        self.components = components or {
            "bottom": [StatusBar],
        }

    def render(self, instance):
        for component in self.components["bottom"]:
            component(instance).render()