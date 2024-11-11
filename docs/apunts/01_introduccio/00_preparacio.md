---
template: document.html
title: "Preparació de l'entorn"
icon: material/book-open-variant
alias: preparacio
comments: true
tags:
  - git
  - VS Code
---

## Preparació de l'entorn
En aquesta secció, veurem com instal·lar i configurar les eines necessàries
per a treballar amb :material-git: Git i :material-microsoft-visual-studio-code: Visual Studio Code.

## Per què la terminal?
En aquest curs, utilitzarem la terminal per a interactuar amb Git, però això no significa que siga l'única manera de fer-ho.
De fet, pràcticament tots els entorns de desenvolupament moderns tenen integració amb Git, la qual cosa permet realitzar
les mateixes operacions que proporciona la terminal, però de manera més visual i intuïtiva.

No obstant això, és important conéixer com funcionen les comandes de Git en la terminal, per diferents raons:

- __Portabilitat__: La terminal és un entorn comú en tots els sistemes operatius i en qualsevol entorn de desenvolupament.
- __Flexibilitat__: La terminal permet realitzar operacions més avançades i personalitzades que les interfícies gràfiques.
- __Comprensió__: Permet entendre com funcionen les comandes de Git i els processos que realitza en el sistema.


## Instal·lació de :material-git: Git
Git està disponible a https://git-scm.com/ per a Windows, macOS i Linux.

=== "Ubuntu"

    ```bash
    sudo apt update
    sudo apt install git
    ```

=== "Windows"

    Descarrega i executa l'instal·lador de Git des de https://git-scm.com/

    Una vegada instal·lat, pots utilitzar la consola __Git Bash__.
    És una terminal basada l'intèrpret __Bash__, que et permetrà
    realitzar les comandes de Git en la consola.

### Configuració inicial
Git utilitza un editor de text per a realitzar certes operacions,
com ara escriure missatges de commit.

Per defecte, Git utilitza l'editor [`ViM`](https://www.vim.org/),
un editor de text per terminal molt potent, però difícil i poc intuïtiu
per treballar.


Si desitgeu canviar l'editor per defecte, podeu utilitzar
la següent comanda des de la consola:

```bash
git config --global core.editor <editor>
```

!!! tip "Editors de text"

    === ":material-microsoft-windows: Windows"

        - `notepad`. Ve instal·lat per defecte.
        - [Notepad++.](https://notepad-plus-plus.org/)

        ```
        git config --global core.editor notepad
        ```

    === ":simple-linux: Linux"

        - `gedit`. Ve instal·lat per defecte en Ubuntu.
        - `nano`. Editor de text bàsic per terminal.
        - `vim`. Editor de text avançat per terminal.
            - `:w` per guardar.
            - `:q` per eixir.

        ```
        git config --global core.editor nano
        ```

    === ":material-asterisk: Multiplataforma"

        - [:material-microsoft-visual-studio-code: Visual Studio Code](https://code.visualstudio.com/)
            - [StackOverflow: How to use Visual Studio Code as default editor for git?](https://stackoverflow.com/questions/30024353/how-to-use-visual-studio-code-as-default-editor-for-git){:target=_blank}

        ```
        git config --global core.editor "code --wait"
        ```

!!! recommend
    Com que utilitzarem :material-microsoft-visual-studio-code: Visual Studio Code com a editor de text,
    vos recomane que l'utilitzeu també com a editor per a Git.

    ```bash
    git config --global core.editor "code --wait"
    ```


## Instal·lació de :material-microsoft-visual-studio-code: Visual Studio Code
[:material-microsoft-visual-studio-code: Visual Studio Code](https://code.visualstudio.com/){:target=_blank}
és un editor de text gratuït i de codi obert desenvolupat per :material-microsoft: Microsoft.

És un editor molt popular entre els desenvolupadors per la seua lleugeresa, rendiment i gran quantitat d'extensions disponibles,
que permeten personalitzar-lo per a qualsevol llenguatge de programació.

Per a instal·lar-lo, descarrega'l des de la seua pàgina web i executa l'instal·lador.

### Configuració
Anem a realitzar algunes configuracions bàsiques per a treballar amb Git en Visual Studio Code.

#### Integració amb la terminal
:material-microsoft-visual-studio-code: Visual Studio Code permet obrir una terminal integrada
en la part inferior de la finestra, la qual cosa facilita la seua utilització sense haver de canviar
de finestra.

Es pot obrir la terminal mitjançant el menú __Terminal__ > __New Terminal__.


!!! tip
    En sistemes :material-microsoft-windows: Windows,
    la terminal integrada utilitza :material-powershell: PowerShell per defecte.

    Podeu seleccionar Git Bash des del [menú desplegable de la terminal](https://code.visualstudio.com/docs/terminal/basics#_terminal-shells){:target=_blank},
    on també podeu configurar que aquesta opció siga la predeterminada.

    ![Menú desplegable de la terminal](img/vscode_terminal.png)
    /// attribution
    [Documentació oficial de :material-microsoft-visual-studio-code: Visual Studio Code](https://code.visualstudio.com/docs/terminal/basics#_terminal-shells){:target=_blank}
    ///
    /// figure-caption
    Menú desplegable de la terminal en :material-microsoft-visual-studio-code: Visual Studio Code.
    ///

#### Extensió Git Graph
Per a visualitzar la història dels commits de manera gràfica,
podeu instal·lar l'extensió [__Git Graph__](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph){:target=_blank}
des de l'apartat d'extensions de Visual Studio Code.

![Demostració de l'extensió Git Graph](img/git_graph_demo.gif)
/// attribution
[Extensió Git Graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph){:target=_blank}
///
/// figure-caption
Demostració de l'extensió Git Graph
///

Una vegada instal·lada, podeu accedir a la vista gràfica de
la història de commits des del botó __Git Graph__ en la barra inferior esquerra de l'editor.

![Botó Git Graph](img/git_graph.png)
/// figure-caption
Botó Git Graph en :material-microsoft-visual-studio-code: Visual Studio Code.
///

## Recursos addicionals
- [Extensió Git Graph per a Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph){:target=_blank}
- [StackOverflow: What is the shortcut for displaying the GitGraph tab on VS Code?](https://stackoverflow.com/questions/57803207/what-is-the-shortcut-for-displaying-the-gitgraph-tab-on-vs-code){:target=_blank}