# econophysics-lecture-notes
This is a repository for the lecture notes of the Econophysics course at the University of Pavia.

## Compile

From this folder, run:

```sh
./compile
```

This runs `latexmk` with XeLaTeX and Biber as often as necessary, produces
`econophysics-lecture-notes.pdf`, and removes its temporary build directory on
success or failure. The previous PDF is preserved if compilation fails; error
details are printed in the terminal. Requires a TeX installation (MacTeX on macOS)
and the Minion Pro font used by the document. Every invocation is a fresh build.

To use the exact word `compile` in your current terminal session, run this once:

```sh
alias compile='./compile'
```

Then `compile` works whenever this project is your current directory. The alias
does not persist across terminal sessions; `./compile` always works without setup.

## Save and upload with Git

Git records local snapshots called commits. GitHub hosts a remote copy.
`git add` selects changes for the next snapshot; `git commit` saves that snapshot
locally; `git push` uploads commits. Saving or compiling a file does not upload it.

This repository already has the remote `origin` configured as
`https://github.com/AlessandroCasti/econophysics-lecture-notes.git`, with the local
branch `main` tracking `origin/main`. You do not need `git init` or a new remote.

Typical workflow from the project folder:

```sh
./compile
git status
git diff
git add -A
git diff --cached --stat
git diff --cached
git commit -m "Review lecture notes and add clean compilation command"
git push origin main
```

Check the staged changes before committing: `git add -A` stages all non-ignored
new files, edits, and deletions in the repository, including previous work. Use
`git add path/to/file` instead to select particular files. To unstage a file while
keeping its edits, use `git restore --staged path/to/file`. Binary PDFs appear in
the change list but cannot be reviewed as a text diff.

The existing `.gitignore` excludes raw handwritten notes, reference books in
`slides_and_others`, complex-systems drafts, and build files. The backup folder
also ignores its archives. The final lecture PDF is included when staged.
Ignore rules do not stop tracking files already committed.

Before starting future work, with a clean working tree, obtain remote updates:

```sh
git pull --ff-only origin main
```

If a push is rejected because GitHub has newer commits, first commit your intended
local work, then run:

```sh
git pull --rebase origin main
git push origin main
```

If Git reports conflicts, edit the indicated files, stage the resolutions with
`git add`, and run `git rebase --continue`. To cancel that rebase and return to the
state before it, use `git rebase --abort`. Recompile after resolving source changes
and commit the rebuilt PDF if it changes. Do not use force-push for this workflow.

The HTTPS remote requires GitHub authentication when pushing. Use the browser or
credential-manager sign-in if offered; if prompted for a password, GitHub requires
a personal access token instead of your account password. Keep credentials out of
repository files and commands saved in shell history.

Useful checks:

```sh
git status              # uncommitted changes and branch status
git log -5 --oneline    # five most recent local commits
git remote -v          # configured upload/download address
```

References: [Git tutorial](https://git-scm.com/docs/gittutorial),
[push](https://git-scm.com/docs/git-push),
[pull](https://git-scm.com/docs/git-pull).
