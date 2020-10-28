## Atlan Assessment
Atlan Collect has a variety of long-running tasks that require time and resources on the servers. As it stands now, once we have triggered off a long-running task, there is no way to tap into it and pause/stop/terminate the task, upon realizing that an erroneous request went through from one of the clients (mostly web or pipeline).

## Getting started
### File System Description
The Below file description is for files contained in `application` folder.
- There is 1 python file `api.py` which is the main server(flask) file.
- There are 2 Folders: `templates` which contain 1 HTML file  for rendering the web-view(dashboard) and `modules` which contain files for process manipulation and data-fetching (processing).
- Dockerfile is used by docker-compose respectively.
- Note: When <strong>Start</strong> request is given via web-dashboard to the server, the `fetch.py` script uses `data.csv`(a fake .csv data) (location: `./application/modules/`)

#### Requirements and Assumption
- Have Python3 installed in your system.
- Make a new environment inside root folder (recommended) (use `python3 -m venv atlanVenv`).
- Activate the Environment (use `source ./atlanVenv/bin/activate`) and move to ```./application/``` folder
- Use ```pip install -r requirements.txt``` to install the dependencies and packages.
- <strong>Docker</strong> should be installed in the environment/system where this code is to run.

### Run (FLASK)
- Activate the Environment (use `source ./atlanVenv/bin/activate`)
- Goto the `./application` folder.
- Simply run the ```python api.py``` to start the server.
- To Open the dashboard (HTML rendering), goto the localhost IP address, which can be found in terminal as well.
- Click the START button, for starting the process (printing in terminal will start as soon as start button is clicked)
- Follow up with PAUSE, RESUME and STOP buttons to see the pausing, resuming and stopping of the process respectively.

### ouput/result
- Note: As of now the working of buttons and processing (data fetching) can be seen in terminal only. Except when the process is finished and stopped a simple json output is shown in the web-view.

### Run (DOCKER)
- Goto the root folder.
- Simply run the ```sudo docker-compose build``` to build the container for running.
- Run ```sudo docker-compose up``` to start the server.
- To Open the dashboard (HTML rendering), goto the localhost IP address, which can be found in terminal as well.
- Click the START button, for starting the process (printing in terminal will start as soon as start button is clicked)
- <strong>NOTE:</strong>
   - There is a problem in docker running task. Somehow I wasn't able to manipulate the process using docker (stopping/pausing/resuming). So stop the terminal process using `ctrl+c`.
   - But via FLASK (above section), this system works like a charm :).


Regards: Himanshu Khairajani