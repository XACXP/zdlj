(async () => {
  const result = {
    url: window.location.href,
    title: document.title,
    hasSearchBox: !!document.querySelector('input[placeholder*="Search"], input[placeholder*="搜索"], .next-input input'),
    allText: document.body.innerText.substring(0, 1000)
  };
  return result;
})()