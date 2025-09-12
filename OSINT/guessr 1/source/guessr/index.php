<?php

?><!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>HCS INTERSEC - OSINT</title>

  <link
    rel="stylesheet"
    href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"
    integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY="
    crossorigin=""/>
  <script
    src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"
    integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo="
    crossorigin=""></script>

  <link rel="stylesheet" type="text/css" href="https://unpkg.com/pannellum/build/pannellum.css"/>
  <script type="text/javascript" src="https://unpkg.com/pannellum/build/pannellum.js"></script>

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="css/style.css?v=<?php echo time(); ?>" />
</head>
<body>
  <div id="app">
    <header class="nav">
      <div class="brand">
        <div class="logo"></div>
        <div class="title">HCS INTERSEC — <span class="accent">OSINT</span> Platform</div>
      </div>
      <nav class="menu">
        <button class="menu-btn" data-target="1">guessr 1</button>
        <button class="menu-btn" data-target="2">guessr 2</button>
        <button class="menu-btn" data-target="3">guessr 3</button>
      </nav>
    </header>

    <main class="main">
      <section class="panel pano-panel">
        <div id="pano"></div>
        <div class="pano-overlay">
          <div class="pills">
            <span class="pill">360°</span>
            <span class="pill">No Walk</span>
          </div>
        </div>
      </section>

      <section class="panel map-panel">
        <div id="map"></div>

        <div class="floating-card">
          <div class="row">
            <div class="status">
              <div class="status-dot"></div>
              <span id="statusText">Pick a spot, then Submit.</span>
            </div>
          </div>
          <div class="row actions">
            <button id="resetBtn" class="ghost">Reset</button>
            <button id="submitBtn" class="primary">Submit Guess</button>
          </div>
        </div>
      </section>
    </main>

    <footer class="footer">
      <div class="left">
        <span class="muted">Built by VibeCoder with Love</span>
      </div>
      <div class="right">
        <span id="targetLabel" class="tag">Target: <strong>guessr 1</strong></span>
      </div>
    </footer>
  </div>

  <script src="js/script.js?v=<?php echo time(); ?>"></script>
</body>
</html>
