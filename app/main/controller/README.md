# Controller

## Resources

[User Controller](https://www.freecodecamp.org/news/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563/ "Free Code Camp")

[Token Based Auth](https://www.youtube.com/watch?v=xF30i_A6cRw "Pretty Printed")

## Terminology

- **api.route:**
  A decorator to route resources

- **api.marshal_with:**
  A decorator specifying the fields to use for serialization (userDto)

- **api.marshal_list_with:**
  A shortcut decorator for marshal_with above withas_list = True

- **api.doc:**
  A decorator to add some api documentation to the decorated object

- **api.response:**
  A decorator to specify one of the expected responses

- **api.expect:**
  A decorator to Specify the expected input model (userDto)

- **api.param:**
  A decorator to specify one of the expected parameters
