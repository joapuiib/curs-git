---
template: document.html
title: "Exemples de fluxos de treball"
icon: material/file-check-outline
alias: actions-exemples
---

## Exemples de fluxos de treball
Per veure com combinar totes aquestes opcions, anem a veure diferents exemples
d'automatitzacions en projectes de naturalesa distinta.


### Publicació d'un lloc web estàtic generat amb MkDocs a GitHub Pages
!!! success "Exemple en el repositori d'aquesta documentació: [`curs-git`][curs-git]"

[curs-git]: {{ config.repo_url }}

La següent automatització permet __generar aquest lloc web__ amb el [generador de webs estàtiques MkDocs][mkdocs]
i __publicar-lo__ a [:octicons-browser-24: GitHub Pages][pages].

Aquesta acció s'executa sempre que es publiquen nous canvis sobre la branca `main`. També es pot executar manualment.

Els passos que la componen són els següents:

/// html | div.steps
1. __Compila el lloc web estàtic amb MkDocs.__
    - Còpia els fitxers del repositori amb l'acció predefinida [`actions/checkout`][actions-checkout].
    - Configura Python amb l'acció predefinida [`actions/setup-python`][actions-setup-python].
    - Instal·la les dependències necessàries per executar MkDocs.
    - Compila el lloc web amb l'ordre `mkdocs build`.
    - Emmagatzema el directori (`site/`) com a artefacte per a la
        següent tasca amb l'acció predefinida [`actions/upload-pages-artifact`][actions-upload-pages-artifact].
2. __Publica el lloc web a :octicons-browser-24: GitHub Pages.__
    - Sols s'executa si la tasca anterior s'ha executat correctament.
    - Publica l'artefacte generat en la tasca anterior l'acció predefinida [`actions/deploy-pages`][actions-deploy-pages].


[mkdocs]: https://www.mkdocs.org/
[pages]: https://pages.github.com/
[actions-checkout]: https://github.com/marketplace/actions/checkout
[actions-setup-python]: https://github.com/marketplace/actions/setup-python
[actions-upload-pages-artifact]: https://github.com/actions/upload-pages-artifact
[actions-deploy-pages]: https://github.com/actions/deploy-pages

```yaml title=".github/workflows/deploy.yml"
--8<-- ".github/workflows/deploy.yml"
```


### Prova de correcció ortogràfica
!!! success "Exemple en el repositori d'aquesta documentació: [`curs-git`][curs-git]"

Aquest flux de treball comprova la correcció ortogràfica de la documentació
del repositori utilitzant el programa [`pyspelling`][pyspelling].

[pyspelling]: https://facelessuser.github.io/pyspelling/

S'executa quan es crea Pull Request o es marca com a que està llesta per a revisió
sobre la branca `main`.

El flux de treball es compon de dues tasques. S'ha configurat d'aquesta manera
perquè la tasca de correcció ortogràfica només s'executa quan s'han modificat fitxers de documentació,
evitant així executar-la innecessàriament quan es modifiquen altres fitxers.

/// html | div.steps
1. __`changed-files`: Comprova si cal realitzar la correcció ortogràfica.__
    - Comprova si s'han modificat fitxers de documentació (`*.md`) respecte a la branca `main`.
    - Emmagatzema el resultat en la variable `EXIST_CHANGED_FILES`.

2. __`spellcheck`: En cas afirmatiu, comprova la correcció ortogràfica dels fitxers modificats.__
    - S'executa només si `needs.changed-files.outputs.EXIST_CHANGED_FILES == 1`.
    - Instal·la les dependències.
    - Es descarrega els diccionaris necessaris.
    - Executa la correcció ortogràfica amb `pyspelling`.
///

```yaml title=".github/workflows/spellcheck.yml"
--8<-- ".github/workflows/spellcheck.yml"
```

