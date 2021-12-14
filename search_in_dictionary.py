import deep_translator.exceptions
from bs4 import BeautifulSoup
import requests
from deep_translator import GoogleTranslator


class SearchInDict:
    def __init__(self, options, word):
        self.selected_options = options
        self.word = word
        self.result_in_en = self.search()
        self.result_in_pl = self.translate()

    def search(self):
        link = "http://www.kingjamesbibledictionary.com/Dictionary/" + self.word.lower()

        response = requests.get(link)
        soup = BeautifulSoup(response.text, "html.parser")

        title_list = soup.find_all(class_="defdct")
        text_list = soup.find_all(class_="deftxt")

        index = [title_list.index(title) for title in title_list if title.get_text() in self.selected_options]

        finded_titles = [title.get_text() for title in title_list if title.get_text() in self.selected_options]
        finded_txt = [text.get_text() for text in text_list if text_list.index(text) in index]

        results = []
        try:
            for title in finded_titles:
                results.append([title, finded_txt[finded_titles.index(title)]])
        except IndexError:
            results.append(["Brak wyników", ""])

        return results

    def translate(self):
        translator = GoogleTranslator(source="en", target="pl")
        try:
            return [translator.translate(text[1]) for text in self.result_in_en]
        except deep_translator.exceptions.NotValidPayload:
            return ["Tłumacz przyjmuje maksymalnie 5000 znaków" for _ in range(len(self.result_in_en))]
