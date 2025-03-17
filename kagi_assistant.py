import sublime
import sublime_plugin
import webbrowser
from urllib.parse import quote

MODEL_OPTIONS = {
    "Claude 3.7 Sonnet": "claude-3-sonnet",
    "o3 mini": "o3-mini",
    "GPT 4o": "gpt-4o",
    "DeepSeek R1": "deepseek-r1",
}


class KagiAssistantCommand(sublime_plugin.WindowCommand):
    def run(self, model, query):
        url = "https://kagi.com/assistant?q={}&profile={}".format(
            quote(query), model
        )
        webbrowser.open(url)

    def input(self, args):
        return ModelInputHandler()


class ModelInputHandler(sublime_plugin.ListInputHandler):
    def __init__(self):
        super().__init__()
        self.last_model = None

    def placeholder(self):
        return "Select model"

    def initial_text(self):
        if self.last_model:
            return self.last_model

        # TODO: add settings for default option
        # settings = sublime.load_settings("AskPerplexity.sublime-settings")
        # default_focus = settings.get("perplexity_focus")
        # if default_focus in FOCUS_OPTIONS.values():
        #     return default_focus

    def confirm(self, model):
        self.last_model = model
        return model

    def list_items(self):
        order = ["Claude 3.7 Sonnet", "o3 mini", "GPT 4o", "DeepSeek R1"]
        ordered_items = [(key, MODEL_OPTIONS[key]) for key in order]
        return list(ordered_items)

    def next_input(self, args):
        return QueryInputHandler()


class QueryInputHandler(sublime_plugin.TextInputHandler):
    def placeholder(self):
        return "Enter your question"
