# GitHub API Assignment

HW Assignment for SSW 567
This project retrieves a GitHub user's public repositories and counts the number of commits in each.  
It uses GitHub's REST API and is designed with **unit testing in mind**.

## 🔗 GitHub Repository

[GitHub Repository Link](https://github.com/SpurthiSetty/GitHubApi567-hw4a)

## ✅ Build Status (Travis CI)

[![Build Status](https://app.travis-ci.com/SpurthiSetty/GitHubApi567-hw4a.svg?token=uUkA27xxGEnZmDyetwdU&branch=main)](https://app.travis-ci.com/SpurthiSetty/GitHubApi567-hw4a)

## How to Run the Program

1. **Clone this repository**:

   ```bash
   git clone https://github.com/yourusername/GitHubApi567-hw4a.git
   ```

2. Navigate to Project directory
   ```bash
   cd GitHubApi567-hw4a
   ```
3. Install required dependencies
   ```bash
   pip install -r requirements.txt
   ```
4. Set up GitHub API authentication (optional):
   Create a .env file in the project root.
   Add the following line:

   ```bash
   GITHUB_TOKEN=your_personal_access_token_here
   ```

5. Run the Script

   ```bash
   python github_api.py
   ```

6. Run unit tests
   ```
   pytest
   ```
