# API Testing Framework with Python Requests

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![pytest-xdist](https://img.shields.io/badge/xdist-parallel_testing-orange?style=for-the-badge)
![uv](https://img.shields.io/badge/uv-FF6A33?style=for-the-badge)
![Ruff](https://img.shields.io/badge/Ruff-10B981?style=for-the-badge&logo=ruff&logoColor=white)
![Pyright](https://img.shields.io/badge/Pyright-4EAAAF?style=for-the-badge)
![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

API automation testing framework built with Python Requests. Designed for reliability and scalability with advanced features for comprehensive API testing.

## ✨ Features

- **Complete HTTP Methods Support**: GET, POST, PUT, DELETE and more
- **Parallel Test Execution**: Distributed testing with xdist for faster results
- **JSON Handling**: Built-in JSON parsing and validation
- **CI/CD Ready**: Integration with GitHub Actions

## 🛠 Technology Stack

| Category | Technologies |
|----------|--------------|
| **HTTP Client** | Python Requests |
| **Testing Framework** | pytest |
| **Package Management** | uv |
| **Code Quality** | ruff |
| **Type Checking** | pyright |

## 📋 Prerequisites

- **Python 3.13** or higher
- **Docker** for containerization
- **Allure** for test reporting
- **Git** for version control
- **uv** for package management

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/sdet0mis/api-testing.requests.git
cd api-testing.requests
```

### 2. Install Dependencies

```bash
uv sync
```

### 3. Run Tests and Generate Report

```bash
./run_tests.sh
```

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
