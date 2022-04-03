FROM python:3.9-slim
COPY ./app.py /deploy/
COPY ./face_shape.h5 /deploy/
COPY ./templates /deploy/templates
COPY ./static /deploy/static
COPY ./requirements.txt /deploy/
WORKDIR /deploy/
RUN pip install -r requirements.txt
EXPOSE 80
EXPOSE 8000
ENTRYPOINT ["python", "app.py"]
