from python:3
LABEL maintainer="zanglang@gmail.com"

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
COPY . /

EXPOSE 26661
ENTRYPOINT ["python"]
CMD ["/main.py"]
