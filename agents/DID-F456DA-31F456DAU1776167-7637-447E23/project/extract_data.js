(async () => {
  const images = Array.from(document.querySelectorAll('.main-image-vo-list img, .next-upload-list-item-thumbnail img, .product-image-list img'))
    .map(img => img.src)
    .filter(src => src && !src.includes('base64'));
  
  const priceRows = Array.from(document.querySelectorAll('tr')).filter(tr => tr.innerText.includes('US $'));
  const priceInfo = priceRows.map(tr => tr.innerText.replace(/\n/g, ' '));

  return {
    images: images,
    priceInfo: priceInfo
  };
})()