# What is integration test?
Unlike unittest, testing individual 

# Tools to run integration test
Not much difference from unit test tools; It is all about how you write the test.

However, there is one tool that I would like to share with you about for API integration test: 

Automated API testing -- Postman/Newman 

# What is Postman and Newman?

[Postman](https://www.postman.com/downloads/)

[Newman](https://support.getpostman.com/hc/en-us/articles/115003710329-What-is-Newman-#:~:text=Chris,the%20collection%20runner%20in%20Postman.)

[Newman Repo and Demo](https://github.com/postmanlabs/newman)


# Hands on query EasyCRM

1. spin up EasyCRM by following the README.md file in the EasyCRM repo

2. Once its up try import `EasyCRM.postman_collection.json`

3. Click the config button on the top right corner 

4. Create an environment variable set called `EasyCRM_Environment` and 
set the `host` as `http://0.0.0.0:8090` or `http://localhost:8090` 
and `cookie_session` empty
![Alt text](../../images/set_ev.png?raw=true)

5. Run the postman runner with Change the `No environment` to Environment
![Alt text](../../images/postman_runner.png?raw=true)

6. Click manage the environment variable and EasyCRM, what do you see?

7. Could you create another two queries, 
one for POST `/contact/create` and 
one for GET `/contact/<con_id>` 

8. Export the json file for future use.

9. Homework: try use newman and add newman to run the queries in sequence with travis CI. 
   Tips: try use the exported json file

# Difference between Unit Test and Integration Test
https://stackoverflow.com/questions/10752/what-is-the-difference-between-integration-and-unit-tests