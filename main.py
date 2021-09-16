from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
from ulauncher.api.shared.action.DoNothingAction import DoNothingAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from src.thesaurus import cnrtl, larousse
import random

STRING_resulticonfile = "images/iconsyn.png"
STRING_ulauncherquery = None
STRING_currentsrc = None
LIST_suggestions = {}
STRING_currentcat = None
STRING_notcurrentcat = None
LIST_currentresults = []
INT_currentposition = 0
INT_entereventmode = None



def no_input_item():
    global STRING_resulticonfile, STRING_currentsrc
    return [
        ExtensionResultItem(
            icon=STRING_resulticonfile, name="Pas de réponse sur " + STRING_currentsrc + ".fr", on_enter=DoNothingAction()
        )
    ]

def show_source_item():
    global STRING_currentsrc, STRING_notcurrentcat
    if STRING_currentsrc == "larousse":
        STRING_notcurrentsrc = "cnrtl"
    else:
        STRING_notcurrentsrc = "larousse"
    return [
        ExtensionResultItem(
            icon="images/iconswitch.png",
            name="",
            description="Cliquer/Entrer ici pour basculer vers les résultats " + STRING_notcurrentsrc + ".fr\nAlt+Entrer pour basculer vers les " + STRING_notcurrentcat,
            on_enter=ExtensionCustomAction(2, keep_app_open=True),
            on_alt_enter=ExtensionCustomAction(1, keep_app_open=True)
        )
    ]

def show_header_item():
    global STRING_resulticonfile, LIST_currentresults, STRING_notcurrentcat
    if len(LIST_currentresults) > 10:
        return [
            ExtensionResultItem(
                icon="images/icon.png",
                name=str(len(LIST_currentresults)) + " résultats sur " + STRING_currentsrc + " .fr :   " + "\U0001F500",
                description="Cliquer/Entrer ici pour les résultats suivants\nAlt+Entrer pour basculer vers les " + STRING_notcurrentcat,
                on_enter=ExtensionCustomAction(0, keep_app_open=True),
                on_alt_enter=ExtensionCustomAction(1, keep_app_open=True)
            )
        ]
    else:
        return [
            ExtensionResultItem(
                icon="images/icon.png",
                name=str(len(LIST_currentresults)) + " résultats sur " + STRING_currentsrc + " .fr :",
                description="Alt+Entrer pour basculer vers les " + STRING_notcurrentcat,
                on_enter=DoNothingAction(),
                on_alt_enter=ExtensionCustomAction(1, keep_app_open=True)
            )
        ]


def show_suggestion_items():
    global STRING_resulticonfile, LIST_currentresults, INT_currentposition
    if not LIST_currentresults:
        return [
            ExtensionResultItem(
                icon=STRING_resulticonfile,
                name="Pas de réponse",
                on_enter=DoNothingAction(),
                description="Alt+Entrer pour basculer vers les Antonymes",
                on_alt_enter=ExtensionCustomAction(1, keep_app_open=True),
            )
        ]
    elif len(LIST_currentresults) < 11:
        return [
            ExtensionResultItem(
                icon=STRING_resulticonfile,
                name=result,
                on_enter=CopyToClipboardAction(result),
                description="\n\nCliquer/Entrer ici pour copier ce résultat" if ("\n" in result) else "Cliquer/Entrer ici pour copier ce résultat",
                on_alt_enter=ExtensionCustomAction(1, keep_app_open=True),
            )
            for result in LIST_currentresults
        ]
    else:
        while INT_entereventmode == 0:
            INT_currentposition += 10
            if INT_currentposition > len(LIST_currentresults):
                INT_currentposition = 0
            SYN_END_POSITION = INT_currentposition + 10
            return [
                ExtensionResultItem(
                    icon=STRING_resulticonfile,
                    name=result,
                    on_enter=CopyToClipboardAction(result),
                    description="\n\nCliquer/Entrer ici pour copier ce résultat" if ("\n" in result) else "Cliquer/Entrer ici pour copier ce résultat",
                    on_alt_enter=ExtensionCustomAction(1, keep_app_open=True),
                )
                for result in LIST_currentresults[INT_currentposition:SYN_END_POSITION]
            ]
        return [
            ExtensionResultItem(
                icon=STRING_resulticonfile,
                name=result,
                on_enter=CopyToClipboardAction(result),
                description="\n\nCliquer/Entrer ici pour copier ce résultat" if ("\n" in result) else "Cliquer/Entrer ici pour copier ce résultat",
                on_alt_enter=ExtensionCustomAction(1, keep_app_open=True),
            )
            for result in LIST_currentresults[0:9]
        ]


class SynFrExtension(Extension):
    def __init__(self):
        super(SynFrExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        query = event.get_argument() or str()
        if len(query.strip()) == 0:
            return RenderResultListAction(no_input_item())
        global STRING_ulauncherquery, STRING_resulticonfile, STRING_currentsrc, LIST_suggestions, STRING_currentcat, LIST_currentresults, INT_currentposition, STRING_notcurrentcat
        STRING_resulticonfile = "images/iconsyn.png"
        STRING_currentsrc = extension.preferences["thesaurus_src"]
        STRING_ulauncherquery = query
        LIST_suggestions = dict(eval(STRING_currentsrc)(STRING_ulauncherquery))
        STRING_currentcat = "syn"
        STRING_notcurrentcat = "Antonymes"
        LIST_currentresults = [
            (value)
            for key, value in LIST_suggestions.items()
            if key.startswith(STRING_currentcat)
        ]
        INT_currentposition = 0
        return RenderResultListAction(show_header_item() + show_suggestion_items() + show_source_item())


class ItemEnterEventListener(EventListener):
    def on_event(self, event, extension):
        global STRING_ulauncherquery, STRING_resulticonfile, STRING_currentsrc, LIST_suggestions, STRING_currentcat, LIST_currentresults, INT_entereventmode, STRING_notcurrentcat
        INT_entereventmode = event.get_data()
        if INT_entereventmode == 0:
            return RenderResultListAction(show_header_item() + show_suggestion_items() + show_source_item())
        elif INT_entereventmode == 2:
            if STRING_currentsrc == "larousse":
                STRING_currentsrc = "cnrtl"
            else:
                STRING_currentsrc = "larousse"
            LIST_suggestions = dict(eval(STRING_currentsrc)(STRING_ulauncherquery))
            LIST_currentresults = [
                (value)
                for key, value in LIST_suggestions.items()
                if key.startswith(STRING_currentcat)
            ]
            INT_currentposition = 0
            return RenderResultListAction(show_header_item() + show_suggestion_items() + show_source_item())
        else:
            if STRING_currentcat == "syn":
                STRING_currentcat = "ant"
                STRING_resulticonfile = "images/iconant.png"
                STRING_notcurrentcat = "Synonymes"
            else:
                STRING_currentcat = "syn"
                STRING_resulticonfile = "images/iconsyn.png"
                STRING_notcurrentcat = "Antonymes"
            LIST_currentresults = [
                (value)
                for key, value in LIST_suggestions.items()
                if key.startswith(STRING_currentcat)
            ]
            return RenderResultListAction(show_header_item() + show_suggestion_items() + show_source_item())


if __name__ == "__main__":
    SynFrExtension().run()