# Contributing to the Site

All contributions to the website and the materials are welcome!

If you are interested in contributing to the association (events, meetups, etc.),
see [our website](./index.md).

## Developer Environment

For development, everything is powered by Dev Containers and GitHub Actions.
See the Dev Container configuration in the repository for the versions used for the builds,
in the case you need to reproduce the developer environment outside of the container.

## Under the Hood

The site is built with [MkDocs](https://www.mkdocs.org/),
[MkDocs Multirepo Plugin](https://github.com/jdoiro3/mkdocs-multirepo-plugin/tree/main),
and [Material for MkDocs](https://squidfunk.github.io/mkdocs-material).

## Quick Start

For the local development without full rebuild:

```shell
FULL_BUILD=false INSIDERS=false mkdocs serve
```

## License

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/oleg-nenashev/oleg-nenashev">This site</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/oleg-nenashev/">Oleg Nenashev</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></a></p>
