# CMSC495Capstone: Python-Game-Hub (Group 1)
[![Static Badge](https://img.shields.io/badge/Documents-Units-blue)](https://github.com/javonpayne100/CMSC495Capstone/tree/main/doc) [![Static Badge](https://img.shields.io/badge/History-GameHub-purple)](https://www.samsung.com/us/apps/gaming-hub/) [![Static Badge](https://img.shields.io/badge/History-TicTacToe-purple)](https://en.wikipedia.org/wiki/Tic-tac-toe) [![Static Badge](https://img.shields.io/badge/History-Trivia-purple)](https://en.wikipedia.org/wiki/Trivia) [![Static Badge](https://img.shields.io/badge/History-Breakout-purple)](https://en.wikipedia.org/wiki/Breakout_(video_game))
## Copyright Usage and License
Regarding Copyright laws by GitHub, it states that a public repository without a license means that others must fork the repository to utilize and modify the code as the team retains all proprietary rights.
Links:  
- [GitHub Copyright and Licenses](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)
- [GitHub Terms of Service](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service)

## Information
Based on our CMSC 495 CS Capstone class, the **Python Game Hub** project is designed to create a centralized platform for multiple mini-games, including **Tic-Tac-Toe**, **Trivia**, and **Breakout**. The application is developed using **Python** and **Pygame**, providing an engaging and interactive user interface. This project focuses on integrating games into one platform with a smooth user experience, modular game logic, and easy-to-understand code structure. The project’s purpose is to create a centralized Offline Game Hub, allowing users to select and play various games in one application. Git will be used for version control, and unit testing will ensure each component meets requirements. Deliverables include a fully functional game hub with an intuitive GUI, featuring modular game components and, an interactive **Information** Button (requires internet access) to the README.md file for the history and other information about the game. The development will be tracked through version control and tested using unit testing.

### Contact and Outside Contributing
- Feel free to reach out to our team on GitHub if you want to use our code under a specific license, without needing to fork this repository, or want to be a part of the contribution team.

## Authors / Team
  - Note: These roles are what the majority of the time each person is completing, but the team is willing to swap out roles to help out in other sections.
  - **Victoria Lee** - *Project Manager / Technical Writer / Tester (GitHub Actions / Repo)*  
    [VictoriaRaven](https://github.com/VictoriaRaven)
  - **James Mutry** - *Technical Writer / Tester (Unit Tests & Manual Tests)*  
    [jamesmutry](https://github.com/jamesmutry)
  - **Javon Payne** - *Git Lead (.py files) / Developer (MainMenu & Trivia) / Sub Tester*  
    [javonpayne100](https://github.com/javonpayne100)
  - **Todasha Foster** - *Developer (Breakout) / Sub Tester*  
    [DatFoster123](https://github.com/DayFoster123)
  - **Dajin Chung** - *Developer (TicTacToe) / Sub Tester*  
    [dajinchung](https://github.com/dajinchung)
  - **Oluwatumininu Ipaye** - *Developer (Breakout) / Sub Tester*  
    [tumiwiththewave](https://github.com/tumiwiththewave)

## Table of Contents (Key Parts Only)
  * [**How to Set Up the Game**](#how-to-set-up-the-game)
  * [**How to Play the Games & Navigate the Game Hub's Main Menu**](#how-to-play-the-games--navigate-the-game-hubs-main-menu)
  * [**History of the Game Hub and Games**](#history-of-the-game-hub-and-games)
  * [**Python Game Hub Introduction, Requirements, and Objectives**](#python-game-hub-introduction-requirements-and-objectives)
    + [Unit Testing and Manual Testing Instructions](#unit-testing-and-manual-testing-instructions)
    + [Overview of Unit 1-8 Progress Conclusion](#overview-of-unit-1-8-progress-conclusion)
    + [User Guide](#user-guide-before-deployment)
  * [**Acknowledgements / Resources / References**](#acknowledgements--resources--references)

# **Quick Project Overview**
The **Python Game Hub** provides a Game Hub to host three games: **Tic-Tac-Toe**, **Trivia**, and **Breakout**. It uses **Python** and **Pygame** to deliver a rich, interactive user interface with seamless transitions between games. The hub also integrates Git for version control to manage the development lifecycle.

## **How to Set Up the Game**
### 0. Forking Repository
This option is **ONLY** if you have a Git Account and are comfortable using Git to run the application. This is also for users who would like to add contributions to our game as well as per the GitHub policies previously mentioned in the Copyright / License Section. **Skip to 1)** if you do not want to use this method.
- First, Login with your Git account
- Go to the repository page of this project
- Then click **Fork**
- Then select **Create a new fork**
- Make sure to copy only main
- Then Go to the step of *2) Options to Run Application* **part c**

### 1. Download the Zip / Clone Repository
To get started with the project, first go to the repository page of this project. Then CLICK in this order at the top right-hand green button:
```bash
<>Code -> Download Zip
OR
<>Code -> $ git clone https://github.com/javonpayne100/CMSC495Capstone.git
```
This will allow you to download the Zip file or clone the repository successfully. If you have the Zip file extract it onto a Python IDE Directory folder of the new project, but you must have Python installed on your machine.
## **2. Options to Run Application**
- a) Run through a Python IDE
- b) Run through Python Terminal after setting up the virtual environment
- c) Run through Python IDE after Forking Repository

### **a. Set up PyCharm, Set up a virtual environment, Install dependencies, Run Application**
Before running the application, make sure you have **Python** installed on your machine. You can download Python from the official website: [Download Python](https://www.python.org/downloads/).
Once Python is installed, you'll need to install the dependencies for the project either through the PYTHON IDE terminal that you installed PyCharm [Download PyCharm Community for Windows](https://www.jetbrains.com/pycharm/download/?section=windows) OR [Download PyCharm Community for Mac](https://www.jetbrains.com/pycharm/download/?section=mac) OR [Download PyCharm Community for Linux](https://www.jetbrains.com/pycharm/download/?section=linux).
Then you must open PyCharm:
  - Make a new Project with these instructions: [Create a Python Project](https://www.jetbrains.com/help/pycharm/creating-empty-project.html)
  - Follow all steps including making sure a virtual environment is set up with the Python you installed.
  - Close the project and exit the application.
  - Go to the Directory of the project you created
  - Extract the Zip files into that folder
  - Open PyCharm again and access the project you created as it should have all the files in the Project
  - 2) This option would be to use the Git clone but you *must* clone it to the new project's directory. See this link: [Git Clone to Project](https://www.jetbrains.com/help/pycharm/set-up-a-git-repository.html#put-existing-project-under-Git)
  - Next, once Python and Pycharm are set up and installed, you'll need to install the dependencies for the project either through the Python terminal that you installed. Make sure pip is updated. Use these commands to navigate to them and install them:
```bash
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
```
  - Next, if this does not work, you will have to install the imports one by one by clicking on all the **MainMenu.py**, **test.py**, **Breakout.py**, **TicTacToe.py**, **Trivia.py**, and at the top of the imports, click on every imports so that they can be automatically downloaded through PyCharm's Python. Or go to each of them and then type in the Python Packages search bar for each one and install them there.
  - Then once done, **Run** the Python application:
```bash
python MainMenu.py
```
  - OR you could go to the top, double click on the **MainMenu.py** file
  - Then go to the top left corner near the arrow run button and click on the **tab** -> **CurrentFile**.
  - Then while staying on that file click on the **Run** button which is the Green Arrow.

### **b. Set up a virtual environment, Install dependencies, Run Application**
Before running the application, make sure you have **Python** installed on your machine. You can download Python from the official website: [Download Python](https://www.python.org/downloads/).
Once Python is installed, you'll need to install the dependencies for the project either through the Python terminal that you installed. Use these commands to navigate to them and install them:
```bash
cd <directory location where you put the project files>
[ex: cd D:\CMSC495Capstone]
```
Next, set up a virtual environment:
  - For Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```
  - macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```
Next, these dependencies are listed in the **requirements.txt** file. Make sure pip is updated. Use the following commands to install them:
```bash
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
```
Run the Python application: After the dependencies are installed, they can simply run the Python application, for example:
```bash
python MainMenu.py
```
### **c. After Forking, Set up PyCharm, Set up virtual environment, Install dependencies, Run Application**
Before running the application, make sure you have **Python** installed on your machine. You can download Python from the official website: [Download Python](https://www.python.org/downloads/).
Once Python is installed, you'll need to install the dependencies for the project either through the PYTHON IDE terminal that you installed PyCharm [Download PyCharm Community for Windows](https://www.jetbrains.com/pycharm/download/?section=windows) OR [Download PyCharm Community for Mac](https://www.jetbrains.com/pycharm/download/?section=mac) OR [Download PyCharm Community for Linux](https://www.jetbrains.com/pycharm/download/?section=linux).
Then you must open PyCharm:
  - Make a new Project with these instructions: [Create a Python Project](https://www.jetbrains.com/help/pycharm/creating-empty-project.html)
  - Follow all steps including making sure a virtual environment is set up with the Python you installed.
  - Login the Git into the Python and use the Git Clone or fetch the repository of the Forked repository you made. [Forking PyCharm Help](https://www.jetbrains.com/help/pycharm/fork-github-projects.html)
  - 2) This option would be to use the Git clone but you *must* clone it to the new project's directory. See this link: [Git Clone to Project](https://www.jetbrains.com/help/pycharm/set-up-a-git-repository.html#put-existing-project-under-Git)
  - Next, once Python and Pycharm are set up and installed, you'll need to install the dependencies for the project either through the Python terminal that you installed. Make sure pip is updated. Use these commands to navigate to them and install them:
```bash
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
```
  - Next, if this does not work, you will have to install the imports one by one by clicking on all the **MainMenu.py**, **test.py**, **Breakout.py**, **TicTacToe.py**, **Trivia.py**, and at the top of the imports, click on every imports so that they can be automatically downloaded through PyCharm's Python. Or go to each of them and then type in the Python Packages search bar for each one and install them there.
  - Then once done, **Run** the Python application:
```bash
python MainMenu.py
```
  - OR you could go to the top, double click on the **MainMenu.py** file
  - Then go to the top left corner near the arrow run button and click on the **tab** -> **CurrentFile**.
  - Then while staying on that file click on the **Run** button which is the Green Arrow.

## **How to Play the Games & Navigate the Game Hub's Main Menu**
### Main Menu (Game Hub)
- Once *"MainMenu.py"* is running, the user can select the following options:
    - Information
    - Tic Tac Toe
    - Trivia
    - Breakout
    - Exit
- Options on how to play are below...
### Information
- Select Information from the main menu.
- This redirects the user to a hyperlink of our Python Game Hub Repository on GitHub.
- The user can select the history at the top of the README.md file and other information on the README.md file.
- The user can use the README.md file to learn how the game works/how to play.
- The user can see our development/testing/documentation process.
- This option requires internet (not offline) and the other games are offline.
### Tic-Tac-Toe
- Select Tic-Tac-Toe from the main menu.
- In this game, the AI is the X, and the player is you O.
- Use mouse clicks to place X's and O's on the board.
- AI will automatically make decisions.
- You as the user as O make a move after AI who is X.
- Three X's or O's means you win, else you either lose or tie.
- The game will automatically check for win/loss/draw conditions after each move.
- Once the game is over, you can choose to play again or return to the main menu.
### Trivia
- Select Trivia from the main menu.
- The user has the option for 1 player (human) or 2 player (human vs. human)
- The user will input their name
- The user can select 1 of the different subjects for the Trivia
- The game will display a multiple-choice question with four options.
- Answer the question before the time runs out (indicated by the timer and music).
- The timer is green when it's more time, yellow when getting closer to the end time, and it turns red, meaning it is the end of time to select an answer.
- When you answer, it will quickly flash if you got it wrong (red), or correct(green)
- The score will increase for each correct answer.
- If doing 2 players, it will show the scores and tell who wins.
- Once all questions are answered, you will see your final score and can choose to play again or return to the main menu.
### Breakout
- Select Breakout from the main menu.
- Control the paddle with the left and right arrow keys.
- Try to break all the blocks with the bouncing ball.
- Some blocks require the ball to hit more than 1 to destroy the block.
- You have three lives, and it counts the score based on the blocks you destroyed with the ball with sound effects.
- If you lose all your lives, you will hear the game over sound, and you can restart the game or return to the main menu.
### Exit
- Select Exit from the main menu.
- It will Exit the Python Game Hub and exit the Python Application.
## History of the Game Hub and Games
### Gaming Hub  
- This Gaming Hub is similar to the Samsung Gaming Hub, which lets users access multiple games (like a library) without needing a console.
- For this case, the only thing that needs the internet is the **Information** selection. The rest are all offline games as it's been integrated into the game hub.
### Tic-Tac-Toe
- Tic-Tac-Toe is an ancient game, going back to Roman times. It’s simple—just a 3x3 grid where players try to get three Xs or Os in a row.
- It became popular worldwide because it’s easy to learn and quick to play.
### Trivia
- Trivia games took off in the 20th century, especially with board games like *Trivial Pursuit* in the 1980s.
- The idea is simple: answer questions on random topics. Now it's everywhere—from bar nights to mobile apps like HQ Trivia.
### Breakout
- Breakout was created by Atari in 1976. Players control a paddle to bounce a ball and break bricks at the top of the screen.
- It helped shape the arcade gaming boom and inspired many block-breaking games afterward.
### More History Details?
- Refer to the History links at the top of the **README.md** file.
- It will send you hyperlinks to a Wikipedia page of the whole history behind it per each topic.
## **Python Game Hub Introduction, Requirements, and Objectives**
This document outlines the deliverables for a CMSC Capstone project: a multi-game application developed with Python and Pygame, featuring games like Tic-Tac-Toe, Trivia, and Breakout within a unified GUI. The project follows the Waterfall development model, progressing through defined phases: Requirements Analysis, System Design, Implementation, Testing, and Maintenance. This focuses on gathering detailed requirements, initial design, and prototyping, as well as developing functional modules like the main menu and early versions of the games. The project’s purpose is to create a centralized Game Hub, allowing users to select and play various games in one application. Git will be used for version control, and unit testing will ensure each component meets requirements. Deliverables include a fully functional game hub with an intuitive GUI, featuring modular game components and, optionally, an SQLite database for tracking user profiles and high scores. The development will be tracked through version control and tested using unit testing.
### Testing/Debugging Requirements:
  - To track progress on each coding section, we will use Git for Version Control.
  -  Each process will include a Git commit section
  - Each readme file will ensure that the user knows how the set the requirements of the software and run the application to play the games.
  - Note: Refer to "doc" folder which is up-to-date with all our Technical Documentation per Unit (weeks: 1-8)
### Version Control with Git
This project uses Git for version control. Git will be used to track the progress of the project, manage code changes, and ensure collaboration between developers. Every change made to the codebase will be tracked with commit messages, providing a clear history of the project's development. Here's how we manage code changes:
#### Branching and Commit Process
- Create a Branch: Each developer creates a separate feature branch for a specific task (e.g., name-of-team-member/MainMenu; name-of-team-member/TicTacToe.py, etc.).
- Commit Changes: Developers commit incremental changes with descriptive commit messages (e.g., Added game over condition for TicTacToe.py, Triva.py, Breakout.py).
- Push Changes: After completing tasks in a remote branch that was created, developers push the branch to GitHub.
- Pull Request (PR): Create a Pull Request for code review. Once approved, the changes are merged into the main branch.
### Code Review and Merge
- If changing major game files `.py`, the Git Leader will get approvals from the PR and ensure code quality and functionality.
- If changing minor files (txt, md, not game files, etc) the user(name of team) will get approvals from the PR and ensure code quality and functionality.
- Once the Git Leader/User(team) passes the review, it will be merged into the main branch.
- The Project Manager and the Testers will ensure that each update is working and tested.
- Developers will regularly pull the latest changes from the main branch to keep their feature branches up to date and avoid conflicts.
- If any merge conflicts arise, the developer will resolve them before pushing their changes, ensuring that the codebase remains functional and consistent.
#### See Git History Progress
  - To see the Progress go to the project repository [CMSC495Capstone](https://github.com/javonpayne100/CMSC495Capstone)
  - Click on Branches to see all Branches. Then click on Each branch individually to see the changes in each branch. Once finished, go back to the project
  - Click on Pull Requests to see all the branches that were merged into the main. Opens are the ones not merged but able to be compared, the closed ones should show the branches that were merged into the main after approval and comparison. This method protects the main final and makes sure that the main files are not touched. Once, finished, go back to the project.
- Click on the Issues to see all the open and closed issues per milestones and tags.
- Click on the Actions to see all the Unit Tests run through GitHub actions by the (.yml) files.
  - Note: You can also see each Weekly Unit progress on Git through the "docs" folder where it shows per each week.
### Testing and Debugging
- Unit Testing: Test each game module (Tic-Tac-Toe, Trivia, Breakout) for correctness.
- Integration Testing: Ensure the main menu and individual game modules work seamlessly together.
- System Testing: Test the full application to ensure the overall user experience is smooth.
### **Unit Testing and Manual Testing Instructions:**
- Go to the file **"test.py"** in the main branch and Run it. It should test 13 unit tests all in that file for the games.
- Go to the file **"test.py"** in the James branch and run it through his branch. It should test 24 unit tests all in that file for the games.
- If it doesn't work, click on each method section for the game and run it one by one.
0)  **Steps/Procedures**:
1) **GitHub Actions (24 unit tests) (new test.py) (Skip if you do not have access to the Repo)**:
- Go to https://github.com/javonpayne100/CMSC495Capstone
- Go to Actions Tab
- If Workflow is Disabled, Enable it
- Click on the Workflow [1) Run Unit Tests For Mac with all push (James Branch); 2) Run Unit Tests For Windows with all push (James Branch); 3) Run Unit Tests For Ubuntu with all push (James Branch)]
- Go to the right side of “This workflow has a workflow_dispatch event trigger.”
- Click on Run Workflow
- Make sure it’s on Main branch (the .yml files autoruns on separate branches even if run through main)
- Click Run Workflow (green to confirm)
- Refresh the page to see the GitHub Action process and if green it passes
- Environments runs (Win, Mac, Linux), but Ubuntu has glitches due to Git’s ongoing issue.
- Now Repeat Steps (1-10) ONLY if you want to test out the old test.py with 13 unit tests. 
- On step 4 choose these workflows: [ Run Unit Tests For Mac with all push; Run Unit Tests For Windows with all push; Run Unit Tests For Ubuntu with all push ]
- Command line, terminal or PowerShell steps: 
- Download the code from GitHub in the “james” branch. Refer to README.md for help.
- Navigate to the project directory
- Ensure installation of pygame, numpy and pyautogui using “pip install pygame numpy pyautogui” or install dependencies through the requirements.txt like shown in README.md
- Run python -m unnitest test.py
2) **Testing in IDE**:
- Download the code from GitHub in the “james” branch. 
- Open IDE and open the project from where it was saved
- Install all needed libraries (IDE should prompt to do this automatically)
- Select the test.py
- Run test.py
3) **Test Data preparation**:
- Old Unit Testing will be done through the “main” branch of the GitHub, test.py.
- New Unit Testing will be done through the “james” branch of the GitHub, test.py will not work properly in another branch
- Manual Testing will be done through the “james” and “main” branches.
- Questions.json data must be valid and located in the directory the Trivia module expects it
- brick.wav, wall.wav, paddle.wav, and any other required .wav files in the same directory as the game files.
- Breakout mechanics depend on default positions and attributes defined in the code—ensure these are not modified before testing.
4) **Test Environment Configuration**:
- Operating System: Windows, macOS, or Linux
- Python Version: 3.9 or later
- Terminal Tools: Command line, PowerShell, terminal, or IDE
- Required Libraries: Pygame, json, math, random, sys, time, unnittest, numpy, pyautogui
- Audio: Ensure audio output is enabled to validate sound-related tests.
- Display: Use a resolution of at least 600x400 for consistent rendering.
- GitHub Actions:  Required you have access to the Repository and can go to the Actions tab
0) **CMSC 495 Project Test Plan.xlsx (Manual Testing):**
- Go to the docs to find a copy of the Excel sheet/ table for manual testing. 
- Or Go to the docs in unit 5 to get the link to the Excel sheet / table for manual testing.
- This is 20 Manual Tests using the Excel method that was proven in the Unit Week Learning Resources.
- Specifically, it will demonstrate the Main Menu(5 manual testing), Trivia(5 manual testing), Tic-Tac-Toe(5 manual testing), and Breakout(5 manual testing).
- This makes a total of 20 Manual Tests for this manual testing.xlsx file.
1) **Steps/Procedures**:
- Command line, terminal or PowerShell steps: 
- Download the code from github in the “james” branch. Refer to README.md for help.
- Navigate to the project directory
- Ensure installation of pygame, numpy and pyautogui using “pip install pygame numpy pyautogui” or install dependencies through the requirements.txt like shown in README.md
- Run the main menu with: python MainMenu.py
- From there test Main Menu and each linked game (Tic Tac Toe, Trivia, Breakout)
- Follow the steps provided in the CMSC 495 Project Test Plan.xlsx file
- For each test Perform the Input/Action
- Observe the result
- Compare it against the Expected Result
- Log pass/fail status
- Repeat (steps 1-6) but download the code from github in the “main” branch. Refer to README.md for help. This is only for manual, you cannot do this for unit tests.
2) **Testing in IDE**:
- Download the code from GitHub in the “james” branch. Refer to README.md for help.
- Open IDE and open the project from where it was saved
- Install all needed libraries (IDE should prompt to do this automatically)
- Select and run MainMenu.py
- From there test Main Menu and each linked game (Tic Tac Toe, Trivia, Breakout)
- Follow the steps provided in the CMSC 495 Project Test Plan.xlsx file
- For each test Perform the Input/Action
- Observe the result
- Compare it against the Expected Result
- Log pass/fail status
- Repeat (steps 1-6) but download the code from GitHub in the “main” branch. Refer to README.md for help. This is only for manual, you cannot do this for unit tests.
3) **Test Data preparation**:
- Old Unit Testing will be done through the “main” branch of the GitHub, test.py.
- New Unit Testing will be done through the “james” branch of the GitHub, test.py will not work properly in another branch
- Manual Testing will be done through the “james” and “main” branches.
- Questions.json data must be valid and located in the directory the Trivia module expects it
- brick.wav, wall.wav, paddle.wav, and any other required .wav files in the same directory as the game files.
- Breakout mechanics depend on default positions and attributes defined in the code—ensure these are not modified before testing.
4) **Test Environment Configuration**:
- Operating System: Windows, macOS, or Linux
- Python Version: 3.9 or later
- Terminal Tools: Command line, PowerShell, terminal or IDE
- Required Libraries: Pygame, json, math, random, sys, time, unnittest, numpy, pyautogui
- Audio: Ensure audio output is enabled to validate sound-related tests.
- Display: Use a resolution of at least 600x400 for consistent rendering.
#### Testing Overview:
Automated testing was implemented using Python’s `unittest` framework to validate critical components of the Tic Tac Toe, Trivia, and Breakout modules. The test suite verifies game mechanics such as win detection, board state, and AI behavior in Tic Tac Toe. For Trivia, tests were written to inspect the structure of the question data loaded from JSON, as well as the correctness of answer indexing. The Breakout tests include health reduction of blocks, ball reset logic, paddle boundaries, and collision detection between game elements. In other words, all 14 tests focus on critical game mechanics like win detection, board state, and AI behavior (Tic Tac Toe), question structure and answer indexing (Trivia), and collision detection and block health (Breakout).
Following the Waterfall development methodology, future testing will be structured as a distinct phase conducted after the completion of full system implementation. This dedicated testing phase will begin with unit testing, targeting each module, Tic Tac Toe, Trivia, and Breakout to verify core functionalities such as AI decisions, answer validation, collision detection, and object behavior. Once unit-level verification is complete, the process will move into integration testing to ensure smooth interaction between components, including menu navigation, game transitions, and audio/visual responses. System testing will follow, simulating real-world usage scenarios to confirm that the application performs reliably under typical and extreme conditions. Lastly, acceptance testing will be performed to validate that all project requirements have been met and the application aligns with stakeholder expectations. Testing outcomes will be documented in detail, and any issues uncovered will be addressed through a feedback loop prior to final deployment. This structured approach ensures a thorough and sequential validation of the system’s readiness for delivery. Through the testing approach, we will also use the software engineering techniques of unit Testing to ensure that each part is tested and debugged correctly.
- **Next Phase Testing (Breakdown)**:
  - Future testing will follow the Waterfall methodology, starting after full system implementation.
  - **Unit Testing**: Verify core functionalities (AI decisions, answer validation, collision detection).
  - **Integration Testing**: Ensure smooth interaction between components (menu navigation, game transitions, audio/visual responses).
  - **System Testing**: Simulate real-world scenarios to confirm reliability under typical and extreme conditions.
  - **Acceptance Testing**: Validate that all project requirements are met and align with stakeholder expectations.
  - All testing outcomes will be documented, and issues will be addressed through a feedback loop before final deployment.
- **Unit Testing Focus**:
  - **Game Logic**: Test game loops, score updates, and win/loss conditions for each game.
  - **UI Components**: Ensure UI elements (buttons, menus, score displays) are interactive, responsive, and correctly linked to game functions.
  - **High Scores**: Verify that user scores are saved and retrieved correctly.
  - **Lives & Scoreboard**: Test accurate tracking, display, and updating of lives and scores during gameplay.
  - **Error Handling**: Ensure the game handles unexpected inputs and errors, maintaining a smooth user experience.
- **Debugging Process (Simple Breakdown)**:
  - Debug each game module systematically to identify and fix issues.
  - **UI Debugging**: Ensure the interface is intuitive and responsive across devices and screen sizes.
  - **Performance Testing**: Confirm games load in under 3 seconds and run smoothly, even on lower-end devices.
  - **Cross-Platform Compatibility**: Test the application on multiple platforms to ensure consistent functionality across operating systems.
#### Debugging Process
- Use Git to track and resolve issues by creating separate branches for bug fixes.
- Issues can be either included in the Git or done thorough a local machine.
- Each commit / new push after a PR will document the changes and improvements made during debugging.

## Project Architecture
This portion is included in the document folder **"docs"** showing each unit per week and the diagrams included in one of the sections.
### Start of the Implementation:
- **Implementation Overview**: 
  - Built a multi-game desktop app using Python and Pygame.
  - Project follows a modular design with separate game modules (Tic Tac Toe, Trivia, Breakout) integrated through a centralized menu.
- **Main Interface**:
  - MainMenu.py features a gradient background, hover-sensitive buttons, and click interactions.
  - Games are launched through a navigate() function.
  - Background music plays continuously in the menu and stops/resumes when switching games.
- **Breakout Game**:
  - Core classes: Ball, Striker, and Block.
  - Collision detection and sound effects triggered with `pygame.mixer.Sound()`.
  - Block health varies by color, where some blocks must be hit more than once, with blocks removed upon destruction and player scores incremented.
  - Game over condition triggers a replay prompt using pyautogui, with an option to play again or exit.
- **Tic Tac Toe**:
  - Graphical board with grid lines and symbols (X and O).
  - Player moves are registered via mouse clicks.
  - AI opponent uses minimax algorithm for optimal moves (recursive logic for win, loss, and draw).
  - Displays result and a custom “Play Again” button after each round to play again or exit.
- **Trivia Game**:
  - Randomly shuffled multiple-choice questions with four answer options.
  - Circular countdown timer uses trigonometric functions to show remaining time.
  - Correct answers increase the score, incorrect ones skip the question.
  - A “Game Over” screen appears at the end with an option to play again or exit.
- **Sound and Media**:
  - Sound effects and background music handled via `pygame.mixer`.
  - Scalable and maintainable design, allowing easy addition of new games or features.
  - Iterative development with continuous testing, feedback, and refinement.
### Use Case Diagram
The use case diagram illustrates how users interact with the application: starting from launching the app, selecting a game from the main menu, and engaging with the game mechanics (e.g., playing against the AI in Tic-Tac-Toe or answering questions in Trivia).
### Activity Diagram
The activity diagram shows the flow of actions, starting from the application launch, progressing through the game selection, game flow, and end-of-game options (such as playing again or returning to the main menu).
### Class/UML Diagram
- Tic-Tac-Toe: Contains classes like Board, Player, and AI.
- Trivia: Includes classes such as QuestionManager, Timer, and Score.
- Breakout: Utilizes classes like Ball, Paddle, and Block.
- MainMenu: Contains the Game Hub main files so that the user can access this and it will select the games to be played.

## Overview of Unit 1-8 Progress Conclusion
### Project Plan Goals:
- Develop a Python-based Game Hub application with multiple mini-games (Tic Tac Toe, Trivia, and Breakout).
- Use a modular design for easy maintenance and future game additions.
- Integrate version control with Git and implement unit testing for component verification.
- Follow the Waterfall development model for structured project phases.
### Project Design Goals:
- Create a centralized menu system for easy navigation between games.
- Implement individual game modules (Tic Tac Toe, Trivia, Breakout) with interactive user interfaces.
- Use Pygame to build an engaging graphical and audio experience for users.
- Ensure scalability and maintainability for future enhancements.
### Phase 1 Goals:
- Focus on requirements gathering, initial design, and prototyping.
- Develop early functional modules like the main menu and working versions of the games.
- Ensure alignment between project objectives and technical execution.
- Set a foundation for reliable, maintainable development in subsequent phases.
### Testing Goals:
- Implement automated unit tests using Python’s `unittest` framework to validate core game mechanics.
- Perform unit testing for game logic, UI components, high score tracking, error handling, and performance.
- Follow a structured testing approach including unit, integration, system, and acceptance testing.
- Document testing outcomes and address issues before final deployment.
### Phase 2 Goals:
- Conduct full system implementation with finalized features and functionality.
- Perform integration testing to ensure smooth interaction between components (e.g., game transitions, audio, menu navigation).
- Simulate real-world usage scenarios through system testing.
- Conduct acceptance testing to confirm the application meets all project requirements and stakeholder expectations.
### User Guide (Before Deployment):
- Develop a clear and concise **User Guide** detailing how to navigate the Game Hub.
- Provide instructions for starting the application, selecting games, and using UI features (e.g., scoreboards, game controls).
- Include troubleshooting tips, known issues, and any additional features or options available in the game hub.
- Refer to the docs folder section in the unit 7 folder to access our User Guide version.
- Link is here: [User Guide (docs/Unit7)](https://github.com/javonpayne100/CMSC495Capstone/tree/main/doc/Unit7)
### Deployment Goals:
- Finalize the application after testing and bug fixes.
- Ensure cross-platform compatibility and smooth performance on different devices.
- Deploy the project for user access, ensuring all requirements are met.
- Monitor post-deployment performance and user feedback for future updates.
### Acknowledgements / Resources / References
- **NOTE:** This *README.md* file was created and updated by the team member: [VictoriaRaven](https://github.com/VictoriaRaven)
- As a **Team**, we would like to take this moment to express our heartfelt thanks to our teammates who helped bring this project to life.
- The **Python Game Hub** wouldn’t have been possible without the dedication, collaboration, and expertise of each team member.
- All of the gratitudes are below:
  - **Victoria Lee** [GitHub: VictoriaRaven](https://github.com/VictoriaRaven): As a Project Manager / Technical Writer / Tester (GitHub Actions / Repo), I want to express my deepest gratitude to my amazing team for their unwavering dedication and hard work throughout this project. The way we came together, blending our skills, strengths, commitment,and teamwork like in the *Avengers*, a Marvel movie, made this experience truly special (Whedon, 2012). I also want to extend a heartfelt thank you to my peers and family, whose suggestions helped shape the final product. Your support, both on and off the project, was invaluable and truly appreciated. Thank you and as always, “Not all treasure is silver and gold, mate.” - Captain Jack Sparrow (Pirates of the Caribbean) (Verbinski, 2003).
  - **James Mutry** [GitHub: jamesmutry](https://github.com/jamesmutry): As a Technical Writer / Tester (Unit Tests & Manual Tests), I would like to take this opportunity to sincerely thank my entire team for their dedication, hard work, and collaboration throughout the Python Game Hub project. Each member brought their own unique skills and strengths, contributing to the success of this challenging and rewarding experience. From initial planning to final deployment, our team consistently supported one another, tackled obstacles together, and maintained a strong commitment to producing a polished and functional final product. I am especially grateful for the positive attitude, adaptability, and professionalism that everyone demonstrated during each phase of the project. Working alongside such a talented and motivated group made this capstone experience not only educational but truly enjoyable. I am proud of what we accomplished together and thankful to have had the opportunity to collaborate with such an outstanding team.
  - **Javon Payne**  [GitHub: javonpayne100](https://github.com/javonpayne100): As a Git Lead (.py files) / Developer (MainMenu & Trivia) / Sub Tester), I want to give a huge thanks to my team for bringing me on board with open arms. It’s a blessing to have a team with diverse skills, restless drive, and great character. This experience has definitely taught me a lot and this type of camaraderie should be the standard of many development teams. I want to especially thank Victoria; her organization skills and leadership is unmatched. Congratulations everyone, graduation is here! “May the force be with you.” - Yoda
  - **Todasha Foster** (GitHub: DayFoster123](https://github.com/DayFoster123): As a Developer (Breakout) / Sub Tester, I would like to express my sincere appreciation to my team members for their energy, creativity, and collaboration throughout this project. Contributing as a developer was a rewarding experience that allowed me to strengthen my skills and grow professionally. I am proud of the challenges we overcame together and the final products we created. This achievement reflects the passion, effort, and dedication of every member of the team. "I never dreamed about success. I worked for it." – Estée Lauder
  - **Dajin Chung** [GitHub: dajinchung](https://github.com/dajinchung): As a Developer (TicTacToe) / Sub Tester, I’d like to thank my entire team for their hard work and collaboration throughout this project. Each member contributed their strengths, from development and testing to design and documentation, to bring this project to life. A special thanks to Victoria, who truly stepped up as project manager. Her organization, communication, and consistent support helped keep our team focused and on track. We would not have reached this level of polish and completion without her leadership. Everybody, thank you for all your hard work. As a wise ogre once said, “That’ll do Donkey. That’ll do.” - Shrek
  - **Oluwatumininu Ipaye** (GitHub: tumiwiththewave](https://github.com/tumiwiththewave): As a Developer (Breakout) / Sub Tester, I want to express my deepest gratitude to the entire team for their hard work and resilience to get this project done. I have been able to learn a lot from each single member and effectively learnt how to work in a group setting such as this. My skills have been boosted and challenged at the same time, which shows that being a coder/programmer is a never ending lesson. I would like to specially thank Victoria Lee, as she was the backbone of this entire project and ensured everything went smoothly and without any hitches. I am proud of what we were able to accomplish in a short period, and wish you all the best ahead. "The sky’s the limit."

- [Pygame Documentation](https://www.pygame.org/docs/)
- [Python Documentation](https://docs.python.org/3/)
- [GeeksforGeeks SDLC Waterfall Model](https://www.geeksforgeeks.org/software-development-life-cycle-sdlc/)
- [GitHub Resources](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service)
- [Google Scholar](https://scholar.google.com/)
- [Wikipedia](https://www.wikipedia.org/)
- [UMGC Library](https://libguides.umgc.edu/home)
- [UMGC CS Resources](https://libguides.umgc.edu/c.php?g=316603&p=2114865)
- [UMGC Peer to Peer File Sharing](https://www.umgc.edu/content/dam/umgc/documents/upload/peer-to-peer-file-sharing.pdf)
- [UMGC Copyright and Fair Use](https://libguides.umgc.edu/copyright#s-lg-box-26283861)
- [UMGC Creative Commons](https://libguides.umgc.edu/c.php?g=23404&p=7944948)
