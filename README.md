# Basic Auth Header Generator

A small Python script that generates an HTTP `Basic Authorization` header from a username and password.

## Description

This repository contains a minimal example of how to encode credentials in the `username:password` format with Base64 and print them as a `Basic` authentication header.

The script uses only the Python standard library and does not require any external dependencies.

## Files

```text
.
├── basic_auth_header.py
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

## Requirements

- Python 3.x

## Installation

Clone the repository:

```bash
git clone https://github.com/Trachti/basic-auth-header-generator.git
cd basic-auth-header-generator
```

No packages need to be installed because the script only uses the Python standard library.

## Usage

Run the script:

```bash
python basic_auth_header.py
```

Example output:

```text
Basic dXNlcm5hbWU6cGFzc3dvcmQ=
```

## Security Notice

This script is intended for learning and demonstration purposes. Do not store real passwords, API keys, or credentials directly in source code, and do not upload them to a public GitHub repository.

For real projects, credentials should be managed through environment variables, secret managers, or other secure configuration mechanisms.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
