let aside = document.querySelector('aside');
let toggler = document.querySelector('.toggler');
let right = document.querySelector('.right')
let user = document.querySelector('.user')

toggler.addEventListener('click', () => {
  aside.classList.toggle('aside-active')
})

user.addEventListener('click', () => {
  right.classList.toggle('right-active')
})



let body = document.querySelector('body');
let nav = document.querySelector('.nav');
let shorts = document.querySelector('.section-for-shorts');
let navbar = document.querySelector('.navbar');
let mode = document.querySelector('.aside');
let options = document.querySelector('.options')
let switch_mode = document.querySelector('.choose');
let switch_mode2 = document.querySelector('.choose2');
let span = document.querySelector('.material-symbols-outlined');


switch_mode.addEventListener('click', () => {
  body.classList.toggle('body-active');
  nav.classList.toggle('nav-active');
  navbar.classList.toggle('navbar-active');
  mode.classList.toggle('mode-active');
  options.classList.toggle('options-active');
  span.classList.toggle('span-active');
  shorts.classList.toggle('shorts-active');
  aside.classList.toggle('aside-active2');
  right.classList.toggle('right-active2')
});
