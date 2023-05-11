# API Docs

## Show recipies

```bash
curl http://host:5000/recipies/<index>
```

## Delete a recipie

```bash
curl -X DELETE http://host:5000/delrecipie/<index>
```

## Add a recipie

```bash
curl -X POST -d 'Recipie Data' http://host:5000/addrecipie
```