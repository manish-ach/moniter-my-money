# Budget-tracker (Svelte+django)

APP in progress.

<img width="1470" height="855" alt="image" src="https://github.com/user-attachments/assets/c6698740-fddd-4506-afb0-da8fde76db79" />


# Run it yourself

- `git clone https://github.com/manish-ach/moniter-my-money.git`
- `cd monitor-my-money`
- `docker compose up --build`
- go to site `http://0.0.0.0:3000/` [http://localhost:3000]

note: Ensure docker is running before docker compose. I have been testing locally for hot-reloading, docker should run as well but havent tested it properly
if it doesnt work as intented, do:
```
docker compose down -v && docker compose up --build
```

**note**: As of commit `bd37cc0`, the build artifacts are automated to dockerhub on any git push through github actions CI. So you can run this program through docker. Either,

- create a `docker-compose.yml`
```dockerfile
services:
  backend:
    image: manuach/monitor-my-money-backend:latest
    ports:
      - "8000:8000"
    environment:
      - DEBUG=0
      - ALLOWED_HOST=localhost,127.0.0.1,backend

  frontend:
    image: manuach/monitor-my-money-frontend:latest
    ports:
      - "3000:3000"
    depends_on:
      - backend
    environment:
      - PUBLIC_API_URL=http://localhost:8000/api
```
Then run `docker compose up` on the .yml file directory

- OR, manually run it in terminal
```
docker run -dp 8000:8000 manuach/monitor-my-money-backend:latest
```
and,
```
docker run -dp 3000:3000 -e PUBLIC_API_URL=http://localhost:8000/api manuach/monitor-my-money-frontend:latest
```

*Dont use manual method unless you know how to stops running container and remove the unused images(remove the unused images btw)*

since its work in progress currently due to user conflict, transactions page cant fetch data. Will be fixed later.
