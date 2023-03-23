FROM python:3.8.10-buster

WORKDIR /app

COPY freez  freez

RUN pip install --no-cache --user -r freez

COPY . .

EXPOSE 5000

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]