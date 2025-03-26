```sh
FROM python:3-alpine
WORKDIR /src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . ./
RUN ln -sf /dev/stdout /src/app.log \
    && ln -sf /dev/stderr /src/error.log
EXPOSE 5000
ENTRYPOINT [z"python3", "src/app.py"]
```
