# review manager app

Простое приложение на fastapi для управления отзывами. Автоматически помечает отзывы как негативные, позитивные или нейтральные. Структура проекта:
```bash
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
```bash
python3 -m venv env
source ./env/bin/activate
python3 -m pip install fastapi aiosqlite uvicorn # или python3 -m pip install -r requirements.txt
uvicorn main:app --reload # или ./run.sh
```

## swagger:
Откройте в браузере http://localhost:8000/docs

## Запросы curl
```bash
sabmodem@debian> curl -X 'POST' \                                                                                                                                                                            ~/projects/ucar-test-app
  'http://localhost:8000/reviews' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "review 1. Плохо"
}'; echo "";
{"id":1,"text":"review 1. Плохо","sentiment":"NEGATIVE","created_at":"2025-08-01T23:25:52.805976"}

sabmodem@debian> curl -X 'POST' \                                                                                                                                                                            ~/projects/ucar-test-app
  'http://localhost:8000/reviews' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "review 2. Хорошо"
}'; echo "";
{"id":2,"text":"review 2. Хорошо","sentiment":"POSITIVE","created_at":"2025-08-01T23:26:07.479013"}

sabmodem@debian> curl -X 'POST' \                                                                                                                                                                            ~/projects/ucar-test-app
  'http://localhost:8000/reviews' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "review 3"        
}'; echo "";
{"id":3,"text":"review 3","sentiment":"NEUTRAL","created_at":"2025-08-01T23:26:14.739620"}

sabmodem@debian> curl -X 'GET' \                                                                                                                                                                       ~/projects/ucar-test-app
  'http://localhost:8000/reviews' \
  -H 'accept: application/json'; echo "";
[{"id":1,"text":"review 1. Плохо","sentiment":"NEGATIVE","created_at":"2025-08-01T23:25:52.805976"},{"id":2,"text":"review 2. Хорошо","sentiment":"POSITIVE","created_at":"2025-08-01T23:26:07.479013"},{"id":3,"text":"review 3","sentiment":"NEUTRAL","created_at":"2025-08-01T23:26:14.739620"}]

sabmodem@debian> curl -X 'GET' \                                                                                                                                                                             ~/projects/ucar-test-app
  'http://localhost:8000/reviews?sentiment=POSITIVE' \
  -H 'accept: application/json'; echo "";
[{"id":2,"text":"review 2. Хорошо","sentiment":"POSITIVE","created_at":"2025-08-01T23:26:07.479013"}]

sabmodem@debian> curl -X 'GET' \                                                                                                                                                                             ~/projects/ucar-test-app
  'http://localhost:8000/reviews?sentiment=NEGATIVE' \
  -H 'accept: application/json'; echo "";
[{"id":1,"text":"review 1. Плохо","sentiment":"NEGATIVE","created_at":"2025-08-01T23:25:52.805976"}]

sabmodem@debian> curl -X 'GET' \                                                                                                                                                                             ~/projects/ucar-test-app
  'http://localhost:8000/reviews?sentiment=NEUTRAL' \
  -H 'accept: application/json'; echo "";
[{"id":3,"text":"review 3","sentiment":"NEUTRAL","created_at":"2025-08-01T23:26:14.739620"}]
```