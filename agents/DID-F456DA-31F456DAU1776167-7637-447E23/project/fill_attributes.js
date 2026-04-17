(async () => {
  const findByLabel = (label) => {
    const el = Array.from(document.querySelectorAll('label, span, div')).find(e => e.innerText && e.innerText.includes(label));
    if (el) {
      const parent = el.closest('.next-form-item') || el.parentElement;
      return parent ? parent.querySelector('input, textarea, .next-select') : null;
    }
    return null;
  };

  const results = {
    keywords: document.querySelectorAll('input[name*="keyword"], .keyword-input input').length,
    description: !!document.querySelector('.description-editor, #description, .next-rte'),
    attributes: {}
  };

  // Try to fill attributes
  const fields = {
    "工业用途": "Gift & Craft",
    "纸张类型": "Paperboard",
    "品牌名称": "OEM",
    "产地": "China",
    "型号": "16x112/122",
    "尺寸": "16x112mm, 16x122mm"
  };

  for (const [label, value] of Object.entries(fields)) {
    const input = findByLabel(label);
    if (input) {
      if (input.tagName === 'INPUT') {
        input.value = value;
        input.dispatchEvent(new Event('input', { bubbles: true }));
        input.dispatchEvent(new Event('change', { bubbles: true }));
        results.attributes[label] = "filled";
      }
    }
  }

  return results;
})()