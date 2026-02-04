FROM node:20-alpine AS builder

WORKDIR /app
RUN npm install -g bun
COPY frontend/package.json frontend/bun.lock ./
RUN bun install --frozen-lockfile
COPY frontend/ .
RUN bun run build

FROM node:20-alpine
WORKDIR /app
COPY --from=builder /app/build ./build
COPY --from=builder /app/package.json .

EXPOSE 3000

CMD [ "node", "build" ]
