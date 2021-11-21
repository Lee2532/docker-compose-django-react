FROM node:16.13.0


WORKDIR /app/frontend

COPY package.json ./

RUN npm install

COPY ./ ./

CMD ["npm","run" ,"start"]
