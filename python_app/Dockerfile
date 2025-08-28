# FROM python:alpine3.21
# WORKDIR /app
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
# COPY app.py .
# EXPOSE 5000
# ENTRYPOINT [ "python" , "app.py" ]

#-------stage 1-------
FROM python:alpine3.21 AS build
WORKDIR /app
COPY requirements.txt .
RUN pip install --prefix=/install --no-cache-dir -r requirements.txt


#----------stage2-------
FROM python:3.12-alpine
WORKDIR /app
COPY --from=build /install /usr/local
COPY app.py .
EXPOSE 5000
ENTRYPOINT [ "python" , "app.py" ]
