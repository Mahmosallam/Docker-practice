#------- build stage------
FROM golang:1.21-alpine AS build
WORKDIR /app
COPY . .
RUN go mod tidy
RUN go build -o app 

#-------- run stage---------
FROM alpine:3.21
WORKDIR /app
COPY --from=build /app/app .
EXPOSE 8080
CMD [ "./app" ]
