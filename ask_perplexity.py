import sublime
import sublime_plugin
import webbrowser
from urllib.parse import quote


class AskPerplexityCommand(sublime_plugin.WindowCommand):
    def run(self, focus, query):
        url = f"https://www.perplexity.ai/search?q={quote(query)}&focus={focus}"
        webbrowser.open(url)
    
    def input(self, args):
        if "query" in args:
            return None

        if "focus" in args:
            return QueryInputHandler()

        settings = sublime.load_settings("Preferences.sublime-settings")
        default_focus = settings.get("perplexity_focus")

        if default_focus:
            args["focus"] = default_focus
            return QueryInputHandler()

        return FocusInputHandler()


class FocusInputHandler(sublime_plugin.ListInputHandler):
    def name(self):
        return "focus"

    def placeholder(self):
        return "Select focus"

    def list_items(self):
        return [
            ("Web", "web"),
            ("Academic", "academic"),
            ("Writing", "writing"),
            ("Math", "math"),
        ]

    def next_input(self, args):
        return QueryInputHandler()


class QueryInputHandler(sublime_plugin.TextInputHandler):
    def name(self):
        return "query"

    def placeholder(self):
        return "Enter your question"
