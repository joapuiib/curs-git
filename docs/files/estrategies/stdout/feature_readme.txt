anna@fp:~/git_estrategies $ cd ~/git_estrategies/anna
anna@fp:~/git_estrategies/anna (main) $ git config user.name "Anna"
anna@fp:~/git_estrategies/anna (main) $ git config user.email "anna@alu.edu.gva.es"
anna@fp:~/git_estrategies/anna (main) $ git checkout develop
branch 'develop' set up to track 'origin/develop'.
Switched to a new branch 'develop'
anna@fp:~/git_estrategies/anna (develop) $ git checkout -b feature/readme
Switched to a new branch 'feature/readme'
anna@fp:~/git_estrategies/anna (feature/readme) $ echo "Les estratègies de ramificació proporcionen un" >> README.md
anna@fp:~/git_estrategies/anna (feature/readme) $ echo "marc de treball organitzat que facilita la col·laboració" >> README.md
anna@fp:~/git_estrategies/anna (feature/readme) $ echo "entre diferents desenvolupadors en un mateix projecte" >> README.md
anna@fp:~/git_estrategies/anna (feature/readme) $ git commit -a -m "README.md: Descripció"
[feature/readme 502dadb] README.md: Descripció
 1 file changed, 3 insertions(+)
anna@fp:~/git_estrategies/anna (feature/readme) $ echo "" >> README.md
anna@fp:~/git_estrategies/anna (feature/readme) $ echo "La característica principal és la utilització" >> README.md
anna@fp:~/git_estrategies/anna (feature/readme) $ echo "de branques amb un únic propòsit." >> README.md
anna@fp:~/git_estrategies/anna (feature/readme) $ git commit -a -m "README.md: Branques propòsit únic"
[feature/readme ea2559a] README.md: Branques propòsit únic
 1 file changed, 3 insertions(+)
anna@fp:~/git_estrategies/anna (feature/readme) $ git push -u origin feature/readme
branch 'feature/readme' set up to track 'origin/feature/readme'.
To ~/git_estrategies/remot
 * [new branch]      feature/readme -> feature/readme
anna@fp:~/git_estrategies/anna (feature/readme) $ git lga
* ea2559a - (0 seconds ago) README.md: Branques propòsit únic - Anna (HEAD -> feature/readme, origin/feature/readme)
* 502dadb - (0 seconds ago) README.md: Descripció - Anna
* ec0e2bd - (0 seconds ago) Commit inicial - Joan Puigcerver (origin/main, origin/develop, origin/HEAD, main, develop)
