Este repo nacio por la flojera de usar varios gestores como postman, y en cada request configurar header en otra seccion, 
Aca la idea es en un solo json, hacer el request

\
\
I use poetry to admin packages
\
\
To install poetry:
```bash
$curl -sSL https://install.python-poetry.org | python3 -
```
\
\
To install packages

```bash
$poetry install
```
\
\
Activate virtual environment
```bash
$source .venv/bin/activate
```
\
\
Ejecutar el servidor
```bash
$python app.py
```


\
\
Usar el servidor y hacer un request
```javascript
{
  "method": "get",
  "url": "https://pokeapi.co/api/v2/pokemon/ditto",
  "params": null,
  "json": null,
  "headers": null
}
```


