const ITS_SURABAYA = { lat: -7.2825, lng: 112.7954 }; // initial map view only

let currentTarget = 1;
let guessMarker = null;

let viewer = pannellum.viewer('pano', {
  default: {
    firstScene: "t1",
    autoLoad: true,
    autoRotate: -2,
    keyboardZoom: false,
    showFullscreenCtrl: true,
    showControls: true,
    compass: false,
  },
  scenes: {
    t1: {
      type: "equirectangular",
      panorama: "assets/panos/target1.jpg",
      hfov: 100,
    },
    t2: {
      type: "equirectangular",
      panorama: "assets/panos/target2.jpg",
      hfov: 100,
    },
    t3: {
      type: "equirectangular",
      panorama: "assets/panos/target3.jpg",
      hfov: 100,
    }
  }
});

function loadPanoForTarget(targetId){
  const id = targetId === 1 ? "t1" : targetId === 2 ? "t2" : "t3";
  try{
    viewer.loadScene(id, null, 750);
  }catch(e){
    viewer.destroy();
    viewer = pannellum.viewer('pano', {
      default: { firstScene: id, autoLoad: true, autoRotate: -2, keyboardZoom: false, showFullscreenCtrl: true, showControls: true, compass: false },
      scenes: {
        t1: { type: "equirectangular", panorama: "assets/panos/target1.jpg", hfov: 100 },
        t2: { type: "equirectangular", panorama: "assets/panos/target2.jpg", hfov: 100 },
        t3: { type: "equirectangular", panorama: "assets/panos/target3.jpg", hfov: 100 },
      }
    });
  }
}

function attachWebGLLifecycleHandlers(){
  const canvas = document.querySelector('#pano canvas');
  if (!canvas) return;
  const onLost = (e)=>{
    e.preventDefault();
    showToast("WebGL context lost. Reloading panorama…", false);
    const id = currentTarget === 1 ? "t1" : currentTarget === 2 ? "t2" : "t3";
    setTimeout(()=>{
      try { viewer.loadScene(id); } catch { /* ignore */ }
    }, 200);
  };
  const onRestored = ()=>{
    showToast("WebGL context restored.", true);
  };
  canvas.addEventListener('webglcontextlost', onLost, false);
  canvas.addEventListener('webglcontextrestored', onRestored, false);
}
setTimeout(attachWebGLLifecycleHandlers, 500);

const map = L.map('map', { zoomControl: true })
  .setView([ITS_SURABAYA.lat, ITS_SURABAYA.lng], 13);

L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
  attribution: '&copy; OpenStreetMap &copy; CARTO',
  maxZoom: 19
}).addTo(map);

function placeGuess(latlng){
  if (guessMarker){
    guessMarker.setLatLng(latlng);
  } else {
    guessMarker = L.marker(latlng, {
      title: "Your guess",
      keyboard: false,
    });
    guessMarker.getElement?.classList?.add('guess');
    guessMarker.addTo(map);
  }
  document.getElementById('statusText').textContent = `Guess set: ${latlng.lat.toFixed(5)}, ${latlng.lng.toFixed(5)}`;
}

map.on('click', (e)=>{
  placeGuess(e.latlng);
});

document.getElementById('resetBtn').addEventListener('click', ()=>{
  if (guessMarker){ map.removeLayer(guessMarker); guessMarker = null; }
  document.getElementById('statusText').textContent = "Pick a spot, then Submit.";
});

document.getElementById('submitBtn').addEventListener('click', async ()=>{
  if (!guessMarker){
    alert("Letakkan titik tebakan di peta terlebih dahulu.");
    return;
  }
  const latlng = guessMarker.getLatLng();
  try{
    const resp = await fetch('api/guess.php', {
      method:'POST',
      headers: { 'Content-Type':'application/json' },
      body: JSON.stringify({
        target_id: currentTarget,
        lat: latlng.lat,
        lng: latlng.lng,
      })
    });
    const data = await resp.json();
    if (data && data.success){
      showToast(`✅ Benar! Flag: ${data.flag}`, true);
    } else {
      showToast(data?.message || "gagal", false);
    }
  }catch(err){
    showToast("Terjadi kesalahan jaringan.", false);
  }
});

document.querySelectorAll('.menu-btn').forEach(btn=>{
  btn.addEventListener('click', ()=>{
    document.querySelectorAll('.menu-btn').forEach(b=>b.classList.remove('active'));
    btn.classList.add('active');
    const id = Number(btn.dataset.target);
    currentTarget = id;
    document.getElementById('targetLabel').innerHTML = `Target: <strong>${id===1?'guessr 1':id===2?'guessr 2':'guessr 3'}</strong>`;
    if (guessMarker){ map.removeLayer(guessMarker); guessMarker = null; }
    document.getElementById('statusText').textContent = "Pick a spot, then Submit.";
    loadPanoForTarget(id);
    setTimeout(attachWebGLLifecycleHandlers, 300);
  });
});
document.querySelector('.menu-btn[data-target="1"]').classList.add('active');

function showToast(text, ok){
  const el = document.createElement('div');
  el.className = 'toast ' + (ok ? 'ok' : 'err');
  el.textContent = text;
  document.body.appendChild(el);
  setTimeout(()=>{ el.classList.add('show'); }, 20);
  setTimeout(()=>{
    el.classList.remove('show');
    setTimeout(()=> el.remove(), 350);
  }, 3500);
}
