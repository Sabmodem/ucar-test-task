# review manager app

Простое приложение на fastapi для управления отзывами. Автоматически помечает отзывы как негативные, позитивные или нейтральные. Структура проекта:
```
.
├── app.py
├── crud
│   └── reviews.py
├── database.py
├── models
│   ├── __init__.py
│   └── reviews.py
├── README.md
├── requirements.txt
├── reviews.db
├── routes
│   └── reviews.py
├── run.sh
└── services
    └── reviews.py
```

## Запуск:
```
bash
python3 -m venv env
source ./env/bin/activate
python3 -m pip install fastapi aiosqlite uvicorn # или python3 -m pip install -r requirements.txt
uvicorn main:app --reload # или ./run.sh
```

## swagger:

Откройте в браузере http://localhost:8000/docs