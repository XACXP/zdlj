(async () => {
  const imageSection = document.querySelector('.next-form-item-label[title="商品图片&视频"]')?.closest('.next-form-item');
  if (!imageSection) {
    return { error: 'Image section not found' };
  }
  const images = imageSection.querySelectorAll('img');
  // Usually, uploaded images have a specific class or are in a specific container.
  // In Alibaba's publisher, uploaded images are often inside .img-box or similar.
  // Let's count all images that are not the "add" placeholder.
  const uploadedImages = Array.from(images).filter(img => img.src && !img.src.includes('plus') && !img.src.includes('upload'));
  return { count: uploadedImages.length, srcs: uploadedImages.map(img => img.src) };
})()