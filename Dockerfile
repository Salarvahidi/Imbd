FROM python:3.12.3-bookworm

WORKDIR /code

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1

COPY requierments.txt /code/

RUN apt-get update && apt-get upgrade -y \
    && apt-get install redis -y \
RUN pip3 install -U pip
RUN pip3 install -r requirements.txt

COPY . /code/

COPY entrypoint.sh /code/

RUN sed -i 's/\r$//g' /code/entrypoint.sh
RUN chmod +x /code/entrypoint.sh

ENTRYPOINT ["/code/entrypoint.sh"]