# Basic Auth Header Generator

Ein kleines Python-Skript, das aus einem Benutzernamen und einem Passwort einen HTTP-`Basic Authorization`-Header erzeugt.

## Beschreibung

Dieses Repository enthält ein minimalistisches Beispiel dafür, wie Zugangsdaten im Format `username:password` per Base64 kodiert und anschließend als `Basic`-Auth-Header ausgegeben werden.

Das Skript nutzt ausschließlich die Python-Standardbibliothek und benötigt keine externen Abhängigkeiten.

## Dateiübersicht

```text
.
├── basic_auth_header.py
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

## Voraussetzungen

- Python 3.x

## Installation

Repository klonen:

```bash
git clone https://github.com/DEIN-USERNAME/basic-auth-header-generator.git
cd basic-auth-header-generator
```

Es müssen keine Pakete installiert werden, da nur die Standardbibliothek verwendet wird.

## Verwendung

Skript ausführen:

```bash
python basic_auth_header.py
```

Beispielausgabe:

```text
Basic dXNlcm5hbWU6cGFzc3dvcmQ=
```

## Sicherheitshinweis

Dieses Skript ist ein Lern- und Demonstrationsbeispiel. Speichere keine echten Passwörter, API-Schlüssel oder Zugangsdaten direkt im Quellcode und lade sie nicht öffentlich auf GitHub hoch.

Für echte Projekte sollten Zugangsdaten zum Beispiel über Umgebungsvariablen, Secret-Manager oder sichere Konfigurationsmechanismen verwaltet werden.

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Details findest du in der Datei `LICENSE`.
