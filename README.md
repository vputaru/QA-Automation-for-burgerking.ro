# QA Automation for BurgerKing.ro

End-to-end test automation project for [burgerking.ro](https://burgerking.ro), built with **Python**, **Pytest**, and **Selenium**.  
The project follows the **Page Object Model (POM)** design pattern for scalable and maintainable test automation.  
Currently focused on **UI testing**, with **API test coverage** planned for future development.

---

## Tech Stack
- **Python 3.12.8**
- **Pytest** – testing framework
- **Selenium WebDriver** – browser automation
- **ChromeDriver** – driver for Google Chrome

---

## Project Structure
QA-Automation-for-burgerking.ro/
- data/            # Test data files (expected results in JSON form)
- pages/           # Page Object Models (POM) - locators & page actions
- tests/           # Test cases
- conftest.py      # Pytest fixtures/config
- pytest.ini       # Pytest configuration
- requirements.txt # Dependencies
- README.md

---

## Prerequisites
- Python 3.12.8
- Google Chrome
- ChromeDriver (must match Google Chrome version)
- Selenium
- Install Python dependencies:
    pip install -r requirements.txt

---

## Running Tests
pytest

---

## Future Improvements
- Finish all pages UI Automation (current)
- API Testing
- CI/CD integration (GitHub actions)
- Test reports & dashboards