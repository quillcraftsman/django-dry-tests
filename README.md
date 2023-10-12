# Django DRY Tests

Package with new powerful TestCases and Assets to test django application fast. TDD is supported

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

