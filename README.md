# REST API User Register

REST API made with FastAPI, PrismaORM and PostgreSQL for register users.

## Requirements

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```
pip install -r requirements.txt
```
## Database

Schema: public  
Database: users_crud  

| users_   | Types         |
|----------|---------------|
| dni (PK) | CHAR(10)      |
| name     | VARCHAR(100)  |
| email    | VARCHAR(50)   |
| password | VARCHAR(300)  |
