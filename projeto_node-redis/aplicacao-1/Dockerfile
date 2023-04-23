FROM node:alpine

WORKDIR /usr/src/app

COPY ./package*.json ./

RUN apk add npm

COPY ./server.js ./

CMD ["npm", "start"]