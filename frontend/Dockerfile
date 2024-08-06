FROM node:22.5.1-alpine

WORKDIR /app

COPY . .

RUN npm install
RUN npm run build
RUN npm prune --production

CMD [ "npm", "start" ]