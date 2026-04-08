1. Fork & Clone (one-time setup)

# Fork on GitHub (click "Fork" button)
git clone git@github.com:harshpujari/gemini-cli.git
cd gemini-cli
git remote add upstream https://github.com/google-gemini/gemini-cli.git
2. Stay Up to Date

git fetch upstream
git checkout main
git merge upstream/main
3. Create a Feature Branch

git checkout -b feat/add-agents-md-default
4. Make Changes & Commit

# make your code changes, then:
git add packages/core/src/tools/memoryTool.ts  # add specific files
git commit -m "feat(core): add AGENTS.md to default context filenames"
5. Push to Your Fork

git push origin feat/add-agents-md-default
6. Open a PR
Go to the upstream repo on GitHub
You'll see a banner saying "Compare & pull request" — click it
Set base: google-gemini/gemini-cli:main ← head: harshpujari/gemini-cli:feat/add-agents-md-default
Write a clear title + description, link the issue (Fixes #12345)
Submit
7. After Review

# If maintainers request changes:
# make fixes on same branch, then:
git add <files>
git commit -m "fix: address review feedback"
git push origin feat/add-agents-md-default
# PR updates automatically
8. After Merge

# Clean up
git checkout main
git merge upstream/main
git branch -d feat/add-agents-md-default
git push origin --delete feat/add-agents-md-default
Key Things to Remember
Never commit directly to main — always use feature branches
Sign the CLA before your first PR (Google requires this)
Run npm run preflight before pushing — catches lint/build/test issues
Follow Conventional Commits — prefix like feat:, fix:, docs:
Keep PRs small and focused — one issue per PR
Respond to reviews promptly — maintainers appreciate it
