# PARMA
A HealthCare Management System (Web app)

## TEAM
James Koduah - Full-Stack Developer
James Koduah is performing duties as a Full-Stack developer due to an understanding and interest in both sides of the application
Farai Ushe - Full Stack Developer
I am capable and experienced in working with both the front-end and back-end technologies. My skill set allows me to contribute effectively to various aspects of the project, making me a valuable asset to the team.
## TECHNOLOGIES
This web app will be built using:
BACKEND:Python (Flask): Flask has been chosen for routing and APIs because the team members are more conversant with Flask compared to other frameworks like Django. Utilizing a technology they are familiar with will lead to faster development and fewer learning curve-related delays
MySQL: The team has opted for MySQL as the database management system for the project. Our experience with MySQL ensures efficient data storage and retrieval for the web application. Python(Flask) - For routing and api’s (Trade-off: Django is also a very popular framework but since we are more conversant with Flask, Flask was selected)
	        MySQL - For our Database
FRONTEND: HTML, CSS, and JavaScript: The team has decided to use these core web technologies for the front-end development of the application. Despite the availability of various frontend frameworks, we believe that sticking to vanilla JavaScript will allow us to meet the project's deadline and deliver a working Minimum Viable Product (MVP) effectively.Html, Css and Javascript. (Trade-off: There are many popular frontend frameworks that have a reputation of making development very easy. But as I believe I am more capable with vanilla Javascript, it would help for the constraints of this project to use the above mentioned languages to build as our aim is to have a working MVP by this projects deadline)

## CHALLENGE
A HealthCare app to create, update, delete and get patient records thereby helping health Care institutions to manage their processes more efficiently and keep a detailed profile of a patient.
This app will keep patient data updated even across different branches and locations.
Reduce patient wait time as most transactions can be automated.
 Provide an easy access store for patients to order prescriptions(medicine)
This app will not:
Eliminate the need for in-person attendance
Provide remote consultation services for illness diagnoses 
Our Targeted Users:
Hospitals
clinics

## Architecture
This project is a web application.
An overview of our application is a Database to store our data,a backend application to serve our data and a user interface.
Server Architecture
We will have a Load balancer that sends requests to several web servers.
Each web server is going to connect to a remote database for information. This provides a horizontal scalability in the application
Database Architecture
As the application scales, the number of servers can increase. Database Replication can share the reading and writing among different servers


## API’s and Methods

‘/hospitals/search’ - Returns a filtered list of hospitals (Full information on the hospital) that match a query. The query can be filtered by name or location. The query is passed as json.
‘/hospitals/search_match’ - Returns a list of hospitals that match a query. This is used in the search box, as the user is typing the matching results will be shown. The query is filtered by name.
‘/hospital/staff’ - Returns a list of the staff of a hospital
‘/patient/details’ - Get patient details
‘/patient/record’ - Get patient records
Other api’s will be added as needed

## User Stories
