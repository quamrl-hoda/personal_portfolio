/* ===== TYPED TEXT ANIMATION ===== */
const typedLines = [
  "Machine Learning Engineer",
  "AI/ML Developer",
  "NLP & LLM Specialist",
  "Agentic AI Builder",
  "Deep Learning Researcher",
];

let lineIdx = 0, charIdx = 0, deleting = false;
const typedEl = document.getElementById("typedText");

function typeLoop() {
  const current = typedLines[lineIdx];
  if (!deleting) {
    typedEl.textContent = current.slice(0, ++charIdx);
    if (charIdx === current.length) {
      deleting = true;
      setTimeout(typeLoop, 1800);
      return;
    }
  } else {
    typedEl.textContent = current.slice(0, --charIdx);
    if (charIdx === 0) {
      deleting = false;
      lineIdx = (lineIdx + 1) % typedLines.length;
      setTimeout(typeLoop, 350);
      return;
    }
  }
  setTimeout(typeLoop, deleting ? 50 : 75);
}
typeLoop();

/* ===== NAVBAR SCROLL ===== */
const navbar = document.getElementById("navbar");
window.addEventListener("scroll", () => {
  navbar.classList.toggle("scrolled", window.scrollY > 30);
});

/* ===== MOBILE NAV TOGGLE ===== */
const navToggle = document.getElementById("navToggle");
const navLinks = document.getElementById("navLinks");
navToggle.addEventListener("click", () => {
  navLinks.classList.toggle("open");
  const spans = navToggle.querySelectorAll("span");
  if (navLinks.classList.contains("open")) {
    spans[0].style.transform = "rotate(45deg) translate(5px,5px)";
    spans[1].style.opacity = "0";
    spans[2].style.transform = "rotate(-45deg) translate(5px,-5px)";
  } else {
    spans.forEach(s => { s.style.transform = ""; s.style.opacity = ""; });
  }
});
document.querySelectorAll(".nav-link").forEach(link => {
  link.addEventListener("click", () => {
    navLinks.classList.remove("open");
    const spans = navToggle.querySelectorAll("span");
    spans.forEach(s => { s.style.transform = ""; s.style.opacity = ""; });
  });
});

/* ===== ACTIVE NAV LINK ON SCROLL ===== */
const sections = document.querySelectorAll("section[id]");
const navLinkEls = document.querySelectorAll(".nav-link");

function updateActiveNav() {
  let current = "";
  sections.forEach(section => {
    const top = section.offsetTop - 100;
    if (window.scrollY >= top) current = section.getAttribute("id");
  });
  navLinkEls.forEach(link => {
    link.classList.toggle("active", link.getAttribute("data-section") === current);
  });
}
window.addEventListener("scroll", updateActiveNav);
updateActiveNav();

/* ===== COUNTER ANIMATION ===== */
function animateCounter(el) {
  const target = parseInt(el.getAttribute("data-target"));
  const isDecimal = el.hasAttribute("data-decimal");
  const duration = 1800;
  const start = performance.now();
  const step = (now) => {
    const progress = Math.min((now - start) / duration, 1);
    const eased = 1 - Math.pow(1 - progress, 3);
    const val = eased * target;
    el.textContent = isDecimal ? (val / 10).toFixed(1) : Math.round(val);
    if (progress < 1) requestAnimationFrame(step);
  };
  requestAnimationFrame(step);
}

/* ===== SKILL BAR ANIMATION ===== */
function animateSkillBars(entries) {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.querySelectorAll(".skill-fill").forEach(fill => fill.classList.add("animated"));
    }
  });
}
const skillObs = new IntersectionObserver(animateSkillBars, { threshold: 0.2 });
document.querySelectorAll(".skill-card").forEach(card => skillObs.observe(card));

/* ===== COUNTER OBSERVER ===== */
const counterObs = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.querySelectorAll(".stat-number").forEach(el => animateCounter(el));
      counterObs.unobserve(entry.target);
    }
  });
}, { threshold: 0.5 });
const heroStats = document.querySelector(".hero-stats");
if (heroStats) counterObs.observe(heroStats);

/* ===== REVEAL ON SCROLL ===== */
const revealObs = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add("visible");
      revealObs.unobserve(entry.target);
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll(
  ".about-card, .skill-card, .exp-card, .project-card, .cert-card, .cert-img-card, .contact-info-item, .about-left p"
).forEach((el, i) => {
  if (!el.classList.contains("reveal")) el.classList.add("reveal");
  revealObs.observe(el);
});

/* ===== CONTACT FORM ===== */
function handleFormSubmit(e) {
  e.preventDefault();
  const btn = document.getElementById("submitBtn");
  const success = document.getElementById("formSuccess");
  btn.textContent = "Sending...";
  btn.disabled = true;
  setTimeout(() => {
    btn.innerHTML = `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg> Send Message`;
    btn.disabled = false;
    success.classList.add("show");
    e.target.reset();
    setTimeout(() => success.classList.remove("show"), 5000);
  }, 1200);
}

/* ===== SMOOTH PARALLAX ORB ===== */
document.addEventListener("mousemove", (e) => {
  const { clientX, clientY } = e;
  const cx = window.innerWidth / 2;
  const cy = window.innerHeight / 2;
  const dx = (clientX - cx) / cx;
  const dy = (clientY - cy) / cy;
  const orbs = document.querySelectorAll(".orb");
  orbs[0].style.transform = `translate(${dx * 18}px, ${dy * 18}px)`;
  orbs[1].style.transform = `translate(${-dx * 14}px, ${-dy * 14}px)`;
  if (orbs[2]) orbs[2].style.transform = `translate(${dx * 10}px, ${dy * 10}px)`;
});
