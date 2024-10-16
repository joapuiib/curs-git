anna@fp:~/gitflow/anna (feature/readme) $ git checkout develop
Your branch is up to date with 'origin/develop'.
Switched to branch 'develop'
anna@fp:~/gitflow/anna (develop) $ git merge --squash feature/readme
Updating 87c24d1..7b5639f
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
[develop 6096544] Merge branch 'feature/readme'
 1 file changed, 6 insertions(+)
anna@fp:~/gitflow/anna (develop) $ git lga
* 6096544 - (0 seconds ago) Merge branch 'feature/readme' - Anna (HEAD -> develop)
| * 7b5639f - (0 seconds ago) README.md: Branques propòsit únic - Anna (origin/feature/readme, feature/readme)
| * 7ea1615 - (0 seconds ago) README.md: Descripció - Anna
|/  
| * c797058 - (0 seconds ago) Autors: Mar - Mar (origin/feature/author)
| * e42be41 - (0 seconds ago) Autors: Pau - Mar
| * 1a39e97 - (0 seconds ago) Autors: Anna - Mar
| * c20b570 - (0 seconds ago) README.md: Secció d'autors - Mar
|/  
| * 1d2a6af - (0 seconds ago) LICENSE: Enllaç a la llicència - Pau (origin/feature/license)
| * c522ea2 - (0 seconds ago) LICENSE: Afegida llicència - Pau
|/  
* 87c24d1 - (0 seconds ago) Commit inicial - Joan Puigcerver (origin/main, origin/develop, origin/HEAD, main)
