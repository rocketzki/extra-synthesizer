## Ulepszony Syntezator Mowy (extra-synthesizer v0.0.1)

Analyzing, transforming human speech and interpreting user data input application.

##Manual (PL)

Środowiskiem uruchomieniowym aplikacji jest Python w wersji 3.7. Ścieżka, w której znajduje się Python 3.7 powinna, dla wygody być przechowana w zmiennej środowiskowej `PYTHONPATH`, a ta wpisana do zmiennej środowiskowej `PATH`.
 
Na początku należy zainstalować biblioteki za pomocą narzędzia pip bądź conda. Tutaj użyto narzędzia pip.
Jeśli lokalna dystrybucja Python nie ma narzędzia pip należy go zainstalować wg instrukcji na stronie: https://pip.pypa.io/en/latest/installing/#installing-with-get-pip-py

1. Instalujemy moduł django komendą: `python -m pip install Django`

2. Kolejno instalujemy moduły:
    ```commandline
   python -m pip install librosa
   python -m pip install scipy
   python -m pip install numpy
   python -m pip install SoundFile
   python -m pip install PyEnchant
   python -m pip install matplotlib   
    ```
3. Nalezy dodać słownik języka polskiego pobrany ze strony: https://sjp.pl/slownik/ort/sjp-myspell-pl-20200916.zip (bądź inną, ostatnią wersję z https://sjp.pl/slownik/ort/) do katalogu zawierającego bibliotekę hunspell.
Wystarczy przekopiować zawartość podarchum PL_pl.zip do katalogu: `%PYTHONPATH%\Lib\site-packages\enchant\data\mingw32\share\enchant\hunspell`

4. Należy ustawić klucz google api dla syntezatora mowy i przypisać go do zmiennej `KEY` w pliku konfiguracyjnym `extra_synthesizer\settings.py`
    ### Uwaga
    Na koncie google musi być aktywowana usługa Google Text-To-Speech API: https://console.cloud.google.com/apis/library/texttospeech.googleapis.com?q=text%20to%20speech - wchodzimy na ten link, wybieramy z górnej belki projekt (jeśli nie mamy żadnego, tworzymy go), a nastepnie klikamy na przycisk `Włącz`.
    Następnie tworzymy klucz API. Instrukcja utworzenia klucza dla darmowej wersji próbnej usługi Google Text-To-Speech API znajduje się na stronie: https://developers.google.com/maps/documentation/javascript/get-api-key


Aplikację uruchamiamy komendą: `python manage.py runserver` i wchodzimy w przeglądarce na adres: http://127.0.0.1:8000/synthesizer/
Aby zsyntetyzowany plik został zapisany (domyślnie w folderze `resources\target`), należy zmienić flagę SHOULD_SAVE_LOCALLY z pliku `app\view.py` na `True`.

Jeśli otwieramy projekt w programie PyCharm, wystarczy załadować konfigurację z pliku `.run\extra_talker.run.xml` i uruchomić konfigurację `extra_talker`


######developed by Michał Markieta
