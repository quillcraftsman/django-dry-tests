# Django DRY Tests Developer Documentation

## Makefile

First check **Makefile**. It contains many useful commands to work with project

## Main commands

### Run Tests

```commandline
make test
```

### Tests coverage

```commandline
make coverage
```

### Lint

```commandline
make lint
```

## How to develop new feature

### Preparation

- Make django test. Let it fail
- Add example view or something else with demo project
- Make the django test work.

This step allow you to comfortably create new feature

### Make new feature

- Add new feature to the dry_tests package
- Make all tests work
- Check the coverage
- Run linter
- Make a new pull-request to contribute
