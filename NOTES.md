# What is the RESTful?

> This is some notes from second talk of Miguel Grinberg in Pycon2015. [Link video](https://youtu.be/pZYRC8IbCwk)
> REST is one of the most confusing topics that people are giving their opinions everyday. This talk is one of that personal opinions.

**REST is about the scalable**

## 6 constraints of REST
These 6 constraints are known from the paper [REST](https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm) of Roy Fielding:

- Client-server
- Stateless
- Cache
- Uniform Interface
- Layered system
- Code on demand

## Code-on-demand (Optional)
- Without knowing this constraint, we still can make a good RESTfull APIs
- This is the only optional constraint in REST principles; do it or don't it's okay anyway
- For simplying purpose, just ignore this principle

## Client-server
- The API should be separated from client. Seprate means the server provides API should be in other process with client. 
- This approach helps application to scale easily
 
## Layer system
```
Client1 | 				    	| Server1 	
Client2 | <-> Load balancer <-> | Server2
Client3 |				    	| Server3	
```

- The client and the server may not talk directly. They talk through a misterious block in the middle. 
- The server shouldn't know about the client, even in the header request. The block in the middle will make client invisible before sending the request to server. 
- The block in the middle is "Load balancer"
- Applying "Load balancer" in the middle keeps the requests from client consistent. Clients only need to send its request to a port of an IP, and the Load balancer will send these requests to any server available. This make the responding faster.

## Cache
- The Block in the middle also can be a "Cacher"
- It stores the responses from server. And if clients request the same request over and over, Cacher will send that response to clients without calling the API again.
- Cacher can be in Server or either Browser Client

## Stateless
- Sessions make scaling server more difficult. 
If a request is sent to the server, it's hard to identify which server is storing session of that request. It's can be solved but so complicated. 
- What about cookies? Nope
Someone assumes using cookies still makes REST is RESTful. Cookies can store access token and use it to authenticate in every request to APIs. That makes sense, thus, cookies is gray area, we can use it or not the REST still is RESTful. 

But Miguel's opinion is we shouldn't use cookies. We can use other techniques to store states like access token.

- Clients must authenticate with every request
- Always use secure HTTP (or HTTPS for short)!

## Uniform interface
#### Identification of resources
- Resources are all the entities of entire application. E.g: Customers, products, etc.
- Each resource should have an unique identifier URL
- Collections of resources also should have indentifier URL
- Indentifier URL is can be any type of patterns. 
E.g. /api/v2.0/books/:id or /api/v2.0/book/:id is okay anyway.

#### Resource of representations
- Clients do not have direct acess to resources; they only see their representations. It means the data client recieves from API depends on how server defines it, or represents it. (Technically, it's call the Serialization)
- The server can provide response in any format (content type) (JSON, XML)
- Clients perform all operation on the reprenstation.

#### Self-descriptive message
- Clients send HTTP requests and recieve responses
	- Operation is given in the request method
	- Targer resource in the request URL
	- Authentication headers provide credentials
	- Content-Type/Accept headers define media type (json/ xml/ text )
	- Resource representation in the body (in case operation wants to change the resource)
	- Operation result is in the response status

#### Hypermedia (HATEOAS) - Nobody does this.
- Clients do not know any resource URLs in the advance except for the root URL of the API
- Resource URLs are discovered through links provided in resource representations.


# Bonus - RESTful API best practices

#### Should the endpoint name be singular or plural?
> PLURAL

```
GET /tickets
```

#### Relations
```
GET /tickets/12/messages - Retrieves list of messages for ticket #12
GET /tickets/12/messages/5 - Retrieves message #5 for ticket #12
POST /tickets/12/messages - Creates a new message in ticket #12
PUT /tickets/12/messages/5 - Updates message #5 for ticket #12
PATCH /tickets/12/messages/5 - Partially updates message #5 for ticket #12
DELETE /tickets/12/messages/5 - Deletes message #5 for ticket #12
```

