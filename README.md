# Bank App TDD – Automatic Testing Project

## Overview
This project is a fully test‑driven designed (TDD) banking application implemented in Python.  
Its main purpose is to demonstrate **unit testing**, **integration testing**, and **behavior‑driven tests** for a simple banking domain involving:

- Personal accounts  
- Company accounts  
- Account registry  
- Transfers  
- Loans  
- Promotions  
- Validation tools  
- Simple API layer

All business logic is created to satisfy tests step‑by‑step — tests describe required behavior first, and code is implemented to pass them.

---

## Project Structure

```
app/
  Account.py                # Base class for all accounts
  PersonalAccount.py        # Logic for private accounts
  CompanyAccount.py         # Logic for company accounts
  AccountRegistry.py        # Storage and lookup service for accounts
  SMTPClient.py             # Fake/mock email client
  api.py                    # Minimal API for CRUD + money transfer
  tools.py                  # Utilities: NIP validation, promo code, etc.

  features/                 # (BDD) test steps for behave/cucumber style
  tests/                    # Unit & integration tests (pytest)
```

---

## How the System Works

### 1. **Account Model**
All accounts derive from the base `Account` class:
- unique ID  
- balance  
- history of operations  

Two concrete implementations:
- **PersonalAccount**  
  - supports personal history  
  - personal loan limits  
- **CompanyAccount**  
  - company‑specific loan rules  
  - requires valid NIP

### 2. **Registry**
`AccountRegistry` stores and manages all accounts:
- create account  
- delete account  
- update data  
- find account by ID  
- ensure uniqueness  
- tested heavily with pytest

### 3. **Transfer Mechanism**
Transfers include:
- validation of funds  
- history entries on both sides  
- tested separately for personal/company accounts

There are tests confirming:
- correct balance updates  
- double‑entry bookkeeping  
- negative operation prevention

### 4. **Loans**
Personal vs company loan logic is different:
- limits  
- validation  
- interest rules  
- logging to account history

### 5. **Tools**
`tools.py` includes:
- **NIP validation**  
- **promo code discount calculation**  
- **helper functions**

Each tool has its own test suite.

### 6. **SMTP / History Sending**
`SMTPClient` is mocked.  
Tests check **only calls**, not actual email delivery.

### 7. **API Layer**
`api.py` simulates a very small REST-like interface:
- create account  
- list accounts  
- send history  
- transfer funds  

Tested using pytest by calling functions directly.

---

## Test-Driven Development Approach

The project is built by writing tests first:

1. **Define expected behavior in a test**  
2. Run tests → fail  
3. Implement minimal code to pass tests  
4. Refactor  
5. Continue to next test

The folder `tests/` shows the development path.

The test coverage includes:
- unit tests per class  
- integration tests across modules  
- API tests  
- BDD steps (`features/steps`)  

---

## Running Tests

### Install dependencies
```
pip install pipenv
pipenv install --dev
```

### Run all tests
```
pytest -vv
```

### Run BDD tests
```
behave
```

---

## Summary

This project is a complete example of:
- clean separation of business logic  
- full coverage with pytest  
- demonstration of TDD/BDD methodology  
- realistic banking logic (transfer, loans, registry, validation)  

It’s an excellent template for learning:
- automated testing  
- Python design patterns  
- incremental system construction through tests  
