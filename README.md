# Flask Rest API on Companies House data

## Features

- CRUD API over Companies House data
- Manage company data
- Edit people with significant control
- Filter and paginate data
- Security via JWT tokens


---


### Development environment setup

#### Prerequisites

- Docker
- VSCode
- Remote Containers extension

#### Guide

##### IDE setup
- Clone repository or download and extract zip file
- Open folder in VSCode
- Choose to reopen in container when prompted
- Give docker a minute to build the container
##### Database setup
- Download the company and people with significant control data files. Find the `wget` commands in the `Dockerfile` in  `.devcontainer` folder
- `cd` to `setup` folder
- Run `python create_table.py` to initialize database
- Run `python import_bcd_data.py` to load company data into the database
- Run `python import_psc_data.py` to load people data into the database
##### Start dev server
- Run `python app.py` to start the development server
- Go to `http://localhost:5000/` for OpenAPI documentation
