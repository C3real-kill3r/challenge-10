# challenge-10

the application a user to register, login, create comment, edit comment, delete his/her comment and view all comments and who posted the comments.

## Getting Started

download the zip folder into your computer.

### Prerequisites

XAMP
Flask
pymysql
jwt


### Installing
*extract the files from the zip folder into another folder within the computer.

*open command prompt and move to the folder directory containing the app.
*on the cmd; install flask by typing:
```
C:\>pip install pymysql
```
*install jwt:
```
C:\>pip install jwt
```
*install flask
```
C:\>pip install flask
```

## Running the app

After successful installation of the app;
**open XAMP and start Mysql and Apache module.
*access the phpMyAmin page on your browser
```
http://localhost/phpmyadmin
```
*create a database called 'flaskdb'
*open postman
*execute the run.py file
*enter the home url in postman for the app to create the required tables on the database
```
http://127.0.0.1:5000/
```
*register a new user into the system
```
http://127.0.0.1:5000/register
```
*type as many comments as you'd prefer
```
http://127.0.0.1:5000/comments
```
*view all comments posted
```
http://127.0.0.1:5000/get_comments
```
*delete a comment
```
http://127.0.0.1:5000/delete_comments/(commentID)
```


## Built With

* [Sublime Text](http://www.sublimetext.com/) - The python text editor used
* [XAMP](https://www.apachefriends.org/index.html) 

## Authors

* **Brian Ryb Okuku** 
