### Sporty Home Test
Test task: WAP for Sporty company.
Automated UI testing framework built in Python with Selenium WebDriver.  
Designed to demonstrate scalable and maintainable test architecture, using Twitch mobile web as a testing target.
A modular-driven framework with layered architecture was chosen.

#### Project Structure
- clients:  Web/mobile driver creation logic
- helpers: Utilities (scrolling, waits, etc.)
- services: Page objects and actions
- tests: Test cases
- conftest.py: Fixtures for Pytest
- requirements.txt: Dependencies
- pytest.ini: pytest configuration file
- README.md: You’re reading it

#### Stack
- Python 3.9+
- Selenium WebDriver
- Pytest
- Allure (optional, for rich test reporting)

#### Installation

```bash
git clone https://github.com/froislove/sporty_hometest.git
cd sporty_hometest
pip install -r requirements.txt
```

#### Test Execution
Run a single test:

```bash
pytest tests/web/test_twitch.py
```

Run with Allure:

```bash
pytest tests/
allure serve allure-results
```

#### Screenshot Management
All screenshots are saved to the screenshots/ directory with device name and timestamp.
Each screenshot is also attached to the Allure report automatically.
