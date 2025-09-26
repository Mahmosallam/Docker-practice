ARG py=3.12-alpine
##-------stage 1-------
FROM python:${py} AS build
WORKDIR /app
COPY requirements.txt .
RUN pip install --prefix=/install --no-cache-dir -r requirements.txt


#----------stage2-------
FROM python:${py}
WORKDIR /app
COPY --from=build /install /usr/local/
COPY app.py .
EXPOSE 5000
ENTRYPOINT [ "python" , "app.py" ]
