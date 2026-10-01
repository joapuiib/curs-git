---
template: document.html
title: "Exemples de fluxos de treball"
icon: material/file-check-outline
alias: actions-exemples
---

## Exemples de fluxos de treball
Aquests apunts recullen diferents exemples d'automatitzacions en projectes de naturalesa diversa,
per a mostrar com es combinen les opcions de GitHub Actions en casos reals.


### Publicació d'un lloc web estàtic generat amb ProperDocs a GitHub Pages
!!! success "Exemple en el repositori d'aquesta documentació: [`curs-git`][curs-git]"

[curs-git]: {{ config.repo_url }}

L'automatització següent permet __generar aquest lloc web__ amb [ProperDocs][properdocs]
i __publicar-lo__ a [:octicons-browser-24: GitHub Pages][pages].
S'executa sempre que es publiquen canvis nous en la branca `main`, i també es pot executar manualment.

Els passos que la componen són els següents:

/// html | div.steps
1. __Compila el lloc web estàtic amb ProperDocs.__
    - Copia els fitxers del repositori amb l'acció predefinida [`actions/checkout`][actions-checkout].
    - Configura Python amb l'acció predefinida [`actions/setup-python`][actions-setup-python].
    - Instal·la les dependències necessàries per a executar ProperDocs.
    - Compila el lloc web amb l'ordre `properdocs build`.
    - Emmagatzema el directori amb la documentació generada (`site/`) com a artefacte per a la tasca
        següent, amb l'acció predefinida [`actions/upload-pages-artifact`][actions-upload-pages-artifact].
2. __Publica el lloc web a :octicons-browser-24: GitHub Pages.__
    - Només s'executa si la tasca anterior ha acabat correctament.
    - Publica l'artefacte generat en la tasca anterior amb l'acció predefinida [`actions/deploy-pages`][actions-deploy-pages].
///


[properdocs]: https://www.properdocs.org/
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

Aquest flux de treball comprova l'ortografia de la documentació del repositori
amb el programa [`pyspelling`][pyspelling]. S'executa quan es crea una _Pull Request_ sobre la branca `main`
o quan es marca com a llesta per a revisió.

[pyspelling]: https://facelessuser.github.io/pyspelling/

El flux de treball es compon de dues tasques. S'ha dividit d'aquesta manera perquè la correcció ortogràfica
només s'execute quan s'han modificat fitxers de documentació i no es faça innecessàriament
quan es modifiquen altres fitxers.

/// html | div.steps
1. __`changed-files`: comprova si cal fer la correcció ortogràfica.__
    - Comprova si s'han modificat fitxers de documentació (`*.md`) respecte de la branca `main`.
    - Emmagatzema el resultat en la variable `EXIST_CHANGED_FILES`.

2. __`spellcheck`: en cas afirmatiu, comprova l'ortografia dels fitxers modificats.__
    - Només s'executa si `needs.changed-files.outputs.EXIST_CHANGED_FILES == 1`.
    - Instal·la les dependències.
    - Descarrega els diccionaris necessaris.
    - Executa la correcció ortogràfica amb `pyspelling`.
///

```yaml title=".github/workflows/spellcheck.yml"
--8<-- ".github/workflows/spellcheck.yml"
```

