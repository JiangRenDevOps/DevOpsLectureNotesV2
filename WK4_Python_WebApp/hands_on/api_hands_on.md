# The Problem 1
We are building an online ordering system for Jiangren.com.au and you are assigned to design an API system.
The API should allow you Create/Read/Update/Delete (CRUD) customers and order details.

Hints: 
* Try to define the scope and break down the task first
* Try to define the API requests and responses 
    * what kinds of requests we would want to make
    * what responses the server should return
    * what the content-type of each response should be
* What test would you add?
* What limitations shall we consider? How would you deal with the limitations? 
* Please follow the dev process to iterate over each task.
* Try to use class Customer and class Order for defining the two objects if you are interested


We have provide you some skeleton code in the `src` folder




# The Problem 2
Let’s imagine we are building a photo-collection site for a different want to make an API to keep track of users, venues, and photos of those venues. This site has an index.html and a style.css. Each user has a username and a password. Each photo has a venue and an owner (i.e. the user who took the picture). Each venue has a name and street address. Can you design a REST system that would accommodate:

* storing users, photos, and venues
* accessing venues and accessing certain photos of a certain venue

Start by writing out:

* what kinds of requests we would want to make
* what responses the server should return
* what the content-type of each response should be


# Advanced 
1. For a stretch, try implement swagger for dev docs enhancement. Reference: 
http://michal.karzynski.pl/blog/2016/06/19/building-beautiful-restful-apis-using-flask-swagger-ui-flask-restplus/


2. Another task: in app.py, there is a function called `send_content_to_process`, 
can you hook this function with a database?