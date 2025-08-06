document.getElementById('contact-form').addEventListener('submit', function (e) {
  e.preventDefault();

  const name = this.name.value.trim();
  const email = this.email.value.trim();
  const message = this.message.value.trim();
  const msg = document.getElementById('form-msg');

  if (name && email && message) {
    msg.textContent = `Thanks for reaching out, ${name}! I'll get back to you soon.`;
    msg.style.color = 'green';
    this.reset();
  } else {
    msg.textContent = 'Please fill in all fields.';
    msg.style.color = 'red';
  }
});
document.getElementById('contact-form').addEventListener('submit', function (e) {
  e.preventDefault();

  const name = this.name.value.trim();
  const email = this.email.value.trim();
  const message = this.message.value.trim();
  const msg = document.getElementById('form-msg');

  if (name && email && message) {
    msg.textContent = `Thanks for reaching out, ${name}! I'll get back to you soon.`;
    msg.style.color = 'green';
    this.reset();
  } else {
    msg.textContent = 'Please fill in all fields.';
    msg.style.color = 'red';
  }
});

// Scroll-triggered reveal
const reveals = document.querySelectorAll('.reveal');

const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('active');
    }
  });
}, {
  threshold: 0.2
});

reveals.forEach(el => observer.observe(el));
