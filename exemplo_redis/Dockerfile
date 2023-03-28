# define a imagem base
FROM alpine

# baixa e instala as dependências
RUN apk add --update redis

RUN apk add --update gcc

# descreve o que deve ser feito ao iniciar o computador
CMD ["redis-server"]