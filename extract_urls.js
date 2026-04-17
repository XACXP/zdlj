(async () => {
  const images = ['t001', 't002', 't003', 't004', 't005'];
  const results = {};
  
  // Find all image items. Usually they are in a grid.
  // We can look for the text of the image names.
  const allElements = Array.from(document.querySelectorAll('*'));
  
  images.forEach(name => {
    const element = allElements.find(el => el.textContent && el.textContent.trim() === name);
    if (element) {
      // Look for an image nearby.
      const parent = element.closest('.next-grid-col') || element.parentElement.parentElement;
      const img = parent.querySelector('img');
      if (img) {
        // In Alibaba Photo Bank, the small image URL usually needs to be converted to the full size URL.
        // Or sometimes there is a data attribute.
        results[name] = img.src;
      }
    }
  });
  
  return results;
})()