
function closeMessage() {
    var message = document.getElementById('message');
    message.style.animation = 'slide-out 0.5s ease-in-out forwards';
  
    setTimeout(function() {
      message.style.display = 'none';
    }, 500);
  }
  
  // Auto-close message after 3 seconds
  setTimeout(function() {
    closeMessage();
  }, 3000);
  
  