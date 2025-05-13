document$.subscribe(function() {
  let carousels = document.querySelectorAll(".carousel");

  carousels.forEach(function(e) {
    let carousel = new Carousel(e);
    carousel.init();
    carousel.setSlide(0);
  });
})

class Carousel {
  constructor(element) {
    this.element = element;
    this.currentIndex = 0;
    this.images = element.querySelectorAll('img');
    this.dots = null;
  }

  init(){
    this.removeParagraphs();
    this.renderControls();
    this.renderDots();
  }

  removeParagraphs(){
    const paragraphs = this.element.querySelectorAll('p');
    paragraphs.forEach(function(p) {
      let childs = p.childNodes;
      let parent = p.parentNode;
      for (let i = 0; i < childs.length; i++) {
        parent.append(childs[i]);
      }
      p.remove();
    });
  }

  renderControls(){
    // Create the "prev" link
    const prev = document.createElement('a');
    prev.className = 'prev';
    prev.innerHTML = '&#10094;'; // Left arrow
    prev.onclick = () => {
      this.currentIndex--;
      if (this.currentIndex < 0) this.currentIndex += this.images.length;
      this.setSlide(this.currentIndex);
    };

    // Create the "next" link
    const next = document.createElement('a');
    next.className = 'next';
    next.innerHTML = '&#10095;'; // Right arrow
    next.onclick = () => {
      this.currentIndex++;
      if (this.currentIndex > this.images.length - 1) this.currentIndex -= this.images.length;
      this.setSlide(this.currentIndex);
    };

    this.element.append(prev);
    this.element.append(next);
  }

  renderDots(){
    const dotContainer = document.createElement('div');
    dotContainer.className = 'carousel__dot-container';

    const images = this.element.querySelectorAll('img');
    for (let i = 0; i < images.length; i++) {
      let dot = document.createElement('span');
      dot.className = 'dot';
      dot.onclick = () => {
        this.currentIndex = i;
        this.setSlide(i);
      };

      dotContainer.append(dot);
    }

    this.element.append(dotContainer);
    this.dots = dotContainer.querySelectorAll('.dot');
  }

  setSlide(n) {
    let i;
    n = n % this.images.length;

    for (i = 0; i < this.images.length; i++) {
      this.images[i].style.display = "none";
    }
    for (i = 0; i < this.dots.length; i++) {
      this.dots[i].className = this.dots[i].className.replace(" active", "");
    }
    this.images[n].style.display = "block";
    this.dots[n].className += " active";
  }
}
