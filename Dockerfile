FROM python:3.6-alpine as bigimage
RUN apk add --no-cache linux-headers g++
RUN pip wheel --wheel-dir=/root/wheels uwsgi


FROM python:3.6-alpine as smallimage
COPY --from=bigimage /root/wheels /root/wheels
WORKDIR /src
COPY ./requirements.txt .
RUN pip3 install --find-links=/root/wheels -r requirements.txt --no-cache-dir
COPY . .
EXPOSE 8080
ENV AM_I_IN_A_CONTAINER="True"
ENTRYPOINT ["uwsgi"]
CMD ["--http", "0.0.0.0:8080", "--wsgi-file", "/src/app.py", "--callable", "app"]
