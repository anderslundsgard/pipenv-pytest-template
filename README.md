## Prerequirements

- [Install pip3][1]
- Environment variable for Pip url needs to be set.  
For example:
```
export PIP_INDEX_URL=https://pypi.org/simple
```

## Get up and running

Install pip env by running .setup_pipenv file in GitBash or similar shell.
```
> . .setup_pipenv
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
