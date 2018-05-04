Step 1: Download and Install Python from https://www.python.org/downloads/
Step 2: Install flask using command "pip install flask"
Step 3: Install flaskRESTfull using command "pip install flask-RESTfull"
Step 4: Download and install Docker Toolbox from https://docs.docker.com/toolbox/toolbox_install_windows/
Step 5: Open Docker Toolbox terminal and enter into your project directory
Step 6: Type docker build -t flask-image:latest . to build image
Step 7: Type docker run -t -p --name flask-container flask-image to run the image 
Step 8: Type 192.168.99.100:5000 to run your image on browser
Step 9: Type 192.168.99.10:5000/Student to see all records of students
Step 10: Type 192.168.99.10:5000/Student/1 to see records of students based on ID
Step 11: Type 192.168.99.10:5000/Student/Computer-Science to see records of all students with Computer Science course
Step 12: Type 192.168.99.10:5000/Student/Information Systems to see records of all students with Information Systems course

