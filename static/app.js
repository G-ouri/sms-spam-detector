async function checkSpam() {
  const message = document.getElementById('sms-input').value.trim();

  // Basic validation
  if (!message) {
    alert('Please enter a message first.');
    return;
  }

  // Show loading state
  const btn = document.getElementById('check-btn');
  btn.disabled = true;
  btn.textContent = 'Checking...';

  // Hide previous results
  document.getElementById('result-box').classList.add('hidden');
  document.getElementById('error-box').classList.add('hidden');

  try {
    // Send message to Django backend
    const response = await fetch('/check/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: message })
    });

    if (!response.ok) {
      throw new Error('Server returned an error.');
    }

    const data = await response.json();

    // Show result
    const resultBox = document.getElementById('result-box');
    resultBox.className = data.verdict; // applies spam/safe/unknown CSS class

    document.getElementById('verdict').textContent =
      data.verdict === 'spam'    ? '🚨 SPAM'     :
      data.verdict === 'safe'    ? '✅ Safe'      : '❓ Uncertain';

    document.getElementById('confidence').textContent =
      `Confidence: ${data.confidence}%`;

    document.getElementById('explanation').textContent = data.explanation;

    resultBox.classList.remove('hidden');

  } catch (err) {
    document.getElementById('error-box').classList.remove('hidden');
  } finally {
    btn.disabled = false;
    btn.textContent = 'Check Message';
  }
}
