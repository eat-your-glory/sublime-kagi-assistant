import sublime
import sublime_plugin
import webbrowser
from urllib.parse import quote

FOCUS_OPTIONS = {
    "Web": "web",
    "Academic": "academic",
    "Writing": "writing",
    "Math": "math",
}


class AskPerplexityCommand(sublime_plugin.WindowCommand):
    def run(self, focus, query):
        url = "https://www.perplexity.ai/search?q={}&focus={}".format(
            quote(query), focus
        )
        webbrowser.open(url)

    def input(self, args):
        return FocusInputHandler()


class FocusInputHandler(sublime_plugin.ListInputHandler):
    def __init__(self):
        super().__init__()
        self.last_focus = None

    def placeholder(self):
        return "Select focus"

    def initial_text(self):
        if self.last_focus:
            return self.last_focus

        # TODO: add settings for default option
        # settings = sublime.load_settings("AskPerplexity.sublime-settings")
        # default_focus = settings.get("perplexity_focus")
        # if default_focus in FOCUS_OPTIONS.values():
        #     return default_focus

    def confirm(self, focus):
        self.last_focus = focus
        return focus

    def list_items(self):
        order = ["Web", "Academic", "Math", "Writing"]
        ordered_items = [(key, FOCUS_OPTIONS[key]) for key in order]
        return list(ordered_items)

    def next_input(self, args):
        return QueryInputHandler()


class QueryInputHandler(sublime_plugin.TextInputHandler):
    def placeholder(self):
        return "Enter your question"
