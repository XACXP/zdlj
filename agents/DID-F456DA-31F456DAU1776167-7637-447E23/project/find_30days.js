(async () => {
  const findAndClick = (text) => {
    const els = Array.from(document.querySelectorAll('button, span, div, li, a'));
    const target = els.find(el => el.textContent.trim() === text);
    if (target) {
      target.click();
      return true;
    }
    return false;
  };

  const results = {};
  results.clicked30Days = findAndClick('最近30天') || findAndClick('Last 30 Days');
  
  // Wait a bit for the page to update
  await new Promise(r => setTimeout(r, 2000));
  
  // Try to find the indicators table
  const indicators = {};
  const rows = Array.from(document.querySelectorAll('tr, .next-table-row, .indicator-item'));
  // This is a guess on the structure. I'll need to refine.
  results.debug_rows = rows.map(r => r.innerText).slice(0, 20);
  
  return results;
})()