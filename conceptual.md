### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
javascript runs the front end while python runs the backend
- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
you can use the .get or setdefault methods
- What is a unit test?
a unit test is a way to test individual portions of code
- What is an integration test?
an integration test is to test if certain portions of code are able to work together as they should
- What is the role of web application framework, like Flask?
to make the coding process smoother
- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
the best way to choose is if you are searching something from a form or going to a new webpage
- How do you collect data from a URL placeholder parameter using Flask?
you use the syntax <var> in the app.route
- How do you collect data from the query string using Flask?
request.args
- How do you collect data from the body of the request using Flask?
request.form
- What is a cookie and what kinds of things are they commonly used for?
a cookie is a way of storing local data to make the user exprience better
- What is the session object in Flask?
the session object is a way to send cookies that take up less memory so you can store more data
- What does Flask's `jsonify()` do?
it takes python information and formats it to JSON to use on the client side