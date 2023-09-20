# Building kicad-amf-plugin

## Preparation

1. Install wxBuilder

https://github.com/wxFormBuilder/wxFormBuilder

2. Install gettext

https://mlocati.github.io/articles/gettext-iconv-windows.html

3. Install POedit

https://poedit.net/download

## Python env

Locate the python shipped with KiCad (e.g C:\Program Files\KiCad\7.0\bin\python)

```sh
cd C:\Program Files\KiCad\7.0\bin
python -m venv .venv
source .venv/scripts/activate

```

## Update translation

1. Extract po files from py

```sh
xgettext.exe xxx.py
```

2. Edit the po files in Poedit

## Debug

The **main**.py is the entry point for debugging

## Deploy
