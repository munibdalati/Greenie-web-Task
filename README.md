# Power Consumption Estimation Tool
This Python project is a simple web server that allows you to estimate the power consumption of a specific application running on your computer based on its CPU usage. The estimation is made by monitoring the average CPU usage of the specified application over a defined duration (1 second for 2 intervals).

## Prerequisites
Before using this project, ensure that you have the following prerequisites installed on your system:

* Python 3.x (https://www.python.org/downloads/)
* psutil library
```
pip install psutil
```
## Usage Instructions

1. Clone or download the project to your local machine.

2. Open a terminal or command prompt and navigate to the project directory.

3. Run the server by executing the following command:
```
python server.py
```
4. Once the server is running, this massage will appear in your terminal:
```
Server is running at http://localhost:8000
```
5. Open a web browser and navigate to http://localhost:8000. This will display a simple web page where you can interact with the server.

6. On the web page, you'll see a form where you can input an application name. So, Enter the name of the application you want to estimate power consumption for.

Important Notes descriping how to enter the application name:
* Open the application you want to calculate its power comsumption
* Open Task manager on your computer (Ctrl+Alt+Delete)
* Open Details section
* You will see the applications which are working at the moment in your computer, Search fot the application you want to calculate its power consumption
* Write the application name at the input as written in Task manager window
#### Examples:
* Google Chrome, Type: chrome.exe
* Visual Studio Code, Type: Code.exe

7. After entering Application Name, click the **Calculate** button.

The server will respond with an estimation of the power consumption for the specified application. The response will be displayed on the web page.

**Note:** Calculation process will take 3-5 seconds after pressing the button

