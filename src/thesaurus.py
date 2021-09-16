import requests
from bs4 import BeautifulSoup
import re
import unidecode

__all__ = ["larousse", "cnrtl"]


def _larousse(mot):
    mot = unidecode.unidecode(mot)
    r = requests.get(
        f"https://www.larousse.fr/dictionnaires/francais/{mot}/",
        allow_redirects=True,
    )
    r.encoding = r.apparent_encoding
    bs = BeautifulSoup(r.text, "html.parser")
    valid_container = bs.find(
        "p", string=["Contraires :", "Contraire :", "Synonymes :", "Synonyme :"]
    )
    if valid_container == None:
        return ()
    valid_container_2 = valid_container.find_parent("ul", class_="Definitions")
    definitions_headers = valid_container_2.find_all("li", class_="DivisionDefinition")
    defnum = 0
    for header in definitions_headers:
        defnum += 1
        defsyn = "syn-" + str(defnum)
        defant = "ant-" + str(defnum)
        if header.find("span", class_="ExempleDefinition") == None:
            exemple = ""
        else:
            exemple = '"' + header.find("span", class_="ExempleDefinition").text + '"\n'
        synonyms_header = header.find("p", string=["Synonymes :", "Synonyme :"])
        antonyms_header = header.find("p", string=["Contraires :", "Contraire :"])
        if synonyms_header == None:
            pass
        else:
            yield defsyn, (
                exemple
                + synonyms_header.find_next("p").text
            )
        if antonyms_header == None:
            pass
        else:
            yield defant, (
                '"'
                + header.find("span", class_="ExempleDefinition").text
                + '"\n'
                + antonyms_header.find_next("p").text
            )


def _cnrtl(mot):
    r1 = requests.get(f"https://cnrtl.fr/synonymie/{mot}//1?ajax=true#")
    r2 = requests.get(f"https://cnrtl.fr/antonymie/{mot}//1?ajax=true#")
    r1.encoding = r1.apparent_encoding
    r2.encoding = r2.apparent_encoding
    bs1 = BeautifulSoup(r1.text, "html.parser")
    bs2 = BeautifulSoup(r2.text, "html.parser")
    synonyms_headers = bs1.find_all("td", {"class": "syno_format"})
    antonyms_headers = bs2.find_all("td", {"class": "anto_format"})
    if synonyms_headers == None and antonyms_headers == None:
        return ()
    defnum = 0
    if synonyms_headers == None:
        pass
    else:
        for syn in synonyms_headers:
            defnum += 1
            defsyn = "syn-" + str(defnum)
            yield defsyn, (syn.findChildren("a")[0].text.strip())
    if antonyms_headers == None:
        pass
    else:
        for ant in antonyms_headers:
            defnum += 1
            defant = "ant-" + str(defnum)
            yield defant, (ant.findChildren("a")[0].text.strip())


def larousse(mot):
    return list(_larousse(mot))


def cnrtl(mot):
    return list(_cnrtl(mot))
