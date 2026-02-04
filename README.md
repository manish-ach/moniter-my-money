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

since its work in progress currently due to user conflict, transactions page cant fetch data. Will be fixed later.
