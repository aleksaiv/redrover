FROM node:20-alpine

WORKDIR /tmp
COPY app/front/package.json ./
RUN npm install --loglevel verbose

