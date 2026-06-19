# Final Assessment
Welcome!
This assessment evaluates your debugging skills, understanding of LangGraph framework, and ability to build AI agents. You will complete two assignments:

Assignment 1: Debug a broken Weather Agent
Assignment 2: Build a Stock Market Analysis Agent from scratch
Before You Begin
Prerequisites
Required Knowledge:

Python programming (functions, classes, data structures)
Basic understanding of APIs and HTTP requests
Familiarity with debugging techniques
Command line / terminal basics
Recommended (but not required):

Experience with Jupyter Notebooks
Understanding of state machines or workflow systems
Basic financial markets knowledge (for Assignment 2)
System Requirements
Python 3.9 or higher
Git installed
Visual Studio Code (recommended) or any Python IDE
Jupyter Notebook support
Stable internet connection (for API calls)
Assignment Overview
Assignment 1: Weather Agent Debugging
Objective: Debug a broken LangGraph weather agent to make it functional.

What you'll receive:

A weather agent codebase with intentional bugs
The agent should fetch location data based on IP address and display current weather
Download the weather agent code here: weather_agent

Your task:

Identify all bugs in the provided code
Fix the bugs systematically
Ensure the agent runs successfully
Document what you fixed in a Jupyter notebook
Test with different scenarios
Expected outcome:

Working weather agent that displays location and weather information
Jupyter notebook demonstrating the fixed agent
Clear documentation of bugs found and fixes applied
Assignment 2: Stock Market Analysis Agent
Objective: Build a LangGraph agent from scratch that analyzes stocks and provides recommendations.

Requirements:

Accept a stock ticker symbol (e.g., "AAPL", "MSFT")
Fetch 60 days of historical stock data using yfinance
Calculate technical indicators:
Simple Moving Average (10-day and 20-day)
Relative Strength Index (14-day)
Provide BUY/HOLD/SELL recommendation based on specified logic
Display formatted analysis report
Your task:

Design and implement the agent architecture with required nodes
Implement technical indicator calculations
Create recommendation logic
Build a working demonstration in Jupyter notebook
Handle errors gracefully (invalid tickers, network issues)
Expected outcome:

Complete stock analysis agent with proper folder structure
Working Jupyter notebook demonstration
Clean, well-documented code
Professional output formatting
Setup Instructions
Step 1: Environment Setup
# Create a virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install Jupyter
pip install jupyter
Step 2: Create Your Repository
# Create a new repository on GitHub
# Name: langgraph-assessment
# Make it PUBLIC

# Clone your repository
git clone https://github.com/[your-username]/langgraph-assessment.git
cd langgraph-assessment

# Create folder structure
mkdir assignment_1 assignment_2
Step 3: Download Assignment Files
Download the Weather Agent code from the SharePoint link provided above and place it in the assignment_1 folder.

Your folder structure should look like:

langgraph-assessment/
├── .gitignore
├── README.md
├── assignment_1/
│   ├── weather_agent_debug.ipynb
│   └── weather_agent/
│       ├── main.py
│       ├── graph.py
│       ├── requirements.txt
│       └── components/
└── assignment_2/
    └── (you'll create this)
Working with Jupyter Notebooks
Why Jupyter for This Assessment?
Jupyter notebooks allow you to:

Run code incrementally and see immediate results
Document your thought process inline
Easily demonstrate working solutions
Debug interactively
Import Path Management
When your code is in a separate folder, you'll need to manage Python's import paths properly. This is a common requirement when working with modular code in notebooks.

Notebook Best Practices
Keep outputs visible - don't clear cell outputs before submission
Use markdown cells to explain your approach and reasoning
Structure your notebook with clear sections
Test different scenarios to demonstrate functionality
Show both working cases and error handling
Evaluation Criteria
What We're Looking For
Assignment 1 (Debugging):

Ability to identify and fix bugs systematically
Understanding of LangGraph concepts
Code quality after fixes
Testing thoroughness
Documentation of changes
Assignment 2 (Building):

Code organization and structure
Correct implementation of technical indicators
Proper error handling
Clean, readable code
Working demonstration
Grading Breakdown
Functionality (40%): Does it work correctly?
Code Quality (25%): Is it clean and well-organized?
Documentation (20%): Is it clear and complete?
Testing (15%): Are edge cases handled?
Use of AI Tools
AI assistants (ChatGPT, Claude, etc.) are allowed as tools to help you understand concepts, write code that you understand, debug issues, or explore solutions. However:

You must understand your code - You should be able to explain every line
AI is a tool, not a replacement - Your implementation and problem-solving approach matter
Be prepared to explain your code - During review, you may be asked to walk through your solution
Submission Instructions
Before submitting, ensure:

 All code runs without errors
 Jupyter notebooks have visible outputs
 README files are complete
 Requirements files are accurate
 Repository is PUBLIC on GitHub
 All files are committed and pushed
Once completed, share your GitHub repository link on Teams:

In the onboarding group
With Heramb Sawant (heramb.sawant@glynac.ai)
With Aman Jaiswar (aman.jaiswar@glynac.ai)
Resources
Documentation:

LangGraph Documentation
Python Requests Library
Pandas Documentation
yfinance Documentation
Python Concepts:

Type Hints: PEP 484
F-strings: PEP 498
Good luck! We're excited to see what you build!
