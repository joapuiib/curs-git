document$.subscribe(function() {
  var tables = document.querySelectorAll("article div.table-sortable table")
  tables.forEach(function(table) {
    new Tablesort(table)
  })
})
