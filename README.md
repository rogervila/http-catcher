# HTTPCatcher

<p align="center"><img height="200" alt="HTTPCatcher" src="https://image.flaticon.com/icons/png/512/2580/2580470.png" /></p>

<p align="center">
  <a href="https://hub.docker.com/r/rogervila/http-catcher"><img alt="DockerHub Downloads" src="https://img.shields.io/docker/pulls/rogervila/http-catcher.svg" /></a>
  <a href="https://github.com/rogervila/http-catcher/blob/main/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/rogervila/http-catcher" /></a>
</p>

## Setup

Running HTTPCatcher with docker is easy, but you can also run it locally.

### Docker setup

The image is available on DockerHub.

```sh
docker run -p 5000:5000 rogervila/http-catcher
```

### Local setup

Clone the repository and run the following commands:

```sh
pip install --user -r requirements.txt

FLASK_APP=web.py flask run -h 0.0.0.0 -p 5000
```


## License

HTTPCatcher is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).


<div>Icons made by <a href="https://www.flaticon.com/authors/smashicons" title="Smashicons">Smashicons</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
