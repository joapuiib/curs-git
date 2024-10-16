anna@fp:~/gitflow/anna (feature/readme) $ git checkout develop
Your branch is up to date with 'origin/develop'.
Switched to branch 'develop'
anna@fp:~/gitflow/anna (develop) $ git merge --squash feature/readme
Updating a1acfb5..ad0d531
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
[develop 069239c] Merge branch 'feature/readme'
 1 file changed, 6 insertions(+)
anna@fp:~/gitflow/anna (develop) $ git lga
* 069239c - (0 seconds ago) Merge branch 'feature/readme' - Anna (HEAD -> develop)
| * ad0d531 - (0 seconds ago) README.md: Branques propòsit únic - Anna (origin/feature/readme, feature/readme)
| * 651842a - (0 seconds ago) README.md: Descripció - Anna
|/  
| * 3e60c32 - (0 seconds ago) Autors: Mar - Mar (origin/feature/author)
| * 32a7bd7 - (0 seconds ago) Autors: Pau - Mar
| * cebc3c1 - (0 seconds ago) Autors: Anna - Mar
| * 0677978 - (0 seconds ago) README.md: Secció d'autors - Mar
|/  
| * db2c8a8 - (0 seconds ago) LICENSE: Enllaç a la llicència - Pau (origin/feature/license)
| * d20ffa3 - (0 seconds ago) LICENSE: Afegida llicència - Pau
|/  
* a1acfb5 - (0 seconds ago) Commit inicial - Joan Puigcerver (origin/main, origin/develop, origin/HEAD, main)
