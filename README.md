# Vehicle_app

My project aims to retrieve information from a JSON file that stores personal and vehicle data and use that data as needed.
A JSON file is created for this purpose.
Firstly, a menu function runs and asks you what you want to do. There are three choices you can make.
These choices include viewing vehicle information, adding a new person, and updating vehicle kilometers.
The information stored in the JSON file consists of an array called "persons," which contains persons and their associated vehicles.
Information such as the vehicle's brand, license plate, and kilometer are stored in the vehicle dictionary. 
When you want to add a new person, you will be asked to provide the vehicle's brand, license plate, kilometer, and the person's name. 
When choosing to update the kilometer, you will first be asked for the owner's name, then the license plate, and finally, you will be prompted to enter the new kilometer.
The project is written using gRPC in a virtual environment.
Inside the project, there is a proto file, a file_manager script, and a main script. In the communication directory, you will find server and client files.

# Requirements

To run the project, you need the following requirements:
-Install gRPC and add the necessary tools to run it on your local machine.
-Compile the proto file.
