# CI/CD Flask App with Docker and GitHub Actions

This project is a minimal Flask web application that demonstrates a full **CI/CD pipeline** using **GitHub Actions** and **DockerHub**.

Whenever code is pushed to the `main` branch, GitHub Actions will:

1. Run automated tests using `pytest`
2. Build a Docker image from the app code
3. Push the Docker image to DockerHub with a versioned tag

---

## CI/CD Workflow

### Trigger:
Runs automatically when code is pushed to the `main` branch.

### Jobs:
#### `build`:
- Logs in to DockerHub
- Builds the Docker image
- Tags it (e.g., `v2`)
- Pushes the image to DockerHub

#### `test`:
- Installs Python and project dependencies
- Runs `pytest` to test the app

---

