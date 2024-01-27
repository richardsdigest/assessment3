### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
      - Syntax and Language Design
      - Typing System
      - Execution Environment
- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
      - Using the get Method
      - Using a try-except Block
- What is a unit test?
      - A unit test is a type of software testing where individual units or components of a software are tested
- What is an integration test?
      - An integration test is a type of software testing where individual units, modules, or components of a software application are combined and tested as a group
- What is the role of web application framework, like Flask?
      - It provides a structured environment in which developers can build and deploy web applications more efficiently and effectively
- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
      - use route parameters when identifying a specific resource or a nested resource hierarchy and use query parameters for optional filters, searches, or sorting criteria. The choice depends on the specific requirements and design principles of your web application
- How do you collect data from a URL placeholder parameter using Flask?
      - In Flask, you can collect data from a URL placeholder parameter using route parameters in your function definitions. A route parameter is part of the URL path and is indicated by angle brackets < > in the route decorator
- How do you collect data from the query string using Flask?
      - In Flask, you can collect data from the query string of a URL using the request object provided by Flask
- How do you collect data from the body of the request using Flask?
      - In Flask, collecting data from the body of a request depends on the content type of the request. The request body can contain data in various formats, such as form data, JSON, or XML.
- What is a cookie and what kinds of things are they commonly used for?
      - A cookie is a small piece of data sent from a website and stored on the user's computer by the user's web browser while the user is browsing
- What is the session object in Flask?
      - In Flask, the session object is a way to store information specific to a user from one request to the next
- What does Flask's `jsonify()` do?
      - Flask's jsonify() function is a helper function provided by the Flask web framework that converts the Python dictionary passed to it into a JSON response.