# Mini Blog in Django
I created this github project to learn Django which can be reference by others who are interested in walking down the same road.
I will be covering below:

- What is Django?
- What basics you need to know to grasp what is happening in Django?
- Important use cases and scenarios that one comes across during basic Web Development.

My approach will be help readers learn Django on use case basis rather than forcing one to go through Documentation of Django.

## What is Django?

Django is a MVC framework written in python to come up with fully functional websites in least time and effort possible. How Django accomplishes it?
Well Django comes with batteries included. Basically all the problems that web developers face during development are already taken care of in Django
and Django developers need not reinvent the wheel. Most of the efforts should be put in finding what is already provided by Django and use it judiciously.

### What is MVC Framework?

MVT stands for Model View Template. Now this is a standard design which is used to facilitate easy refactoring and scaling of the application. Lets dive in the terms one by one.
- **Model**: Each website has its data stored in some form of database. The database usually has entity relationships implemented in its schema. In general scheme of things we need to create Database first with all the schema in place containing tables as entities and the constraints applied. Model part of the MVC takes care of the creation of database entities through code rather than manually. Basically what is done under the hood is normally called as ORM (Object Relational Mapping). You can see the ORM as the layer that connects object oriented programming (OOP) to relational databases. So you write a code in Python decalring models and Django will take care of reflecting its appropriate database structure. For more intuitive understanding search about ORM. Spring Boot is another framework that integrates well with ORM framrworks such as Hibernate. Remember ORM is a Design Pattern not a framework. Similarly MVC is also a design pattern. These design patterns when implemented in any particular langauge are handed over to Devs for development are called frameworks. Django is a Python MVT framework.
    - Model defines the data of the web application which would be persisted in some database technology such as sqlite, mysql or postgresql etc.
- **View**: Now Model takes care of the data persistence part of the website. But a website is all about being viewed by a user and a website is being viewed in some browser in form of HTML pages (called as templates). What happens is we have HTML pages in form of templates and these templates would be filled with appropriate content, rendered by a broweser and viewed to the user upon some user's request. It is the task of the server to listen to the client browser, pick appropriate template, fill it with needful model data, construct a final HTML page and show it on the browser.
    - In nutshell View defines the logic of what to display on a particular request
- **Template**: This is the static content of the website i.e HTML pages that could be updated with dynamically generated content by the server and used by View to display to the user.
