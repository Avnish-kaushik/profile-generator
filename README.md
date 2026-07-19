# profile-generator

Source code that builds and auto-deploys the GitHub profile README for
[Avnish-kaushik/Avnish-kaushik](https://github.com/Avnish-kaushik/Avnish-kaushik).

## How it works

```
templates/README.template.md   → source content with placeholders
scripts/generate.js            → fills placeholders, writes output/README.md
.github/workflows/update-profile.yml → runs the script, pushes result to the
                                        Avnish-kaushik/Avnish-kaushik repo
```

The workflow runs automatically once a day, whenever you push to `main` here,
or on demand from the **Actions** tab ("Run workflow" button).

## One-time setup

1. **Create a Personal Access Token (PAT)**
   - Go to GitHub → Settings → Developer settings → Personal access tokens →
     Fine-grained tokens (or classic).
   - Give it `repo` scope (classic) or read/write **Contents** access scoped
     to the `Avnish-kaushik/Avnish-kaushik` repo (fine-grained).
   - Copy the token.

2. **Add it as a secret in `profile-generator`**
   - Go to this repo → Settings → Secrets and variables → Actions → New
     repository secret.
   - Name: `PROFILE_TOKEN`
   - Value: (paste the PAT)

3. **Push this code**
   ```bash
   git init
   git remote add origin https://github.com/Avnish-kaushik/profile-generator.git
   git add .
   git commit -m "initial profile generator setup"
   git branch -M main
   git push -u origin main
   ```

4. That's it — the Action will run on push, and daily after that, and will
   keep `Avnish-kaushik/Avnish-kaushik`'s README.md in sync automatically.

## Editing your profile content

Don't edit the profile repo's README by hand — edit
`templates/README.template.md` here instead, then push. The workflow
will regenerate and overwrite the live version.

## Local test

```bash
node scripts/generate.js
cat output/README.md
```
