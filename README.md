# Full Stack Assignment

Preliminary Assignment for full stack developers. Welcome! We are delighted to see you applying. Now it's your time to shine.

**NOTE!**: This assignment will be taken into consideration for candidates who will:
Fork the assignment repository, complete the required tasks, and contribute with the finalized stable version of the project to the parent repository (anything apart from GitHub will not be accepted).

Technologies:

Frontend (Basic HTML/Bootstrap)

Backend (Django)

**Please NOTE that the time for this assignment is only 2 hours, starting at the moment you will receive this GitHub repository link.**
<p align="center" border="none">
  <img alt="Hubinit" src="./hubinit.png" align="center">
</p>

## CRUD

The goal of the assignment is to showcase your coding skills and ability to develop features. This is a highly important part of the hiring process, so it's crucial to put effort into this without making it too bloated. Reviewers will put weight on three main aspects: code quality, maintainability, and testing. Based on the results of the assignment review, we will make the decision on proceeding with your application.

#### Requirements

Your task is to write a SIMPLE CRUD to manipulate the object called **"blog"** in the Django admin in addition for the front-end the user should be able to list all the blogs , search,  create ,update, and delete a blog, and customize the __localhost:your_port/__ page using the given **index.html** located in the **carousel folder** (Consider it as you are integrating a template).

### Specification


##### Field details

| Field         | Type     | Description                                       | Example value                         |
|:---           |:---      |:---                                               |:---                                   |
| blog_title    | String   | Title of the blog should be max 50 characters     | What is Django?                       |
| author_name   | String   | The name of the author should be a __ForeignKey__ | If you are connected to django-admin with a user called __Django__, the author_name should be __Django__ |
| blog_text     | TextField| The body of the blog                              | The text of the blog                   |
| blog_status   | String   | No Dropdown, just a simple string                 | __Active or Draft__                   |

### Excellence Point (Optional)

- Usage of __RichTextField__ instead of __TextField__ for the __blog_text__ attribute.

### Expectations

When reviewing your code, we will focus on the part that fulfills the requirements explained above. We would love to see a well-tested and readable solution.

Pro tip: When you think you are ready with the assignment, take at least a few hours break, and then go through the code one more time before returning it.

### Submitting the assignment

Make sure to edit the __readme.md__ to mention steps(without explanation) we need to follow to examine your finalized assignment.

Push your code to your personal GitHub account and contribute to **our repository**.

A good check before pushing your task is making sure the project works well, using the steps you define in readme.md. Forgotten dependencies and instructions can sometimes happen even to the best of us.


<h1>Blog Register Project</h1>

<h2>Overview</h2>
<p>The Blog Register project is a web application built using Django, a high-level Python web framework. It provides a platform for users to register, create, read, update, and delete (CRUD) blog entries. Additionally, users can search for specific blog entries using a dynamic search functionality.</p>

<h4>Features</h4>
<ul>
  <li>User Authentication: Users can register, log in, and log out of the system securely.</li>
  <li>Blog Management: Users can create new blog entries, view existing entries, update their own entries, and delete entries as needed.</li>
  <li>Dynamic Search: The system allows users to search for blog entries based on title, author name, or blog content, providing a versatile search experience.</li>
</ul>

<h4>Technologies Used</h4>
<ul>
  <li>Django: Python web framework for building the backend of the application.</li>
  <li>SQLite: Lightweight database management system used for data storage.</li>
  <li>HTML/CSS/Bootstrap: Frontend technologies for designing and styling the user interface.</li>
  <li>Crispy Forms: Django application for rendering forms using Bootstrap styles.</li>
</ul>

<h4>Setup Instructions</h4>
<ol>
  <li>Clone the repository to your local machine: <br>
  <code>git clone &lt;repository-url&gt;</code></li>
  <li>Navigate to the project directory: <br>
  <code>cd &lt;project-directory&gt;</code></li>
  <li>Install the project dependencies: <br>
  <code>pip install -r requirements.txt</code></li>
  <li>Apply database migrations: <br>
  <code>python manage.py migrate</code></li>
  <li>Run the development server: <br>
  <code>python manage.py runserver</code></li>
  <li>Access the application in your web browser at <a href="http://localhost:8000">http://localhost:8000</a>.</li>
</ol>

<h2>Usage</h2>
<ol>
  <li>Register a new user account or log in with existing credentials.</li>
  <li>Navigate to the "Blog" section to create, view, update, or delete blog entries.</li>
  <li>Use the search functionality to find specific blog entries based on title, author name, or blog content.</li>
</ol>

<p><strong>PS:</strong> This project was developed by a newcomer to Django, who embarked on this journey as a first-time user of the framework. Despite being new to Django, it was an exciting and challenging task to learn about its concepts and features and apply them in a real project within a short period of time.</p>


