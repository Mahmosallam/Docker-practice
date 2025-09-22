# FROM node:18-alpine
# WORKDIR /app
# COPY package*.json .
# RUN npm install --no-cache
# COPY . .
# RUN npm run build
# CMD [ "npm" , "start" ]


#-----------stage 1----------------------------
FROM node:18-alpine AS build
WORKDIR /app
COPY package*.json .
RUN npm ci --no-cache
COPY . .
RUN npm run build

#-----------stage2---------------
FROM node:18-alpine
WORKDIR /app
COPY package*.json .
RUN npm ci --only=production --no-cache
COPY --from=build /app/dist ./dist
RUN adduser -S sallam -u 1001 && \
    addgroup -S sallam -g 1001 && \
    chown -R sallam:sallam /app/
USER sallam
EXPOSE 3000
CMD [ "npm" , "start" ]




