(async () => {
  const result = {};
  const title = document.querySelector('input[placeholder*="标题"], .next-input input'); // Adjust selector
  result.title = document.querySelector('.next-form-item-control input')?.value || "";
  
  // Find specific fields by labels
  const getValByLabel = (label) => {
    const el = Array.from(document.querySelectorAll('label')).find(l => l.innerText.includes(label));
    if (el) {
      const input = el.closest('.next-form-item').querySelector('input, textarea');
      return input ? (input.value || input.innerText) : "not found";
    }
    return "label not found";
  };

  result.all_inputs = Array.from(document.querySelectorAll('input, textarea, select')).map(i => ({
    placeholder: i.placeholder,
    value: i.value,
    id: i.id,
    name: i.name
  })).filter(i => i.value || i.placeholder);

  // Check images
  result.images_count = document.querySelectorAll('.image-upload-item img, .publish-image-list img').length;

  return result;
})()