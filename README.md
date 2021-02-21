# ENV settings
```sh
git clone https://github.com/liyuqi/nexio_flask.git;
cd nexio_flask;
docker-compose up -d;
```
# API usage

* POST | add user
```sh
curl -H "Content-Type: application/json" -X POST -d '{"name":"A"}' http://localhost:5000/api/user
curl -H "Content-Type: application/json" -X POST -d '{"name":"B"}' http://localhost:5000/api/user
```
* GET | get user, id info
```sh
curl http://localhost:5000/api/user
curl http://localhost:5000/api/user/2
curl http://localhost:5000/api/user/3
```
* PUT | mod user by id
```sh
curl -H "Content-Type: application/json" -X PUT -d '{"job_title":"OPS"}' http://localhost:5000/api/user/2
curl -H "Content-Type: application/json" -X PUT -d '{"name":"C"}' http://localhost:5000/api/user/3
```
* DELETE | del user by id
```
curl -H "Content-Type: application/json" -X DELETE http://localhost:5000/api/user/2
```
# Requirements Reference
- Please write an RESTful API using Python Flask
- Build docker images
- Run application with docker-compose- RESTful API Must Include:
1. HTTP Method GET/POST/PUT/DELETE
2. Create User
3. Get User Info
4. Update User Info
5. Delete User 

User info structure Example:
```json
{
"name": "Charles",
"job_title": "SRE",
"communicate_information": {
"email": "charles@gmail.com",
"mobile": "09xx-xxx-xxx"
}
}
```
- Project Must Contain:
1. README.md (Describe Usage)
2. Dockerfile
3. env.example for docker-compose
4. docker-compose.yml