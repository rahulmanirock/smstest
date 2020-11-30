##### **SMS INDIA API ENDPOINT DETAIL -**

Created API for Elements , Commodity , Chemical composition.

**A) Get all chemical elements -** 

1) http://localhost:8000/api/elements/ (GET)

**B) ADD all chemical elements -** 

1) http://localhost:8000/api/elements/ (POST)

**C) Get a commodity by ID -** 

1) http://localhost:8000/api/commodity/ (GET)

**D) Get a commodity by ID -** 

1) http://localhost:8000/api/commodity/ (POST)


**E) Update commodity by id -** 
1) http://localhost:8000/api/commodity/ (PUT)

`{
 "id": 1,
 "name": "Plate & Structural",
 "inventory": "201.5",
 "price": "1234.50"
}`

**F) Add chemical concentration -**
1) http://localhost:8000/api/chemical_composition/ (POST)
`
 {
"commodity_id": 2,
"elements_id": 2,
"percentage": 1
}`


**G) Remove chemical concentration -**
1) http://localhost:8000/api/chemical_composition/ (DELETE)
`{
"commodity_id": "1",
"elements_id": "2"
}`



FOR GETTING TOKEN FOR AUTHENTICATION - 

POST http://localhost:8000/api/token/

`{
	"username":"admin",
	"password":"admin"
}`




