# Mini Blog in Django
I created this github project to learn Django which can be referenced by others who are interested in walking down the same road.
I will be covering below:

- What is Django?
- What basics you need to know to grasp what is happening in Django while doing development?
- Important use cases and scenarios that one comes across during basic Web Development.

My approach will be to help readers learn Django on use case basis rather than forcing one to go through Documentation of Django.

## What is Django?

Django is a MVT framework written in python to come up with fully functional websites in least time and effort possible. How Django accomplishes it?
Well Django comes with batteries included. Basically all the problems that web developers face during development are already taken care of in Django
and Django developers need not reinvent the wheel. Most of the efforts should be put in finding what is already provided by Django and use it judiciously.

### What is MVT Framework?

MVT stands for Model View Template. Now this is a standard design which is used to facilitate easy refactoring and scaling of the application. Lets dive in the terms one by one.
- **Model**: Each website has its data stored in some form of database. The database usually has entity relationships implemented in its schema. In general scheme of things we need to create Database first with all the schema in place containing tables as entities and the constraints applied. Model part of the MVC takes care of the creation of database entities through code rather than manually. Basically what is done under the hood is normally called as ORM (Object Relational Mapping). You can see the ORM as the layer that connects object oriented programming (OOP) to relational databases. So you write a code in Python decalring models and Django will take care of reflecting its appropriate database structure. For more intuitive understanding search about ORM. Spring Boot is another framework that integrates well with ORM framrworks such as Hibernate. Remember ORM is a Design Pattern not a framework. Similarly MVC is also a design pattern. These design patterns when implemented in any particular langauge are handed over to Devs for development are called frameworks. Django is a Python MVT framework.
    - Model defines the data of the web application which would be persisted in some database technology such as sqlite, mysql or postgresql etc.
- **View**: Now Model takes care of the data persistence part of the website. But a website is all about being viewed by a user and a website is being viewed in some browser in form of HTML pages (called as templates). What happens is we have HTML pages in form of templates and these templates would be filled with appropriate content, rendered by a broweser and viewed to the user upon some user's request. It is the task of the server to listen to the client browser, pick appropriate template, fill it with needful model data, construct a final HTML page and show it on the browser.
    - In nutshell View defines the logic of what to display on a particular request
- **Template**: This is the static content of the website i.e HTML pages that could be updated with dynamically generated content by the server and used by View to display to the user.

### What Django offers as MVT?

Now Django is a MVT framework written in python. To develop in Django you must know that Django provides Model, View and Templates as python files namely models.py, views.py, HTML files as templates.

- **models.py** - You write your models here. Django provides an inbuilt class that one needs to extend. The class is `django.db.models.Model`
- **views.py** - this python file defines the Views (functions or class based) that would be called upon a particular request. View functions can either use default templates or can be configured to call a particular template along with the data stored in model.
- **urls.py** - this file provides the mapping between URL request hit and corresponding view function.
- **templates** - these are HTML files which are saved with Django template language to support dynamic content generation. Basically a view function takes care of passing the appropriate context to the template and using the context we can display the information in HTML using Django template syntax.

See the diagram below.

![Django Basic workflow](django_basic_workflow.png)

To know more about Django read here on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction).


## Solving the Django Mini Blog Assignment 

We will solve the [Django Mini blog Assignment](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/django_assessment_blog) mentioned on MDN Web Docs. It is required that you must have gone through the [tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website) first and should have learned how to set up the Django with python virtual environments. It is assumed that you already know python. The aim of this project and illustrative readme file is to directly present you the solutions of the common problems that one would come across with development in django.

1. **Figuring out the schema and entity relationship diagram** - The first step is to design the database schema. In django you would use the models.py that would create the required schema. There is no need to decide on the database software to be used first. Django would take care of reflecting the ERD(Entity Relationship Diagram) described through models in models.py in whatever database is configured for Django e.g mysql, postgresql etc. Lets go through the entities involved.
    
    - _BlogPost_: Everyblog post should have a title, an author who actually created that blogpost, dates when blogpost was published and last edited, content of the blogpost and comments by the users who are logged in.
        - Every blogpost would have only one author which implies a many-to-one relatioship.

    - _Blogger_: Every blogger who is able to create a blogpost should have a first name and last name and other user details. These details can be stored by mapping a Django inbuilt user as a foreign key.
        - about: text field that contains some biographical information about the blogger.
        - user: django auth.user mapped as foreign key with blogger
    
    - _Comment_: A user can comment on any blogpost and only the commentor can edit the comment. Comment would be posted on a particular date and could be edited anytime:
        - commentor: mapped with django inbuilt user as foreign key
        - on_blogpost: blogpost on which user has commented
        - content: what is commented on?
        - posted_on: Date when comment as posted
        - edited_at: date when comment was edited by its commentor.
    
   
    See Diagram Below:

    ![ERD](ERD.png)

    - A blogger has one-to-many relationship with BlogPost
    - A Comment has many-to-one relationship with user
    - A blogger has one-to-one relatioship with Django inbuilt user

2. **Creating Models in models.py** Django provides `django.contrib.auth.models.Model` class which can be extended to create Models.
    Blogger model. 
    - We import the model as `from django.db import models` and use `models.Model` class as shown below.
    - Now to implement users in Django we can either either extend the AbstratUser and create our custom user or we can use the existing User model as one-to-one key. We have used the later approach. For further reading go through [extending-the-existing-user-model](https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#extending-the-existing-user-model)
    - Model class provides few functions that one can override to achieve desired functionality.
        - first function is `__str__` that is overridern to return the desired name for the object which could be displayed in admin site. (Note: Here we assume you have gone through the [tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website) )
        - second function is `get_absolute_url` which is useful when we will dive into views (CreateView, ListView etc). After creating a blogger instance we can use the default redirect to the url provided by this function. In the code below the function returns the path to blogger-detail page. We will further dive into it.

```
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy


class Blogger(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    about = models.TextField(max_length=2000, null=True)
    slug = models.SlugField(max_length=50)

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'
    
    def get_absolute_url(self) -> str:
        return reverse_lazy('blogger-detail', kwargs={'slug': self.slug})
```

3. **Running Django Migrations**

    - Once the models are defined in `models.py` we need to run the migrations. Running migrations in this context essentially means we are sort of running database migration changes. After migrations are completed, Django would reflect the expected changes in database schema. We esentailly run two commands `python3 manage.py makemigrations` and `python3 manage.py migrate`
    - On running `makemigrations` command python files are created in migrations folder that describe the changes to be made to schema. Then `migrate` command would commit those changes to database (pre-configured in `settings.py` default is sqlite)

4. **Creating a view function and mapping a template**

    - In `views.py` we write functions or class-based views that would render and return a certain template. We map the view written in `views.py` to a specific url pattern that a browser could request. When the specific request is made Django knows what to show to the user based upon view-to-url mapping.
    - As a simple example lets consider a home page that would be shown once a user hits the domain name only.
        ```
        urlpatterns = [
        path('', views.home, name='home'),
        ]
        ```
    - Now `views.home` is a function defined in `views.py`. Check below code snippet. It takes request as an argument.
        ```
        from django.shortcuts import get_object_or_404, render
        
        def home(request):
            return render(request, 'home.html')
        ```
    - Now anytime the url `http://127.0.0.1:8000/` would be hit it would load the HTML page `home.html`