// navbar
function myMenuFunction() {
  var menuBtn = document.getElementById("myNavMenu");
  if (menuBtn.className == "nav-menu") {
    menuBtn.className += " responsive";
  } else {
    menuBtn.className = "nav-menu";
  }
}

// add shadow on navigation bar while scrolling

window.onscroll = function () {
  headerShadow();
};
function headerShadow() {
  const navHeader = document.getElementById("header");
  if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
    navHeader.style.boxShadow = "0 1px 6px rgba(0,0,0,0.1)";
    navHeader.style.height = "70px";
    navHeader.style.lineHeight = "70px";
  } else {
    navHeader.style.boxShadow = "none";
    navHeader.style.height = "90px";
    navHeader.style.lineHeight = "70px";
  }
}

// typing
var typingEffect = new Typed(".typedText", {
  strings: [
    "Software Engineer",
    "Fullstack Developer",
    "Django Developer",
    "Backend Developer",
  ],
  loop: true,
  typeSpeed: 100,
  backSpeed: 80,
  backDelay: 2000,
});

// scroll animation
const sr = ScrollReveal({
  origin: "top",
  distance: "80px",
  duration: 2000,
  reset: true,
});

// home
sr.reveal(".featured-text-card", {});
sr.reveal(".featured-name", { delay: 100 });
sr.reveal(".featured-text-info", { delay: 200 });
sr.reveal(".featured-text-btn", { delay: 200 });
sr.reveal(".social-icons", { delay: 200 });
sr.reveal(".featured-image", { delay: 300 });

// project
sr.reveal(".project-box", { interval: 200 });

// heading
sr.reveal(".top-header", {});

// about info
const srLeft = ScrollReveal({
  origin: "left",
  distance: "80px",
  duratin: 2000,
  reset: true,
});

srLeft.reveal(".about-info", { delay: 100 });
srLeft.reveal(".contact-info", { delay: 100 });

// about skill
const srRight = ScrollReveal({
  origin: "right",
  distance: "80px",
  duratin: 2000,
  reset: true,
});

srLeft.reveal(".skills-box", { delay: 100 });
srLeft.reveal(".form-container", { delay: 100 });
