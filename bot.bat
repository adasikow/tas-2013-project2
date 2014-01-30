curl localhost:8000/api/products > stan_poczatkowy.xml
for /l %%x in (1, 1, 100) do (
   curl -d "name=test%%x&description=test%%x&producer=test%%x&category=computer" localhost:8000/api/product
)
curl localhost:8000/api/products > stan_koncowy.xml