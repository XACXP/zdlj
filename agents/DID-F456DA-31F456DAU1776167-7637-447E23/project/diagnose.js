(async () => {
  const url = 'https://crm.alibaba.com/crmlogin/aisales/dingwukong/diagnoseData.json';
  try {
    const r = await fetch(url, {
      method: 'POST',
      credentials: 'include'
    });
    if (!r.ok) throw new Error(`HTTP error: ${r.status}`);
    const data = await r.json();
    return data;
  } catch (e) {
    return { error: e.message };
  }
})()