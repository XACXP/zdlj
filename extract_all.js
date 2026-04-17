(async () => {
  const images = ['t001', 't002', 't003', 't004', 't005'];
  const results = {};
  
  for (const name of images) {
    // Find the button with the name
    const buttons = Array.from(document.querySelectorAll('button'));
    const btn = buttons.find(b => b.textContent.trim() === name);
    if (btn) {
      btn.click();
      // Wait for dialog to appear
      await new Promise(r => setTimeout(r, 1000));
      const downloadLink = document.querySelector('a[href*="attachment=photobank.jpg"]');
      if (downloadLink) {
        results[name] = downloadLink.href.split('?')[0];
      }
      // Close dialog
      const closeBtn = document.querySelector('.next-dialog-close');
      if (closeBtn) closeBtn.click();
      await new Promise(r => setTimeout(r, 500));
    }
  }
  return results;
})()