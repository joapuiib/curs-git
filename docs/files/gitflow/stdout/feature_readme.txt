anna@fp:~/gitflow $ cd ~/gitflow/anna
anna@fp:~/gitflow/anna (main) $ git config user.name "Anna"
anna@fp:~/gitflow/anna (main) $ git config user.email "anna@fpmislata.com"
anna@fp:~/gitflow/anna (main) $ git checkout develop
branch 'develop' set up to track 'origin/develop'.
Switched to a new branch 'develop'
anna@fp:~/gitflow/anna (develop) $ git checkout -b feature/readme
Switched to a new branch 'feature/readme'
anna@fp:~/gitflow/anna (feature/readme) $ echo "Gitflow és una estratègia de ramificació per a Git," >> README.md
anna@fp:~/gitflow/anna (feature/readme) $ echo "que proporciona un marc de treball organitzat que" >> README.md
anna@fp:~/gitflow/anna (feature/readme) $ echo "facilita la col·laboració entre diferents desenvolupadors" >> README.md
anna@fp:~/gitflow/anna (feature/readme) $ echo "en un mateix projecte." >> README.md
anna@fp:~/gitflow/anna (feature/readme) $ git commit -a -m "2. Afegida descripció del projecte"
[feature/readme 61742c0] 2. Afegida descripció del projecte
 1 file changed, 4 insertions(+)
anna@fp:~/gitflow/anna (feature/readme) $ git push
branch 'feature/readme' set up to track 'origin/feature/readme'.
To ~/gitflow/remot
 * [new branch]      feature/readme -> feature/readme
anna@fp:~/gitflow/anna (feature/readme) $ git lga
* 61742c0 - (0 seconds ago) 2. Afegida descripció del projecte - Anna (HEAD -> feature/readme, origin/feature/readme)
* 7cf4080 - (0 seconds ago) 1. Primer commit - Joan Puigcerver (origin/main, origin/develop, origin/HEAD, main, develop)
