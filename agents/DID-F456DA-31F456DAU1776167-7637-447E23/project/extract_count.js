(async () => {
  const getText = (selector) => {
    const el = document.querySelector(selector);
    return el ? el.innerText : null;
  };

  // Common Alibaba result count selectors
  const resultSelectors = [
    '.total-results',
    '.search-res-info',
    '.ui-search-number',
    '.m-search-result-count',
    '.supplier-count',
    '.header-count'
  ];

  let results = {};
  resultSelectors.forEach(s => {
    results[s] = getText(s);
  });

  // Also look for text like "X+ results" or "Showing X results"
  const bodyText = document.body.innerText;
  const match = bodyText.match(/(\d+,?\d*\+?)\s*(results|suppliers|件|个)/i);
  results.regexMatch = match ? match[0] : null;

  return { __result: results };
})()