### Execució de proves unitàries i d'integració en un projecte Java amb Maven
!!! success "Repositori d'exemple: [`tasklist-api`][tasklist-api]"
    Pots observar-ne el comportament en la :octicons-git-pull-request-16: _Pull Request_
    [feature: tasks can be marked as favorites (#1)][pr]:

    1. En el :octicons-git-commit-16: _commit_ [`2ca7024` – feature: tasks can be marked as favorites][pr-skip]
        no s'han executat les proves, perquè la _Pull Request_ encara estava marcada com a esborrany.
    2. En els _commits_ posteriors, una vegada marcada la _Pull Request_ com a llesta per a revisió,
        sí que s'han executat les proves.

[tasklist-api]: https://github.com/cursgit/tasklist-api
[pr]: https://github.com/cursgit/tasklist-api/pull/1
[pr-skip]: https://github.com/cursgit/tasklist-api/actions/runs/22114248635/job/63918090903
[pr-success]: https://github.com/cursgit/tasklist-api/actions/runs/22138402089/job/63996001935

Aquest flux de treball s'executa cada vegada que es publiquen canvis en la branca `main`
o quan es crea o s'actualitza una _pull request_ cap a les branques `main` o `dev`.
Es basa en dues tasques:

/// html | div.steps
1. __`unit-tests`__: executa les proves unitàries del projecte.
    - Configura l'entorn amb JDK 21.
    - Executa les proves unitàries amb l'ordre `mvn test`.

2. __`integration-tests`__: executa les proves d'integració del projecte.
    - Només s'executa si la tasca `unit-tests` ha acabat correctament.
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
a [PyPI](https://pypi.org/) cada vegada que es publica una etiqueta (`tag`) nova en el repositori.

!!! docs "Documentació oficial de PyPI"
    - [:octicons-link-external-16: Publishing to PyPI with a Trusted Publisher](https://docs.pypi.org/trusted-publishers/)
    - [:octicons-link-external-16: Publishing with a Trusted Publisher](https://docs.pypi.org/trusted-publishers/using-a-publisher/)


Els passos que fa són:

1. Configura l'entorn per a utilitzar Python 3.8.
2. Instal·la el paquet `build` per a compilar les distribucions de Python.
3. Compila les distribucions del paquet.
4. Publica les distribucions a PyPI amb l'acció predefinida [`pypa/gh-action-pypi-publish`][pypi-publish].

[pypi-publish]: https://github.com/pypa/gh-action-pypi-publish

```yaml title=".github/workflows/publish-to-pypi.yml"
--8<-- "https://raw.githubusercontent.com/joapuiib/mkdocs-data-plugin/refs/heads/main/.github/workflows/publish-to-pypi.yml"
```

### Creació d'una imatge de Docker
Aquest exemple crea una imatge de Docker a partir d'un repositori de GitHub
i la publica a [Docker Hub](https://hub.docker.com/), seguint el tutorial següent:

!!! info "[:octicons-link-external-16: Using GitHub Actions to automatically build Docker images][tutorial-docker-build] – :simple-medium: Medium"

!!! example "Repositori d'exemple: [`tasklist-api`][tasklist-api]"
    Quan s'ha publicat [l'etiqueta :octicons-tag-16: `v0.1.0`][tag] en el
    [_commit_ :octicons-git-commit-16: `d42ed1e` – Primera versió del projecte][tag-commit],
    el flux de treball s'ha executat correctament i ha publicat la imatge de Docker
    en el [repositori __`joapuiib/tasklist-api`__ de Docker Hub][docker-hub-repo].


[tutorial-docker-build]: https://medium.com/@kicsipixel/using-github-actions-to-automatically-build-docker-images-65a038b8ce56
[docker-action]: https://github.com/cursgit/tasklist-api/actions/runs/22113606749/job/63915873196
[tag]: https://github.com/cursgit/tasklist-api/releases/tag/v0.1.0
[tag-commit]: https://github.com/cursgit/tasklist-api/actions/runs/22113606749/job/63915873196
[docker-hub-repo]: https://hub.docker.com/repository/docker/joapuiib/tasklist-api/general


Aquest flux de treball s'executa cada vegada que es publica en el repositori una :octicons-tag-16: etiqueta
nova amb el format `v*.*.*`. També es pot executar manualment, ja que està configurat amb `workflow_dispatch`.

Consisteix en una única tasca que fa els passos següents:

/// html | div.steps
1. __Copia el repositori en l'entorn d'execució__ amb l'acció predefinida [`actions/checkout`][actions-checkout].
2. __Inicia sessió a Docker Hub__ amb l'acció predefinida [`docker/login-action`][docker-login-action].
    - Utilitza les credencials `DOCKER_USERNAME` i `DOCKER_PASSWORD` emmagatzemades com a
        [:octicons-key-asterisk-16: secrets][secrets] del repositori.
3. __Configura les metadades de la imatge de Docker__ amb l'acció predefinida [`docker/metadata-action`][docker-metadata-action].
    - Especifica el nom de la imatge: `joapuiib/tasklist-api`.
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