### Execució de proves unitàries i d'integració en un projecte Java amb Maven
!!! example "Repositori d'exemple: [`tasklist-api`][tasklist-api]"
    Podeu observar el seu comportament en la :octicons-git-pull-request-16: Pull Request [feature: tasks can be marked as favorites (#1)][pr].

    1. En el :octicons-git-commit-16: commit [`2ca7024` – feature: tasks can be marked as favorites][pr-skip] no s'han executat les proves
        perquè la :octicons-git-pull-request-16: Pull Request encara estava marcada com a esborrany.

    2. En els commits posteriors a haver marcat la :octicons-git-pull-request-16: Pull Request com a llesta per a revisió, sí que s'han executat les proves.

[tasklist-api]: https://github.com/cursgit/tasklist-api
[pr]: https://github.com/cursgit/tasklist-api/pull/1
[pr-skip]: https://github.com/cursgit/tasklist-api/actions/runs/22114248635/job/63918090903
[pr-success]: https://github.com/cursgit/tasklist-api/actions/runs/22138402089/job/63996001935

Aquest flux de treball s'executa cada vegada que es publiquen canvis a la branca `main`
o quan es crea o actualitza una pull request cap a les branques `main` o `dev`.

Es basa en dues tasques:

/// html | div.steps
1. __`unit-tests`__: Executa les proves unitàries del projecte.
    - Configura l'entorn amb JDK 21.
    - Executa les proves unitàries amb l'ordre `mvn test`.

2. __`integration-tests`__: Executa les proves d'integració del projecte.
    - Sols s'executa si la tasca `unit-test` s'ha executat correctament.
    - Configura l'entorn amb JDK 21.
    - Executa les proves d'integració amb l'ordre `mvn verify`, sense tornar a executar les proves unitàries.
///

=== "`.github/workflows/tests.yml`"
    ```yaml title=".github/workflows/tests.yml"
    --8<-- "https://raw.githubusercontent.com/cursgit/tasklist-api/refs/heads/main/.github/workflows/tests.yml"
    ```

=== "`pom.xml`"
    ```xml title="pom.xml"
    --8<-- "https://raw.githubusercontent.com/cursgit/tasklist-api/refs/heads/main/pom.xml"
    ```


### Publicació d'un paquet de Python a PyPI
!!! success "Exemple en el repositori [`mkdocs-data-plugin`][mkdocs-data-plugin]"

[mkdocs-data-plugin]: https://github.com/joapuiib/mkdocs-data-plugin/blob/main/.github/workflows/publish-to-pypi.yml

Aquest flux de treball compila i publica les distribucions d'un paquet de Python
a [PyPI](https://pypi.org/) cada vegada que es publica una nova etiqueta (`tag`)
al repositori.

!!! docs "Documentació"
    - [:octicons-link-external-16: Publishing to PyPI with a Trusted Publisher](https://docs.pypi.org/trusted-publishers/) - PyPI Docs
    - [:octicons-link-external-16: Publishing with a Trusted Publisher](https://docs.pypi.org/trusted-publishers/using-a-publisher/) - PyPI Docs


Els passos que realitza són:

- Configura l'entorn per poder utilitzar Python 3.8.
- Instal·la el paquet `build` per compilar les distribucions de Python.
- Compila les distribucions del paquet.
- Publica les distribucions a PyPI utilitzant l'acció predefinida [`pypa/gh-action-pypi-publish`][pypi-publish].

[pypi-publish]: https://github.com/pypa/gh-action-pypi-publish

```yaml title=".github/workflows/publish-to-pypi.yml"
name: Publish Python 🐍 distributions 📦 to PyPI
on:
  push:
    tags:
      - "*"
jobs:
  build-n-publish:
    runs-on: ubuntu-latest
    name: Build and publish Python 🐍 distributions 📦 to PyPI
    environment:
      name: pypi
      url: https://pypi.org/p/mkdocs-data-plugin
    permissions:
      id-token: write  # IMPORTANT: this permission is mandatory for trusted publishing
    steps:
      - name: Set up Python 3.8
        uses: actions/checkout@master
      - name: Set up Python 3.8
        uses: actions/setup-python@v1
        with:
          python-version: 3.8
      - name: Install pypa/build
        run: >-
          python -m
          pip install
          build
          --user
      - name: Build a binary wheel and a source tarball
        run: >-
          python -m
          build
          --sdist
          --wheel
          --outdir dist/
      - name: Publish package distributions to PyPI
        uses: pypa/gh-action-pypi-publish@release/v1
```

### Creació d'una imatge de Docker
Podeu seguir aquest tutorial per crear una imatge de Docker a partir d'un repositori de GitHub
i publicar-la a [Docker Hub](https://hub.docker.com/).

!!! info "[:octicons-link-external-16: Using GitHub Actions to automatically build Docker images][tutorial-docker-build] – :simple-medium: Medium"

!!! example "Repositori d'exemple: [`tasklist-api`][tasklist-api]"
    Podeu observar quan s'ha publicat [la etiqueta :octicons-tag-16: `v0.1.0`][tag] en el [commit :octicons-git-commit-16: `d42ed1e` – Primera versió del projecte][tag-commit],
    s'ha executat el flux de treball correctament i s'ha publicat la imatge de Docker al [repositori __joapuiib/tasklist-api__ de Docker Hub][docker-hub-repo].


[tutorial-docker-build]: https://medium.com/@kicsipixel/using-github-actions-to-automatically-build-docker-images-65a038b8ce56
[docker-action]: https://github.com/cursgit/tasklist-api/actions/runs/22113606749/job/63915873196
[tag]: https://github.com/cursgit/tasklist-api/releases/tag/v0.1.0
[tag-commit]: https://github.com/cursgit/tasklist-api/actions/runs/22113606749/job/63915873196
[docker-hub-repo]: hhttps://hub.docker.com/repository/docker/joapuiib/tasklist-api/generalttps


Aquest flux de treball s'executa cada vegada que es publica una nova :octicons-tag-16: etiqueta al repositori amb el format `v*.*.*`.
També es pot executar manualment ja que està configurat amb el `workflow_dispatch`.

Consisteix en una única tasca que realitza els següents passos:

/// html | div.steps
1. __Còpia el repositori a l'entorn d'execució__ amb l'acció predefinida [`actions/checkout`][actions-checkout].
2. __Inicia sessió a Docker Hub__ amb l'acció predefinida [`docker/login-action`][docker-login-action].
    - Utilitza les credencials `DOCKER_USERNAME` i `DOCKER_PASSWORD` emmagatzemades com a
        [:octicons-key-asterisk-16: secrets][secrets] del repositori.
3. __Configura les metadades de la imatge de Docker__ amb l'acció predefinida [`docker/metadata-action`][docker-metadata-action].
    - Especifica el nom de la imatge com `joapuiib/tasklist-api`.
    - Configura les etiquetes de la imatge:
        - `latest` per a la branca `main`.
        - El número de versió extret de l'etiqueta publicada amb els patrons `*.*.*`, `*.*` i `*`.
4. __Construeix i publica la imatge de Docker__ amb l'acció predefinida [`docker/build-push-action`][docker-build-push-action].
///

[docker-login-action]: https://github.com/docker/login-action
[docker-metadata-action]: https://github.com/docker/metadata-action
[docker-build-push-action]: https://github.com/docker/build-push-action

[secrets]: [[actions#secrets]]

```yaml title=".github/workflows/docker-build.yml"
--8<-- "https://raw.githubusercontent.com/cursgit/tasklist-api/refs/heads/main/.github/workflows/docker-build.yml"
```
