# ECSE 429 Project

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Setting Up a Virtual Environment

It's recommended to use a virtual environment to manage dependencies for your project. To set up and activate a virtual environment, follow these steps:

1. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   ```

2. **Activate the Virtual Environment**

   - On Windows

     ```bash
     .\venv\Scripts\activate
     ```

   - On MacOS/Linux

     ```bash
     source venv/bin/activate
     ```

3. **Installing Dependencies**

   ```bash
   pip install requests pytest
   ```

4. **Writing Tests**
   Tests are located in `./tests` folder.
   Create a python file prefixed with `test_` in name, e.g., `test_example.py`.
   Refer to the example with the same name for syntax.

5. **Running Tests**
   To run all tests, use pytest command in the root directory of the project.

   ```bash
   pytest
   ```
