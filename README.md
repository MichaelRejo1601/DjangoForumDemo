# DjangoForumDemo

**Overview**
For this project, we decided to use the python-based Django to create a web application forum similar to Reddit. To accomplish this, we took from online examples and documentation. As an overview, our web application uses an SQLite database to hold our forum posts. We decided to use Django primarily as a proof of concept to see the number of hours it would take to create a barebones forum website. The features we created include: login page, feed page (all posts), create post page, and the post itself. Some attributes for these posts include the title, the author, the date, and the content published. Using Django, we were able to standup a basic forum in a few days. Django also has many built-in features which we can use to implement extras. For example, it helped greatly in creating a secure login page and in referencing the SQLite formatted data. By using Django, we quickly were able to make a functional prototype to be styled and updated if we wish to continue. We learned how to use Django a fast, scalable python based framework.

**How it works**
When the User requests a url, Django will find the associated view. The view is a function that can be customized to return a HTTPResponse, a Page, or Redirect to the User at the URL. Using the view, we can load templates (that contain template tags) to create dynamic web pages using our model data. In essence, these steps are the core of almost every feature of Django. It is called the Model View Template pattern.

**Features to Try**
*Register*
Register yourself by going the index and hitting Register! We used an external app to make forms like this prettier.

*Login*
You can login a session using the login page at the index (or any page given that you are not logged in already). It will authenticate you and redirect you to the feed.

*Feed*
Dynamically Created feed using template tag's for loop. If there are no posts, head over below.

*My Page*
In the top left is a my page button. Once pressed, it will lead you to your user page. Here you can find your posts (dynamically created) and a Create Post button in the top left.

*Create Post*
Here is a Model Form that allows you to submit a entry to the Model "Post". By clicking it, you go to a url that then goes to a view which saves your form if it is valid. Errors in all forms on this site are properly handeled.

*Delete Post*
On my page, you can find a delete post button on each post. This will redirect you to a url which looks up a view that deletes the mentioned object. Security measures have been customized so that Users who are not the owner of the post cannot delete it (based on login session).

*Post*
Using dynamic urls, similar to the User page, we are able to create a post page. This displays the information of the post and has urls to the authors of the post.

Try making 2 accounts and test out all the features!

**Instructions**

python 3.7.6

Do 'pip install venv'

create a virtual environment using 'mkvirtualenv [environment_name]'

activate using 'venv .\scripts\activate'

pip install -r *path-to*\requirements.txt

to activate 'venv .\scripts\activate'

/BigFolder [create venv here]

/BigFolder/Scripts

/BigFolder/GithubRepo [clone here]

inside of github repo (my Env)C://BigFolder/GithubRepo, do python manage.py makemigrations

inside of github repo (my Env)C://BigFolder/GithubRepo, do python manage.py migrate

inside of github repo (my Env)C://BigFolder/GithubRepo, do python manage.py runserver --insecure (because we are hosting locally)

your page should load at the local host.
