FROM python:3.8-slim
COPY ./main.py /deploy/
COPY ./face_shape.h5 /deploy/
COPY ./templates /deploy/templates
COPY ./static /deploy/static
COPY ./requirements.txt /deploy/
WORKDIR /deploy/
RUN pip install -r requirements.txt
EXPOSE 80
EXPOSE 8000
ENTRYPOINT ["python", "main.py"]