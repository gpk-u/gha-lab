FROM python:3.12-slim
WORKDIR /srv
COPY app.py .
USER 10001
EXPOSE 8080
CMD ["python", "app.py"]
