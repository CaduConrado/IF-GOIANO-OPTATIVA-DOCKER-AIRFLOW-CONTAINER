#Especificar a imagem base
FROM alpine
#FROM node:alpine

WORKDIR /usr/app

COPY ./package.json ./
RUN apk add npm

COPY ./ ./

#Comando Padrão

CMD ["npm", "start"]