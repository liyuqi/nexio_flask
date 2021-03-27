# FROM python:3.7-alpine
# LABEL MAINTAINER Yuqi Li <am997liyuqi@gmail.com>
# WORKDIR /code
# ENV FLASK_APP=app.py
# ENV FLASK_RUN_HOST=0.0.0.0
# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt
# EXPOSE 5000
# COPY . .
# CMD ["flask", "run"]


FROM alpine
RUN apk add --no-cache python3-dev && pip3 install --upgrade pip
WORKDIR /app
COPY /requirements.txt /app
RUN pip3 install -r requirements.txt
COPY ["mongoAPI.py", "/app"]
EXPOSE 5001
ENTRYPOINT [ "python3" ]
CMD ["mongoAPI.py"]