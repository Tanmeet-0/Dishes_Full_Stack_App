# Dishes Dashboard

A Full Stack Application used to manage and display dish information.  
The dashboard shows the image of the dish, the name of the dish and allows the user to change the published status of the dish.

# Technologies Used
Backend :
- Python + Django framework for web-application and API hosting.
- Mysql for Database

Frontend :
- Javascript + React framework for website and API fetching.

# Dependencies 

For Backend :
- Python (version 3.12.4)
- Django Python Library (version 5.0.7)
- django-cors-headers Python Library (version 4.4.0)
- djangorestframework Python Library (version 3.15.2)
- mysqlclient Python Library (version 2.2.4)
- Mysql Server (version 8.0.38)
  
For Frontend :
- Node (version 22.4.1)
- npm (version 10.8.2)
- React Javascript Library (version 18.3.1)
- react-dom Javascript Library (version 18.3.1)
- react-scripts Javascript Library (version 5.0.1)

# Running

To run the app, make sure you have all of the dependencies.  
The frontend dependencies can easily be installed using `create-react-app`. Visit <https://create-react-app.dev/> for more information.  
You also need to manually create a database named `dishes` to your Mysql server.  
You also need to create a Mysql role with name=`user` and password=`user` and give it all the permissions.  
Open a terminal, go to the backend directory and run the command `python manage.py makemigrations`.  
Then run the command `python manage.py migrate` to initialize the database.  
Then run the command `python manage.py load_json_data_into_database sample_data.json` to load the sample data into the database.  
Then run the command `python manage.py runserver`.  
Open a new terminal, go to the frontend directory and run the command `npm start`.  
Visit <http://localhost:3000/> to view the website.

