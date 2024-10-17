anna@fp:~/gitflow/anna (feature/readme) $ git checkout develop
Your branch is up to date with 'origin/develop'.
Switched to branch 'develop'
anna@fp:~/gitflow/anna (develop) $ git merge --squash feature/readme
Updating b11655b..60e7175
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
[develop 2241b23] Merge branch 'feature/readme'
 1 file changed, 6 insertions(+)
anna@fp:~/gitflow/anna (develop) $ git lga
* 2241b23 - (0 seconds ago) Merge branch 'feature/readme' - Anna (HEAD -> develop)
| * 60e7175 - (0 seconds ago) README.md: Branques propòsit únic - Anna (origin/feature/readme, feature/readme)
| * a32d18d - (0 seconds ago) README.md: Descripció - Anna
|/  
| * 6a65cbc - (0 seconds ago) Autors: Mar - Mar (origin/feature/author)
| * 41f9bfe - (0 seconds ago) Autors: Pau - Mar
| * 36c37ef - (0 seconds ago) Autors: Anna - Mar
| * 4b4163e - (0 seconds ago) README.md: Secció d'autors - Mar
|/  
| * c424285 - (0 seconds ago) LICENSE: Enllaç a la llicència - Pau (origin/feature/license)
| * 2da5ca1 - (0 seconds ago) LICENSE: Afegida llicència - Pau
|/  
* b11655b - (1 second ago) Commit inicial - Joan Puigcerver (origin/main, origin/develop, origin/HEAD, main)
