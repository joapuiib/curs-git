document$.subscribe(function() {
  var codeblocks = document.querySelectorAll(".highlight[data-download]")
  codeblocks.forEach(function(el) {
    mountDownloadButton(el)
  })
})

function mountDownloadButton(el) {
  var code = el.querySelector('code')
  var data_download = el.getAttribute('data-download')
  var parent = code.closest('pre')

  if (data_download == "1") {
    var filename = el.querySelector('span.filename').textContent
    if (filename) {
      const button = renderDownloadContentButton(parent.id, filename)
      parent.insertBefore(button, code)
    }
  } else {
    const button = renderDownloadFileButton(parent.id, data_download)
    parent.insertBefore(button, code)
  }
}

function renderDownloadContentButton(id, filename) {
  // Create the button element instead of returning an HTML string
  const button = document.createElement("button");
  button.className = "md-download md-icon";
  button.title = "Download";

  // Attach a click event listener to handle the download logic
  button.addEventListener("click", function() {
    const codeElement = document.querySelector(`#${id} > code`);
    if (codeElement) {
      const codeContent = codeElement.textContent;
      const blob = new Blob([codeContent], { type: "text/plain" });
      const url = URL.createObjectURL(blob);

      const a = document.createElement("a");
      a.href = url;
      a.download = filename;
      a.click();

      URL.revokeObjectURL(url); // Clean up the URL after download
    }
  });

  return button;
}

function renderDownloadFileButton(id, filepath) {
  // Create the button element instead of returning an HTML string
  const button = document.createElement("a");
  button.className = "md-download md-icon";
  button.title = "Download";
  button.setAttribute("href", filepath);

  var basename = filepath.replace(/^.*[\\/]/, '')
  button.setAttribute("download", basename);

  return button;
}
