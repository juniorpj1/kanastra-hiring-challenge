FROM node:22-alpine

RUN npm install -g vite

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

RUN npm run build

EXPOSE 8080

CMD [ "npm", "run", "dev" ]