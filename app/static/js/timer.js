document.addEventListener('DOMContentLoaded', () => {
  const timer = document.getElementById('timer');
  let seconds = parseInt(timer.dataset.seconds);

  const countdown = setInterval(() => {
    seconds--;
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    timer.textContent = `${mins}:${secs < 10 ? '0' : ''}${secs}`;

    if (seconds <= 10) {
      timer.classList.add('warning');
    }

    if (seconds <= 0) {
      clearInterval(countdown);
      document.querySelector('form').submit();
    }
  }, 1000);
});
