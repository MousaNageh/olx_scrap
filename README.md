# olx scraping

### the app used for scraping Ads from olx ,save the data in to mongodb and send email of sample of data .

## installation

### 2) run docker compose :

- run the following commnand to build images and run containers
  ```sh
    docker-composer up --build
  ```
  or for docker detached mode run :
  ```sh
      docker-composer up --build  -d
  ```
  if you are using new docker version run:
  ```sh
      docker composer up --build
  ```

### 3) send post request:

- url : http://127.0.0.1:5000/
- body:

```sh
      {
        "email":"your-email@dmain.com",
        "keyword":"car",
        "size":20
    }
```
