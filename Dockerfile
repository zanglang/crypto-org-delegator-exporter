from python:3


COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY . /

ENTRYPOINT ["python"]
CMD ["/main.py"]
