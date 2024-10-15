anna@fp:~/gitflow $ cd ~/gitflow/anna
anna@fp:~/gitflow/anna (main) $ git config user.name Anna
anna@fp:~/gitflow/anna (main) $ git config user.email anna@fpmislata.com
anna@fp:~/gitflow/anna (main) $ git checkout develop
Switched to a new branch 'develop'
branch 'develop' set up to track 'origin/develop'.
anna@fp:~/gitflow/anna (develop) $ git checkout -b feature/readme
Switched to a new branch 'feature/readme'
anna@fp:~/gitflow/anna (feature/readme) $ echo Gitflow és una estratègia de ramificació per a Git,
Gitflow és una estratègia de ramificació per a Git,
anna@fp:~/gitflow/anna (feature/readme) $ echo que proporciona un marc de treball organitzat que
que proporciona un marc de treball organitzat que
anna@fp:~/gitflow/anna (feature/readme) $ echo facilita la col·laboració entre diferents desenvolupadors
facilita la col·laboració entre diferents desenvolupadors
anna@fp:~/gitflow/anna (feature/readme) $ echo en un mateix projecte.
en un mateix projecte.
anna@fp:~/gitflow/anna (feature/readme) $ git commit -a -m 2. Afegida descripció del projecte
[feature/readme 97beddf] 2. Afegida descripció del projecte
 1 file changed, 8 insertions(+)
anna@fp:~/gitflow/anna (feature/readme) $ git push
To ~/gitflow/remot
 * [new branch]      feature/readme -> feature/readme
branch 'feature/readme' set up to track 'origin/feature/readme'.
anna@fp:~/gitflow/anna (feature/readme) $ git lga
* 97beddf - (0 seconds ago) 2. Afegida descripció del projecte - Anna (HEAD -> feature/readme, origin/feature/readme)
* 41c3aa7 - (0 seconds ago) 1. Primer commit - Joan Puigcerver (origin/main, origin/develop, origin/HEAD, main, develop)
