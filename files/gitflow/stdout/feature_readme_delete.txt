anna@fp:~/gitflow/anna (develop) $ git branch -d feature/readme
Deleted branch feature/readme (was 99b85bc).
warning: deleting branch 'feature/readme' that has been merged to
         'refs/remotes/origin/feature/readme', but not yet merged to HEAD
anna@fp:~/gitflow/anna (develop) $ git push origin --delete feature/readme
To ~/gitflow/remot
 - [deleted]         feature/readme
anna@fp:~/gitflow/anna (develop) $ git lga
* 6dcedfa - (0 seconds ago) Merge branch 'feature/readme' - Anna (HEAD -> develop, origin/develop)
| * 3e9f87b - (0 seconds ago) Autors: Mar - Mar (origin/feature/author)
| * 2d3d519 - (0 seconds ago) Autors: Pau - Mar
| * 7b77dba - (0 seconds ago) Autors: Anna - Mar
| * 0043084 - (0 seconds ago) README.md: Secció d'autors - Mar
|/  
| * efc6b7f - (0 seconds ago) LICENSE: Enllaç a la llicència - Pau (origin/feature/license)
| * fcfe09d - (0 seconds ago) LICENSE: Afegida llicència - Pau
|/  
* 58facc3 - (0 seconds ago) Commit inicial - Joan Puigcerver (origin/main, origin/HEAD, main)
