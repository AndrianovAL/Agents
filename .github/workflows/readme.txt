GitHub Action YAML file to automatically test and run 1_Wikipedia_and_Math project every time I push or create a pull request.

Notes on potential improvements:
1. Adjust if a project needs environment variables.
	GitHub Actions won’t pick up .env file unless I configure it - right now it won’t work if my .py scripts rely on reading .env for API keys.
	To fix that:
		1. Add my API key as a GitHub secret (Settings → Secrets and variables → Actions → New repository secret) — e.g., OPENAI_API_KEY
		2. Update the YAML to expose it like this:
		    - name: ▶️ Run agent v3
		      run: python 1_Wikipedia_and_Math/agent_langchain_v3.py
		      env:
		        GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
2. GitHub Actions only runs .yml or .yaml files, so it's OK to add to the .GitHub/
3. Save outputs as artifacts
   Check output files
   Save logs
   Add test logs
   Add test assertions
   Run tests
4. Can parameterize it or limit runs only to modified scripts (e.g., only run v2 if it changed)
5. Set up dependabot to auto-check and upgrade GitHub Actions safely - it's a best practice in production setups.
6. Adjust if a project uses a .ipynb notebook to run it.
7-10.
| Feature             | Benefit                                       | How to Add                                           |
| ------------------- | --------------------------------------------- | ---------------------------------------------------- |
| ✅ Matrix testing    | Run against multiple Python versions          | Add a `strategy.matrix` block                        |
| ✅ Linting           | Auto check code quality (e.g., flake8, black) | Add a step with `pip install flake8` then `flake8 .` |
| ✅ Test framework    | Move logic to unit tests (pytest)             | Refactor agents into testable functions + use pytest |
| ✅ Artifacts or logs | Upload results or logs for inspection         | Use `actions/upload-artifact`                        |
11. Can set up each project to explicitly load the root .env (useful for more control).
12. Can use multiple .env files (.env.dev, .env.test, .env.prod etc.).

___Info:
| Line                              | Purpose                                                                           |
| --------------------------------- | --------------------------------------------------------------------------------- |
| `on: push` / `pull_request`       | Triggers this workflow only when files under `1_Wikipedia_and_Math/` are changed. |
| `jobs.test-wikipedia-agent`       | Defines a job named `test-wikipedia-agent`.                                       |
| `runs-on: ubuntu-latest`          | Uses GitHub's Linux VM for the runner.                                            |
| `actions/checkout@v3`             | Downloads your repo so the runner can work with it.                               |
| `actions/setup-python@v4`         | Installs Python 3.11 on the VM.                                                   |
| `pip install -r requirements.txt` | Installs the required Python packages.                                            |
| `python agent.py`                 | Runs your script — adjust the path if needed.                                     |

___Q: What do the "@v3" in "actions/checkout@v3" and the "@43" in "actions/setup-python@v4" mean?
A: The @v3 and @v4 in GitHub Actions like "actions/checkout@v3" and "actions/setup-python@v4" refer to specific versions of those GitHub-provided reusable action modules. Here's what it means:
| Example                   | What It Means                                             |
| ------------------------- | --------------------------------------------------------- |
| `actions/checkout@v3`     | Use version 3 of the official `checkout` action.          |
| `actions/setup-python@v4` | Use version 4 of the official `setup-python` action.      |
| `@v3.5.2`                 | Use an **exact release version** (e.g., 3.5.2).           |
| `@main` or `@master`      | Use the latest from the main branch (⚠️ not recommended). |

Q:Why Use Version Tags?
A:Using fixed versions like @v3 or @v4 ensures stability and predictability. If the action authors update the main branch with breaking changes, your workflow won’t unexpectedly break — because it uses a locked version.
> Best Practice:
	- Stick with a major version tag (@v3, @v4) for most cases — it gets minor fixes without breaking changes.
	- For full stability, you can pin to an exact version (@v3.5.1) using a commit SHA or full tag.
