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

Aquesta acció s'executa sempre que es publiquen nous canvis sobre la branca `main`.

Els passos que la componen són els següents:

1. Còpia el repositori a l'entorn d'execució amb l'acció predefinida [`actions/checkout@v4`][actions-checkout].
1. Canvia les credencials de git perquè els commits estiguen associats a un bot de GitHub.
1. Configura l'entorn per poder utilitzar Python 3.
1. Instal·la les dependències de Python.
1. Genera i publica el lloc web amb l'ordre [`mkdocs gh-deploy`][gh-deploy]

[mkdocs]: https://www.mkdocs.org/
[gh-deploy]: https://www.mkdocs.org/user-guide/cli/#mkdocs-gh-deploy
[actions-checkout]: https://github.com/marketplace/actions/checkout
[pages]: https://pages.github.com/

```yaml title=".github/workflows/deploy.yml"
--8<-- ".github/workflows/deploy.yml"
```


### Prova de correcció ortogràfica
!!! success "Exemple en el repositori d'aquesta documentació: [`curs-git`][curs-git]"

Aquest flux de treball comprova la correcció ortogràfica de la documentació
del repositori utilitzant el programa [`pyspelling`][pyspelling].

[pyspelling]: https://facelessuser.github.io/pyspelling/

El flux de treball es compon de dues tasques. S'ha configurat d'aquesta manera
perquè la tasca de correcció ortogràfica només s'executa quan s'han modificat fitxers de documentació,
evitant així executar-la innecessàriament quan es modifiquen altres fitxers.

- __`changed-files`__: Comprova si cal realitzar la correcció ortogràfica.
    - Comprova si s'han modificat fitxers de documentació (`*.md`) respecte a la branca `main`.
    - Emmagatzema el resultat en la variable `EXIST_CHANGED_FILES`.

- __`spellcheck`__: En cas afirmatiu, comprova la correcció ortogràfica dels fitxers modificats.
    - S'executa només si `needs.changed-files.outputs.EXIST_CHANGED_FILES == 1`.
    - Instal·la les dependències.
    - Es descarrega els diccionaris necessaris.
    - Executa la correcció ortogràfica amb `pyspelling`.

```yaml title=".github/workflows/spellcheck.yml"
--8<-- ".github/workflows/spellcheck.yml"
```

### Execució de proves unitàries i d'integració en un projecte Java amb Maven
!!! example "Repositori d'exemple: [`tasklist-api`][tasklist-api]"

[tasklist-api]: https://github.com/cursgit/tasklist-api

Aquest flux de treball s'executa cada vegada que es publiquen canvis a la branca `main`
o quan es crea o actualitza una pull request cap a les branques `main` o `development`.

Es basa en dues tasques:

- __`unit-test`__: Executa les proves unitàries del projecte.
    - Configura l'entorn amb JDK 21.
    - Executa les proves unitàries amb l'ordre `mvn test`.
- __`integration-test`__: Executa les proves d'integració del projecte.
    - Sols s'executa si la tasca `unit-test` s'ha executat correctament.
    - Configura l'entorn amb JDK 21.
    - Executa les proves d'integració amb l'ordre `mvn verify`, sense tornar a executar les proves unitàries.

=== "`maven-tests.yml`"
    ```yaml title=".github/workflows/maven-tests.yml"
    name: Test Java with Maven

    on:
      push:
        branches: [ "main" ]
      pull_request:
        # Tipus d'events sobre la pull request
        types: [ 'opened', 'edited', 'reopened', 'synchronize', 'ready_for_review' ]
        branches: [ "main", "development" ]
      workflow_dispatch:

    jobs:
      unit-test:
        if: github.event_name == 'push' || github.event.pull_request.draft == false

        runs-on: ubuntu-latest

        steps:
        - uses: actions/checkout@v4
        - name: Set up JDK 21
          uses: actions/setup-java@v3
          with:
            java-version: '21'
            distribution: 'temurin'
            cache: maven
        - name: Run Unit Tests with Maven
          run: mvn --batch-mode test

      integration-test:
        needs: unit-test
        if: github.event_name == 'push' || github.event.pull_request.draft == false

        runs-on: ubuntu-latest

        steps:
        - uses: actions/checkout@v4
        - name: Set up JDK 21
          uses: actions/setup-java@v3
          with:
            java-version: '21'
            distribution: 'temurin'
            cache: maven
        - name: Run Integration Tests with Maven
          run: mvn --batch-mode verify -Dskip.ut=true
    ```

=== "`pom.xml`"
    ```xml title="pom.xml"
    <project>
        ...
        <properties>
            <skip.ut>false</skip.ut> 
        </properties>

        <dependencies>
            ...
        </dependencies>

        <build>
            <plugins>
                <plugin>
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-surefire-plugin</artifactId>
                    <!-- JUnit 5 requires Surefire version 2.22.0 or higher -->
                    <version>3.5.2</version>
                    <configuration>
                        <skipTests>${skip.ut}</skipTests>
                    </configuration>
                </plugin>
                ...
            </plugins>
        </build>
    </project>
    ```

### Desplegament d'un projecte Java a AWS
!!! warning "TODO"

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

__[:octicons-link-external-16: Using GitHub Actions to automatically build Docker images][docker-build] – :simple-medium: Medium__

[docker-build]: https://medium.com/@kicsipixel/using-github-actions-to-automatically-build-docker-images-65a038b8ce56
