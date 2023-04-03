# rime-marinator
A group project producing a rhyming dictionary out of a corpus (of Polish songs)

Poniżej przedstawiam plan działania:
## Struktura
* GUI
* * Wskazanie jednego folderu
* * albo pozwolenie na tworzenie plików tekstowych
* * Żadne wyszukiwarki ani API, darujemy sobie
* Język: Python, biblioteka NLTK czy jak jej tam + biblioteka do GUI (Tkinter) + coś do rozbicia tekstu do IPA
* Wykrywanie rymów. Opcja:
* * Podzbiór zbioru rymów
* * Podobieństwo wyrazów (litery, głoski)
* Rym rymowi nierówny
* * Któryś zostanie na lodzie
* Tryby
* * Zachowawczo - trzy ostatnie sylaby w wersie
* * plus środek wersu
* * 4 wersy plus minus - otoczenie
* * Wszystkie tokeny jak leci (przetestować dla stop words)
* być może pokolorowanie wykrytych rymów w korpusie
* Zapis tych wykrytych rymów (format: słowo1 słowo2 ile_razy)
* * CSV wystarczy, żaden YAML czy JSON
## Plan działania

### Termin ostateczny: 20 czerwca
2 i pół miesiąca

Janek:
* Testy jednostkowe
* GUI

Ja:
* 1-3 strony PDF pitchu i tam, kto co robi
* NLTK i tak dalej
* zgromadzenie materiałów do testów
