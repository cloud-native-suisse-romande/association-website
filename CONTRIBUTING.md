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

For the local development without a full rebuild:

```shell
FULL_BUILD=false INSIDERS=false mkdocs serve
```

## Editing

If you are a coding agent, see also the [Copilot Instructions](./.github/copilot-instructions.md) :)

### Contribution Flow

We keep it simple.
Just fork a repository and submit your changes as a pull request when ready.

### Style Guide

#### Color Schema

The main Color scheme is built around the logo colors:

- Blue: `#326ce5`
- Red: `#ff0000`
- White: `#ffffff`

Additional colors:

- Dark Blue: `#1a36b4`
- Gray for backgrounds and covers: `#f6f5ec`
- Text and Hyperlink colors for the dark mode: `#58a6ff`

## Deployment

The website is deployed automatically when the changes are merged into the main repository.
For included repositories (governance, KCD), it is possible to manually trigger the deployment pipeline [here](https://github.com/cloud-native-suisse-romande/association-website/actions/workflows/deploy.yml).

## License

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/oleg-nenashev/oleg-nenashev">This site</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/oleg-nenashev/">Oleg Nenashev</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></a></p>
