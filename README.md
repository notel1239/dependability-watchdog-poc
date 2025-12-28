# Dependability Watchdog PoC

A proof-of-concept software watchdog timer for demonstrating dependability principles in safety-critical systems.

## Purpose

This project implements a software-based watchdog timer mechanism to illustrate fault detection and recovery patterns. It serves as an educational tool for engineers working on safety-critical embedded systems, showcasing how to monitor application health and initiate recovery actions.

## Architecture

The project consists of two main components:

1. **Application Logic**: A simple application that runs in a loop, performs periodic tasks, and regularly "pets" the watchdog to signal it is alive.
2. **Watchdog Service**: A separate service that monitors the application's "pet" signals. If the application fails to check in within a specified timeout, the watchdog logs a critical error and simulates a system recovery.

A fault simulation feature is also included, allowing deliberate failure injection to test the watchdog's detection capabilities.

## Dependability Principles Demonstrated

- **Fault Detection**: The watchdog continuously monitors the application's liveness.
- **Error Recovery**: Upon detecting a fault (timeout), the watchdog initiates a recovery action.
- **Redundancy**: The watchdog runs as a separate thread/process, providing an independent monitoring entity.
- **Fail-Safe Behavior**: The system is designed to fail into a safe state (recovery) rather than continuing with undetected errors.

## Getting Started

### Prerequisites

- Python 3.8+
- No external dependencies required.

### Installation

Clone the repository:

```bash
git clone https://github.com/notel1239/dependability-watchdog-poc.git
cd dependability-watchdog-poc
```

### Usage

Run the main application:

```bash
python main.py
```

To simulate a failure and trigger watchdog recovery:

```bash
python main.py --fail
```

Or set the environment variable:

```bash
export SIMULATE_FAILURE=1
python main.py
```

## Project Structure

- `main.py` – Entry point that launches both application and watchdog.
- `application.py` – Implements the periodic task logic and watchdog petting.
- `watchdog.py` – Implements the watchdog service with timeout monitoring.
- `README.md` – This file.
- `LICENSE` – MIT License.

## Development Workflow

This project was developed using a disciplined GitHub workflow:

1. **Requirements Tracking**: Issues were used to define each component.
2. **Feature Branching**: Each feature was developed in its own branch.
3. **Pull Request Reviews**: Code reviews (including automated Copilot reviews) ensured quality.
4. **Integration**: Final integration and documentation were merged via a dedicated pull request.
5. **Release**: A versioned release (v1.0.0) marks the stable demonstrator.

## License

This project is licensed under the MIT License – see the LICENSE file for details.