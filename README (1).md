# LMS
LMS
# Requirements:
- [Python 3.12+](https://www.python.org/downloads/release/python-3120/)
- [Vs code 1.95.3](https://code.visualstudio.com/updates/v1_95). Open vs code --> Extension --> Install Django v1.15.0
# Installation

- Clone the repo with

```bash
https://github.com/
```

## Tạo môi trường ảo (virtual environment)

```bash
python -m venv venv
```

## Active môi trường ảo

```bash
venv\Scripts\activate
```

(Inactive) `$ deactivate`
- Create and activate a python virtual environment

```bash
pip install -r requirements.txt
```
- Create a .env file inside the root directory
- Copy and paste everything in the .env.example file into the .env file. Then, edit the variable values
```bash
python manage.py migrate
```

```bash
python manage.py createsuperuser
```

```bash
python manage.py runserver
```

Finally, open the browser http://127.0.0.1:8000
