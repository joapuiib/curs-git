document$.subscribe(({ body }) => { 
  document.querySelectorAll('.arithmatex').forEach((el) => {
    renderMathInElement(el, {
      delimiters: [
        { left: "$$",  right: "$$",  display: true },
        { left: "$",   right: "$",   display: false },
        { left: "\\(", right: "\\)", display: false },
        { left: "\\[", right: "\\]", display: true }
      ],
    })
  })
})
