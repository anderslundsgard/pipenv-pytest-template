

[![Build Status](https://travis-ci.org/anderslundsgard/pipenv-pytest-template.svg?branch=master)](hhttps://travis-ci.org/anderslundsgard/pipenv-pytest-template)

Showcase following programming languages, frameworks/tools and techniques:

 - Python
 - Pytest
 - Pipenv
 - Flake8
 - Travis CI

## Prerequirements

- [Install pip3][1]
- Environment variable for Pip url needs to be set.  
For example:
```
export PIP_INDEX_URL=https://pypi.org/simple
```

## Get up and running

Install pipenv by running:

**GitBash on Windows**:  
```
> . .setup_pipenv
```

**Mac:**
```
> chmod +x .setup_pipenv 
> ./p.setup_pipenv
```

## Tips

### Install your needed python modules
```
> pipenv install requests -i pypi
*or*
> pipenv install 
```

### Remove virtual environment

```
> pipenv --rm
```

### Step into virtual environment

```
> pipenv shell
```

[1]: https://www.google.com/search?q=install+pip3&oq=install+pip3
