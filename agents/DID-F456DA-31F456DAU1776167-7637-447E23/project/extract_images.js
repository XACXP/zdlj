(async () => {
  const results = {
    mainImages: [],
    detailImages: []
  };

  // Find Main Images
  // Main images are usually in a list under the "Main Image" label.
  // We can look for image tags in the upload list.
  const mainImageContainers = document.querySelectorAll('.next-upload-list-item-thumbnail img, .product-image-list img, [data-test-id="main-image"] img');
  mainImageContainers.forEach(img => {
    if (img.src && !img.src.includes('base64')) {
      results.mainImages.push(img.src);
    }
  });

  // If the above fails, let's look for images in the section that contains "主图"
  if (results.mainImages.length === 0) {
    const sections = Array.from(document.querySelectorAll('div, section, tr, td'));
    const mainImgSection = sections.find(s => s.innerText && s.innerText.includes('主图') && s.querySelector('img'));
    if (mainImgSection) {
      const imgs = mainImgSection.querySelectorAll('img');
      imgs.forEach(img => {
        if (img.src && !img.src.includes('base64')) {
          results.mainImages.push(img.src);
        }
      });
    }
  }

  // Find Detail Images
  // Detail images are usually in the description editor.
  // They might be in a div with class like "p-desc-content" or inside an iframe.
  const descContainer = document.querySelector('.product-detail-editor, .p-desc-content, #product-detail-editor');
  if (descContainer) {
    const imgs = descContainer.querySelectorAll('img');
    imgs.forEach(img => {
      if (img.src && !img.src.includes('base64')) {
        results.detailImages.push(img.src);
      }
    });
  }

  // If still no detail images, check the whole document for images that look like they belong to the description
  if (results.detailImages.length === 0) {
     // Look for images in the description section identified by ref e201/e199 etc.
     // But since we are in console, we just look for images in a large container near the bottom.
     const allImgs = Array.from(document.querySelectorAll('img'));
     allImgs.forEach(img => {
       const rect = img.getBoundingClientRect();
       // Description images are usually larger and lower in the page
       if (rect.top > 1000 && rect.width > 300) {
          results.detailImages.push(img.src);
       }
     });
  }

  return { __result: results };
})()