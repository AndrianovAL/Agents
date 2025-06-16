GitHub Action YAML file to automatically test and run 1_Wikipedia_and_Math project every time I push or create a pull request.

Notes on potential improvements:
1. Adjust if a project uses a .ipynb notebook or needs environment variables.
2. Check output files, run tests, or save logs/artifacts.
   Can parameterize it or run only changed scripts.
3. Set up dependabot to auto-check and upgrade GitHub Actions safely - it's a best practice in production setups.

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
