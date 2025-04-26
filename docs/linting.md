# Linting

Linting is the process of running a program that will analyze your code for potential errors, stylistic inconsistencies, and coding standard violations.

We use pylint and our linting configuration is stored in the `.pylintrc` file in the root directory of this project.

Pylint is run:
- during development with `pylint .` (by the developer)
<!--
- when pushing or creating a pull request (automatically by GitHub actions)

Currently our configuration requires for the score to be at least 9.5/10.0 to pass the test.
Editing the pylint config or changing the fail treshold is discouraged unless absolutely necessary.
-->

## Initial setup

> [!NOTE]
>
> This step has already been completed and is included only for reference.

To generate a `.pylintrc` file, run `pylint --generate-rcfile > .pylintrc`
