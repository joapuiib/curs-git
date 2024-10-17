anna@fp:~/gitflow/anna (feature/readme) $ git checkout develop
Your branch is up to date with 'origin/develop'.
Switched to branch 'develop'
anna@fp:~/gitflow/anna (develop) $ git merge --squash feature/readme
Updating ec0e2bd..ea2559a
Fast-forward
Squash commit -- not updating HEAD
 README.md | 6 ++++++
 1 file changed, 6 insertions(+)
anna@fp:~/gitflow/anna (develop) $ git status
On branch develop
Your branch is up to date with 'origin/develop'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   README.md

anna@fp:~/gitflow/anna (develop) $ git diff --staged
diff --git a/README.md b/README.md
index 05c1f5b..9e7f142 100644
--- a/README.md
+++ b/README.md
@@ -1 +1,7 @@
 # Estratègies de ramificació
+Les estratègies de ramificació proporcionen un
+marc de treball organitzat que facilita la col·laboració
+entre diferents desenvolupadors en un mateix projecte
+
+La característica principal és la utilització
+de branques amb un únic propòsit.
anna@fp:~/gitflow/anna (develop) $ git commit -m "Merge branch 'feature/readme'"
[develop 2bc4029] Merge branch 'feature/readme'
 1 file changed, 6 insertions(+)
anna@fp:~/gitflow/anna (develop) $ git lga
* 2bc4029 - (0 seconds ago) Merge branch 'feature/readme' - Anna (HEAD -> develop)
| * a216550 - (1 second ago) Autors: Mar - Mar (origin/feature/author)
| * 1d5ba44 - (1 second ago) Autors: Pau - Mar
| * 8683319 - (1 second ago) Autors: Anna - Mar
| * 24be503 - (1 second ago) README.md: Secció d'autors - Mar
|/  
| * c213387 - (1 second ago) LICENSE: Enllaç a la llicència - Pau (origin/feature/license)
| * b11b498 - (1 second ago) LICENSE: Afegida llicència - Pau
|/  
| * ea2559a - (2 seconds ago) README.md: Branques propòsit únic - Anna (origin/feature/readme, feature/readme)
| * 502dadb - (2 seconds ago) README.md: Descripció - Anna
|/  
* ec0e2bd - (2 seconds ago) Commit inicial - Joan Puigcerver (origin/main, origin/develop, origin/HEAD, main)
