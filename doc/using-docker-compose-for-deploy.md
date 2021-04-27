# Deploy using docker-compose


## Download repos 

First off all we need crate folder currency. 
Where we put repository.

```
mkdir currency
cd currency
```

Download repos 

```
gti clone front
gti clone back
```

We should get this dir structure 


├── cryptocurrency-backend
└── crypto-currency-frontend 


## When create images use docker

For frontend 
```
cd crypto-currency-frontend
docker build -t currency-frontend .
```

For backend 

```
cd cryptocurrency-backend
docker build -t currency-backend -f deploy/Dockerfile .
```

# Run docker-compose

Go to root dir and run docker-compose

```
docker-compose -f cryptocurrency-backend/deploy/docker-compose.yml up
```
