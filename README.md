# VK filter

Список following находится в файле backend/following.json

## backend

Предполгается что запущен экземпляр momgoDB на порте 27017. Для запуска сервера необходимо подтянуть зависимости и установить переменные окружения.

```
cd ./backend
pip install -r requirements.txt
export FLASK_APP=src
export FLASK_ENV=development
flask run
```

## frontend

```
cd ../frontend
npm i
npm start
```

## Используемые библеотеки

Для распознавания лиц использовал OpenCV. Mongoengine для интеграции DB. В качестве основного фреймворка для backend -- Flask.
