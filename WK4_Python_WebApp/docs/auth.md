# Basic Authentication

HTTP Basic Authentication is rarely recommended due to its inherent security vulnerabilities.

This is the most straightforward method and the easiest. With this method, the sender places a username:password into the request header. The username and password are encoded with Base64, which is an encoding technique that converts the username and password into a set of 64 characters to ensure safe transmission.

This method does not require cookies, session IDs, login pages, and other such specialty solutions, and because it uses the HTTP header itself, there’s no need to handshakes or other complex response systems.

Here’s an example of a Basic Auth in a request header:
`Authorization: Basic bG9sOnNlY3VyZQ==`



# Cookies based Authentication 

works normally in these 4 steps-

1. The user provides a username and password in the login form and clicks Log In.
2. After the request is made, the server validate the user on the backend by querying in the database. If the request is valid, it will create a session by using the user information fetched from the database and store them, for each session a unique id called session Id is created ,by default session Id is will be given to client through the Browser.
3. Browser will submit this session Id on each subsequent requests, the session ID is verified against the database, based on this session id website will identify the session belonging to which client and then give access the request.
4. Once a user logs out of the app, the session is destroyed both client-side and server-side.


## Let us take Jira as an example

https://developer.atlassian.com/cloud/jira/platform/jira-rest-api-cookie-based-authentication/


# OAuth Simplified
https://medium.com/@darutk/the-simplest-guide-to-oauth-2-0-8c71bd9a15bb




