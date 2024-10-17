anna@fp:~/gitflow $ cd ~/gitflow/anna
anna@fp:~/gitflow/anna (main) $ git config user.name "Anna"
anna@fp:~/gitflow/anna (main) $ git config user.email "anna@fpmislata.com"
anna@fp:~/gitflow/anna (main) $ git checkout develop
Branch 'develop' set up to track remote branch 'develop' from 'origin'.
Switched to a new branch 'develop'
anna@fp:~/gitflow/anna (develop) $ git checkout -b feature/readme
Switched to a new branch 'feature/readme'
anna@fp:~/gitflow/anna (feature/readme) $ echo "Les estratègies de ramificació proporcionen un" >> README.md
anna@fp:~/gitflow/anna (feature/readme) $ echo "marc de treball organitzat que facilita la col·laboració" >> README.md
anna@fp:~/gitflow/anna (feature/readme) $ echo "entre diferents desenvolupadors en un mateix projecte" >> README.md
anna@fp:~/gitflow/anna (feature/readme) $ git commit -a -m "README.md: Descripció"
[feature/readme a32d18d] README.md: Descripció
 1 file changed, 3 insertions(+)
anna@fp:~/gitflow/anna (feature/readme) $ echo "" >> README.md
anna@fp:~/gitflow/anna (feature/readme) $ echo "La característica principal és la utilització" >> README.md
anna@fp:~/gitflow/anna (feature/readme) $ echo "de branques amb un únic propòsit." >> README.md
anna@fp:~/gitflow/anna (feature/readme) $ git commit -a -m "README.md: Branques propòsit únic"
[feature/readme 60e7175] README.md: Branques propòsit únic
 1 file changed, 3 insertions(+)
anna@fp:~/gitflow/anna (feature/readme) $ git push -u origin feature/readme
Branch 'feature/readme' set up to track remote branch 'feature/readme' from 'origin'.
To ~/gitflow/remot
 * [new branch]      feature/readme -> feature/readme
anna@fp:~/gitflow/anna (feature/readme) $ git lga
* 60e7175 - (0 seconds ago) README.md: Branques propòsit únic - Anna (HEAD -> feature/readme, origin/feature/readme)
* a32d18d - (0 seconds ago) README.md: Descripció - Anna
* b11655b - (1 second ago) Commit inicial - Joan Puigcerver (origin/main, origin/develop, origin/HEAD, main, develop)
