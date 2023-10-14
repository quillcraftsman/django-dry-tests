# Django DRY Tests

Package with new powerful TestCases and Assets to test django application fast. TDD is supported

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
[![Documentation](https://readthedocs.org/projects/django-dry-tests/badge/?version=latest)](http://django-dry-tests.readthedocs.io/en/latest/?badge=latest)
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

#### Repository Stats
[![Stars](https://img.shields.io/github/stars/quillcraftsman/django-dry-tests
)](https://github.com/quillcraftsman/django-dry-tests/)
[![Contributors](https://img.shields.io/github/contributors/quillcraftsman/django-dry-tests
)](https://github.com/quillcraftsman/django-dry-tests/graphs/contributors)
[![Forks](https://img.shields.io/github/forks/quillcraftsman/django-dry-tests
)](https://github.com/quillcraftsman/django-dry-tests/)

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

- Special **Request** and **Response** classes to simple set test data
- Special **SimpleTestCase** class with:
    - `assertTrueResponse(self, current_response, true_response)` - Main assert to compare real response with expected
    - `assertResponsesAreTrue(self, response_pairs)` - Compare many responses
    - Other more simple asserts (`assertStatusCode`, `assertRedirectUrl`, `assertValueInContext`, 
          `assertContextValues`, `assertContentValues`)
- Special **TestCase** class. Similar with **SimpleTestCase** but with testing database (**Not ready yet**)

## Requirements

- `Django==4` (Lower versions haven't been tested)

## Development Status

- **django-dry-tests**
- **v0.1.0**
- **3 - Alpha**

Package available on [PyPi](https://pypi.org/project/django-dry-tests/)

## Install

### with pip

```commandline
pip install django-dry-tests
```

### from release page

Download source code from [GitHub Releases page](https://github.com/quillcraftsman/django-dry-tests/releases)

### clone from GitHub

```commandline
git clone https://github.com/quillcraftsman/django-dry-tests.git
make install
```

## Quickstart

For example, you need to test some view like this:

```python
def index_view(request):
    if request.method == 'GET':
        context = {
            'title': 'Title'
        }
        return render(request, 'demo/index.html', context)

    name = request.POST.get('name', None)
    if name is not None:
        Simple.objects.create(name=name)
    return HttpResponseRedirect('/')
```

And you want to check:
- GET response status code
- GET response context data
- GET response some html data
- POST response status code
- POST response redirect url
- POST response save object to database (**Not implemented yet**)

Let`s see the tests code:
```python
from dry_tests import (
    Request,
    TrueResponse as Response,
    SimpleTestCase,
    POST,
)


class ViewTestCase(SimpleTestCase):

    def test_main(self):
        data = [
            # Multy parameters GET
            {
                'request': Request(url='/'),
                'response': Response(
                    status_code=200,
                    in_context='title',
                    context_values={'title': 'Title'},
                    content_values=['Title'],
                ),
            },
            # Multy parameters POST
            {
                'request': Request(url='/', method=POST),
                'response': Response(
                    status_code=302,
                    redirect_url='/',
                ),
            },
        ]
        for item in data:
            request = item['request']
            true_response = item['response']
            current_response = request.get_url_response(self.client)
            self.assertTrueResponse(current_response, true_response)
```

That's all this simple test cover all your test tasks with (**assertTrueResponse**)

## Contributing

You are welcome! To easy start please check:
- [Developer Guidelines](CONTRIBUTING.md)
- [Developer Documentation](DEVELOPER_DOCUMENTATION.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Security Policy](SECURITY.md)

