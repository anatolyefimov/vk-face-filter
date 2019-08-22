FROM python:3

WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP src
ENV FLASK_ENV development

CMD ["flask", "run"]