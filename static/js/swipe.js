
let swiper = new Swiper(".mySwiper", {
  observer: true,
        observeParents: true,
  grabCursor: true,
  
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
 });