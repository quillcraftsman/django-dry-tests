# Django DRY Tests

Package with new powerful TestCases and Assets to test django application fast. TDD is supported

You can find **Full Project Documentation** [here][documentation_path]

<hr>

#### Workflows
[![Tests](https://github.com/quillcraftsman/django-dry-tests/actions/workflows/run-tests.yml/badge.svg?branch=main)](https://github.com/quillcraftsman/django-dry-tests/actions/workflows/run-tests.yml)
[![Pylint](https://github.com/quillcraftsman/django-dry-tests/actions/workflows/lint.yml/badge.svg?branch=main)](https://github.com/quillcraftsman/django-dry-tests/actions/workflows/lint.yml)

#### Package
[![Version](https://img.shields.io/pypi/v/django-dry-tests.svg)](https://pypi.python.org/pypi/django-dry-tests/)
[![Development Status](https://img.shields.io/pypi/status/django-dry-tests.svg)](https://pypi.python.org/pypi/django-dry-tests)
[![Python version](https://img.shields.io/pypi/pyversions/django-dry-tests.svg)](https://pypi.python.org/pypi/django-dry-tests/)
[![License](https://img.shields.io/pypi/l/django-dry-tests)](https://github.com/quillcraftsman/django-dry-tests/blob/main/LICENSE)
[![Wheel](https://img.shields.io/pypi/wheel/django-dry-tests.svg)](https://pypi.python.org/pypi/django-dry-tests/)

#### Support
[![Documentation](https://img.shields.io/badge/docs-0094FF.svg)][documentation_path]
[![Discussions](https://img.shields.io/badge/discussions-ff0068.svg)](https://github.com/quillcraftsman/django-dry-tests/discussions/)
[![Issues](https://img.shields.io/badge/issues-11AE13.svg)](https://github.com/quillcraftsman/django-dry-tests/issues/)

#### Downloads
[![Day Downloads](https://img.shields.io/pypi/dd/django-dry-tests)](https://pepy.tech/project/django-dry-tests)
[![Week Downloads](https://img.shields.io/pypi/dw/django-dry-tests)](https://pepy.tech/project/django-dry-tests)
[![Month Downloads](https://img.shields.io/pypi/dm/django-dry-tests)](https://pepy.tech/project/django-dry-tests)
[![All Downloads](https://img.shields.io/pepy/dt/django-dry-tests)](https://pepy.tech/project/django-dry-tests)

#### Languages
[![Languages](https://img.shields.io/github/languages/count/quillcraftsman/django-dry-tests)](https://github.com/quillcraftsman/django-dry-tests/)
[![Top Language](https://img.shields.io/github/languages/top/quillcraftsman/django-dry-tests)](https://github.com/quillcraftsman/django-dry-tests/)

#### Development
[![Release date](https://img.shields.io/github/release-date/quillcraftsman/django-dry-tests
)](https://github.com/quillcraftsman/django-dry-tests/releases)
[![Last Commit](https://img.shields.io/github/last-commit/quillcraftsman/django-dry-tests/main
)](https://github.com/quillcraftsman/django-dry-tests/)
[![Issues](https://img.shields.io/github/issues/quillcraftsman/django-dry-tests
)](https://github.com/quillcraftsman/django-dry-tests/issues/)
[![Closed Issues](https://img.shields.io/github/issues-closed/quillcraftsman/django-dry-tests
)](https://github.com/quillcraftsman/django-dry-tests/issues/)
[![Pull Requests](https://img.shields.io/github/issues-pr/quillcraftsman/django-dry-tests
)](https://github.com/quillcraftsman/django-dry-tests/pulls)
[![Closed Pull Requests](https://img.shields.io/github/issues-pr-closed-raw/quillcraftsman/django-dry-tests
)](https://github.com/quillcraftsman/django-dry-tests/pulls)
[![Discussions](https://img.shields.io/github/discussions/quillcraftsman/django-dry-tests
)](https://github.com/quillcraftsman/django-dry-tests/discussions/)

[//]: # (#### Repository Stats)

[//]: # ([![Stars]&#40;https://img.shields.io/github/stars/quillcraftsman/django-dry-tests)

[//]: # (&#41;]&#40;https://github.com/quillcraftsman/django-dry-tests/&#41;)

[//]: # ([![Contributors]&#40;https://img.shields.io/github/contributors/quillcraftsman/django-dry-tests)

[//]: # (&#41;]&#40;https://github.com/quillcraftsman/django-dry-tests/graphs/contributors&#41;)

[//]: # ([![Forks]&#40;https://img.shields.io/github/forks/quillcraftsman/django-dry-tests)

[//]: # (&#41;]&#40;https://github.com/quillcraftsman/django-dry-tests/&#41;)

<hr>

## Menu

- [Mission](#mission)
- [Open Source Project](#open-source-project)
- [Features](#features)
- [Requirements](#requirements)
- [Development Status](#development-status)
- [Install](#install)
- [Quickstart](#quickstart)
- [Contributing](#contributing)

## Mission

The mission of the **Django DRY Tests** to design and develop open source python package to test **django**
application
- fast
- with minimal code duplication
- with the ability to use **TDD** easily 
- simple and comfortable

## Open Source Project

This is the open source project with [MIT license](LICENSE). 
Be free to use, fork, clone and contribute.

## Features

- Special **Request**, **Response** and **Form** classes to simple set test data
- Special **SimpleTestCase** and **TestCase** classes with new asserts:
- - The main asserts is **assertTrueResponse** and **assertTrueForm**. You can use this for most cases.
- - Other special asserts (See more in [Full Documentation](https://drytest.craftsman.lol/about.html#features))

## Requirements

- `Django==4` (Lower versions haven't been tested)
- See more in [Full Documentation](https://drytest.craftsman.lol/about.html#requirements)

## Development Status

- Package already available on [PyPi](https://pypi.org/project/django-dry-tests/)
- See more in [Full Documentation](https://drytest.craftsman.lol/about.html#development-status)

## Install

### with pip

```commandline
pip install django-dry-tests
```

See more in [Full Documentation](https://drytest.craftsman.lol/install.html)

## Quickstart

### To test view

```python
class QuickStartViewSimpleTestCase(SimpleTestCase):
    """
    SimpleTestCase example
    """

    def test_get(self):
        """
        Test Example with django-dry-tests
        :return:
        """
        # Create Request Model
        request = Request(
            url='/quickstart/'
        )

        # Create Response Model to check all view.
        # You can set only one param without others to check it.
        true_response = TrueResponse(
            status_code=200,
            context=Context(
                keys=['quickstart'],  # check that quickstart key in context
                values=['Quickstart'],  # check that "Quickstart" value in context
                items={
                    'quickstart': 'Quickstart'
                },  # check both keys and values in context
                types={
                    'quickstart': str
                }  # check values types without check values
            ),
            content_values = [
                'Quickstart',
                '<h1>Quickstart title</h1>'
            ],  # check values after template will be rendered
        )

        # get url response with Django default Test Client
        current_response = request.get_response(self.client)
        # Use main assert to run all asserts
        self.assertTrueResponse(current_response, true_response)
```

### To test Form

```python
class ExampleFromTestCase(SimpleTestCase):
    """
    Example Form Test Class
    """

    def test_form(self):
        """
        Example Test with django-dry-tests
        :return:
        """
        true_form = TrueForm(  # Set Up TrueForm instance
               Fields(  # TrueForm Fields
                   count=2,  # check fields count
                   names=[
                       'number', 'name'
                   ],  # check field names
                   types={
                       'name': forms.CharField,
                       'number': forms.IntegerField
                   }  # check fields types
               ),
            )
        current_form = ExampleForm()  # Get project form
        self.assertTrueForm(current_form, true_form)  # use this main assert to check all conditions
```

### More examples in [Full Documentation][documentation_path]

## Contributing

You are welcome! To easy start please check:
- [Developer Guidelines](CONTRIBUTING.md)
- [Developer Documentation](https://drytest.craftsman.lol/dev_documentation.html)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Security Policy](SECURITY.md)

[documentation_path]: https://drytest.craftsman.lol