# [REST API Quick Tips](https://www.codecademy.com/articles/what-is-rest)

## What is REST?

REST, or REpresentational State Transfer, is an architectural style for providing standards between computer systems on the web, making it easier for systems to communicate with each other. 

REST-compliant systems, often called RESTful systems, are characterized by how they are stateless and separate the concerns of client and server. We will go into what these terms mean and why they are beneficial characteristics for services on the Web.

API consumers are capable of sending GET, POST, PUT, and DELETE verbs, which greatly enhance the clarity of a given request.

### SEPARATION OF CLIENT AND SERVER

In the REST architectural style, the implementation of the client and the implementation of the server can be done independently without each knowing about the other. 

### STATELESSNESS

Systems that follow the REST paradigm are stateless, meaning that the server does not need to know anything about what state the client is in and vice versa. In this way, both the server and the client can understand any message received, even without seeing previous messages. This constraint of statelessness is enforced through the use of resources, rather than commands. Resources are the nouns of the Web - they describe any object, document, or thing that you may need to store or send to other services.

### COMMUNICATION BETWEEN CLIENT AND SERVER

In the REST architecture, clients send requests to retrieve or modify resources, and servers send responses to these requests. Let’s take a look at the standard ways to make requests and send responses.

### MAKING REQUESTS

REST requires that a client make a request to the server in order to retrieve or modify data on the server. A request generally consists of:

* an HTTP verb, which defines what kind of operation to perform
* a header, which allows the client to pass along information about the request
* a path to a resource
* an optional message body containing data

### HTTP VERBS
There are 4 basic HTTP verbs we use in requests to interact with resources in a REST system:

* GET — retrieve a specific resource (by id) or a collection of resources
* POST — create a new resource
* PUT — update a specific resource (by id)
* DELETE — remove a specific resource by id

### HEADERS AND ACCEPT PARAMETERS

In the header of the request, the client sends the type of content that it is able to receive from the server. This is called the Accept field, and it ensures that the server does not send data that cannot be understood or processed by the client. The options for types of content are MIME Types (or Multipurpose Internet Mail Extensions, which you can read more about in the [MDN Web Docs]. (https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types)

MIME Types, used to specify the content types in the Accept field, consist of a type and a subtype. They are separated by a slash (/).

For example, a text file containing HTML would be specified with the type `text/html`. If this text file contained CSS instead, it would be specified as `text/css`. A generic text file would be denoted as `text/plain`. 
This default value, text/plain, is not a catch-all, however. If a client is expecting text/css and receives text/plain, it will not be able to recognize the content.

Other types and commonly used subtypes:

* image — image/png, image/jpeg, image/gif
* audio — audio/wav, image/mpeg
* video — video/mp4, video/ogg
* application — application/json, application/pdf, application/xml, application/octet-stream

For example, a client accessing a resource with id 23 in an articles resource on a server might send a GET request like this:

```
GET /articles/23
Accept: application/json
```

### PATHS

Requests must contain a path to a resource that the operation should be performed on. In RESTful APIs, paths should be designed to help the client know what is going on.

Conventionally, the first part of the path should be the plural form of the resource. This keeps nested paths simple to read and easy to understand.

A path like `fashionboutique.com/customers/223/orders/12` is clear in what it points to, even if you’ve never seen this specific path before, because it is hierarchical and descriptive. We can see that we are accessing the order with id `12` for the customer with id `223`.

Paths should contain the information necessary to locate a resource with the degree of specificity needed. When referring to a list or collection of resources, it is unnecessary to add an id to a POST request to a `fashionboutique.com/customers` path would not need an extra identifier, as the server will generate an id for the new object.

### Response Code

```
Status code	Meaning
200 (OK)	This is the standard response for successful HTTP requests.
201 (CREATED)	This is the standard response for an HTTP request that resulted in an item being successfully created.
204 (NO CONTENT)	This is the standard response for successful HTTP requests, where nothing is being returned in the response body.
400 (BAD REQUEST)	The request cannot be processed because of bad request syntax, excessive size, or another client error.
403 (FORBIDDEN)	The client does not have permission to access this resource.
404 (NOT FOUND)	The resource could not be found at this time. It is possible it was deleted, or does not exist yet.
500 (INTERNAL SERVER ERROR)	The generic answer for an unexpected failure if there is no more specific information available.
```
* GET — return 200 (OK)
* POST — return 201 (CREATED)
* PUT — return 200 (OK)
* DELETE — return 204 (NO CONTENT) If the operation fails, return the most specific status code possible corresponding to the problem that was encountered.

More to read: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

### Requests and Responses Example


[Request] Create a customer
```
POST http://fashionboutique.com/customers
Body:
{
    "name" = "Yu"
    "email" = "yu.wang.jr@gmail.com"
}
```

[Response] The server then generates an id for that object and returns it back to the client, with a header like:
```
201 (CREATED)
Content-type: application/json
{
  "customer_id": 1
}
```

[Request] Get customer with id 
```
GET http://fashionboutique.com/customers/1
Accept: application/json
```

[Response]
```
Status Code: 200 (OK)
Content-type: application/json

{
    "id" = 1
    "name" = "Yu"
    "email" = "yu.wang.jr@gmail.com"
}
```


[Request] Get all customers
```
GET http://fashionboutique.com/customers
Accept: application/json
```

[Response]
```
Status Code: 200 (OK)
Content-type: application/json
[
  {
    "id" = 1
    "name" = "Yu"
    "email" = "yu.wang.jr@gmail.com"
  }, 
  {
    "id" = 2
    ...
  }
]

```

[Request] Update existing entry
```
PUT http://fashionboutique.com/customers/1
Body:
{
    "name" = "Yu Wang"
    "email" = "yu.wang.jr@gmail.com"
}
```

[Request] Delete
```
DELETE http://fashionboutique.com/customers/1
```
[Response]
```
Status Code: 204 (No Content)
Content-type: application/json
```



## API Design Example

GET `/customers/<customer_id>`
```
{
    "id": <Integer>,
    “username”: <String>,
    “password”: <String>
}
```

PUT `/customers/<customer_id>`
```
{
    “username”: <String>,
    “password”: <String>
}
```

# Other types of APIs

## Modern APIs

* REST
* gRPC (gRPC is a technology for implementing RPC APIs that uses HTTP 2.0 as its underlying transport protocol.)
* GraphQL (a query language for your API)

More to read: 
* https://cloud.google.com/blog/products/api-management/understanding-grpc-openapi-and-rest-and-when-to-use-them
* https://developers.google.com/protocol-buffers
* https://medium.com/@nikhildhyani365/what-the-heck-is-serialization-and-why-do-we-need-it-9301487db47a
* https://graphql.org/learn/

## Legacy/Special Purpose APIs 

* SOAP 
* XML-RPC
* JSON-RPC 

More to read: https://rapidapi.com/blog/types-of-apis/
